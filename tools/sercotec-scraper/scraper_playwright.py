"""
Sercotec — scraper Playwright de postulaciones abiertas.

Por qué Playwright:
- /postulaciones-abiertas/ embebe un iframe a `sctwebwidgets.sercotec.cl/convocatorias`,
  que es una app Next.js client-side. requests + BS4 ven HTML vacío. Playwright renderiza
  JS y deja extraer las cards reales (nombre, región, fechas, link).
- Cada link de card apunta a una página de convocatoria que SÍ es server-rendered. Para esos
  detalles usamos requests + BS4 (más rápido que abrir browser por página).

Estructura confirmada del accordion en la página de detalle:
    <button data-bs-target="#collapseThree">¿Quiénes pueden acceder?</button>
    <div id="collapseThree"><div class="accordion-body">
        <p>...descripción completa...</p>
    </div></div>

Uso:
    pip install -r tools/sercotec-scraper/requirements.txt
    playwright install chromium

    python scraper_playwright.py                  # default (headless)
    python scraper_playwright.py --headed         # ver el browser
    python scraper_playwright.py --limit 5        # debug con pocas cards
    python scraper_playwright.py --out custom.csv # cambia destino
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import io
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

BASE = "https://www.sercotec.cl"
WIDGET_URL = "https://sctwebwidgets.sercotec.cl/convocatorias"
LISTING_URL = f"{BASE}/postulaciones-abiertas/"

OUT_DIR = Path(__file__).parent / "outputs"
DEFAULT_CSV = OUT_DIR / "postulaciones_pw.csv"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
HEADERS = {"User-Agent": UA, "Accept-Language": "es-CL,es;q=0.9"}
HTTP_TIMEOUT = 30
PAGE_TIMEOUT_MS = 60_000

REGIONES_CL = [
    "Arica y Parinacota", "Arica Parinacota", "Tarapacá", "Tarapaca",
    "Antofagasta", "Atacama", "Coquimbo", "Valparaíso", "Valparaiso",
    "Metropolitana", "O'Higgins", "OHiggins", "Maule", "Ñuble", "Nuble",
    "Biobío", "Biobio", "La Araucanía", "Araucanía", "Araucania",
    "Los Ríos", "Los Rios", "Los Lagos", "Aysén", "Aysen", "Magallanes",
]
REGION_CANONICAL = {
    "Arica Parinacota": "Arica y Parinacota",
    "Tarapaca": "Tarapacá",
    "Valparaiso": "Valparaíso",
    "OHiggins": "O'Higgins",
    "Nuble": "Ñuble",
    "Biobio": "Biobío",
    "Araucanía": "La Araucanía",
    "Araucania": "La Araucanía",
    "Los Rios": "Los Ríos",
    "Aysen": "Aysén",
}

REQ_HEADING_KEYS = [
    "¿quiénes pueden acceder?",
    "¿quiénes pueden postular?",
    "¿quiénes pueden participar?",
    "quiénes pueden acceder",
    "quiénes pueden postular",
    "quiénes pueden participar",
    "quienes pueden acceder",
    "quienes pueden postular",
    "quienes pueden participar",
    "requisitos",
]

DATE_INICIO_RE = re.compile(r"inicio[:\s]+(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})", re.IGNORECASE)
DATE_CIERRE_RE = re.compile(r"cierre[:\s]+(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})", re.IGNORECASE)
DATE_GENERIC_RE = re.compile(r"\b(\d{1,2}[/-]\d{1,2}[/-]\d{4})\b")


@dataclass
class Convocatoria:
    nombre: str
    fecha_inicio: str
    fecha_cierre: str
    region: str
    link: str
    requisitos: str = ""


JS_EXTRACT_CARDS = r"""
() => {
  // Toma todos los anchors a páginas de convocatoria. Para cada uno, sube por el DOM
  // hasta encontrar un contenedor "card" (con suficiente texto y al menos una fecha).
  const isConvLink = (href) =>
    href && (href.includes('/convocatoria/') || href.includes('/convocatoria-'));

  const anchors = Array.from(document.querySelectorAll('a[href]'))
    .filter(a => isConvLink(a.href));

  const seen = new Set();
  const out = [];
  for (const a of anchors) {
    if (seen.has(a.href)) continue;
    seen.add(a.href);

    let card = a;
    for (let i = 0; i < 8; i++) {
      const parent = card.parentElement;
      if (!parent) break;
      card = parent;
      const t = (card.innerText || '').trim();
      if (t.length > 80 && /\d{1,2}[/-]\d{1,2}[/-]\d{2,4}/.test(t)) break;
    }

    out.push({
      href: a.href,
      anchorText: (a.innerText || '').trim(),
      cardText: (card.innerText || '').trim(),
    });
  }
  return out;
}
"""


def parse_region(text: str) -> str:
    if not text:
        return ""
    matches: list[str] = []
    for r in REGIONES_CL:
        if re.search(rf"\b{re.escape(r)}\b", text, re.IGNORECASE):
            canonical = REGION_CANONICAL.get(r, r)
            if canonical not in matches:
                matches.append(canonical)
    return ", ".join(matches)


def parse_card(card: dict) -> Convocatoria:
    text = card.get("cardText", "") or ""
    anchor = card.get("anchorText", "") or ""

    m_ini = DATE_INICIO_RE.search(text)
    m_cie = DATE_CIERRE_RE.search(text)

    fecha_inicio = m_ini.group(1) if m_ini else ""
    fecha_cierre = m_cie.group(1) if m_cie else ""

    if not fecha_inicio or not fecha_cierre:
        # Fallback: dos fechas dd/mm/yyyy en orden de aparición
        all_dates = DATE_GENERIC_RE.findall(text)
        if not fecha_inicio and all_dates:
            fecha_inicio = all_dates[0]
        if not fecha_cierre and len(all_dates) > 1:
            fecha_cierre = all_dates[1]

    region = parse_region(anchor) or parse_region(text) or parse_region(card.get("href", ""))

    nombre = ""
    for src in (anchor, text):
        if src:
            for line in src.splitlines():
                line = line.strip()
                if line and not DATE_GENERIC_RE.search(line) and len(line) > 5:
                    nombre = line
                    break
            if nombre:
                break
    if not nombre:
        nombre = card.get("href", "").rstrip("/").rsplit("/", 1)[-1].replace("-", " ").title()

    return Convocatoria(
        nombre=nombre,
        fecha_inicio=fecha_inicio or "No informado",
        fecha_cierre=fecha_cierre or "No informado",
        region=region or "No informado",
        link=card.get("href", ""),
    )


LOAD_MORE_SELECTORS = [
    'button[aria-label="Cargar más postulaciones disponibles"]',
    'button[title="Cargar más postulaciones"]',
    'button.btn-red-acento.rounded-pill',
    'button:has-text("Cargar más postulaciones")',
]
MAX_LOAD_MORE_CLICKS = 60  # tope de seguridad


async def _click_load_more_until_done(page, max_clicks: int = MAX_LOAD_MORE_CLICKS) -> int:
    """Hace clic en 'Cargar más postulaciones' hasta que el botón desaparezca o
    deje de aumentar la cantidad de cards. Devuelve cuántos clics realizó."""
    clicks = 0
    prev_count = await page.evaluate(
        "() => document.querySelectorAll(\"a[href*='/convocatoria']\").length"
    )

    while clicks < max_clicks:
        btn = None
        for sel in LOAD_MORE_SELECTORS:
            try:
                candidate = page.locator(sel).first
                if await candidate.count() > 0 and await candidate.is_visible():
                    btn = candidate
                    break
            except Exception:
                continue

        if btn is None:
            break

        try:
            await btn.scroll_into_view_if_needed(timeout=3_000)
            await btn.click(timeout=5_000)
        except Exception as e:
            print(f"[load-more] clic falló ({e}); detengo paginación", file=sys.stderr)
            break

        clicks += 1
        try:
            await page.wait_for_function(
                """(prev) => document.querySelectorAll("a[href*='/convocatoria']").length > prev""",
                arg=prev_count,
                timeout=10_000,
            )
        except Exception:
            await page.wait_for_timeout(1_500)

        new_count = await page.evaluate(
            "() => document.querySelectorAll(\"a[href*='/convocatoria']\").length"
        )
        print(f"[load-more] clic #{clicks}: {prev_count} → {new_count} cards", file=sys.stderr)
        if new_count <= prev_count:
            break
        prev_count = new_count

    return clicks


async def scrape_listing(headless: bool = True, debug_dump: Path | None = None) -> list[dict]:
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=headless)
        ctx = await browser.new_context(user_agent=UA, locale="es-CL")
        page = await ctx.new_page()

        await page.goto(WIDGET_URL, wait_until="networkidle", timeout=PAGE_TIMEOUT_MS)
        try:
            await page.wait_for_selector(
                "a[href*='/convocatoria']", timeout=15_000, state="attached"
            )
        except Exception:
            print("[warn] no aparecieron anchors /convocatoria/ en 15s; continúo igual",
                  file=sys.stderr)
        await page.wait_for_timeout(1500)

        clicks = await _click_load_more_until_done(page)
        if clicks:
            print(f"[load-more] {clicks} clics totales para paginación completa", file=sys.stderr)
            await page.wait_for_timeout(800)

        if debug_dump:
            html = await page.content()
            debug_dump.parent.mkdir(parents=True, exist_ok=True)
            debug_dump.write_text(html, encoding="utf-8")
            print(f"[debug] HTML renderizado guardado en {debug_dump}", file=sys.stderr)

        cards: list[dict] = await page.evaluate(JS_EXTRACT_CARDS)
        await browser.close()
        return cards


def fetch_requisitos(url: str, session: requests.Session) -> str:
    """Obtiene la descripción completa del bloque "¿Quiénes pueden acceder?" (o equivalente)."""
    try:
        r = session.get(url, headers=HEADERS, timeout=HTTP_TIMEOUT)
        r.raise_for_status()
    except requests.RequestException as e:
        return f"ERROR_FETCH: {e}"

    soup = BeautifulSoup(r.text, "lxml")

    for btn in soup.select("button[data-bs-target]"):
        btn_txt = btn.get_text(" ", strip=True).lower()
        if any(k in btn_txt for k in REQ_HEADING_KEYS):
            target_id = (btn.get("data-bs-target") or "").lstrip("#")
            if not target_id:
                continue
            container = soup.find(id=target_id)
            if container:
                body = container.find("div", class_="accordion-body") or container
                txt = body.get_text("\n", strip=True)
                if txt:
                    return _normalize_text(txt)

    for level in ("h2", "h3", "h4"):
        for h in soup.find_all(level):
            txt = h.get_text(" ", strip=True).lower()
            if not any(k in txt for k in REQ_HEADING_KEYS):
                continue
            chunks = []
            for sib in h.find_next_siblings():
                if sib.name in ("h1", "h2", "h3", "h4") and sib.name <= level:
                    break
                t = sib.get_text("\n", strip=True)
                if t:
                    chunks.append(t)
            if chunks:
                return _normalize_text("\n".join(chunks))

    return "No informado"


def _normalize_text(s: str) -> str:
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def write_outputs(rows: list[Convocatoria], csv_path: Path) -> Path:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    json_path = csv_path.with_suffix(".json")

    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["nombre", "fecha_inicio", "fecha_cierre", "region", "link", "requisitos"])
        for c in rows:
            w.writerow([
                c.nombre, c.fecha_inicio, c.fecha_cierre, c.region, c.link,
                c.requisitos.replace("\n", " ⏎ "),
            ])

    json_path.write_text(
        json.dumps([asdict(c) for c in rows], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return json_path


def _force_utf8_stdio() -> None:
    for name in ("stdout", "stderr"):
        stream = getattr(sys, name)
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            setattr(sys, name, io.TextIOWrapper(stream.buffer, encoding="utf-8", errors="replace"))


async def run(args: argparse.Namespace) -> int:
    debug_dump = OUT_DIR / "_widget_rendered.html" if args.debug else None
    print("[1/3] Render Playwright del widget…")
    raw_cards = await scrape_listing(headless=not args.headed, debug_dump=debug_dump)
    print(f"      → {len(raw_cards)} cards detectadas")

    if args.limit:
        raw_cards = raw_cards[: args.limit]

    print("[2/3] Parseo de cards (nombre, fechas, región, link)…")
    convocatorias = [parse_card(c) for c in raw_cards]

    print("[3/3] Descarga de páginas de detalle y extracción de requisitos…")
    session = requests.Session()
    for i, c in enumerate(convocatorias, 1):
        if not c.link:
            c.requisitos = "Sin link"
            continue
        print(f"      [{i}/{len(convocatorias)}] {c.link}")
        c.requisitos = fetch_requisitos(c.link, session)

    csv_path = args.out
    json_path = write_outputs(convocatorias, csv_path)
    print(f"\n✓ {len(convocatorias)} convocatorias procesadas")
    print(f"  CSV : {csv_path}")
    print(f"  JSON: {json_path}")
    return 0


def main() -> int:
    _force_utf8_stdio()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--headed", action="store_true", help="Lanza el browser visible (debug).")
    ap.add_argument("--limit", type=int, default=0, help="Limita cantidad de convocatorias a procesar.")
    ap.add_argument("--out", type=Path, default=DEFAULT_CSV,
                    help=f"Ruta del CSV (también genera .json). Default: {DEFAULT_CSV}")
    ap.add_argument("--debug", action="store_true",
                    help="Guarda el HTML renderizado del widget en outputs/_widget_rendered.html.")
    args = ap.parse_args()
    return asyncio.run(run(args))


if __name__ == "__main__":
    sys.exit(main())

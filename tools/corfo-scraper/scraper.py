"""
CORFO — scraper de programas y convocatorias abiertas.

Por qué este diseño:
- /sites/cpp/programasyconvocatorias/ pinta los resultados con AJAX vía
  `admin-ajax.php`, action `filter_convocatorias`. Ese endpoint es público
  (solo requiere un `nonce` que viene en el HTML del listing) y devuelve
  JSON con `found` (total) y `html` (cards de la página solicitada).
- Es mucho más estable y rápido que renderizar con Playwright. Discovery y
  metadata de cada card (nombre, fechas, región, link) salen del propio
  AJAX. Para los requisitos completos hay que ir a la página de detalle.

Estructura confirmada en cada card del AJAX:
    <div class="caja-resultados_uno">
      <h4>NOMBRE</h4>
      <div class="apertura"><span> dd/mm/yyyy </span></div>
      <div class="cierre"><span> dd/mm/yyyy </span></div>
      <h5><em>Alcance: REGION</em></h5>
      <h6>Estado: ABIERTAS</h6>
      <p>descripción corta…</p>
      <div class="foot-caja_result"><a href="…/convocatoria/SLUG/">Más Información</a></div>
    </div>

En la página de detalle:
    <h2>¿Quiénes pueden postular?</h2>
    <div class="postula_fase2-cuerpodos_fase2"> …requisitos… </div>

Uso:
    pip install -r tools/corfo-scraper/requirements.txt
    python scraper.py                  # default, todas las convocatorias
    python scraper.py --limit 5        # debug
    python scraper.py --out custom.csv # cambia destino
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import math
import re
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path

import requests
from bs4 import BeautifulSoup, Tag

BASE = "https://www.corfo.gob.cl"
LISTING_URL = f"{BASE}/sites/cpp/programasyconvocatorias/"
AJAX_URL = f"{BASE}/sites/cpp/wp-admin/admin-ajax.php"

OUT_DIR = Path(__file__).parent / "outputs"
DEFAULT_CSV = OUT_DIR / "convocatorias.csv"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
HEADERS = {"User-Agent": UA, "Accept-Language": "es-CL,es;q=0.9"}
TIMEOUT = 30
SLEEP_BETWEEN = 0.5
PAGE_SIZE = 10  # convocatorias-filters.js usa pageLength: 10

REQ_HEADING_KEYS = [
    "¿quiénes pueden postular?",
    "¿quiénes pueden acceder?",
    "¿quiénes pueden participar?",
    "quiénes pueden postular",
    "quiénes pueden acceder",
    "quiénes pueden participar",
    "quienes pueden postular",
    "quienes pueden acceder",
    "quienes pueden participar",
    "requisitos",
]

NONCE_RE = re.compile(r'convocatoriasAjax\s*=\s*\{[^}]*"nonce"\s*:\s*"([a-f0-9]+)"')


@dataclass
class Convocatoria:
    nombre: str
    fecha_inicio: str
    fecha_cierre: str
    region: str
    link: str
    requisitos: str = ""
    estado: str = ""
    descripcion_corta: str = ""


def get_nonce(session: requests.Session) -> str:
    r = session.get(LISTING_URL, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    m = NONCE_RE.search(r.text)
    if not m:
        raise RuntimeError("No pude extraer el nonce desde el listing. ¿Cambió la página?")
    return m.group(1)


def fetch_page(session: requests.Session, nonce: str, page: int) -> dict:
    payload = {
        "action": "filter_convocatorias",
        "post_type": "convocatoria",
        "nonce": nonce,
        "page": str(page),
    }
    r = session.post(AJAX_URL, data=payload, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def _txt(node: Tag | None) -> str:
    if node is None:
        return ""
    return re.sub(r"\s+", " ", node.get_text(" ", strip=True)).strip()


def parse_cards(html: str) -> list[Convocatoria]:
    soup = BeautifulSoup(html, "lxml")
    out: list[Convocatoria] = []
    for caja in soup.select(".caja-resultados_uno"):
        h4 = caja.select_one(".titulo-cajas_fechas h4")
        ap = caja.select_one(".apertura span")
        ci = caja.select_one(".cierre span")
        h5 = caja.select_one("h5 em") or caja.select_one("h5")
        h6 = caja.select_one("h6")
        desc = caja.select_one(".contenido-caja_prog > p")
        link_a = caja.select_one(".foot-caja_result a")

        region = _txt(h5)
        if region.lower().startswith("alcance:"):
            region = region.split(":", 1)[1].strip()

        estado = _txt(h6)
        if estado.lower().startswith("estado:"):
            estado = estado.split(":", 1)[1].strip()

        out.append(Convocatoria(
            nombre=_txt(h4) or "Sin nombre",
            fecha_inicio=_txt(ap) or "No informado",
            fecha_cierre=_txt(ci) or "No informado",
            region=region or "No informado",
            link=link_a.get("href", "") if link_a else "",
            estado=estado,
            descripcion_corta=_txt(desc),
        ))
    return out


def fetch_requisitos(url: str, session: requests.Session) -> str:
    if not url:
        return "Sin link"
    try:
        r = session.get(url, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
    except requests.RequestException as e:
        return f"ERROR_FETCH: {e}"

    soup = BeautifulSoup(r.text, "lxml")

    # Quitar modales/diálogos para que no contaminen la extracción
    for modal in soup.select(".modal, .modal-dialog"):
        modal.decompose()

    target_h2: Tag | None = None
    for h2 in soup.find_all(["h1", "h2"]):
        txt = _txt(h2).lower()
        if any(k in txt for k in REQ_HEADING_KEYS):
            target_h2 = h2
            break
    if target_h2 is None:
        return "No informado"

    # Estrategia A: el bloque siguiente con clase .postula_fase2-cuerpodos_fase2
    block = target_h2.find_next(class_="postula_fase2-cuerpodos_fase2")
    if block:
        text = block.get_text("\n", strip=True)
        if text:
            return _normalize_text(text)

    # Estrategia B (fallback): texto desde el h2 hasta el próximo h1/h2
    chunks: list[str] = []
    for sib in target_h2.find_all_next():
        if sib.name in ("h1", "h2") and sib is not target_h2:
            break
        if sib.name in ("p", "li", "div") and sib.find(["p", "li"]) is None:
            t = sib.get_text("\n", strip=True)
            if t:
                chunks.append(t)
    return _normalize_text("\n".join(chunks)) or "No informado"


def _normalize_text(s: str) -> str:
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def write_outputs(rows: list[Convocatoria], csv_path: Path) -> Path:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    json_path = csv_path.with_suffix(".json")

    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow([
            "nombre", "fecha_inicio", "fecha_cierre", "region", "link",
            "estado", "descripcion_corta", "requisitos",
        ])
        for c in rows:
            w.writerow([
                c.nombre, c.fecha_inicio, c.fecha_cierre, c.region, c.link,
                c.estado, c.descripcion_corta,
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


def run(args: argparse.Namespace) -> int:
    session = requests.Session()

    print("[1/3] Obteniendo nonce desde listing…")
    nonce = get_nonce(session)
    print(f"      nonce = {nonce}")

    print("[2/3] Recorriendo páginas del AJAX (filter_convocatorias)…")
    convocatorias: list[Convocatoria] = []
    total = None
    page = 1
    while True:
        data = fetch_page(session, nonce, page)
        if total is None:
            total = int(data.get("found") or 0)
            total_pages = max(1, math.ceil(total / PAGE_SIZE))
            print(f"      total reportado: {total} convocatorias ({total_pages} páginas)")
        cards = parse_cards(data.get("html") or "")
        if not cards:
            break
        convocatorias.extend(cards)
        print(f"      [pág {page}] +{len(cards)} cards (acumulado: {len(convocatorias)})")
        if len(convocatorias) >= total:
            break
        page += 1
        if page > 200:  # tope de seguridad
            print("[warn] excedido tope de 200 páginas; deteniendo", file=sys.stderr)
            break
        time.sleep(SLEEP_BETWEEN)

    if args.limit:
        convocatorias = convocatorias[: args.limit]

    print("[3/3] Descargando páginas de detalle y extrayendo requisitos…")
    for i, c in enumerate(convocatorias, 1):
        print(f"      [{i}/{len(convocatorias)}] {c.link}")
        c.requisitos = fetch_requisitos(c.link, session)
        time.sleep(SLEEP_BETWEEN)

    csv_path = args.out
    json_path = write_outputs(convocatorias, csv_path)
    print(f"\n✓ {len(convocatorias)} convocatorias procesadas")
    print(f"  CSV : {csv_path}")
    print(f"  JSON: {json_path}")
    return 0


def main() -> int:
    _force_utf8_stdio()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, default=0, help="Limita cantidad de convocatorias a procesar (debug).")
    ap.add_argument("--out", type=Path, default=DEFAULT_CSV,
                    help=f"Ruta del CSV (también genera .json). Default: {DEFAULT_CSV}")
    args = ap.parse_args()
    return run(args)


if __name__ == "__main__":
    sys.exit(main())

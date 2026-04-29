"""Cliente reusable para invocar Deep Research Max de Google.

Diseñado para correr 1 o más prompts versionados en `prompts/`, esperar de manera
asíncrona, y guardar los outputs como markdown en `docs/research/_runs-deep-research/`
con frontmatter completo y banner de "síntesis de fuente externa".

Uso:
    python tools/deep-research/run.py <slug-del-prompt> [...]
    python tools/deep-research/run.py --all

Configurar `GEMINI_API_KEY` en `tools/deep-research/.env` antes de correr.
"""

from __future__ import annotations

import base64
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    from google import genai
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Falta el SDK de Google. Ejecuta: pip install -r tools/deep-research/requirements.txt"
    ) from exc

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


# Rutas absolutas estables (independiente del cwd al ejecutar)
TOOLS_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOLS_DIR.parent.parent
PROMPTS_DIR = TOOLS_DIR / "prompts"
ASSETS_DIR = REPO_ROOT / "docs" / "assets" / "research" / "deep-research-runs"
RUNS_DIR = REPO_ROOT / "docs" / "research" / "_runs-deep-research"

DEFAULT_AGENT = "deep-research-max-preview-04-2026"
DEFAULT_POLL_SECONDS = 10
DEFAULT_TIMEOUT_SECONDS = 60 * 60  # 60 min, máximo de Deep Research


# ─────────────────────────────────────────────────────────────────────────────
# Carga de prompts
# ─────────────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Prompt:
    """Prompt versionado leído desde un archivo markdown en `prompts/`."""

    slug: str
    titulo: str
    objetivo: str
    cuerpo: str
    archivo: Path

    @classmethod
    def desde_archivo(cls, ruta: Path) -> "Prompt":
        contenido = ruta.read_text(encoding="utf-8")
        frontmatter, cuerpo = _separar_frontmatter(contenido)
        return cls(
            slug=ruta.stem,
            titulo=frontmatter.get("titulo", ruta.stem),
            objetivo=frontmatter.get("objetivo", ""),
            cuerpo=cuerpo.strip(),
            archivo=ruta,
        )


def _separar_frontmatter(texto: str) -> tuple[dict[str, str], str]:
    """Parser minimal de frontmatter YAML (key: value, sin anidación)."""
    if not texto.startswith("---\n"):
        return {}, texto
    fin = texto.find("\n---\n", 4)
    if fin == -1:
        return {}, texto
    bloque = texto[4:fin]
    cuerpo = texto[fin + 5 :]
    fields: dict[str, str] = {}
    for linea in bloque.splitlines():
        if ":" in linea and not linea.startswith(" "):
            clave, _, valor = linea.partition(":")
            fields[clave.strip()] = valor.strip().strip('"')
    return fields, cuerpo


def cargar_prompt(slug: str) -> Prompt:
    ruta = PROMPTS_DIR / f"{slug}.md"
    if not ruta.exists():
        disponibles = sorted(p.stem for p in PROMPTS_DIR.glob("*.md"))
        raise FileNotFoundError(
            f"No existe el prompt '{slug}'. Disponibles: {', '.join(disponibles) or '(ninguno)'}"
        )
    return Prompt.desde_archivo(ruta)


def cargar_todos_los_prompts() -> list[Prompt]:
    return [Prompt.desde_archivo(p) for p in sorted(PROMPTS_DIR.glob("*.md"))]


# ─────────────────────────────────────────────────────────────────────────────
# Ejecución del agente
# ─────────────────────────────────────────────────────────────────────────────


def _crear_cliente() -> "genai.Client":
    if load_dotenv is not None:
        load_dotenv(TOOLS_DIR / ".env")
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit(
            "Falta GEMINI_API_KEY. Crea tools/deep-research/.env desde .env.example "
            "y agrega tu API key de https://aistudio.google.com/apikey"
        )
    # El SDK lee GOOGLE_API_KEY o GEMINI_API_KEY de env automáticamente
    os.environ.setdefault("GOOGLE_API_KEY", api_key)
    return genai.Client()


def ejecutar_prompt(
    prompt: Prompt,
    agent: str = DEFAULT_AGENT,
    poll_seconds: int = DEFAULT_POLL_SECONDS,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> dict:
    """Lanza un Deep Research task y hace polling hasta `completed`/`failed`.

    Devuelve un dict con metadata + outputs + citaciones.
    """
    client = _crear_cliente()

    print(f"\n[{prompt.slug}] Lanzando Deep Research Max...")
    print(f"[{prompt.slug}]   archivo: {prompt.archivo.relative_to(REPO_ROOT)}")
    print(f"[{prompt.slug}]   modelo:  {agent}")
    print(f"[{prompt.slug}]   tokens estimados de input: {len(prompt.cuerpo) // 4}")

    inicio = time.time()
    interaction = client.interactions.create(
        input=prompt.cuerpo,
        agent=agent,
        background=True,
        agent_config={
            "type": "deep-research",
            "thinking_summaries": "auto",
            "visualization": "auto",
            "collaborative_planning": False,
        },
    )
    print(f"[{prompt.slug}]   interaction_id: {interaction.id}")

    # Polling
    while True:
        transcurrido = time.time() - inicio
        if transcurrido > timeout_seconds:
            raise TimeoutError(
                f"[{prompt.slug}] Excedió timeout de {timeout_seconds}s sin completarse."
            )
        result = client.interactions.get(interaction.id)
        estado = getattr(result, "status", "in_progress")
        if estado == "completed":
            print(
                f"[{prompt.slug}] ✓ Completado en {int(transcurrido)}s "
                f"({transcurrido / 60:.1f} min)"
            )
            break
        if estado == "failed":
            err = getattr(result, "error", "(sin detalle)")
            raise RuntimeError(f"[{prompt.slug}] Falló: {err}")
        # Heartbeat cada poll
        print(
            f"[{prompt.slug}]   ... estado={estado} "
            f"({int(transcurrido)}s transcurridos)",
            flush=True,
        )
        time.sleep(poll_seconds)

    return _extraer_resultado(result, prompt, agent, transcurrido)


def _extraer_resultado(result, prompt: Prompt, agent: str, segundos: float) -> dict:
    """Normaliza outputs y citaciones a un dict serializable."""
    outputs_raw = getattr(result, "outputs", []) or []
    bloques_texto: list[str] = []
    imagenes: list[bytes] = []

    for out in outputs_raw:
        # SDK puede devolver dict o objeto; soportamos ambos
        tipo = _attr(out, "type")
        if tipo == "text":
            texto = _attr(out, "text") or ""
            if texto:
                bloques_texto.append(texto)
        elif tipo == "image":
            data_b64 = _attr(out, "data") or ""
            if data_b64:
                try:
                    imagenes.append(base64.b64decode(data_b64))
                except Exception:
                    pass

    citaciones_raw = getattr(result, "citations", None) or []
    citaciones = [c if isinstance(c, str) else _attr(c, "url", str(c)) for c in citaciones_raw]

    return {
        "interaction_id": getattr(result, "id", None),
        "agent": agent,
        "slug": prompt.slug,
        "titulo": prompt.titulo,
        "objetivo": prompt.objetivo,
        "duracion_segundos": int(segundos),
        "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "texto": "\n\n".join(bloques_texto),
        "imagenes": imagenes,
        "citaciones": citaciones,
    }


def _attr(obj, nombre, default=None):
    """Lee un atributo o key, soportando dict y objetos del SDK."""
    if isinstance(obj, dict):
        return obj.get(nombre, default)
    return getattr(obj, nombre, default)


# ─────────────────────────────────────────────────────────────────────────────
# Persistencia: markdown en docs/research/_runs-deep-research/
# ─────────────────────────────────────────────────────────────────────────────


def guardar_resultado(resultado: dict) -> Path:
    """Escribe el resultado como .md con frontmatter y banner correcto."""
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    fecha = resultado["fecha_utc"][:10]  # YYYY-MM-DD
    slug = resultado["slug"]
    nombre_archivo = f"{fecha}-{slug}.md"
    destino = RUNS_DIR / nombre_archivo

    # Imágenes: las guardamos como assets y las referenciamos
    referencias_imagen: list[str] = []
    for i, blob in enumerate(resultado["imagenes"], start=1):
        nombre_img = f"{fecha}-{slug}-{i:02d}.png"
        ruta_img = ASSETS_DIR / nombre_img
        ruta_img.write_bytes(blob)
        # Ruta relativa desde docs/research/_runs-deep-research/<file>.md
        rel = "../../assets/research/deep-research-runs/" + nombre_img
        referencias_imagen.append(f"![{nombre_img}]({rel})")

    contenido = _renderizar_markdown(resultado, referencias_imagen)
    destino.write_text(contenido, encoding="utf-8")
    print(f"[{slug}]   guardado en {destino.relative_to(REPO_ROOT)}")
    return destino


def _renderizar_markdown(resultado: dict, referencias_imagen: list[str]) -> str:
    titulo = resultado["titulo"] or resultado["slug"]
    fecha = resultado["fecha_utc"][:10]

    citaciones_md = ""
    if resultado["citaciones"]:
        items = "\n".join(f"- <{url}>" for url in resultado["citaciones"])
        citaciones_md = f"\n## Citaciones\n\n{items}\n"

    imagenes_md = ""
    if referencias_imagen:
        imagenes_md = "\n## Visualizaciones\n\n" + "\n\n".join(referencias_imagen) + "\n"

    return f"""---
title: "Run Deep Research: {titulo}"
description: "{_escapar(resultado['objetivo'])}"
autor: "Google Deep Research Max ({resultado['agent']})"
fecha: {fecha}
categoria: tecnologia
linea: transversal
tags:
  - research
  - deep-research
  - run
  - {resultado['slug']}
interaction_id: "{resultado['interaction_id']}"
duracion_segundos: {resultado['duracion_segundos']}
---

# Run Deep Research: {titulo}

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Output crudo del agente **Google Deep Research Max** (`{resultado['agent']}`).
    Ejecutado el {fecha} a partir del prompt `tools/deep-research/prompts/{resultado['slug']}.md`.
    **Verificar citaciones antes de citar en el pitch.**

> **Objetivo del prompt:** {resultado['objetivo'] or '(sin objetivo declarado)'}
>
> **Duración:** {resultado['duracion_segundos']} s ({resultado['duracion_segundos'] / 60:.1f} min) ·
> **Interaction ID:** `{resultado['interaction_id']}`

## Reporte

{resultado['texto'] or '*(el agente no devolvió texto)*'}
{imagenes_md}{citaciones_md}
---

*Próximo paso recomendado: revisar este reporte y promover los hallazgos accionables a notas estructuradas en `docs/research/<categoria>/<slug>.md`. No usar como fuente primaria sin verificar las citaciones.*
"""


def _escapar(s: str) -> str:
    return s.replace('"', '\\"').replace("\n", " ").strip()


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────


def listar_prompts() -> None:
    print("Prompts disponibles en tools/deep-research/prompts/:\n")
    for p in cargar_todos_los_prompts():
        print(f"  {p.slug}")
        if p.titulo:
            print(f"    título: {p.titulo}")
        if p.objetivo:
            print(f"    objetivo: {p.objetivo[:100]}{'...' if len(p.objetivo) > 100 else ''}")
        print()


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in {"-h", "--help", "help"}:
        print(__doc__)
        listar_prompts()
        return 0

    if argv[1] == "--list":
        listar_prompts()
        return 0

    if argv[1] == "--all":
        prompts = cargar_todos_los_prompts()
    else:
        prompts = [cargar_prompt(slug) for slug in argv[1:]]

    if not prompts:
        print("No hay prompts para ejecutar.")
        return 1

    print(f"Ejecutando {len(prompts)} prompt(s) secuencialmente.")
    print(f"Costo estimado: USD {len(prompts) * 5}-{len(prompts) * 7} (Max).")
    fallidos: list[str] = []
    for prompt in prompts:
        try:
            resultado = ejecutar_prompt(prompt)
            guardar_resultado(resultado)
        except Exception as exc:  # pragma: no cover
            print(f"[{prompt.slug}] ERROR: {exc}", file=sys.stderr)
            fallidos.append(prompt.slug)

    if fallidos:
        print(f"\n{len(fallidos)} fallaron: {', '.join(fallidos)}", file=sys.stderr)
        return 1
    print(f"\n✓ {len(prompts)} prompt(s) completados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

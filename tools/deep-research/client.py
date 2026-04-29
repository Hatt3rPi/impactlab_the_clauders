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


_CLIENT_SINGLETON: Optional["genai.Client"] = None


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


def obtener_cliente() -> "genai.Client":
    """Cliente singleton — evita re-instanciar entre pasos del flujo collaborative."""
    global _CLIENT_SINGLETON
    if _CLIENT_SINGLETON is None:
        _CLIENT_SINGLETON = _crear_cliente()
    return _CLIENT_SINGLETON


def _crear_y_esperar(
    *,
    prompt: "Prompt",
    agent: str,
    agent_config: dict,
    input_override: Optional[str] = None,
    previous_interaction_id: Optional[str] = None,
    poll_seconds: int = DEFAULT_POLL_SECONDS,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> tuple:
    """Crea una interaction y hace polling hasta `completed`. Devuelve (sdk_result, duracion)."""
    client = obtener_cliente()
    body = input_override if input_override is not None else prompt.cuerpo
    interaction = client.interactions.create(
        input=body,
        agent=agent,
        background=True,
        agent_config=agent_config,
        previous_interaction_id=previous_interaction_id,
    )
    print(f"[{prompt.slug}]   interaction_id: {interaction.id}")

    inicio = time.time()
    while True:
        transcurrido = time.time() - inicio
        if transcurrido > timeout_seconds:
            raise TimeoutError(
                f"[{prompt.slug}] Excedió timeout de {timeout_seconds}s sin completarse."
            )
        result = client.interactions.get(interaction.id)
        estado = getattr(result, "status", "in_progress")
        if estado == "completed":
            return result, transcurrido
        if estado == "failed":
            err = getattr(result, "error", "(sin detalle)")
            raise RuntimeError(f"[{prompt.slug}] Falló: {err}")
        print(
            f"[{prompt.slug}]   ... estado={estado} ({int(transcurrido)}s)",
            flush=True,
        )
        time.sleep(poll_seconds)


def ejecutar_prompt(
    prompt: Prompt,
    agent: str = DEFAULT_AGENT,
    poll_seconds: int = DEFAULT_POLL_SECONDS,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> dict:
    """Lanza un Deep Research task directo (sin collaborative planning) y espera el resultado."""
    print(f"\n[{prompt.slug}] Lanzando Deep Research Max (modo directo)...")
    print(f"[{prompt.slug}]   archivo: {prompt.archivo.relative_to(REPO_ROOT)}")
    print(f"[{prompt.slug}]   modelo:  {agent}")
    print(f"[{prompt.slug}]   tokens estimados de input: {len(prompt.cuerpo) // 4}")

    sdk_result, duracion = _crear_y_esperar(
        prompt=prompt,
        agent=agent,
        agent_config={
            "type": "deep-research",
            "thinking_summaries": "auto",
            "visualization": "auto",
            "collaborative_planning": False,
        },
        poll_seconds=poll_seconds,
        timeout_seconds=timeout_seconds,
    )
    print(
        f"[{prompt.slug}] ✓ Completado en {int(duracion)}s ({duracion / 60:.1f} min)"
    )
    return _extraer_resultado(sdk_result, prompt, agent, duracion, tipo_run="ejecucion-directa")


# ─────────────────────────────────────────────────────────────────────────────
# Flujo collaborative_planning
# ─────────────────────────────────────────────────────────────────────────────


def solicitar_plan(
    prompt: Prompt,
    *,
    previous_interaction_id: Optional[str] = None,
    feedback: Optional[str] = None,
    agent: str = DEFAULT_AGENT,
) -> dict:
    """Pide un plan al agente (collaborative_planning=True). Si hay previous_id + feedback, refina."""
    if previous_interaction_id and feedback:
        print(f"\n[{prompt.slug}] Refinando plan con tu feedback...")
        input_text = feedback
    else:
        print(f"\n[{prompt.slug}] Solicitando plan inicial al agente (no ejecuta queries todavía)...")
        input_text = prompt.cuerpo

    sdk_result, duracion = _crear_y_esperar(
        prompt=prompt,
        agent=agent,
        agent_config={
            "type": "deep-research",
            "thinking_summaries": "auto",
            "visualization": "auto",
            "collaborative_planning": True,
        },
        input_override=input_text,
        previous_interaction_id=previous_interaction_id,
    )
    print(f"[{prompt.slug}] ✓ Plan recibido en {int(duracion)}s ({duracion / 60:.1f} min)")
    tipo = "plan-refinado" if previous_interaction_id else "plan-inicial"
    return _extraer_resultado(sdk_result, prompt, agent, duracion, tipo_run=tipo)


def aprobar_y_ejecutar(
    prompt: Prompt,
    plan_interaction_id: str,
    *,
    agent: str = DEFAULT_AGENT,
) -> dict:
    """Aprueba un plan y ejecuta el research completo (donde se gastan los USD reales)."""
    print(f"\n[{prompt.slug}] Aprobando plan y ejecutando research completo (5-20 min)...")
    sdk_result, duracion = _crear_y_esperar(
        prompt=prompt,
        agent=agent,
        agent_config={
            "type": "deep-research",
            "thinking_summaries": "auto",
            "visualization": "auto",
            "collaborative_planning": False,
        },
        input_override=(
            "El plan se ve bien. Procede con la investigación completa siguiendo "
            "exactamente lo planteado en tu plan anterior."
        ),
        previous_interaction_id=plan_interaction_id,
    )
    print(
        f"[{prompt.slug}] ✓ Ejecución completada en {int(duracion)}s ({duracion / 60:.1f} min)"
    )
    resultado = _extraer_resultado(sdk_result, prompt, agent, duracion, tipo_run="ejecucion-aprobada")
    resultado["plan_interaction_id"] = plan_interaction_id
    return resultado


def flujo_collaborative(prompt: Prompt) -> Optional[dict]:
    """Loop interactivo: plan → revisar → (aprobar | refinar | cancelar)."""
    sep = "═" * 78
    print(f"\n{sep}")
    print(f"  COLLABORATIVE PLANNING — {prompt.slug}")
    print(f"  Verás el plan del agente antes de gastar la ejecución completa.")
    print(sep)

    plan = solicitar_plan(prompt)
    plan_path = guardar_resultado(plan, sufijo="-plan-00")
    contador_refinement = 0

    while True:
        _mostrar_plan(plan)
        print("\n  ¿Qué hacemos?")
        print("    [a] Aprobar y ejecutar  (~USD 3-7, 5-20 min)")
        print("    [r] Refinar el plan con feedback")
        print("    [c] Cancelar  (no se gasta nada más)")
        try:
            accion = input(f"\n  [{prompt.slug}] > ").strip().lower()
        except EOFError:
            print(f"\n[{prompt.slug}] Cancelado (EOF). Plan guardado en {plan_path.relative_to(REPO_ROOT)}")
            return None

        if accion in ("a", "aprobar", "ejecutar"):
            resultado = aprobar_y_ejecutar(prompt, plan["interaction_id"])
            return resultado
        if accion in ("c", "cancelar", "cancel", "salir"):
            print(
                f"\n[{prompt.slug}] Cancelado. "
                f"Plan guardado en {plan_path.relative_to(REPO_ROOT)} para referencia."
            )
            return None
        if accion in ("r", "refinar"):
            print("\n  Escribe tu feedback al agente (termina con línea vacía o Ctrl+D):")
            feedback = _leer_feedback_multilinea()
            if not feedback:
                print("  Sin feedback. Vuelvo a mostrar el plan.")
                continue
            contador_refinement += 1
            plan = solicitar_plan(
                prompt,
                previous_interaction_id=plan["interaction_id"],
                feedback=feedback,
            )
            plan_path = guardar_resultado(
                plan, sufijo=f"-plan-{contador_refinement:02d}"
            )
            continue

        print(f"  Opción no reconocida: {accion!r}. Usa 'a', 'r' o 'c'.")


def _mostrar_plan(plan: dict) -> None:
    sep = "═" * 78
    print(f"\n{sep}")
    print(f"  PLAN DEL AGENTE — {plan.get('titulo', plan.get('slug', ''))}")
    print(f"  interaction_id: {plan['interaction_id']}")
    print(f"  duración:       {plan['duracion_segundos']}s")
    print(f"  tipo:           {plan.get('tipo_run', 'plan')}")
    print(sep)
    texto = plan.get("texto") or "(plan vacío)"
    print(texto)
    if plan.get("citaciones"):
        print(f"\n  Citaciones referenciadas: {len(plan['citaciones'])}")
    print(sep)


def _leer_feedback_multilinea() -> str:
    lineas: list[str] = []
    while True:
        try:
            linea = input("  > ")
        except EOFError:
            break
        if linea == "":
            break
        lineas.append(linea)
    return "\n".join(lineas).strip()


def _extraer_resultado(
    result,
    prompt: Prompt,
    agent: str,
    segundos: float,
    *,
    tipo_run: str = "ejecucion-directa",
) -> dict:
    """Normaliza outputs y citaciones a un dict serializable.

    `tipo_run` distingue entre "plan-inicial", "plan-refinado", "ejecucion-aprobada",
    "ejecucion-directa". Se usa para elegir el banner correcto al renderizar markdown.
    """
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
        "tipo_run": tipo_run,
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


def guardar_resultado(resultado: dict, *, sufijo: str = "") -> Path:
    """Escribe el resultado como .md con frontmatter y banner correcto.

    `sufijo` se añade al nombre del archivo (sin punto). Útil para distinguir
    planes intermedios (ej: '-plan-00', '-plan-01') del archivo final.
    """
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    fecha = resultado["fecha_utc"][:10]  # YYYY-MM-DD
    slug = resultado["slug"]
    nombre_archivo = f"{fecha}-{slug}{sufijo}.md"
    destino = RUNS_DIR / nombre_archivo

    # Imágenes: las guardamos como assets y las referenciamos
    referencias_imagen: list[str] = []
    for i, blob in enumerate(resultado["imagenes"], start=1):
        nombre_img = f"{fecha}-{slug}{sufijo}-{i:02d}.png"
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
    tipo_run = resultado.get("tipo_run", "ejecucion-directa")
    es_plan = tipo_run.startswith("plan")

    citaciones_md = ""
    if resultado.get("citaciones"):
        items = "\n".join(f"- <{url}>" for url in resultado["citaciones"])
        citaciones_md = f"\n## Citaciones\n\n{items}\n"

    imagenes_md = ""
    if referencias_imagen:
        imagenes_md = "\n## Visualizaciones\n\n" + "\n\n".join(referencias_imagen) + "\n"

    plan_id_md = ""
    if resultado.get("plan_interaction_id"):
        plan_id_md = (
            f"> **Plan aprobado:** `{resultado['plan_interaction_id']}` "
            "(ver el archivo correspondiente con sufijo `-plan-NN` para la deliberación previa).\n>\n"
        )

    titulo_seccion = "Plan del agente" if es_plan else "Reporte"
    titulo_doc = (
        f"Plan Deep Research: {titulo}" if es_plan else f"Run Deep Research: {titulo}"
    )
    banner_titulo = (
        ":material-clipboard-text-outline: Plan colaborativo del agente (no es el reporte final)"
        if es_plan
        else ":material-book-open-variant: Síntesis de fuentes externas"
    )
    banner_cuerpo = (
        f"Plan generado por **Google Deep Research Max** (`{resultado['agent']}`) "
        f"antes de ejecutar el research completo. **Aún no se gastó la ejecución.** "
        "El equipo revisó este plan y decidió aprobar/refinar/cancelar."
        if es_plan
        else (
            f"Output crudo del agente **Google Deep Research Max** (`{resultado['agent']}`). "
            f"Ejecutado el {fecha} a partir del prompt "
            f"`tools/deep-research/prompts/{resultado['slug']}.md`. "
            "**Verificar citaciones antes de citar en el pitch.**"
        )
    )
    banner_admonition = "warning" if es_plan else "info"

    siguiente_paso = (
        "*Este archivo registra solo el plan inicial/refinado del agente. El reporte "
        "completo aprobado vive en el archivo `YYYY-MM-DD-<slug>.md` (sin sufijo).*"
        if es_plan
        else (
            "*Próximo paso recomendado: revisar este reporte y promover los hallazgos "
            "accionables a notas estructuradas en `docs/research/<categoria>/<slug>.md`. "
            "No usar como fuente primaria sin verificar las citaciones.*"
        )
    )

    return f"""---
title: "{titulo_doc}"
description: "{_escapar(resultado['objetivo'])}"
autor: "Google Deep Research Max ({resultado['agent']})"
fecha: {fecha}
categoria: tecnologia
linea: transversal
tipo_run: {tipo_run}
tags:
  - research
  - deep-research
  - {('plan' if es_plan else 'run')}
  - {resultado['slug']}
interaction_id: "{resultado['interaction_id']}"
duracion_segundos: {resultado['duracion_segundos']}
---

# {titulo_doc}

<!-- AUTO-BANNER -->
!!! {banner_admonition} "{banner_titulo}"
    {banner_cuerpo}

> **Objetivo del prompt:** {resultado['objetivo'] or '(sin objetivo declarado)'}
>
> **Duración:** {resultado['duracion_segundos']} s ({resultado['duracion_segundos'] / 60:.1f} min) ·
> **Interaction ID:** `{resultado['interaction_id']}` ·
> **Tipo:** `{tipo_run}`
{plan_id_md}
## {titulo_seccion}

{resultado['texto'] or '*(el agente no devolvió texto)*'}
{imagenes_md}{citaciones_md}
---

{siguiente_paso}
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
        print(
            "Modo collaborative_planning: agrega --plan para revisar el plan del agente\n"
            "antes de gastar la ejecución completa. Recomendado para prompts caros.\n"
        )
        listar_prompts()
        return 0

    args = list(argv[1:])
    modo_plan = False
    if "--plan" in args:
        args.remove("--plan")
        modo_plan = True

    if not args:
        print("Falta especificar el slug del prompt o --all / --list.")
        return 1

    if args[0] == "--list":
        listar_prompts()
        return 0

    if args[0] == "--all":
        prompts = cargar_todos_los_prompts()
    else:
        prompts = [cargar_prompt(slug) for slug in args]

    if not prompts:
        print("No hay prompts para ejecutar.")
        return 1

    modo_str = "COLLABORATIVE PLANNING (plan → revisar → aprobar)" if modo_plan else "directo"
    print(f"Ejecutando {len(prompts)} prompt(s) en modo {modo_str}.")
    if not modo_plan:
        print(f"Costo estimado: USD {len(prompts) * 3}-{len(prompts) * 7} (Max).")
    else:
        print(
            f"Costo estimado: USD {len(prompts) * 3}-{len(prompts) * 7} si apruebas todos.\n"
            "Si cancelas tras ver el plan, costo es ~USD 0,30 por plan generado."
        )

    fallidos: list[str] = []
    cancelados: list[str] = []
    completados: list[str] = []

    for prompt in prompts:
        try:
            if modo_plan:
                resultado = flujo_collaborative(prompt)
                if resultado is None:
                    cancelados.append(prompt.slug)
                    continue
            else:
                resultado = ejecutar_prompt(prompt)
            guardar_resultado(resultado)
            completados.append(prompt.slug)
        except Exception as exc:  # pragma: no cover
            print(f"[{prompt.slug}] ERROR: {exc}", file=sys.stderr)
            fallidos.append(prompt.slug)

    print(f"\nResumen:")
    print(f"  Completados: {len(completados)}  → {', '.join(completados) or '-'}")
    if cancelados:
        print(f"  Cancelados:  {len(cancelados)}  → {', '.join(cancelados)}")
    if fallidos:
        print(f"  Fallidos:    {len(fallidos)}  → {', '.join(fallidos)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

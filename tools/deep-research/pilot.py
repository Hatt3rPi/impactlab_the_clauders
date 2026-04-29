"""Wrapper CLI no-interactivo del flujo collaborative.

Permite ejecutar el ciclo plan → refine → approve desde scripts o desde un
agente que no tiene un teclado real para responder a `input()`.

Uso:
    python pilot.py plan <slug>
        → genera plan inicial. Imprime interaction_id y plan.

    python pilot.py refine <slug> <previous_id> "<feedback>"
        → genera plan refinado a partir del previous_id.

    python pilot.py approve <slug> <plan_id>
        → aprueba el plan y ejecuta el research completo (cobra USD 3-7).

Cada paso guarda automáticamente el resultado en
docs/research/_runs-deep-research/.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Asegura que `client` se pueda importar al ejecutar como script
sys.path.insert(0, str(Path(__file__).resolve().parent))

from client import (  # noqa: E402
    aprobar_y_ejecutar,
    cargar_prompt,
    guardar_resultado,
    recuperar_resultado,
    solicitar_plan,
)


def _imprimir_resumen(resultado: dict) -> None:
    sep = "=" * 78
    print(f"\n{sep}")
    print(f"  TIPO:           {resultado.get('tipo_run', '?')}")
    print(f"  INTERACTION_ID: {resultado['interaction_id']}")
    print(f"  DURACIÓN:       {resultado['duracion_segundos']}s")
    print(sep)
    print(resultado.get("texto") or "(sin texto)")
    if resultado.get("citaciones"):
        print(f"\n  Citaciones: {len(resultado['citaciones'])}")
        for c in resultado["citaciones"][:20]:
            print(f"    - {c}")
        if len(resultado["citaciones"]) > 20:
            print(f"    ... ({len(resultado['citaciones']) - 20} más)")
    print(sep)


def cmd_plan(slug: str) -> int:
    prompt = cargar_prompt(slug)
    plan = solicitar_plan(prompt)
    ruta = guardar_resultado(plan, sufijo="-plan-00")
    print(f"\n[OK] Plan guardado en: {ruta}")
    _imprimir_resumen(plan)
    return 0


def cmd_refine(slug: str, previous_id: str, feedback: str, refinement_n: int) -> int:
    prompt = cargar_prompt(slug)
    plan = solicitar_plan(prompt, previous_interaction_id=previous_id, feedback=feedback)
    ruta = guardar_resultado(plan, sufijo=f"-plan-{refinement_n:02d}")
    print(f"\n[OK] Plan refinado guardado en: {ruta}")
    _imprimir_resumen(plan)
    return 0


def cmd_approve(slug: str, plan_id: str) -> int:
    prompt = cargar_prompt(slug)
    resultado = aprobar_y_ejecutar(prompt, plan_id)
    ruta = guardar_resultado(resultado)
    print(f"\n[OK] Reporte completo guardado en: {ruta}")
    _imprimir_resumen(resultado)
    return 0


def cmd_rescue(slug: str, interaction_id: str, tipo_run: str, sufijo: str) -> int:
    """Recupera un resultado ya completado en la API que se perdió localmente."""
    prompt = cargar_prompt(slug)
    resultado = recuperar_resultado(prompt, interaction_id, tipo_run=tipo_run)
    ruta = guardar_resultado(resultado, sufijo=sufijo)
    print(f"\n[OK] Resultado rescatado y guardado en: {ruta}")
    _imprimir_resumen(resultado)
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in {"-h", "--help", "help"}:
        print(__doc__)
        return 0

    cmd = argv[1]

    if cmd == "plan":
        if len(argv) != 3:
            print("Uso: pilot.py plan <slug>", file=sys.stderr)
            return 2
        return cmd_plan(argv[2])

    if cmd == "refine":
        if len(argv) < 5:
            print(
                'Uso: pilot.py refine <slug> <previous_id> "<feedback>" [n_refinement]',
                file=sys.stderr,
            )
            return 2
        n = int(argv[5]) if len(argv) > 5 else 1
        return cmd_refine(argv[2], argv[3], argv[4], n)

    if cmd == "approve":
        if len(argv) != 4:
            print("Uso: pilot.py approve <slug> <plan_id>", file=sys.stderr)
            return 2
        return cmd_approve(argv[2], argv[3])

    if cmd == "rescue":
        # rescue <slug> <interaction_id> [tipo_run] [sufijo]
        # tipo_run: plan-inicial | plan-refinado | ejecucion-aprobada | ejecucion-directa
        if len(argv) < 4:
            print(
                "Uso: pilot.py rescue <slug> <interaction_id> [tipo_run] [sufijo]",
                file=sys.stderr,
            )
            return 2
        tipo_run = argv[4] if len(argv) > 4 else "plan-inicial"
        sufijo = argv[5] if len(argv) > 5 else "-plan-00"
        return cmd_rescue(argv[2], argv[3], tipo_run, sufijo)

    print(f"Comando desconocido: {cmd!r}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

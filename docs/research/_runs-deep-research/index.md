---
title: "Runs de Deep Research"
description: "Outputs crudos de Google Deep Research Max ejecutados por el equipo. Cada run quedó versionado al pegar el resultado del cliente Python."
tags:
  - research
  - deep-research
---

# Runs de Deep Research

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../../convenciones-de-contenido.md).

Los archivos `YYYY-MM-DD-<slug>.md` aquí son **outputs crudos** del agente Google Deep Research Max ejecutados desde `tools/deep-research/`. Vive en este directorio para diferenciarlos de las notas de research consolidadas que escribe el equipo.

## Flujo

1. **Felipe ejecuta** `python tools/deep-research/run.py <slug>` con la API key configurada.
2. El cliente guarda el output aquí automáticamente con frontmatter completo y banner correcto.
3. El equipo **lee y discute** los outputs antes del Tollgate 1.
4. Los hallazgos accionables (no el reporte completo) se **promueven** a notas estructuradas en `docs/research/<categoria>/<slug>.md`.

## Cómo está estructurado cada run

Cada archivo lleva:

- Frontmatter con `interaction_id` (trazable a Google AI Studio), `duracion_segundos` y `agent`.
- Banner de "síntesis de fuente externa".
- Objetivo del prompt.
- Cuerpo del reporte tal cual lo devolvió el modelo.
- Visualizaciones generadas (si las hay).
- Citaciones de fuentes.

## Runs registrados

| Fecha | Run | Duración | Citaciones | Costo estimado |
|---|---|---|---|---|
| 2026-04-29 | [Money left on the table en Chile](2026-04-29-04-money-left-on-the-table.md) | ~10 min | 54 fuentes (CMF, Hacienda, AAFP, La Tercera, BioBío, etc.) | ~USD 5 |
| 2026-04-29 | [Ideas fuera del radar (15 ideas)](2026-04-29-01-ideas-fuera-del-radar.md) | ~18 min | 25 fuentes (CMF, Mintrab, MOP, BCN, Sup. Salud, etc.) + casos análogos UK/USA/Singapur/India/Brasil | ~USD 5 |

## Hallazgo operacional importante (29-abr-2026)

El primer run reveló que **`collaborative_planning: True` en el SDK preview de Google NO devuelve un plan corto** (como sugiere la doc) sino la **ejecución completa** del research. Implicancias:

1. El costo del paso "plan" es el costo de la ejecución completa (~USD 3-7), no los ~USD 0,30 que asumimos.
2. Para los siguientes prompts, **conviene ejecutarlos en modo directo** (`collaborative_planning: False`) y refinar via follow-ups con `previous_interaction_id` solo si el output amerita.
3. El cliente local crashea al imprimir caracteres unicode en cmd de Windows — corregido en commit posterior.

## Documentación de la herramienta

- [API Deep Research de Google · guía operativa](../herramientas/deep-research-google.md)
- README del cliente Python: `tools/deep-research/README.md` en el repo.
- Prompts versionados: `tools/deep-research/prompts/` en el repo.

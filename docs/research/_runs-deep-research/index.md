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

> Por ahora vacío. Se llena automáticamente al ejecutar el cliente.

| Fecha | Run | Duración | Tokens aprox | Costo aprox |
|---|---|---|---|---|
| — | — | — | — | — |

## Documentación de la herramienta

- [API Deep Research de Google · guía operativa](../herramientas/deep-research-google.md)
- README del cliente Python: `tools/deep-research/README.md` en el repo.
- Prompts versionados: `tools/deep-research/prompts/` en el repo.

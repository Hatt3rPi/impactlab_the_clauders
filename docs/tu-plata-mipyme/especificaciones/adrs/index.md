---
title: ADRs
description: Architecture Decision Records — las decisiones técnicas y por qué.
tags:
  - especificaciones
  - adrs
---

# ADRs — Architecture Decision Records

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../../../convenciones-de-contenido.md).

Registro **inmutable** de las decisiones técnicas relevantes del equipo. Cada ADR captura **una** decisión: el contexto, la decisión tomada, las consecuencias y las alternativas consideradas.

## Por qué ADRs

- Sirven de memoria del equipo: en seis meses, cualquiera entiende **por qué** algo está así.
- Reducen las re-discusiones sobre temas ya zanjados.
- Para el pitch: nos permiten explicar nuestras decisiones con seguridad.

## Convenciones

- Numeración secuencial: `0001`, `0002`, `0003`...
- Slug descriptivo: `0042-elegimos-postgres.md`.
- **Inmutables**: si cambia la decisión, escribir un ADR nuevo que diga `Supersedes 0042` y marcar el `0042` como `Estado: superado por 0099`.
- Plantilla en [`_template.md`](_template.md).

## Listado

| ID | Título | Estado | Fecha |
|---|---|---|---|
| [0001](0001-uso-de-adrs.md) | Uso de ADRs | Aceptado | 2026-04-29 |
| [0002](0002-linea-tematica-inclusion-financiera.md) | Selección de línea temática: Inclusión Financiera | Aceptado | 2026-04-29 |
| [0003](0003-plataforma-web-mobile-first.md) | Plataforma: web mobile-first (no app nativa) | Aceptado | 2026-04-29 |

## Estados posibles

- **Propuesto** — borrador, en discusión.
- **Aceptado** — vigente.
- **Rechazado** — se evaluó y se descartó.
- **Superado** — reemplazado por otro ADR (referenciar cuál).
- **Obsoleto** — la decisión ya no aplica (contexto cambió).

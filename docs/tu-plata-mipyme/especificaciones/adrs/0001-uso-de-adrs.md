---
title: "ADR 0001 — Uso de ADRs"
estado: "Aceptado"
fecha: 2026-04-29
autor: "The Clauders"
tags:
  - adr
  - meta
---

# ADR 0001 — Uso de ADRs

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Documento generado por el equipo The Clauders. Es fuente primaria para este tema.

## Contexto

El equipo trabajará en un sprint corto (48 h efectivas) con varias decisiones técnicas relevantes que se tomarán bajo presión: stack, modelo de Claude, patrón agéntico, datasets, hosting. Sin un registro:

- Las razones de cada decisión se pierden.
- Discusiones zanjadas se reabren.
- El pitch del 7 de mayo cuesta más porque no podemos justificar elecciones con seguridad.

## Decisión

Adoptamos **Architecture Decision Records (ADRs)** como mecanismo estándar para documentar decisiones técnicas y de producto que afecten a más de una persona.

- Vivirán en `docs/especificaciones/adrs/`.
- Numeración secuencial.
- Plantilla común en [`_template.md`](_template.md).
- Son **inmutables**: una decisión se reemplaza con un ADR nuevo, no se edita el viejo.

## Consecuencias

### Positivas

- Memoria del equipo: cualquiera (incluso quien no estuvo en la reunión) entiende el porqué.
- Pitch más sólido: tenemos las razones por escrito.
- Reducción de re-discusiones.

### Negativas / costos

- Pequeño overhead por decisión registrada (~5-10 minutos).
- Riesgo de **sobre-documentar** decisiones triviales.

### Neutras

- El equipo debe acordar **cuándo** una decisión amerita ADR (regla del pulgar: si afecta a más de una persona o se va a repreguntar, sí).

## Alternativas consideradas

### Opción A — Notas sueltas en cada reunión

- **Pros:** menor fricción.
- **Contras:** difícil encontrar la decisión después; no hay estado (vigente vs superada).
- **Razón de descarte:** vamos a tomar muchas decisiones técnicas y necesitamos un índice navegable.

### Opción B — Wiki en otra herramienta (Notion, Confluence)

- **Pros:** edición colaborativa más rica.
- **Contras:** se aleja del repo, pierde la trazabilidad con commits y código.
- **Razón de descarte:** queremos todo en git por reproducibilidad y deploy automático.

## Referencias

- Plantilla: [`_template.md`](_template.md).
- Convención: [adrs/index.md](index.md).

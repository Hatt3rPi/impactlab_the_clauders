---
title: Ideas
description: Tablero de ideas con scoring contra los criterios oficiales.
tags:
  - ideas
---

# Tablero de ideas

Pool **pre-evaluado** de ideas para el lab, derivado del [research del equipo](../research/index.md) (estrategia + deep research previos).

!!! info "Estado"
    El equipo eligió la línea **Inclusión Financiera** ([ADR 0002](../especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md)). De estas 9 ideas, **6 encajan en esa línea**, **2 pertenecen a líneas descartadas** (Ciberseg y Datos) y **1 está descartada-soft** (Open Finance Explainer, B2B). La decisión final cae sobre las primeras 3-4.

## Tabla maestra

Scoring sobre 100 (criterios oficiales) + bonus +5. Ver detalle en cada ficha.

| # | Idea | Línea | Tipo | Impacto (25) | Datos (20) | Claude (25) | Func (15) | Pitch (15) | Total | Estado |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [**Defensor**](defensor-dicom.md) :material-star: | Inclusión | Reactivo cobranza | 23,75 | 16,00 | 23,75 | 12,00 | 13,50 | **89,00** | :material-circle:{ style="color: limegreen" } activa, **estrella** |
| 2 | [Letra Chica / Tu Plata](letra-chica-cae.md) | Inclusión | Preventivo contrato | 22,50 | 16,00 | 22,50 | 11,25 | 14,25 | **86,50** | :material-circle:{ style="color: limegreen" } activa, plan B |
| 3 | [Mis Datos · ARCOP](mis-datos-arcop.md) | **Datos** | Empoderamiento | 22,50 | 19,00 | 21,25 | 11,25 | 12,00 | **86,00** | :material-circle:{ style="color: dodgerblue" } fuera de línea |
| 4 | [Antiestafa / Pillo](antiestafa-pillo.md) | **Ciberseg** | Antifraude | 23,75 | 15,00 | 20,00 | 12,75 | 13,50 | **85,00** | :material-circle:{ style="color: dodgerblue" } fuera de línea |
| 5 | [Mi Plan B](mi-plan-b-sobreendeudamiento.md) | Inclusión | Sobreendeudamiento | 22,50 | 15,00 | 22,50 | 11,25 | 12,00 | **83,25** | :material-circle:{ style="color: gold" } solapa con Defensor |
| 6 | [Tu Plata Mipyme](tu-plata-mipyme.md) | Inclusión | Microemprendedores | 21,25 | 16,00 | 22,50 | 11,25 | 12,00 | **83,00** | :material-circle:{ style="color: limegreen" } activa, plan C |
| 7 | [ConfíaConmigo](confiaconmigo-migrantes.md) | Inclusión | Migrantes | 21,25 | 15,00 | 20,00 | 10,50 | 12,00 | **78,75** | :material-circle:{ style="color: gold" } refinamiento |
| 8 | [Mi Pensión](mi-pension.md) | Inclusión | Previsional | 21,25 | 15,00 | 20,00 | 10,50 | 11,25 | **78,00** | :material-circle:{ style="color: gold" } refinamiento |
| 9 | [Open Finance Explainer](open-finance-explainer.md) | Inclusión | B2B | 15,00 | 17,00 | 18,75 | 12,00 | 8,25 | **71,00** | :material-circle:{ style="color: lightgray" } descartada-soft |

> Scoring inicial heurístico sobre la base del research previo y la guía estratégica. Ajustar tras spike técnico, entrevistas y validación con mentores.

## Top 3 candidatas dentro de la línea

1. :material-star: **Defensor** (89,00) — segmento más numeroso, cuatro capacidades de Claude juntas, ya recomendada por la estrategia.
2. **Letra Chica / Tu Plata** (86,50) — demo más visual, dolor del 80 %+ de la población.
3. **Tu Plata Mipyme** (83,00) — cruza inclusión con formalización SII, mentores potenciales en SII/SERCOTEC.

## Tensión a resolver con el equipo

- :material-alert: **Mis Datos · ARCOP** (86,00) tiene **score muy alto** y ataca un dolor del top 2 del scoring deep research, pero requiere **cambio de línea temática**. Si en próximas reuniones aparece evidencia clara de mejor encaje (mentores, datasets, demo), se podría revisar el [ADR 0002](../especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md).
- :material-alert: **Antiestafa / Pillo** (85,00) similar situación: gran score en su línea pero fuera de la elegida.

## Cómo proceder

1. **Esta semana:** cada miembro lee las 3 candidatas top y trae una **objeción concreta** o **enriquecimiento** (entrevista con un usuario potencial, dato faltante, riesgo no contemplado).
2. **Próxima reunión técnica:** decidir entre Defensor / Letra Chica / Tu Plata Mipyme.
3. **Decisión registrada como ADR 0004** apenas se cierre.
4. **Spike técnico** de la idea ganadora **antes del 5 de mayo**.

## Cómo agregar una idea nueva

1. Copiar [`_template.md`](_template.md) a `docs/ideas/<slug>.md`.
2. Llenar la plantilla (problema, hipótesis, scoring, esfuerzo).
3. Sumar la fila a la tabla maestra de arriba.
4. Etiquetar con la línea (`inclusion-financiera`, `ciberseguridad`, `proteccion-datos`).

## Estados

- :material-circle:{ style="color: limegreen" } **Activa** — en evaluación.
- :material-circle:{ style="color: gold" } **En refinamiento** — necesita más research.
- :material-circle:{ style="color: dodgerblue" } **Fuera de línea** — pertenece a otra línea temática.
- :material-circle:{ style="color: lightgray" } **Descartada-soft** — backlog post-lab.
- ⚪ **Archivada** — descartada totalmente (mover a `archivadas/`).

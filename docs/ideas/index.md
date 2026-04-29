---
title: Ideas
description: Tablero de ideas con scoring contra los criterios oficiales.
tags:
  - ideas
---

# Tablero de ideas

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../convenciones-de-contenido.md).

Pool **pre-evaluado** de ideas para el lab, derivado del [research del equipo](../research/index.md) (estrategia + deep research previos) más una idea unificadora emergente.

!!! info "Estado"
    El equipo eligió la línea **Inclusión Financiera** ([ADR 0002](../especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md)). De estas **10 ideas**, 1 es **unificadora** ([sabidurIA ciudadana](sabiduria-ciudadana.md)), **6 encajan** en la línea como casos individuales, **2 pertenecen a líneas descartadas** (Ciberseg y Datos) y **1 está descartada-soft** (Open Finance Explainer, B2B). Todas siguen en validación del equipo hasta el [Tollgate 1](../equipo/proceso-y-hoja-de-ruta.md#tollgate-1-entre-discovery-y-diseno).

## Idea unificadora: sabidurIA ciudadana

[**sabidurIA ciudadana**](sabiduria-ciudadana.md) es una **wiki de la vida del ciudadano chileno**: una sola web que recibe lo que estás viviendo en lenguaje natural y te devuelve qué derechos, beneficios, trámites y datos te tocan, citando la normativa. Surgió en conversación al revisar el research del equipo y notar que las 9 ideas previas son **casos particulares** del mismo motor.

| | Ideas individuales (las 9) | sabidurIA ciudadana |
|---|---|---|
| **Alcance** | Un evento o nicho | Cualquier evento de vida, con módulos progresivos |
| **Métrica de pitch** | "Resolvemos X" | "Cada chileno cruza ~12 eventos de éstos en su vida; los traducimos todos" |
| **Demo** | Producto único terminado | Motor agéntico + 2-3 módulos brutalmente bien + roadmap visible |
| **Diferenciación frente a 200 equipos** | "Otro RAG sobre regulación" | Mapa vital con motor transversal |

**Las 9 fichas siguen vigentes y standalone** — si el equipo decide construir solo una en vez de la unificadora, no se pierde nada. Si decide ir por sabidurIA, las 9 sirven como **especificación detallada** de los módulos correspondientes.

## Tabla maestra

Scoring sobre 100 (criterios oficiales) + bonus +5. Ver detalle en cada ficha.

| # | Idea | Línea | Tipo | Impacto (25) | Datos (20) | Claude (25) | Func (15) | Pitch (15) | Total | Estado |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | [**sabidurIA ciudadana**](sabiduria-ciudadana.md) :material-star: | Inclusión | **Unificadora** (wiki de la vida) | 23,75 | 17,00 | 23,75 | 11,25 | 13,50 | **89,25** | :material-circle:{ style="color: limegreen" } activa, **unificadora** |
| 1 | [Defensor](defensor-dicom.md) | Inclusión | Reactivo cobranza | 23,75 | 16,00 | 23,75 | 12,00 | 13,50 | **89,00** | :material-circle:{ style="color: limegreen" } activa |
| 2 | [Letra Chica / Tu Plata](letra-chica-cae.md) | Inclusión | Preventivo contrato | 22,50 | 16,00 | 22,50 | 11,25 | 14,25 | **86,50** | :material-circle:{ style="color: limegreen" } activa |
| 3 | [Mis Datos · ARCOP](mis-datos-arcop.md) | **Datos** | Empoderamiento | 22,50 | 19,00 | 21,25 | 11,25 | 12,00 | **86,00** | :material-circle:{ style="color: dodgerblue" } fuera de línea |
| 4 | [Antiestafa / Pillo](antiestafa-pillo.md) | **Ciberseg** | Antifraude | 23,75 | 15,00 | 20,00 | 12,75 | 13,50 | **85,00** | :material-circle:{ style="color: dodgerblue" } fuera de línea |
| 5 | [Mi Plan B](mi-plan-b-sobreendeudamiento.md) | Inclusión | Sobreendeudamiento | 22,50 | 15,00 | 22,50 | 11,25 | 12,00 | **83,25** | :material-circle:{ style="color: gold" } solapa con Defensor |
| 6 | [Tu Plata Mipyme](tu-plata-mipyme.md) | Inclusión | Microemprendedores | 21,25 | 16,00 | 22,50 | 11,25 | 12,00 | **83,00** | :material-circle:{ style="color: limegreen" } activa |
| 7 | [ConfíaConmigo](confiaconmigo-migrantes.md) | Inclusión | Migrantes | 21,25 | 15,00 | 20,00 | 10,50 | 12,00 | **78,75** | :material-circle:{ style="color: gold" } refinamiento |
| 8 | [Mi Pensión](mi-pension.md) | Inclusión | Previsional | 21,25 | 15,00 | 20,00 | 10,50 | 11,25 | **78,00** | :material-circle:{ style="color: gold" } refinamiento |
| 9 | [Open Finance Explainer](open-finance-explainer.md) | Inclusión | B2B | 15,00 | 17,00 | 18,75 | 12,00 | 8,25 | **71,00** | :material-circle:{ style="color: lightgray" } descartada-soft |

> Scoring inicial heurístico sobre la base del research previo y la guía estratégica. Ajustar tras spike técnico, entrevistas y validación con mentores.

## Candidatas top dentro de la línea

- :material-star: **sabidurIA ciudadana** (89,25) — apuesta unificadora; demo de 2-3 módulos brutalmente bien hechos + roadmap visible.
- **Defensor** (89,00) — segmento más numeroso, cuatro capacidades de Claude juntas, ya recomendada por la estrategia. Funciona como módulo dentro de sabidurIA o como producto único.
- **Letra Chica / Tu Plata** (86,50) — demo más visual, dolor del 80 %+ de la población. Funciona como módulo o producto único.
- **Tu Plata Mipyme** (83,00) — cruza inclusión con formalización SII, mentores potenciales en SII/SERCOTEC. Funciona como módulo o producto único.

## Tensiones a resolver con el equipo

- :material-alert: **Apuesta unificadora vs caso particular.** sabidurIA tiene mayor amplitud y mejor pitch, pero más riesgo de alcance. Defensor/Letra Chica son más acotadas, más seguras de demostrar end-to-end. Decisión clave en el [Tollgate 1](../equipo/proceso-y-hoja-de-ruta.md#tollgate-1-entre-discovery-y-diseno).
- :material-alert: **Mis Datos · ARCOP** (86,00) ataca un dolor del top 2 del scoring deep research, pero requiere **cambio de línea temática**. Si emerge evidencia clara, se revisa el [ADR 0002](../especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md).
- :material-alert: **Antiestafa / Pillo** (85,00) similar situación: gran score en su línea pero fuera de la elegida.

## Cómo proceder

1. **Esta semana:** cada miembro lee la idea unificadora + las 3 candidatas top individuales y trae una **objeción concreta** o **enriquecimiento** (entrevista con un usuario potencial, dato faltante, riesgo no contemplado).
2. **Próxima reunión técnica:** decidir entre **sabidurIA ciudadana** (apuesta unificadora) y las **3 candidatas individuales** (Defensor / Letra Chica / Tu Plata Mipyme).
3. **Decisión registrada como ADR 0004** apenas se cierre el [Tollgate 1](../equipo/proceso-y-hoja-de-ruta.md#tollgate-1-entre-discovery-y-diseno).
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

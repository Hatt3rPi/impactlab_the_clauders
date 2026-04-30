---
title: Ideas
description: Tablero de ideas con scoring contra los criterios oficiales.
tags:
  - ideas
---

# Tablero de ideas

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../../convenciones-de-contenido.md).

Pool de **25 ideas** para el lab, todas con ficha individual y scoring formal contra los 5 criterios oficiales. Provienen de tres fuentes:

- **9 ideas individuales originales** del [research previo del equipo](../research/index.md) (estrategia + deep research de Calibria).
- **1 idea unificadora** ([sabidurIA ciudadana](sabiduria-ciudadana.md)) emergida de conversación al revisar el research.
- **15 ideas adicionales** del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md), inspiradas en casos comparables de UK, USA, Singapur, India, Brasil, Países Bajos, México.

!!! info "Estado"
    El equipo eligió la línea **Inclusión Financiera** ([ADR 0002](../../tu-plata-mipyme/especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md)). De estas 25 ideas, **22 encajan en esa línea**, **2 pertenecen a líneas descartadas** (Mis Datos · ARCOP en Datos, Antiestafa / Pillo en Ciberseg) y **1 está descartada-soft** (Open Finance Explainer, B2B). Todas siguen en validación hasta el [Tollgate 1](../../equipo/proceso-y-hoja-de-ruta.md#tollgate-1-entre-discovery-y-diseno).

## Idea unificadora: sabidurIA ciudadana

[**sabidurIA ciudadana**](sabiduria-ciudadana.md) es una **wiki de la vida del ciudadano chileno**: una sola web que recibe lo que estás viviendo en lenguaje natural y te devuelve qué derechos, beneficios, trámites y datos te tocan, citando la normativa.

Las **24 ideas individuales** son **casos particulares** (módulos potenciales) del mismo motor. Si el equipo elige sabidurIA, **2-3 módulos brutalmente bien hechos** componen el demo y los demás quedan como roadmap visible.

| | Ideas individuales (las 24) | sabidurIA ciudadana |
|---|---|---|
| **Alcance** | Un evento o nicho | Cualquier evento de vida, con módulos progresivos |
| **Métrica de pitch** | "Resolvemos X" | "Cada chileno cruza ~12 eventos de éstos en su vida; los traducimos todos" |
| **Demo** | Producto único terminado | Motor agéntico + 2-3 módulos brutalmente bien + roadmap visible |
| **Diferenciación frente a 200 equipos** | "Otro RAG sobre regulación" | Mapa vital con motor transversal |

## Tabla maestra (25 ideas, ordenadas por score)

Scoring sobre 100 (criterios oficiales) + bonus +5. **Heurístico inicial** — ajustar tras spike técnico, entrevistas y validación.

| # | Idea | Línea | Tipo | Impacto (25) | Datos (20) | Claude (25) | Func (15) | Pitch (15) | Total | Estado |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [**Rescate Ciudadano**](rescate-ciudadano-acreencias.md) :material-star: | Inclusión | Acreencias bancarias | 23,75 | 17,00 | 22,50 | 12,00 | 14,25 | **89,50** | :material-circle:{ style="color: limegreen" } activa, top |
| 2 | [**sabidurIA ciudadana**](sabiduria-ciudadana.md) :material-star: | Inclusión | **Unificadora** | 23,75 | 17,00 | 23,75 | 11,25 | 13,50 | **89,25** | :material-circle:{ style="color: limegreen" } activa, **unificadora** |
| 3 | [Defensor (DICOM)](defensor-dicom.md) | Inclusión | Reactivo cobranza | 23,75 | 16,00 | 23,75 | 12,00 | 13,50 | **89,00** | :material-circle:{ style="color: limegreen" } activa |
| 4 | [**Legado Claro / Herencia Bot**](legado-claro-herencias.md) :material-star: | Inclusión | Post-mortem | 23,75 | 16,00 | 23,75 | 11,25 | 13,50 | **88,25** | :material-circle:{ style="color: limegreen" } activa, top |
| 5 | [Letra Chica / Tu Plata](letra-chica-cae.md) | Inclusión | Preventivo contrato | 22,50 | 16,00 | 22,50 | 11,25 | 14,25 | **86,50** | :material-circle:{ style="color: limegreen" } activa |
| 6 | [Mis Datos · ARCOP](mis-datos-arcop.md) | **Datos** | Empoderamiento | 22,50 | 19,00 | 21,25 | 11,25 | 12,00 | **86,00** | :material-circle:{ style="color: dodgerblue" } fuera de línea |
| 7 | [GES-Claim](ges-claim-salud-retroactiva.md) | Inclusión | Salud retroactiva | 23,75 | 15,00 | 22,50 | 11,25 | 13,50 | **86,00** | :material-circle:{ style="color: limegreen" } activa |
| 8 | [RutaJusta](rutajusta-ley-uber.md) | Inclusión | Ley Uber | 21,25 | 16,00 | 23,75 | 11,25 | 13,50 | **85,75** | :material-circle:{ style="color: limegreen" } activa |
| 9 | [Antiestafa / Pillo](antiestafa-pillo.md) | **Ciberseg** | Antifraude | 23,75 | 15,00 | 20,00 | 12,75 | 13,50 | **85,00** | :material-circle:{ style="color: dodgerblue" } fuera de línea |
| 10 | [CuidaDerechos](cuidaderechos-cuidadoras.md) | Inclusión | Cuidadoras | 23,75 | 15,00 | 21,25 | 10,50 | 13,50 | **84,00** | :material-circle:{ style="color: limegreen" } activa |
| 11 | [Agua Comunitaria / APR-Bot](agua-comunitaria-apr.md) | Inclusión | Rural APR | 22,50 | 15,00 | 21,25 | 11,25 | 13,50 | **83,50** | :material-circle:{ style="color: limegreen" } activa |
| 12 | [Mi Plan B](mi-plan-b-sobreendeudamiento.md) | Inclusión | Sobreendeudamiento | 22,50 | 15,00 | 22,50 | 11,25 | 12,00 | **83,25** | :material-circle:{ style="color: gold" } solapa con Defensor |
| 13 | [EmancipIA / Despegue](emancipia-egresados-sename.md) | Inclusión | Egresados SENAME | 22,50 | 14,00 | 22,50 | 10,50 | 13,50 | **83,00** | :material-circle:{ style="color: limegreen" } activa |
| 14 | [Tu Plata Mipyme](tu-plata-mipyme.md) | Inclusión | Microemprendedores | 21,25 | 16,00 | 22,50 | 11,25 | 12,00 | **83,00** | :material-circle:{ style="color: limegreen" } activa |
| 15 | [Re-Inicia](re-inicia-quiebra-personal.md) | Inclusión | Quiebra personal | 21,25 | 15,00 | 22,50 | 10,50 | 12,00 | **81,25** | :material-circle:{ style="color: limegreen" } activa |
| 16 | [Viuda Protegida](viuda-protegida-pension.md) | Inclusión | Pensión sobrevivencia | 22,50 | 15,00 | 20,00 | 10,50 | 12,00 | **80,00** | :material-circle:{ style="color: gold" } refinamiento |
| 17 | [Voz Financiera](voz-financiera-accesibilidad.md) | Inclusión | Accesibilidad visual | 21,25 | 15,00 | 21,25 | 10,50 | 12,00 | **80,00** | :material-circle:{ style="color: gold" } refinamiento |
| 18 | [Retención Alimentos](retencion-alimentos.md) | Inclusión | Violencia económica | 22,50 | 14,00 | 20,00 | 9,75 | 13,50 | **79,75** | :material-circle:{ style="color: gold" } refinamiento |
| 19 | [ConfíaConmigo (migrantes)](confiaconmigo-migrantes.md) | Inclusión | Migrantes | 21,25 | 15,00 | 20,00 | 10,50 | 12,00 | **78,75** | :material-circle:{ style="color: gold" } refinamiento |
| 20 | [Mi Pensión](mi-pension.md) | Inclusión | Previsional | 21,25 | 15,00 | 20,00 | 10,50 | 11,25 | **78,00** | :material-circle:{ style="color: gold" } refinamiento |
| 21 | [Cosecha Justa](cosecha-justa-temporeros.md) | Inclusión | Temporeros | 21,25 | 13,00 | 18,75 | 10,50 | 12,00 | **75,50** | :material-circle:{ style="color: gold" } refinamiento |
| 22 | [Respiro CAE](respiro-cae-desertores.md) | Inclusión | Desertores universitarios | 20,00 | 14,00 | 18,75 | 10,50 | 12,00 | **75,25** | :material-circle:{ style="color: gold" } refinamiento |
| 23 | [Feria Legal](feria-legal-ambulantes.md) | Inclusión | Ambulantes | 20,00 | 14,00 | 18,75 | 9,75 | 11,25 | **73,75** | :material-circle:{ style="color: gold" } refinamiento |
| 24 | [Talento Tributa](talento-tributa-creadores.md) | Inclusión | Creadores / e-sports | 18,75 | 14,00 | 18,75 | 10,50 | 11,25 | **73,25** | :material-circle:{ style="color: gold" } refinamiento |
| 25 | [Open Finance Explainer](open-finance-explainer.md) | Inclusión | B2B | 15,00 | 17,00 | 18,75 | 12,00 | 8,25 | **71,00** | :material-circle:{ style="color: lightgray" } descartada-soft |

> Scoring inicial heurístico **del piloto** (no del equipo). Ajustar tras spike técnico, entrevistas y validación con mentores. Las 15 últimas en estado "refinamiento" provienen del run Deep Research #01 del 29-abr.

## Top 7 dentro de la línea (los que merecen lectura del equipo esta semana)

1. :material-star: **Rescate Ciudadano** (89,50) — demo *wow* en vivo: dinero recuperado en 60 s. Módulo natural de sabidurIA.
2. :material-star: **sabidurIA ciudadana** (89,25) — apuesta unificadora; demo de 2-3 módulos brutalmente bien + roadmap visible.
3. **Defensor** (89,00) — segmento más numeroso (3,9 M morosos), 4 capacidades de Claude juntas. Funciona como módulo o standalone.
4. :material-star: **Legado Claro** (88,25) — cubre el gap 41 % AFP herencias. Módulo natural de sabidurIA.
5. **Letra Chica / Tu Plata** (86,50) — demo más visual, dolor del 80 %+ de la población.
6. **GES-Claim** (86,00) — sale del nicho fintech, entra a salud financiera. Dolor universal.
7. **RutaJusta** (85,75) — narrativa única ("IA del trabajador audita IA del empleador").

## Tensiones a resolver con el equipo

- :material-alert: **Apuesta unificadora vs casos individuales.** sabidurIA tiene mayor amplitud y mejor pitch, pero más riesgo de alcance. Los casos individuales son más acotados, más seguros de demostrar end-to-end. Decisión clave en el [Tollgate 1](../../equipo/proceso-y-hoja-de-ruta.md#tollgate-1-entre-discovery-y-diseno).
- :material-alert: **Mis Datos · ARCOP** (86,00) y **Antiestafa / Pillo** (85,00) tienen score alto pero pertenecen a líneas descartadas. Si emerge evidencia clara, se revisa el [ADR 0002](../../tu-plata-mipyme/especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md).
- :material-alert: **15 ideas con scoring del piloto** (de Rescate Ciudadano para abajo en el listado del run #01) — el equipo debe validar el scoring asignado y ajustar antes del Tollgate 1.

## Cómo proceder

1. **Esta semana:** cada miembro lee:
    - El **top 7 con sus fichas** y trae una **objeción concreta** o **enriquecimiento** (entrevista con un usuario potencial, dato faltante, riesgo no contemplado).
    - El [catálogo emergente original](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md) si quiere ver casos análogos internacionales completos.
2. **Próxima reunión técnica:** decidir entre **sabidurIA ciudadana** (apuesta unificadora) y las **3-5 candidatas individuales** (Rescate Ciudadano, Defensor, Legado Claro, Letra Chica, GES-Claim).
3. **Decisión registrada como ADR 0004** apenas se cierre el [Tollgate 1](../../equipo/proceso-y-hoja-de-ruta.md#tollgate-1-entre-discovery-y-diseno).
4. **Spike técnico** de la idea ganadora **antes del 5 de mayo**.

## Cómo agregar una idea nueva

1. Copiar [`_template.md`](_template.md) a `docs/ideas-evaluadas/<slug>.md`.
2. Llenar la plantilla (problema, hipótesis, scoring, esfuerzo).
3. Sumar la fila a la tabla maestra de arriba.
4. Etiquetar con la línea (`inclusion-financiera`, `ciberseguridad`, `proteccion-datos`).

## Estados

- :material-circle:{ style="color: limegreen" } **Activa** — en evaluación.
- :material-circle:{ style="color: gold" } **En refinamiento** — necesita más research / validación del equipo.
- :material-circle:{ style="color: dodgerblue" } **Fuera de línea** — pertenece a otra línea temática.
- :material-circle:{ style="color: lightgray" } **Descartada-soft** — backlog post-lab.
- ⚪ **Archivada** — descartada totalmente (mover a [`archivadas/`](archivadas/index.md)).

## Referencia histórica

El catálogo emergente original con detalle por idea (problema, datasets, demo imaginado, capacidades Claude, gap local, casos análogos internacionales, riesgo) sigue disponible como referencia: [15 ideas fuera del radar (run #01)](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

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

Pool **pre-evaluado** de ideas para el lab, derivado del [research del equipo](../research/index.md) (estrategia + deep research previos) más una idea unificadora emergente y 15 ideas adicionales del [run Deep Research del 29-abr](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

!!! info "Estado"
    El equipo eligió la línea **Inclusión Financiera** ([ADR 0002](../especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md)).

    **Total: 25 ideas** divididas en dos grupos:

    - **10 ideas con ficha completa** y scoring formal ([Tabla maestra](#tabla-maestra)): 1 unificadora ([sabidurIA](sabiduria-ciudadana.md)), 6 en línea, 2 fuera de línea, 1 descartada-soft.
    - **15 ideas emergentes** del run Deep Research #01 ([Tabla emergentes](#ideas-emergentes-del-run-01-pendientes-de-validacion)) sin scoring formal todavía. **Pendientes de discutir en próxima reunión.**

    Todas siguen en validación hasta el [Tollgate 1](../equipo/proceso-y-hoja-de-ruta.md#tollgate-1-entre-discovery-y-diseno).

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

## Ideas emergentes del run #01 (pendientes de validación)

15 ideas adicionales generadas por [Google Deep Research Max el 29-abr-2026](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md), inspiradas en casos comparables de UK, USA, Singapur, India, Brasil, Países Bajos, México. **Sin scoring formal todavía** — el equipo debe evaluarlas en próxima reunión y promover las que merezcan ficha standalone a la [Tabla maestra](#tabla-maestra).

### Top 2 según mi lectura como piloto (módulos perfectos de sabidurIA)

| # | Idea | Línea | Por qué destaca |
|---|---|---|---|
| **E1** :material-star: | **Rescate Ciudadano / Bombero Pyme** | Inclusión | Demo wow: subes cédula → encuentras CLP en acreencias bancarias en vivo (CLP 106.845 M en pozo 2026, caduca a Bomberos en 3 años). Cubre cifra del [run #04](../research/usuarios/transferencias-no-activadas-chile-2026.md). |
| **E2** :material-star: | **Legado Claro / Herencia Bot** | Inclusión | Cubre directamente el gap 41 % AFP fallecidos. Foto cert. defunción → cronograma de trámites. **Match perfecto con módulo Legado de sabidurIA.** |

### Top 5 según el agente Deep Research

1. **Rescate Ciudadano** — momento *wow* en demo (recuperar plata real en 60 s).
2. **Agua Comunitaria / APR-Bot** — desmarque temático absoluto (>2 M chilenos abastecidos por APR rurales).
3. **RutaJusta / Algoritmo Transparente** — Vision audita screenshots Uber/Rappi. "IA del trabajador audita IA del empleador".
4. **CuidaDerechos** — sub-segmento 100 % invisible (cuidadoras informales). $32.991/mes activable.
5. **GES-Claim** — activación retroactiva cobertura GES sobre boletas médicas. Salud financiera.

### Las 15 emergentes completas

| # | Idea | Línea | Sub-segmento | Cifra ancla |
|---|---|---|---|---|
| E1 | [Rescate Ciudadano](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md#categoría-1--reclamación-de-beneficios-y-fondos-olvidados) :material-star: | Inclusión | Mipymes quebradas + adultos mayores | CLP 106.845 M en acreencias 2026 |
| E2 | [Legado Claro / Herencia Bot](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md#categoría-3--transiciones-de-vida-críticas-y-vulnerabilidad-absoluta) :material-star: | Inclusión | Viudas, hijos de fallecidos | Gap 41 % AFP = CLP 93.000 M |
| E3 | CuidaDerechos | Inclusión | Cuidadoras informales NSE D-E | $32.991/mes (Ley 21.380) |
| E4 | RutaJusta | Inclusión | Repartidores Uber/Rappi/PedidosYa | Ley 21.431 + 1,2× IMM |
| E5 | GES-Claim | Inclusión | Familias dx catastrófico | Copago 0-20 % GES vs particular |
| E6 | EmancipIA / Despegue | Inclusión | Egresados SENAME 17-19 | Roleplay anti-CAE 40 % TMC |
| E7 | Re-Inicia | Inclusión | Ex-presos + microemprendedores quebrados | Ley 21.563 quiebra autoservicio |
| E8 | Viuda Protegida | Inclusión | Viudas <65 sin historial cotización | Pensión sobrevivencia AFP + SUSESO |
| E9 | Agua Comunitaria / APR-Bot | Inclusión | Tesoreros comités APR | >2 M chilenos abastecidos |
| E10 | Cosecha Justa | Inclusión | Temporeros agrícolas | SMS-first, denuncia anónima DT |
| E11 | Retención Alimentos | Inclusión | Madres con sentencia impaga | Ley 21.484 ejecución embargo |
| E12 | Voz Financiera / InclusiBot | Inclusión | >1 M con discapacidad visual | Vision + TTS con énfasis emocional |
| E13 | Respiro CAE | Inclusión | Desertores universitarios CAE en mora | Reprogramación al 10 % de renta |
| E14 | Talento Tributa | Inclusión | Atletas amateur, e-sports, creadores | Régimen tributación irregular |
| E15 | Feria Legal | Inclusión | Vendedores ambulantes | MEF + ordenanzas municipales |

> Detalle completo (problema, datasets, demos imaginados, casos análogos internacionales, riesgos) en el [catálogo emergente](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

## Candidatas top dentro de la línea

### De la tabla maestra (con scoring formal)

- :material-star: **sabidurIA ciudadana** (89,25) — apuesta unificadora; demo de 2-3 módulos brutalmente bien hechos + roadmap visible.
- **Defensor** (89,00) — segmento más numeroso, cuatro capacidades de Claude juntas, ya recomendada por la estrategia. Funciona como módulo dentro de sabidurIA o como producto único.
- **Letra Chica / Tu Plata** (86,50) — demo más visual, dolor del 80 %+ de la población. Funciona como módulo o producto único.
- **Tu Plata Mipyme** (83,00) — cruza inclusión con formalización SII, mentores potenciales en SII/SERCOTEC. Funciona como módulo o producto único.

### De las emergentes del run #01 (sin scoring formal pero alta promesa)

- :material-star: **Rescate Ciudadano** — demo wow con CLP recuperados en vivo (CLP 106.845 M en pozo CMF). **Módulo natural de sabidurIA.**
- :material-star: **Legado Claro** — cubre el gap 41 % AFP herencias del [run #04](../research/usuarios/transferencias-no-activadas-chile-2026.md). **Módulo natural de sabidurIA.**
- **Agua Comunitaria** — desmarque temático absoluto (>2 M chilenos APR rurales).
- **CuidaDerechos** — sub-segmento invisible (cuidadoras informales) con cifra concreta $32.991/mes.

## Tensiones a resolver con el equipo

- :material-alert: **Apuesta unificadora vs caso particular.** sabidurIA tiene mayor amplitud y mejor pitch, pero más riesgo de alcance. Defensor/Letra Chica son más acotadas, más seguras de demostrar end-to-end. Decisión clave en el [Tollgate 1](../equipo/proceso-y-hoja-de-ruta.md#tollgate-1-entre-discovery-y-diseno).
- :material-alert: **Mis Datos · ARCOP** (86,00) ataca un dolor del top 2 del scoring deep research, pero requiere **cambio de línea temática**. Si emerge evidencia clara, se revisa el [ADR 0002](../especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md).
- :material-alert: **Antiestafa / Pillo** (85,00) similar situación: gran score en su línea pero fuera de la elegida.
- :material-alert: **15 emergentes sin scoring formal** — el equipo debe priorizar 1 hora en próxima reunión para revisarlas y decidir cuáles promover a ficha standalone (sumar a tabla maestra) y cuáles dejar archivadas en el catálogo emergente.

## Cómo proceder

1. **Esta semana:** cada miembro lee:
    - La idea unificadora ([sabidurIA](sabiduria-ciudadana.md)).
    - Las 3 candidatas top con ficha (Defensor, Letra Chica, Tu Plata Mipyme).
    - Las 15 ideas emergentes ([catálogo del run #01](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md)) — al menos para identificar cuáles 2-3 sumar al pool serio.
    - Trae una **objeción concreta** o **enriquecimiento** por idea.
2. **Próxima reunión técnica:** decidir entre **sabidurIA ciudadana** (apuesta unificadora) y las **3-5 candidatas individuales** (incluye top 2 emergentes Rescate Ciudadano + Legado Claro si el equipo las valida como módulos).
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

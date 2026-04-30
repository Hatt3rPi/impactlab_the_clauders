---
title: "Idea: sabidurIA ciudadana — wiki de la vida del ciudadano chileno"
description: "Una sola web que recibe lo que estás viviendo en lenguaje natural y te devuelve qué derechos, beneficios, trámites y datos te tocan, citando la normativa."
autor: "Síntesis emergente sobre research previo del equipo"
fecha: 2026-04-29
linea: inclusion-financiera
estado: activa
prioridad: estrella
tags:
  - idea
  - inclusion-financiera
  - eventos-de-vida
  - unificadora
---

# Idea: sabidurIA ciudadana — wiki de la vida del ciudadano chileno :material-star:

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [PDF de estrategia](../../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf) y/o el [Deep Research de Calibria](../../assets/research/2026-04-29-deep-research-calibria.html). **Aún no validada por el equipo.**

> *Para cualquier chileno que está viviendo un momento de la vida (cesantía, enfermedad, parto, muerte de un familiar, deuda, fraude, emprendimiento), sabidurIA ciudadana recibe en lenguaje natural lo que está viviendo y le devuelve qué derechos, beneficios, trámites y datos le tocan, citando la normativa, generando las cartas y agendando los plazos.*

> :material-link-variant: **Idea unificadora.** Las otras 9 ideas del [tablero](index.md) son **casos particulares** (módulos) de este sistema. La estrategia es construir el motor agéntico genérico + **2-3 módulos brutalmente bien hechos** para el demo, dejando los demás como roadmap visible en la app.

## Tesis (validada con cifras Deep Research, 29-abr-2026)

> **El Estado chileno opera bajo un paradigma de "postulación activa": traslada la carga burocrática al ciudadano y genera pozos ciegos de capital no reclamado.**

sabidurIA invierte la carga. No es "literacy financiera" — es **devolverle al ciudadano la plata que ya es suya y nadie le dijo cómo cobrar**.

## Magnitud del problema (cifras oficiales chilenas)

| | |
|---|---|
| **TAM (Mercado Total Direccionable)** | **> CLP 1 billón anual** (1 millón de millones CLP) |
| **Capital cautivo base documentable** | CLP 524.832 millones (sólo cifras oficiales sólidas) |
| **Slide-ready 60 palabras** | *"Más de **CLP 403 mil millones** sin cobrar; **CLP 612.000 prom. anual** por persona en AFC + Acreencias + PGU"* |
| **Gap más alarmante** | **41 % en herencias AFP** — 220.000 afiliados fallecidos; familia abandona el saldo por no poder pagar la posesión efectiva |
| **Top 3 cifras agregadas** | Isapres CLP 1,2 billones · AFC CLP 156.051 M · PGU anual CLP 152.830 M |

> Detalle completo + fuentes: [Transferencias no activadas en Chile](../research/usuarios/transferencias-no-activadas-chile-2026.md).

## Origen

Surgió en conversación al revisar el research del equipo. Los "5 millones de chilenos con derechos que no pueden ejercer" cubren muchos territorios distintos (DICOM, contratos, cesantía, enfermedad, herencia, subsidios, fraude, datos, emprendimiento, migración, jubilación, vivienda...). Cada uno admite una idea separada — pero **todas comparten el mismo patrón estructural**: el ciudadano vive un evento, hay datos públicos que iluminan qué le toca, y nadie hace la traducción.

## Problema

- **5 millones de chilenos con derechos que no entienden** (frase declarada del Track 1).
- **45 % alcanza el mínimo OCDE de alfabetización financiera** (deep research, OECD/INFE 2023).
- **67 % no sabe cómo se usan sus datos personales** (Ipsos vía Deloitte).
- **62 % no cubre un imprevisto sin crédito** (deep research).
- Datos públicos abundantes y bien estructurados (CMF, SII, SERNAC, IPS, MinDes, FONASA, MinVu, AFC, Reg. Civil, Sup. Pensiones), pero **fragmentados** entre sitios oficiales, formularios PDF, FAQs y leyes que el ciudadano no sabe cruzar.
- Los chatbots oficiales actuales (Daniela del BCH, Santi de Santander, CMF Educa, Bendi) **funcionan como FAQs por institución**, no como guía por evento de vida.

## Hipótesis

Si una persona puede **describir lo que está viviendo en una sola frase** y obtener todos los derechos, beneficios, trámites y plazos que le aplican —cruzando datasets oficiales y citando cada norma— entonces:

1. Activa **transferencias monetarias** que ya tenía derecho a recibir y no estaba cobrando.
2. Evita **infracciones** o cobros indebidos que no sabía que eran ilegales.
3. **Reduce ansiedad** y dependencia de intermediarios (abogados, contadores informales, "amigos que saben de plata").
4. Construye **agencia regulatoria** progresiva — la siguiente vez ya conoce parte del sistema.

## Propuesta

### Qué hace

- **Recibe en lenguaje natural** lo que la persona está viviendo (texto, voz, foto de un documento).
- **Identifica el o los eventos de vida** implicados.
- **Cruza datasets oficiales** para devolver:
    1. **Qué te toca** — derechos, beneficios, plazos, requisitos.
    2. **Qué tienes que hacer** — paso a paso, con documentos necesarios y dónde tramitar.
    3. **Cita la fuente** — artículo + ley + circular.
    4. **Genera artefactos** — carta tipo, formulario pre-llenado, cálculo de monto.
    5. **Agenda recordatorios** — plazos, próximos pasos.

### Qué NO hace

- No tramita por el usuario (no podemos llenar formularios oficiales con su RUT sin autenticación).
- No recomienda institución específica (línea roja AUP).
- No sustituye al abogado / contador / asistente social — los complementa con disclosure permanente.
- No cubre todos los eventos en el demo del 7 de mayo — solo 2-3 hechos brutalmente bien.

## Mapa de eventos de vida (matriz del producto)

| Evento de vida | Datasets que cruzaríamos | Cubierto hoy en backlog |
|---|---|---|
| Tener un hijo | IPS, FONASA, MinSal, MinDes (RSH) | — |
| Egresar enseñanza media | Mineduc, JUNAEB | — |
| Primer trabajo | Mintrab, AFP, AFC | — |
| Casarse / convivir | Reg. Civil, SII | — |
| **Pedir crédito / firmar contrato** | CMF, SERNAC | [Letra Chica](letra-chica-cae.md) |
| Comprar casa | MinVu, CMF | — |
| **Enfermarse / cuidar enfermo** | FONASA, MinSal, isapres | — |
| **Quedar cesante** | AFC, Mintrab | — |
| **Ser víctima de fraude** | CMF, SERNAC, PDI | [Pillo](antiestafa-pillo.md) (Ciberseg) |
| **Estar en DICOM / repactar** | Equifax, CMF | [Defensor](defensor-dicom.md) |
| **Sobreendeudarse** | CMF, Sup. Insolvencia | [Mi Plan B](mi-plan-b-sobreendeudamiento.md) |
| **Heredar / fallecimiento** | Reg. Civil, SII, AFPs | — |
| Discapacidad | RNDis, MinSal | — |
| **Migrar** | Servicio Migraciones | [ConfíaConmigo](confiaconmigo-migrantes.md) |
| **Querer emprender** | SII, CORFO, SERCOTEC | [Tu Plata Mipyme](tu-plata-mipyme.md) |
| **Jubilarse** | AFP, Sup. Pensiones | [Mi Pensión](mi-pension.md) |
| **Querer controlar datos** | APDP, normativa Ley 21.719 | [Mis Datos · ARCOP](mis-datos-arcop.md) (Datos) |
| Activar subsidios sociales | MinDes, IPS, MinVu | — |

> 9 de las 18 filas son cubiertas por las ideas del backlog. Las otras 9 son territorios sin tocar — varios con dolor masivo (cesantía, enfermedad, herencia, subsidios sociales).

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 como cerebro (1 M de contexto para cargar el corpus regulatorio del módulo activo) + Haiku 4.5 para clasificación inicial del evento.
- **Patrones agénticos** (las cinco capacidades de Claude juntas):
    - **Vision** para leer documentos del usuario (cartolas AFP, finiquito, contrato, RSH, boleta médica).
    - **Citations API** — cada respuesta cita el artículo y la ley exacta.
    - **Structured outputs** con schema `{evento, beneficio, ley, articulo, requisitos, plazo, monto, accion}`.
    - **Tool use** — validar RUT en SII, consultar deuda en CMF, calcular montos UF/UTM, buscar normativa en MCP.
    - **Memory tool** — recordar al usuario los plazos a las semanas/meses.
- **MCPs custom propuestos:**
    - `cl-leyes` — RAG sobre normativa chilena con citación obligatoria.
    - `cl-beneficios` — catálogo estructurado de subsidios y trámites con metadata de elegibilidad.
    - `cl-datasets` — wrapper sobre datasets de CMF/SII/SERNAC/IPS/MinDes.
- **Datasets:** Ley 21.521, Ley 21.719, Ley 21.673, Ley 21.563, Ley 21.680, normativa MinDes (RSH, SUF, beneficios sociales), AFC, GES, ENIF 2025, ChileAtiende.

## Demo en 60 segundos (recomendado)

Tres módulos brutalmente bien hechos, conectados por la misma UI:

1. **"Hola, contame qué estás viviendo"** — input libre por voz o texto.
2. Usuario: *"Mi mamá tiene 64, trabaja informal vendiendo en feria, y la operaron hace dos meses por una hernia. Yo la cuido."*
3. La IA descompone:
    - Evento principal: **enfermedad + cuidado familiar**.
    - Sub-eventos: **trabajo informal** + **adulto pre-jubilación**.
4. Devuelve, citando cada fuente:
    - **GES**: la operación califica para cobertura, ¿la usaron? *(Decreto MinSal art. X).*
    - **Cuidador**: postulación a Subsidio al Cuidador. *(Ley 21.380 art. Y).*
    - **Adulto mayor**: cuenta cuánto le falta para PGU al cumplir 65 + cómo pre-postular.
    - **Trabajador informal**: si genera boleta, derecho a 7 % salud + AFP voluntaria con tope.
    - **Tú como cuidador**: días por enfermedad grave de pariente, postnatal extendido.
5. Cierra: *"¿Quieres que postulemos al Subsidio del Cuidador ahora? Te quedan 14 días."*

**Por qué este demo concreto:**

- Cubre 3 eventos en una misma narrativa (enfermedad + cuidado + trabajo informal).
- Sub-segmento prioritario ("mujeres jefas de hogar / cuidadoras") coincide con el priorizado por la estrategia para [Defensor](defensor-dicom.md).
- Activa una transferencia monetaria concreta — métrica cuantificable para el pitch ("este caso recupera CLP $X/mes").
- Usa Vision (cartola FONASA), Citations (5 leyes distintas), Tool use (validar RUT), Structured outputs (schema beneficios), Memory (recordatorio del plazo de 14 días). Las cinco capacidades, no decorativas.

## Scoring (criterios oficiales)

| Criterio | Peso | Score (0-1) | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,95 | 23,75 |
| Uso responsable de datos | 20 | 0,85 | 17,00 |
| Claude & Agentic Thinking | 25 | 0,95 | 23,75 |
| Funcionalidad | 15 | 0,75 | 11,25 |
| Calidad del pitch | 15 | 0,90 | 13,50 |
| **Total** | **100** | | **89,25** |
| Bonus agentic (+5) | 5 | 0,90 | +4,50 |

> Scoring inicial heurístico. Posicionada al tope del tablero apenas por encima de [Defensor](defensor-dicom.md) (89,00) por la amplitud del impacto y el uso integral de las 5 capacidades de Claude.

## Viabilidad en 48 h

- **Esfuerzo:** L-XL (es la idea más ambiciosa del tablero). **Mitigable** restringiendo el demo a 2-3 módulos.
- **Riesgos técnicos:**
    - **Alcance** — riesgo #1 según Calibria. Mitigación: demo enfocado, módulos no construidos quedan como roadmap visible.
    - **Cobertura limitada** del corpus normativo en 7 días. Mitigación: priorizar las 5-6 leyes más usadas en los módulos del demo.
    - **Falsas expectativas** del usuario. Mitigación: disclosure permanente + frase "no encontré información oficial sobre esto" cuando no haya base.
- **Datos disponibles ya:** parcial. La mayoría son públicos, pero la curaduría a formato chunkable + citable toma tiempo.
- **Demo end-to-end factible:** sí, restringiendo módulos.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Alcance ("solución para todo") suena grande pero hueco | Alta | Alto (descalifica) | Demo de 2-3 módulos brutalmente bien + roadmap de los demás visible |
| Alucinación regulatoria al cruzar varias leyes | Alta | Alto (descalifica) | Citations obligatorias, eval set de 30 prompts gold-standard, fallback "no tengo info oficial" |
| Generar expectativas falsas de elegibilidad para subsidios | Media | Alto | Disclaimer explícito: "el cálculo final lo hace [institución]"; nunca decir "te aprobarán" |
| Datos sensibles que el usuario revela (salud, ingreso, situación familiar) | Alta | Medio | No persistir input crudo, anonimizar en logs, opción de borrar sesión |
| Bases de datos de subsidios cambian con frecuencia | Media | Medio | RAG con caching, fechas explícitas en cada dato, "verificar en sitio oficial" |
| El jurado lo ve como "muy ambicioso para 48h" | Media | Alto | Llegar al lab con MVP testeado; el día 7 solo afinar |

## Por qué gana

- **Encaja literalmente** con el wording del Track 1 del lab: "5 millones de chilenos con derechos que no pueden ejercer".
- **Genuinamente IA-nativa**: no se puede hacer sin LLM (necesitas entender lenguaje natural ambiguo y mapear a estructura legal).
- **Las 5 capacidades de Claude** son requisito del producto, no decoración. Diferencial frente a wrappers.
- **Métrica de impacto medible** — cada caso activa una transferencia o evita una pérdida cuantificable en CLP.
- **Pitch de alto impacto** — la narrativa "tu vida en Chile, traducida a derechos" se entiende en 8 segundos.
- **Diferenciación por canal** — combinada con SEO/AI-citability ([ADR 0003](../../tu-plata-mipyme/especificaciones/adrs/0003-plataforma-web-mobile-first.md)), se vuelve el primer resultado cuando el chileno busca "qué hago si me echan", "puedo demandar a mi banco", "qué subsidios me tocan". Distribución cero post-lab.
- **Stakeholders alineados** — todos los reguladores invitados al Lab (CMF, SII, SERNAC, MinDes implícito) tienen incentivo en presentar esto.

## Por qué se diferencia de las 9 ideas del backlog

| Eje | Ideas individuales | sabidurIA ciudadana |
|---|---|---|
| **Alcance** | Un solo evento o nicho | Cualquier evento de vida (con módulos progresivos) |
| **Métrica del pitch** | "Resolvemos X" | "Cada chileno cruza ~12 de estos eventos en su vida; los traducimos todos" |
| **Reuso de research** | Cada una usa parte del research | Usa todo el research como insumo |
| **Diferenciación frente a 200 equipos** | "Otro RAG sobre regulación" | "Mapa vital con motor agéntico transversal" |
| **Roadmap post-lab** | Producto en su nicho | Plataforma con N módulos a futuro |

## Próximos pasos para validar (antes de Tollgate 1)

- [ ] Llevar la idea a la **reunión express de las 21:00** para feedback del equipo.
- [ ] **Encuesta abierta** una sola pregunta vía redes sociales del equipo: *"¿cuál ha sido el trámite o decisión financiera más confusa de tu vida?"*. Objetivo: 30-50 respuestas en 24h. Si los eventos mencionados se concentran en 2-3 categorías → módulos del demo confirmados por evidencia, no por voto.
- [ ] **3 conversaciones de 30 min** con un abogado del consumidor, un contador de microempresarios y una asistente social de municipalidad — perfiles que ven los dolores recurrentes y los nombran sin tecnicismos.
- [ ] **Spike técnico (medio día)**: Sonnet 4.6 con prompt cacheado de Ley 21.521 + AFC + GES, alimentado con el caso del demo de la mamá enferma. Medir exactitud de citas, tiempo de respuesta, costo.
- [ ] **Análisis de queries reales en Google Trends** sobre términos legales/financieros chilenos para validar el ángulo de SEO + AI-citability.

## Notas y referencias

- Origen: conversación posterior a la incorporación del [research previo del equipo](../research/index.md) y la [hoja de ruta de Jose](../../equipo/proceso-y-hoja-de-ruta.md). Si se valida, queda registrada en el ADR 0004 como decisión de idea.
- Sub-segmento priorizado de partida: **mujeres jefas de hogar de quintiles D-E**, mismo que la estrategia priorizó para [Defensor](defensor-dicom.md). Permite reusar entrevistas y dataset.
- Combos de demo recomendados (a discutir con el equipo):
    1. **Cesantía + Enfermedad/cuidado + DICOM** (3 eventos comunes y emocionalmente cargados; permite reusar trabajo de Defensor).
    2. **Subsidios sociales + Cesantía + Pedir crédito** (foco en transferencias monetarias activadas, métrica más dura).
    3. **Enfermedad/cuidado + Sobreendeudamiento + Subsidios** (narrativa de "rescate" — la persona en crisis encuentra todos los apoyos juntos).
- Las **9 ideas del backlog se mantienen como fichas standalone** y son perfectamente válidas si el equipo decide hacer una sola en lugar de la unificadora.

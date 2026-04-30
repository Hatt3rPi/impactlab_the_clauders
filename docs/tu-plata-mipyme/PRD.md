---
title: PRD — Tu Plata Mipyme
description: Documento de Requerimiento de Producto de Tu Plata Mipyme, idea ganadora del equipo The Clauders para el Claude Impact Lab Chile 2026.
tags:
  - tu-plata-mipyme
  - prd
  - especificaciones
---

# PRD — Tu Plata Mipyme

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Documento de Requerimiento de Producto consolidado a partir de research, definiciones del producto, ADRs, plan técnico, backlog y reuniones del equipo The Clauders.

> **Tu Plata Mipyme** es un copiloto freemium en WhatsApp + Web que acompaña al microemprendedor chileno desde el sueño hasta la PYME, con agentes IA especializados por etapa que hablan en su idioma y citan la norma.

| | |
|---|---|
| **Versión** | 1.0 |
| **Fecha** | 2026-04-30 |
| **Equipo** | The Clauders (Felipe · Jose · Cristian · Anahi) |
| **Competencia** | Claude Impact Lab Chile 2026 — *El puente al ciudadano* |
| **Línea temática** | Inclusión Financiera ([ADR 0002](especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md)) |
| **Producto** | Tu Plata Mipyme ([Tollgate 1 cerrado](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md)) |
| **Canal principal** | WhatsApp-first + Web complementaria ([ADR 0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md)) |
| **Modelo de negocio** | Freemium (Free · Pro · Plus · Marketplace) |
| **Pitch final** | 7 de mayo de 2026 · 12:00 · Espacio Riesco |

> **Relación con otros documentos:** este PRD da el *frame de producto* (qué problema, para quién, qué éxito). Para el detalle técnico ver [Plan de implementación](plan.md). Para las 60 features categorizadas y decisiones del equipo ver [Backlog](backlog.md). Para la definición canónica del producto ver [Qué es y para quién](que-es.md).

---

## 1. Problema

### 1.1 Descripción del problema actual

En Chile hay aproximadamente **1,08 millones de microemprendedores informales** (INE EME8) *(Fuente: [que-es.md](que-es.md))* que sostienen su actividad sin registro tributario, sin contabilidad sistemática y sin acceso real a los instrumentos de fomento que el Estado ya tiene diseñados para ellos. **El 59 % de los informales son mujeres** y en regiones como **la Araucanía la informalidad alcanza el 38 %** *(Fuente: [que-es.md](que-es.md))*; en Los Ríos la brecha de ingresos entre mujeres y hombres microemprendedores llega a **-43,7 %** *(Fuente: [research run #06](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md))*. La asesoría de gestión, tributaria y de fomento existe — vive en SII, CORFO, SERCOTEC, contadores y OTECs — pero está geográfica, lingüística y económicamente fuera del alcance del segmento que más la necesita.

### 1.2 Causas principales

- **Mercado de asesores con barrera económica de entrada.** Los contadores, OTECs y oficinas SERCOTEC operan con tarifas y presencia geográfica que excluyen al segmento informal — el costo de transporte, espera y honorarios por hora supera la disposición/capacidad de pago en NSE D-E rural *(Fuente: [que-es.md](que-es.md))*.
- **Lenguaje técnico-legal como barrera.** La normativa relevante (Ley 21.521, circulares CMF, reglamentos SII, bases CORFO/SERCOTEC) está escrita en registro denso. El segmento objetivo es predominantemente NSE D-E con escolaridad baja y comprensión lectora bajo nivel 3 PIAAC; en palabras del equipo: *"estamos pensando en una persona que tiene escolaridad baja, poco tiempo para leer, y lo que lee le cuesta mucho entenderlo"* *(Fuente: [reunión 29-abr](../reuniones/2026-04-29-definicion-problema-setup.md))*.
- **Canal equivocado: el canal donde el segmento ya vive no es donde llegan las soluciones digitales actuales.** Las soluciones existentes asumen que el usuario "buscará un sitio web" o instalará una app. La penetración mobile en Chile es 95,3 % *(Fuente: [comportamiento digital Chile 2026](../competencia/research/usuarios/comportamiento-digital-chile-2026.md))* pero el modo natural de uso del segmento NSE D-E es la conversación asincrónica por WhatsApp, no la navegación web ni el llenado de formularios *(Fuente: [ADR-0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md))*.
- **Sin tier gratuito viable en el mercado de asesoría existente.** Los proveedores de asesoría (contadores, consultoras, OTECs) requieren pago al primer contacto, lo que excluye estructuralmente al segmento que aún no tiene flujo de ingresos suficiente. La disposición a pagar emerge solo en puntos de inflexión (formalizar, postular a subsidio) — pero hoy nadie acompaña gratis hasta ese punto *(Fuente: [plan.md](plan.md))*.
- **Corpus regulatorio fragmentado y cambiante.** La formalización no es un acto: es un flujo de 4 a 6 sub-trámites en agencias que no conversan entre sí (RES, SII, Municipalidad, SEREMI). **El 35-40 % de los borradores en Tu Empresa en Un Día (RES) no se firma** por dudas técnicas *(Fuente: [research run #06](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md))*.

### 1.3 Impactos observables

- **Tiempo perdido.** Trámites diseñados para una hora terminan tomando semanas o se abandonan. El 35-40 % de borradores RES quedan sin firmar (ver causa 5 en 1.2); los que avanzan recorren entre 4 y 6 sub-trámites en agencias desconectadas (RES → SII F4415 → boleta/factura → patente municipal → SEREMI cuando aplica).
- **Dinero dejado en la mesa.** **Más del 50 % de las postulaciones a SERCOTEC/CORFO se rechazan** por mala formulación o inadmisibilidad *(Fuente: [research run #06](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md))*. **El 44 % de los emprendedores identifica el acceso a financiamiento como su barrera principal** *(Fuente: [research run #06](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md))*. Dueños únicos que califican al régimen Pro-Pyme Transparente (14 D N°8, 0 % impuesto de primera categoría a nivel empresa) "siguen en el régimen general gravoso (27 %) por desconocimiento técnico y contable" *(Fuente: [run #04 money-left-on-the-table](../competencia/research/_runs-deep-research/2026-04-29-04-money-left-on-the-table.md))*. A esto se suman ventas B2B perdidas por no poder facturar y multas municipales de 1 a 3 UTM por decomiso de fiscalizadores *(Fuente: [research run #06](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md))*.
- **Capacidad no construida.** Sin contabilidad sistemática el emprendedor no ve su utilidad real, no distingue finanzas familiares de las del negocio y no puede demostrar trayectoria al banco; el crecimiento es invisible. **~60 % de las ideas informales mueren antes de la primera venta** *(Fuente: [research run #06](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md))*.

### 1.4 Costo de no actuar

Cada mes que el segmento informal sigue operando sin acompañamiento accesible se traduce en formalizaciones que no ocurren, postulaciones a subsidios que se rechazan por errores de formulario, y regímenes tributarios favorables que no se aprovechan — capital público asignado que no llega a quien debía llegar. Cada cohorte que abandona en el borrador RES o que nunca postula a CORFO/SERCOTEC consolida la informalidad como estado permanente y reproduce la brecha regional y de género que el sistema ya tiene medida.

---

## 2. Resultado esperado

### 2.1 Estado futuro deseado

Habilitar que cualquier microemprendedor chileno —desde el momento en que tiene una idea hasta que opera como PYME formalizada que postula a subsidios— pueda **conversar por WhatsApp con un copiloto que lo entienda en su idioma, lo acompañe al ritmo asincrónico de su día y lo derive al instrumento estatal correcto cuando corresponda**. El sistema funciona en el smartphone que el usuario ya tiene, gratis hasta el punto en que el siguiente paso (formalización o postulación a subsidio) genera valor monetario evidente que justifica un cobro modesto. La web complementa con visualización (gráficos de utilidad), formularios largos y descargas (carta a banco, checklists de trámites) — nunca exclusiviza *(Fuente: [ADR-0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md))*.

El acompañamiento se entrega vía **cuatro agentes especializados por etapa del journey** (`mentor-inicio`, `acompanante-informal`, `gestor-formalizacion`, `estratega-crecimiento`) coordinados por un supervisor que enruta por etapa+intención y comparten un expediente único del emprendedor. Cada respuesta cita la norma chilena verificable (SII, CORFO, SERCOTEC) y cada cálculo ejecuta la regla *"no te calculo, te enseño lo que debes saber"* — el copiloto orienta y deriva, no reemplaza al contador ni al abogado *(Fuente: [plan.md](plan.md))*. En palabras del equipo: *"Es ofrecer la ayuda a que este gallo deje de pensar y se dedique a emprender"* *(Fuente: [reunión 30-abr](../reuniones/2026-04-30-revision-dolores-backlog.md))*.

### 2.2 Beneficios esperados

- **Cobertura efectiva del segmento donde ya está.** Llegar al 1,08 M de microemprendedores informales por el canal que ya usan, sin pedirles aprender una app nueva ni instalar nada: WhatsApp con 95,3 % de penetración mobile en Chile *(Fuente: [comportamiento digital Chile 2026](../competencia/research/usuarios/comportamiento-digital-chile-2026.md))*. Esto cierra la brecha de canal descrita en la causa 3 de la Sección 1.
- **Acompañamiento continuo, no consulta puntual.** Sustituir el modelo "una visita al contador / una llamada a SERCOTEC" por una conversación recurrente y asincrónica que captura ventas y gastos día a día, recuerda plazos y siembra conciencia de formalización sin presionar — diferenciador estructural frente a los RAG estáticos que dominarán el lab *(Fuente: [ADR-0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md))*.
- **Asesoría especializada por etapa, no genérica.** Cuatro agentes con system prompts focalizados <2k tokens por etapa (vs. >8k que degradan calidad en evals internos), cada uno con sus tools y memoria. Un soñador no recibe el mismo trato que una PYME que postula a CORFO; el supervisor enruta y los handoffs pasan contexto JSON estructurado *(Fuente: [plan.md](plan.md))*.
- **Modelo económico inclusivo y sostenible.** Tier Free indefinido para soñador e informal activo; cobro solo cuando el valor monetario del siguiente paso es evidente para el usuario (Pro ~$4.990 CLP/mes al formalizar; Plus $15.000-30.000 CLP por postulación a subsidio); marketplace con comisión 10-15 % al derivar a contador/abogado certificado regional. Captura willingness-to-pay real sin reproducir la barrera económica que es causa raíz del problema *(Fuente: [que-es.md](que-es.md))*.
- **Trazabilidad normativa con cita verificable.** Cada respuesta tributaria, jurídica o de fomento incluye link a la fuente oficial (SII, CORFO, SERCOTEC, CMF), implementado vía MCP propio sobre corpus regulatorio chileno con prompt caching de Anthropic (>80 % hit objetivo) — mitiga el riesgo descalificante de alucinación legal del lab *(Fuente: [estrategia de pitch](../equipo/estrategia-pitch-lab.md))*.
- **Reducción de capital público no aprovechado.** Bajar el >50 % de rechazo en SERCOTEC/CORFO por mala formulación y la fuga de dueños únicos que pagan 27 % de primera categoría cuando calificarían a 0 % en Pro-Pyme Transparente, vía postulación asistida y match probabilístico con instrumentos *(Fuente: [research run #06](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md))*.

### 2.3 Indicadores de éxito

#### 2.3.1 Producto (mensuales)

| # | Indicador | Definición | Meta Fase 1 |
|---|---|---|---|
| 1 | MAU | Emprendedores con ≥ 1 mensaje en el mes | 50 → 500 |
| 2 | Retención semana 4 | % activo a 4 semanas | > 40 % |
| 3 | Tasa avance de etapa | % que pasa de etapa N a N+1 en el mes | 5 % E2→E3 · 15 % E3→E4 |
| 4 | Conversión Free → Pro | % que paga al ver el trigger contextual | > 8 % |
| 5 | NPS | Encuesta WhatsApp post-interacción | > 40 |

*(Fuente: [plan.md §8.1](plan.md))*

#### 2.3.2 Impacto (trimestrales, reporte público)

| # | Indicador | Definición | Meta |
|---|---|---|---|
| 6 | Formalizaciones inducidas | Inicios de Actividades SII confirmados con código de referido | Reportado trimestral |
| 7 | Subsidios postulados | Postulaciones CORFO/SERCOTEC asistidas con la plataforma | Reportado trimestral |
| 8 | Subsidios adjudicados | Postulaciones asistidas que ganaron | Reportado trimestral |
| 9 | Distribución regional | % usuarios fuera de RM (proxy descentralización) | Crecimiento sostenido |
| 10 | Brecha de género cerrada | % usuarias mujeres vs línea base 59 % informalidad femenina | ≥ 59 % |

*(Fuente: [plan.md §8.2](plan.md))*

#### 2.3.3 Técnicos

| # | Indicador | Meta |
|---|---|---|
| 11 | Latencia p95 respuesta WhatsApp | < 4 s |
| 12 | Costo por usuario activo / mes | < $0,30 USD (con caching) |
| 13 | Cache hit rate (corpus regulatorio) | > 80 % |
| 14 | Uptime gateway WhatsApp | > 99,5 % |

*(Fuente: [plan.md §8.3](plan.md))*

#### 2.3.4 Específicos al pitch del lab

| # | Indicador | Meta |
|---|---|---|
| 15 | Auto-score interno vs criterios oficiales | ≥ 85 / 100 *(Fuente: [criterios-evaluacion](../competencia/criterios-evaluacion.md))* |
| 16 | Demo end-to-end del agente `acompanante-informal` (E2 — universo 1,08 M) | < 90 s en mobile *(Fuente: [plan.md §7](plan.md))* |
| 17 | Cita verificable en respuesta tributaria/regulatoria de la demo | 100 % de respuestas con link a fuente oficial (SII/CORFO/SERCOTEC/CMF) *(Fuente: [estrategia de pitch](../equipo/estrategia-pitch-lab.md))* |

---

## 3. Alcance

### 3.1 Fase 0 — Alcance del demo del lab (in scope)

La Fase 0 cubre los 7 días del lab (cierre 7 de mayo) y aplica el principio *un agente, una etapa, un flujo dorado*. El alcance funcional es deliberadamente reducido para llegar al pitch con un demo end-to-end que funciona, no con una superficie amplia a medio terminar *(Fuente: [plan.md §7](plan.md))*.

- **Bot WhatsApp con un único agente operativo: `acompanante-informal`** (Etapa 2 del journey — el de mayor universo: 1,08 M de microemprendedores informales). El resto de los agentes existen como diseño documentado pero no se construyen en Fase 0 *(Fuente: [plan.md §7](plan.md))*.
- **1 tool funcional:** simulador Pro-Pyme básico (régimen tributario simplificado para microempresarios, con disclaimer "no te calculo, te enseño lo que debes saber") *(Fuente: [plan.md §7](plan.md))*.
- **1 tool de generación:** carta de presentación a banco en PDF descargable, como output diferenciador del flujo dorado *(Fuente: [plan.md §7](plan.md))*.
- **Memoria persistente entre sesiones** (Postgres + memory tool del Agent SDK) que materializa el expediente del emprendedor para que la conversación retome el contexto día a día *(Fuente: [plan.md §7](plan.md))*.
- **Telemetría anónima básica** (eventos opt-in, sin PII) para medir flujo dorado y latencia p95 *(Fuente: [plan.md §7](plan.md))*.
- **Web landing con embed del chat** para usar como soporte visual durante el pitch (mitigación del riesgo "demo en vivo de WhatsApp es menos espectacular que UI rica") *(Fuente: [plan.md §7](plan.md))*.
- **Demo end-to-end de 90 segundos** con script ensayado al menos 2 veces antes del pitch del 7 de mayo *(Fuente: [plan.md §7](plan.md))*.

### 3.2 Usuarios y stakeholders in scope

**Usuario primario para Fase 0:** mujer microemprendedora de **30 a 50 años, NSE D-E, regiones del sur de Chile** — segmento priorizado por concentración del dolor (**Araucanía 38 % de informalidad**, **59 % de los informales son mujeres** según INE EME8) *(Fuente: [que-es.md](que-es.md))*. El demo se ensaya con un caso humano nombrado en el sur (microemprendedora de mermeladas en Pucón) para anclar la narrativa del pitch *(Fuente: [estrategia de pitch](../equipo/estrategia-pitch-lab.md))*.

**Stakeholders del demo (audiencia del 7 de mayo):**

- **Equipo del proyecto** — Felipe Abarca (AI Builder + Tech lead), Jose Foncea (PM + Comercial/Producto), Cristian Astorga (AI Builder de apoyo), Anahi Gonzalez (UX/UI + Vibecoder) *(Fuente: [reunión 29-abr](../reuniones/2026-04-29-definicion-problema-setup.md))*.
- **Jurado y panel evaluador** del lab — evalúa con los 5 criterios oficiales (Impacto cívico 25 %, Uso responsable de datos 20 %, Claude & Agentic Thinking 25 %, Funcionalidad 15 %, Calidad del pitch 15 %) más bonus +5 puntos por *agentic thinking* excepcional *(Fuente: [criterios-evaluacion.md](../competencia/criterios-evaluacion.md))*.
- **Mentores** del lab disponibles durante los 2 días del venue para feedback técnico y de pitch *(Fuente: [timeline.md](../competencia/timeline.md))*.
- **Organizadores** — Anthropic, BenditaIA, FinteChile (organización del Claude Impact Lab Chile 2026) *(Fuente: [reglas](../competencia/reglas.md))*.

**Stakeholders del producto post-lab (Fases 1-3, contexto):**

- **Microemprendedores en las 4 etapas del journey** — soñador con idea (E1), informal activo (E2 — foco Fase 0), recién formalizado (E3), PYME que postula a subsidio (E4) *(Fuente: [ADR-0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md))*.
- **SII, CORFO, SERCOTEC, CMF, SERNAC** — receptores institucionales de reportes anonimizados sin PII a partir de Fase 2; fuentes de datos oficiales preferidas por las reglas del lab *(Fuente: [reglas](../competencia/reglas.md))*.
- **ONGs partner para reclutamiento del piloto** — Fondo Esperanza y Hogar de Cristo, contempladas para reclutar 50-100 emprendedoras reales en Fase 1 *(Fuente: [plan.md §7](plan.md))*.
- **Asesores humanos certificados** — contadores y abogados regionales que entrarán al marketplace en Fase 2 con comisión 10-15 % por derivación *(Fuente: [que-es.md](que-es.md))*.

### 3.3 Sistemas y datasets in scope

**Stack obligatorio del lab.** Las reglas del Claude Impact Lab Chile 2026 fijan: uso de Claude API obligatorio (es lo que evalúan en el criterio "Claude & Agentic Thinking"), datos preferentemente desde fuentes públicas (CMF, SII, SERNAC) o datasets provistos por la organización, y no se exige un lenguaje o framework específico. La Fase 0 además se apoya en Claude Code, Agent SDK y MCPs para capturar el bonus +5 puntos por *agentic thinking* *(Fuente: [reglas](../competencia/reglas.md))*.

**Stack del producto Fase 0.** La elección concreta para los 7 días del lab es:

- **WhatsApp gateway:** Twilio (más rápido para prototipo; migración a Meta WhatsApp Business Cloud API directa diferida a ADR 0005) *(Fuente: [plan.md §4.2](plan.md))*.
- **API gateway / orquestación:** FastAPI (Python), mismo lenguaje que Agent SDK, deploy fácil en Cloud Run *(Fuente: [plan.md §4.2](plan.md))*.
- **Modelos:** Claude Sonnet 4.6 como motor de conversación y razonamiento; Claude Haiku 4.5 como fallback para clasificación de intención y respuestas FAQ *(Fuente: [plan.md §4.2](plan.md))*.
- **Memoria y datos:** Postgres + memory tool del Agent SDK para el expediente del emprendedor *(Fuente: [plan.md §4.2](plan.md))*.
- **Web:** Next.js 14 (App Router) + Tailwind para landing con embed del chat (Astro vs Next.js sigue abierto en ADR 0006 pendiente) *(Fuente: [plan.md §4.2](plan.md))*.
- **Hosting:** Google Cloud Run para la API y Vercel/Netlify para la web; ambos pay-per-use con escala a 0 entre usos *(Fuente: [plan.md §4.2](plan.md))*.

**Datasets oficiales del lab.** Reunión 30-abr aclara que los organizadores curan APIs/MCPs sobre fuentes legales/regulatorias y esperan que conectemos un MCP de Claude a sus fuentes *(Fuente: [reglas](../competencia/reglas.md))*. Para Tu Plata Mipyme aplican:

- **SII (crítico):** F29, F22, F4415 inicio actividades, Pro-Pyme Transparente, RCV, Carpeta Tributaria, e-Boleta. Es la fuente regulatoria principal del flujo dorado y del simulador Pro-Pyme *(Fuente: [plan.md](plan.md))*.
- **SERNAC (parcial, tangencial):** SERNAC Financiero como referencia para reclamos de cobranza en el journey post-MVP *(Fuente: [reglas](../competencia/reglas.md))*.
- **CMF (opcional, agregados):** educación financiera básica y Open Banking Ley 21.521 quedan diferidos a Fase 3; en Fase 0 solo se usan agregados públicos sin integración transaccional *(Fuente: [plan.md](plan.md))*.

### 3.4 Roadmap post-lab (Fases 1-3)

El roadmap post-lab está definido a alto nivel en `plan.md` y será refinado durante la fase de Diseño de Solución (post-Tollgate 1) y la **aceleración AI Fintech Sandbox** (60 días desde junio 2026 para los equipos ganadores del lab) *(Fuente: [timeline.md](../competencia/timeline.md))*.

| Fase | Ventana | Alcance |
|---|---|---|
| **1 — Piloto cerrado** | mes 1-3 post-lab | Los 4 agentes operativos (`mentor-inicio`, `acompanante-informal`, `gestor-formalizacion`, `estratega-crecimiento`) · MCP SII real (validar RUT + estado) · 50-100 emprendedoras reclutadas vía Fondo Esperanza / Hogar de Cristo · marco ARCO/privacidad pulido con asesoría legal |
| **2 — Apertura** | mes 4-9 | Tier Pro activado (Webpay / Mercado Pago) · marketplace de asesores humanos en 3 regiones piloto (RM + 2) · reportes anonimizados a SERCOTEC |
| **3 — Crecimiento** | mes 10+ | Repositorio contable Git-like · Tier Plus (postulación asistida) generalizado · integraciones bancarias vía Open Finance (Ley 21.521) |

*(Fuente: [plan.md §7](plan.md))*

### 3.5 Out of scope (exclusiones explícitas)

Esta sección lista lo que **no** entra en el alcance — separado en (a) funcionalidades fuera del demo del lab pero en roadmap post-lab, (b) ideas no priorizadas del Tollgate 1 que siguen vigentes como referencia o roadmap, y (c) exclusiones de producto y temáticas que se mantienen fuera de alcance de forma permanente.

#### a) Funcionalidades fuera del demo del lab (pero en roadmap)

- **Los 3 agentes que no son `acompanante-informal`** (`mentor-inicio`, `gestor-formalizacion`, `estratega-crecimiento`) — diseñados y documentados, pero no construidos en Fase 0 *(Fuente: [ADR-0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md))*.
- **Cobro Tier Pro/Plus.** La lógica freemium queda implementada conceptualmente pero **sin pasarela de pago activa** en Fase 0 *(Fuente: [plan.md §7](plan.md))*.
- **Marketplace de asesores humanos** (contadores y abogados certificados con comisión 10-15 %) — se activa en Fase 2 *(Fuente: [plan.md §7](plan.md))*.
- **Repositorio contable Git-like** (visión post-MVP de Fase 3) *(Fuente: [plan.md §7](plan.md))*.
- **TTS y Whisper de salida.** Fase 0 = solo texto. La voz saliente vía ElevenLabs y el audio entrante vía Whisper quedan diferidos *(Fuente: [plan.md §4.2](plan.md))*.

#### b) Ideas no priorizadas del Tollgate 1

Las siguientes 24 ideas evaluadas en el catálogo del equipo NO son parte del alcance de Tu Plata Mipyme. Siguen vigentes como referencia o roadmap post-lab; sus fichas individuales viven en `docs/competencia/ideas-evaluadas/`. *(Fuente: [ideas-evaluadas/index.md](../competencia/ideas-evaluadas/index.md))*

- [agua-comunitaria-apr](../competencia/ideas-evaluadas/agua-comunitaria-apr.md)
- [antiestafa-pillo](../competencia/ideas-evaluadas/antiestafa-pillo.md)
- [confiaconmigo-migrantes](../competencia/ideas-evaluadas/confiaconmigo-migrantes.md)
- [cosecha-justa-temporeros](../competencia/ideas-evaluadas/cosecha-justa-temporeros.md)
- [cuidaderechos-cuidadoras](../competencia/ideas-evaluadas/cuidaderechos-cuidadoras.md)
- [defensor-dicom](../competencia/ideas-evaluadas/defensor-dicom.md)
- [emancipia-egresados-sename](../competencia/ideas-evaluadas/emancipia-egresados-sename.md)
- [feria-legal-ambulantes](../competencia/ideas-evaluadas/feria-legal-ambulantes.md)
- [ges-claim-salud-retroactiva](../competencia/ideas-evaluadas/ges-claim-salud-retroactiva.md)
- [legado-claro-herencias](../competencia/ideas-evaluadas/legado-claro-herencias.md)
- [letra-chica-cae](../competencia/ideas-evaluadas/letra-chica-cae.md)
- [mi-pension](../competencia/ideas-evaluadas/mi-pension.md)
- [mi-plan-b-sobreendeudamiento](../competencia/ideas-evaluadas/mi-plan-b-sobreendeudamiento.md)
- [mis-datos-arcop](../competencia/ideas-evaluadas/mis-datos-arcop.md)
- [open-finance-explainer](../competencia/ideas-evaluadas/open-finance-explainer.md)
- [re-inicia-quiebra-personal](../competencia/ideas-evaluadas/re-inicia-quiebra-personal.md)
- [rescate-ciudadano-acreencias](../competencia/ideas-evaluadas/rescate-ciudadano-acreencias.md)
- [respiro-cae-desertores](../competencia/ideas-evaluadas/respiro-cae-desertores.md)
- [retencion-alimentos](../competencia/ideas-evaluadas/retencion-alimentos.md)
- [rutajusta-ley-uber](../competencia/ideas-evaluadas/rutajusta-ley-uber.md)
- [sabiduria-ciudadana](../competencia/ideas-evaluadas/sabiduria-ciudadana.md)
- [talento-tributa-creadores](../competencia/ideas-evaluadas/talento-tributa-creadores.md)
- [viuda-protegida-pension](../competencia/ideas-evaluadas/viuda-protegida-pension.md)
- [voz-financiera-accesibilidad](../competencia/ideas-evaluadas/voz-financiera-accesibilidad.md)

#### c) Exclusiones de producto y temáticas

- **No recomendamos bancos ni productos crediticios específicos.** Es un anti-objetivo del producto: orientamos y derivamos pero no comparamos instituciones financieras *(Fuente: [ADR-0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md))*.
- **No sustituimos asesoría profesional cuando el caso lo requiere.** El copiloto enseña y orienta; no firma declaraciones, no presenta F29, no representa en disputas, no emite dictámenes legales — esos casos se derivan al asesor humano del marketplace o al profesional certificado correspondiente *(Fuente: [plan.md §1.3](plan.md))*.
- **No cargamos declaraciones tributarias en nombre del usuario** (no presentamos F29 ni F22 en su lugar; lo acompañamos a llenarlos) *(Fuente: [plan.md §1.3](plan.md))*.
- **No vendemos datos personales.** Los datos agregados sin PII pueden compartirse con SERCOTEC, academia o reguladores bajo opt-in explícito; los datos personales del usuario nunca se venden *(Fuente: [ADR-0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md))*.
- **Líneas temáticas del lab no elegidas.** **Ciberseguridad ciudadana** y **Protección de datos personales** son las otras dos líneas oficiales del lab; quedan fuera del alcance de Tu Plata Mipyme. La línea elegida es **Inclusión Financiera** *(Fuente: [ADR-0002](especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md))*.

---

## 4. Requerimientos

### 4.1 Requerimientos de negocio

Lo que el sistema debe hacer expresado desde dos perspectivas: la del **microemprendedor informal** (usuario primario de Fase 0) y la del **equipo The Clauders** durante el pitch del 7 de mayo.

**Para el microemprendedor informal (Etapa 2 del journey):**

1. **Registrar ventas y gastos diarios por WhatsApp** mediante mensajes en lenguaje natural y recibir cada semana el cálculo de utilidad real comparado contra la simulación del régimen Pro-Pyme Transparente. La conversación respeta el formato ≤ 160 caracteres con 1 idea por mensaje, alineado con comprensión lectora bajo nivel 3 PIAAC del segmento NSE D-E *(Fuente: [plan.md §1.2](plan.md))*.
2. **Recibir recordatorios contextuales con frecuencia adaptativa** (no agresiva) que rompan la invisibilidad del crecimiento sin presionar a formalizar antes de que el cálculo de utilidad lo justifique *(Fuente: [plan.md §3.2](plan.md))*.
3. **Recibir derivaciones explícitas a humanos o instituciones** ("no sé, te derivo") cuando la consulta excede el scope del asistente, en lugar de respuestas alucinadas — regla dura del equipo: *"No te calculo, te enseño lo que debes saber"* *(Fuente: [plan.md §1.2](plan.md))*.
4. **Verificar la fuente de cualquier respuesta normativa** con link verificable a SII, CORFO, SERCOTEC o CMF, sin tener que confiar a ciegas en el bot *(Fuente: [ADR-0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md))*.
5. **Pasar a la Etapa 3 (formalización) con handoff explícito** al `gestor-formalizacion` cuando la utilidad calculada justifica el paso, conservando el expediente del emprendedor para que la conversación retome sin re-pedir datos básicos *(Fuente: [plan.md §3.2](plan.md))*.
6. **Ejercer derechos ARCO desde el mismo canal** mediante los comandos `/mis-datos` y `/borrar-mis-datos` operativos por WhatsApp, en cumplimiento de Ley 19.628 + Ley 21.719 *(Fuente: [plan.md §4.4](plan.md))*.

**Para el equipo The Clauders durante el pitch del 7 de mayo:**

7. **Mostrar una conversación end-to-end en mobile en menos de 90 segundos** que recorra el flujo dorado del `acompanante-informal` (registro de venta → reporte semanal → simulación Pro-Pyme → carta a banco) *(Fuente: [plan.md §7](plan.md))*.
8. **Mostrar lo que el agente está "pensando"** (handoffs entre subagents, tools llamadas, citas resueltas) en un panel paralelo de la web — captura el bonus +5 puntos por *agentic thinking* y mitiga el riesgo "demo en vivo de WhatsApp es menos espectacular que UI rica" *(Fuente: [estrategia de pitch](../equipo/estrategia-pitch-lab.md))*.
9. **Tener fallback offline pre-grabado para los 2 casos demo principales** (registro de venta + carta a banco) si la API de Claude o el gateway WhatsApp fallan en vivo, con indicador visual sutil de "modo offline" sin interrupción del flujo *(Fuente: [estrategia de pitch](../equipo/estrategia-pitch-lab.md))*.

### 4.2 Requerimientos operativos

Lo que el sistema y el equipo deben sostener para que la Fase 0 sea reproducible, auditable y conforme al marco regulatorio chileno.

1. **Demo reproducible end-to-end desde cualquier laptop del equipo.** Felipe, Jose, Cristian o Anahi pueden levantar la demo desde su laptop sin pasos manuales fuera del repo (variables documentadas, secretos en `.env.example`, README con quickstart) *(Fuente: [deliverables.md](../competencia/deliverables.md))*.
2. **Recuperación ante fallo en vivo.** Para los 2 casos demo principales existe fallback pre-grabado o cacheado localmente que se activa si Claude API o el gateway WhatsApp fallan, sin que el jurado lo perciba como ruptura *(Fuente: [estrategia de pitch](../equipo/estrategia-pitch-lab.md))*.
3. **Trazabilidad de consultas.** Cada respuesta del demo guarda un log local con prompt, tools llamadas, citas resueltas y respuesta final — auditable a posteriori por el equipo y por el jurado si lo solicita *(Fuente: [plan.md §4.4](plan.md))*.
4. **Cumplimiento Ley 19.628 + Ley 21.719.** Consentimiento granular al enrolar (opt-in explícito por categoría de dato), comandos `/mis-datos` y `/borrar-mis-datos` operativos en la demo, encriptación at-rest y in-transit (TLS 1.3), retención de telemetría agregada sin PII a 90 días *(Fuente: [plan.md §4.4](plan.md))*.
5. **Repo del equipo como única fuente de verdad.** El equipo opera el lab desde la wiki (PRD, plan, backlog, ADRs, reuniones) sin herramientas externas no conectadas. Filosofía consensuada en kickoff: *"Repositorio como fuente de la verdad — ambiente productivo todo por excelencia"* *(Fuente: [reunión 29-abr](../reuniones/2026-04-29-definicion-problema-setup.md))*.

### 4.3 Tabla de Requerimientos Funcionales (Fase 0)

Cada RF es derivable del backlog ✅ Incluir, del plan técnico (`plan.md` §3 journey por agente, §4 stack) o del ADR-0004. La prioridad usa la escala **Must Have · Should Have · Nice to Have**. Los RF marcados Must Have deben estar funcionales y demostrables en el pitch del 7 de mayo.

| ID | Requerimiento | Prioridad | Criterio de aceptación breve | Fuente |
|---|---|---|---|---|
| RF-01 | Iniciar conversación por WhatsApp con mensaje en lenguaje natural | Must Have | Mensaje del usuario al número del bot genera respuesta en < 4 s p95 | [plan.md §4.2](plan.md) · [plan.md §8.3](plan.md) |
| RF-02 | El supervisor clasifica al usuario en su etapa del journey y rutea al agente correcto (Fase 0: solo `acompanante-informal`) | Must Have | Mensaje del tipo "vendí 30 mil" → rutea a Etapa 2 con expediente cargado | [plan.md §3.2](plan.md) · [plan.md §5.3](plan.md) |
| RF-03 | El bot responde con mensajes ≤ 160 caracteres y 1 idea por mensaje, en lenguaje B1 / 8° básico | Must Have | 100 % de mensajes del demo cumplen el formato; revisión manual por Anahi | [plan.md §1.2](plan.md) · [reunión 30-abr](../reuniones/2026-04-30-revision-dolores-backlog.md) |
| RF-04 | Registrar venta del día por NLP desde texto ("vendí $X") y por audio (post-MVP) | Must Have | Sistema confirma la venta y actualiza el expediente en Postgres | [backlog E1-OPER-09](backlog.md) |
| RF-05 | Memoria persistente del expediente del emprendedor entre sesiones | Must Have | Sesión 2 retoma el contexto sin re-pedir datos básicos al usuario | [plan.md §4.2](plan.md) |
| RF-06 | Reporte semanal de utilidad real vs simulación Pro-Pyme Transparente | Must Have | Mensaje semanal automático con utilidad calculada y comparación contra régimen Pro-Pyme | [plan.md §3.2](plan.md) |
| RF-07 | Tool `simular-pro-pyme` que acepta ventas y gastos anuales y devuelve utilidad neta | Must Have | Tool retorna número en CLP + explicación simple + disclaimer "no te calculo, te enseño" | [plan.md §3.2](plan.md) |
| RF-08 | Tool `generar-carta-banco` que produce carta de presentación a banco en PDF descargable | Must Have | URL de PDF entregada en chat; PDF abre y es legible en mobile | [plan.md §3.2](plan.md) · [backlog E2-FORM-24](backlog.md) |
| RF-09 | Toda respuesta normativa cita su fuente con link verificable a SII / CORFO / SERCOTEC / CMF | Must Have | 100 % de respuestas tributarias o regulatorias del demo incluyen link a fuente oficial | [plan.md §1.2](plan.md) · [estrategia de pitch](../equipo/estrategia-pitch-lab.md) |
| RF-10 | Manejar "no sé, te derivo" cuando la consulta excede el scope, sin alucinar | Must Have | Caso de prueba con prompt fuera de dominio devuelve derivación explícita (no respuesta inventada) | [plan.md §1.2](plan.md) · [reunión 30-abr](../reuniones/2026-04-30-revision-dolores-backlog.md) |
| RF-11 | Comandos ARCO `/mis-datos` y `/borrar-mis-datos` operativos por WhatsApp | Must Have | Demo de cada comando devuelve respuesta esperada (export JSON / confirmación de borrado) | [plan.md §4.4](plan.md) |
| RF-12 | Web pública con landing y embed del chat para soporte visual del pitch | Must Have | URL accesible durante el pitch; embed funcional en mobile y desktop | [plan.md §4.2](plan.md) · [plan.md §7](plan.md) |
| RF-13 | Panel paralelo en la web que muestra handoffs, tools llamadas y citas resueltas en tiempo real | Must Have | Durante la demo el jurado ve simultáneamente la conversación WhatsApp y el "thinking" del agente | [estrategia de pitch](../equipo/estrategia-pitch-lab.md) |
| RF-14 | MCP propio sobre corpus regulatorio chileno (markdown indexado con prompt caching) | Must Have | Cache hit rate del corpus regulatorio > 80 % medido con telemetría local | [plan.md §4.2](plan.md) · [estrategia de pitch](../equipo/estrategia-pitch-lab.md) |
| RF-15 | Fallback offline pre-grabado para los 2 casos demo principales | Must Have | Si Claude API o WhatsApp gateway fallan, la demo continúa desde caché con indicador "modo offline" | [estrategia de pitch](../equipo/estrategia-pitch-lab.md) |
| RF-16 | Stack obligatorio del lab presente y verificable en el repo | Must Have | Repo evidencia uso de Claude API + Agent SDK + ≥ 1 MCP propio; README lo declara | [reglas](../competencia/reglas.md) · [criterios-evaluacion](../competencia/criterios-evaluacion.md) |
| RF-17 | Telemetría anónima básica con eventos opt-in (sin PII) | Must Have | Eventos del flujo dorado registrados; el repo evidencia configuración opt-in | [plan.md §4.4](plan.md) |
| RF-18 | Pitch de ~5 minutos con narrativa Hook → Usuario real → Solución → Demo en vivo → Por qué Claude / agentic → Impacto y próximos pasos | Must Have | Estructura visible y cronometrada; ensayo completo ≥ 2 veces antes del 7-may 12:00 | [deliverables.md](../competencia/deliverables.md) · [estrategia de pitch](../equipo/estrategia-pitch-lab.md) |
| RF-19 | Recordatorio asincrónico ("Hace N días que no me cuentas...") con frecuencia adaptativa | Should Have | Demo muestra el recordatorio activado con regla de frecuencia ajustable | [plan.md §3.2](plan.md) · [backlog E1-OPER-09](backlog.md) |
| RF-20 | Aceptar input de audio entrante por WhatsApp (transcripción vía Whisper) | Nice to Have | Audio WhatsApp se transcribe automáticamente y se procesa por el flujo normal | [plan.md §4.2](plan.md) |
| RF-21 | TTS de salida con voz neutra chilena (vía ElevenLabs MCP) cuando el usuario lo pide | Nice to Have | Bot responde con audio adjunto si el usuario solicita "audio" o "léelo" | [plan.md §4.2](plan.md) · [reunión 30-abr](../reuniones/2026-04-30-revision-dolores-backlog.md) |

> **Total Fase 0:** 21 RF (18 Must Have · 1 Should Have · 2 Nice to Have). La tabla es expandible — pueden agregarse RF nuevos si emergen durante el spike técnico de los 7 días del lab. Los RF no resueltos en Fase 0 se trasladan a Fase 1 del roadmap.
>
> **Cobertura backlog:** los RF de la tabla cubren los 21 features ✅ Incluir del backlog en su versión Fase 0 (registro de ventas, simulador Pro-Pyme, derivación a contador vía handoff, carta a banco, derechos ARCO). El detalle por feature E0-E5 vive en [backlog.md](backlog.md). Las 32 features ⏳ pendientes y las 6 ❌ excluidas no entran en alcance de Fase 0.

---

## 5. Criterios de aceptación

### 5.1 Tabla de criterios

[Pendiente — Tarea 9]

### 5.2 Responsable de validación

[Pendiente — Tarea 9]

---

## 6. Supuestos, dependencias y restricciones

### 6.1 Supuestos del proyecto

[Pendiente — Tarea 10]

### 6.2 Dependencias

[Pendiente — Tarea 10]

### 6.3 Restricciones técnicas

[Pendiente — Tarea 10]

### 6.4 Restricciones del lab y de negocio

[Pendiente — Tarea 10]

### 6.5 Fecha límite y hitos críticos

[Pendiente — Tarea 10]

---

## 7. Riesgos

[Pendiente — Tarea 11]

---

## 8. Anexos — Trazabilidad al repo

[Pendiente — Tarea 12]

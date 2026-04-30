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

[Pendiente — Tarea 7]

### 3.2 Usuarios y stakeholders in scope

[Pendiente — Tarea 7]

### 3.3 Sistemas y datasets in scope

[Pendiente — Tarea 7]

### 3.4 Roadmap post-lab (Fases 1-3)

[Pendiente — Tarea 7]

### 3.5 Out of scope (exclusiones explícitas)

[Pendiente — Tarea 7]

---

## 4. Requerimientos

### 4.1 Requerimientos de negocio

[Pendiente — Tarea 8]

### 4.2 Requerimientos operativos

[Pendiente — Tarea 8]

### 4.3 Tabla de Requerimientos Funcionales (Fase 0)

[Pendiente — Tarea 8]

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

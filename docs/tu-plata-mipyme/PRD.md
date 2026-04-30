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

En Chile hay aproximadamente **1,08 millones de microemprendedores informales** (INE EME8) *(Fuente: docs/tu-plata-mipyme/que-es.md)* que sostienen su actividad sin registro tributario, sin contabilidad sistemática y sin acceso real a los instrumentos de fomento que el Estado ya tiene diseñados para ellos. **El 59 % de los informales son mujeres** y en regiones como **la Araucanía la informalidad alcanza el 38 %** *(Fuente: docs/tu-plata-mipyme/que-es.md)*; en Los Ríos la brecha de ingresos entre mujeres y hombres microemprendedores llega a **-43,7 %** *(Fuente: docs/competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md)*. La asesoría de gestión, tributaria y de fomento existe — vive en SII, CORFO, SERCOTEC, contadores y OTECs — pero está geográfica, lingüística y económicamente fuera del alcance del segmento que más la necesita.

### 1.2 Causas principales

- **Asesoría centralizada en lo urbano y formal.** Los servicios de fomento (SERCOTEC, CORFO, contadores, OTECs) operan asumiendo cliente formalizado, con tiempo y movilidad para tramitar presencialmente. El segmento prioritario — mujeres microemprendedoras 30-50 años en regiones del sur — vive fuera de ese radio *(Fuente: docs/tu-plata-mipyme/que-es.md)*.
- **Lenguaje técnico-legal como barrera.** La normativa relevante (Ley 21.521, circulares CMF, reglamentos SII, bases CORFO/SERCOTEC) está escrita en registro denso. El segmento objetivo es predominantemente NSE D-E con escolaridad baja y comprensión lectora bajo nivel 3 PIAAC; en palabras del equipo: *"estamos pensando en una persona que tiene escolaridad baja, poco tiempo para leer, y lo que lee le cuesta mucho entenderlo"* *(Fuente: docs/reuniones/2026-04-29-definicion-problema-setup.md)*.
- **Canal equivocado.** Las soluciones digitales actuales asumen que el usuario "buscará un sitio web" o instalará una app. La penetración mobile en Chile es 95,3 % *(Fuente: docs/competencia/research/usuarios/comportamiento-digital-chile-2026.md)* pero el modo natural de uso del segmento NSE D-E es la conversación asincrónica por WhatsApp, no la navegación web ni el llenado de formularios *(Fuente: docs/tu-plata-mipyme/especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md)*.
- **Cero capacidad de pago al inicio + alta disposición a pagar en puntos de inflexión.** El emprendedor informal "no puede pagar nada al inicio (es justamente el problema que resolvemos). Pero cuando ya formalizó y empieza a postular a subsidios reales, ahí el valor unitario justifica un cobro modesto" *(Fuente: docs/tu-plata-mipyme/plan.md)*. Cualquier modelo de pago obligatorio reproduce la barrera económica que es la causa raíz.
- **Corpus regulatorio fragmentado y cambiante.** La formalización no es un acto: es un flujo de 4 a 6 sub-trámites en agencias que no conversan entre sí (RES, SII, Municipalidad, SEREMI). **El 35-40 % de los borradores en Tu Empresa en Un Día (RES) no se firma** por dudas técnicas *(Fuente: docs/competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md)*.

### 1.3 Impactos observables

- **Tiempo perdido.** Trámites diseñados para una hora terminan tomando semanas o se abandonan. **35-40 % de borradores RES quedan sin firmar** *(Fuente: docs/competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md)*; los que avanzan recorren entre 4 y 6 sub-trámites en agencias desconectadas (RES → SII F4415 → boleta/factura → patente municipal → SEREMI cuando aplica).
- **Dinero dejado en la mesa.** **Más del 50 % de las postulaciones a SERCOTEC/CORFO se rechazan** por mala formulación o inadmisibilidad *(Fuente: docs/competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md)*. **El 44 % de los emprendedores identifica el acceso a financiamiento como su barrera principal** *(Fuente: docs/competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md)*. Dueños únicos que califican al régimen Pro-Pyme Transparente (14 D N°8, 0 % impuesto de primera categoría a nivel empresa) "siguen en el régimen general gravoso (27 %) por desconocimiento técnico y contable" *(Fuente: docs/competencia/research/_runs-deep-research/2026-04-29-04-money-left-on-the-table.md)*. A esto se suman ventas B2B perdidas por no poder facturar y multas municipales de 1 a 3 UTM por decomiso de fiscalizadores *(Fuente: docs/competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md)*.
- **Capacidad no construida.** Sin contabilidad sistemática el emprendedor no ve su utilidad real, no distingue finanzas familiares de las del negocio y no puede demostrar trayectoria al banco; el crecimiento es invisible. **~60 % de las ideas informales mueren antes de la primera venta** *(Fuente: docs/competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md)*. La consecuencia agregada es brecha de género (59 % de informales son mujeres) y descentralización pendiente (informalidad concentrada en regiones del sur).

### 1.4 Costo de no actuar

Cada mes que el segmento informal sigue operando sin acompañamiento accesible se traduce en formalizaciones que no ocurren, postulaciones a subsidios que se rechazan por errores de formulario, y régimenes tributarios favorables que no se aprovechan — capital público asignado que no llega a quien debía llegar. Cada cohorte que abandona en el borrador RES o que nunca postula a CORFO/SERCOTEC consolida la informalidad como estado permanente y reproduce la brecha regional y de género que el sistema ya tiene medida.

---

## 2. Resultado esperado

### 2.1 Estado futuro deseado

[Pendiente — Tarea 6]

### 2.2 Beneficios esperados

[Pendiente — Tarea 6]

### 2.3 Indicadores de éxito

[Pendiente — Tarea 6]

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

---
titulo: "Money left on the table en Chile (transferencias no activadas)"
objetivo: "Cuantificar con cifras oficiales chilenas 2023-2025 cuánto dinero promedio queda 'sin reclamar' en el sistema chileno por evento de vida — para sustentar el pitch de la idea sabidurIA con métrica cuantitativa dura."
agent: "deep-research-max-preview-04-2026"
linea: inclusion-financiera
prioridad: alto
---

# Prompt: Money left on the table en Chile

## Contexto

Soy parte de un equipo en el **Claude Impact Lab Chile 2026** (6-7 mayo 2026, Track 1: Inclusión Financiera y Literacy Regulatoria). Estamos evaluando una idea unificadora llamada **sabidurIA ciudadana**: una wiki de la vida del ciudadano chileno que recibe un evento de vida en lenguaje natural y devuelve los derechos, beneficios, trámites y datos que aplican, citando normativa.

La métrica más fuerte que esta idea puede traer al pitch es: *"el ciudadano chileno promedio que use sabidurIA activa CLP $X anuales en derechos y beneficios que no estaba cobrando"*.

Necesito el respaldo cuantitativo de esa métrica con fuentes oficiales chilenas, no con estimaciones globales.

## Lo que necesito

Cuantifica con **cifras oficiales chilenas vigentes (2023-2025, idealmente 2024-2025)** cuánto dinero promedio por persona elegible queda "sin reclamar" en el sistema chileno por categoría. Para cada categoría:

- Monto agregado nacional anual (o estimación con fuente).
- Monto promedio por elegible no-reclamante.
- Tasa de elegibilidad vs tasa de reclamo efectivo (gap %).
- Sub-segmento más afectado (por NSE, edad, género, región, sector).
- Fricción documentada (por qué no lo reclaman: desconocimiento, complejidad del trámite, vergüenza, miedo al rechazo, falta de papeles, etc.).
- Fuente oficial verificable (ministerio, superintendencia, paper, Casen, INE, prensa especializada).

## Categorías a investigar

### A. Subsidios y beneficios sociales (MinDes, IPS)

- Subsidio Único Familiar (SUF) — número de elegibles vs cobrantes.
- Bono al Trabajo de la Mujer — postulación vs elegibilidad.
- Subsidio Empleo Joven — postulación vs elegibilidad.
- Subsidio Habitacional DS49, DS01, leasing habitacional — postulación vs elegibilidad.
- Subsidio al Cuidador (Ley 21.380) — postulación vs elegibilidad.
- Subsidio al Pago del Servicio del Pago de la Cuenta de Agua Potable (SAPS).
- Pensión Garantizada Universal (PGU) — pre-postulación vs adjudicación, retraso al cumplir 65.
- Asignación Familiar — gap.
- Subsidio para Personas con Discapacidad.
- Bono Logro Escolar.
- Bono Marzo / Bono Invierno (cuando aplican).

### B. Cesantía y desempleo (AFC, Mintrab)

- AFC postulación efectiva tras cesantía vs elegibles.
- Saldos en Fondo Solidario que se devuelven al cumplir 65 — desconocimiento.
- Indemnizaciones por años de servicio mal calculadas en finiquito — auditoría retroactiva posible.
- Cotización adicional voluntaria AFC — uso vs potencial.

### C. Salud (Fonasa, isapres, Sup. Salud)

- Reembolsos no cobrados de Fonasa por consultas privadas con cobertura.
- Cobertura GES (AUGE) declarada vs efectivamente usada por cada patología.
- CAEC (Cobertura Adicional para Enfermedades Catastróficas) — uso vs elegibilidad.
- Devolución por exceso de cotización en isapres.
- Licencias médicas rechazadas que serían recurribles ante COMPIN.
- Subsidio de Incapacidad Laboral (SIL) — gap.

### D. Tributación (SII)

- Devolución de impuestos por gastos médicos / educación — uso de la rebaja.
- Régimen Pro-Pyme Transparente — emprendedores que califican y siguen en régimen general.
- Boleta de Honorarios — retención 10 % no recuperada en Operación Renta.
- Crédito IVA exportador no solicitado.
- 14 ter — aprovechamiento real.

### E. Previsional (AFP, Sup. Pensiones, IPS)

- Cotizaciones perdidas por empleadores morosos — cobranza no iniciada por el trabajador.
- Bonificaciones por hijo / por postnatal mal aplicadas.
- AFP de fallecidos sin posesión efectiva tramitada — saldos sin cobrar.
- Pensión de viudez no postulada (viudas pre-65).
- APV con beneficio tributario no usado.
- Beneficios pensión PGU pre-postulables.

### F. Herencias y seguros (Reg. Civil, AFPs, compañías de seguros)

- Posesiones efectivas no tramitadas — patrimonio congelado.
- Seguros con beneficiario no cobrados (vida, desgravamen).
- Cuentas bancarias inactivas de fallecidos.
- Saldos de tarjetas crédito a favor del cliente al fallecer.

### G. Otros derechos del consumidor (SERNAC, CMF, Sup. Salud)

- Compensaciones SERNAC por sentencias colectivas no cobradas.
- Multas a empresas con devolución a consumidores no reclamadas.
- Seguros de cesantía hipotecaria forzosos — uso real al quedar cesante.

### H. Vivienda y servicios básicos

- Subsidio al consumo de electricidad / gas — postulación vs elegibilidad.
- Devolución contribuciones bienes raíces (adultos mayores) — gap.
- Beneficios postulables en gobierno regional / municipal.

## Output esperado

1. **Tabla maestra** con todas las categorías, montos y gaps.
2. **Top 10 categorías por "monto perdido per cápita"** (mayor pérdida individual).
3. **Top 10 categorías por "monto agregado nacional"** (mayor pérdida total país).
4. **Análisis cruzado**: ¿qué categorías golpean más al sub-segmento "mujeres jefas de hogar quintil D-E" (que es el sub-segmento priorizado del equipo)?
5. **Slide-ready**: un párrafo de 60 palabras que un PM podría usar en el pitch del 7 de mayo, con cifra ancla específica y fuente.

## Reglas para el agente

- **Cifras oficiales únicamente**. Si no tienes fuente verificable (MinDes, IPS, Casen, INE, Mintrab, Sup. respectivas, paper académico chileno), márcalo como "estimación sin fuente" o "no encontrado".
- **Ojo con cifras de prensa de hace años** — actualiza al año más reciente disponible.
- **Distingue elegibilidad teórica de adjudicación efectiva** — son cosas distintas y la diferencia es donde vive el dolor.
- **Cita el documento oficial específico** (no solo "MinDes", sino "Cuenta Pública MinDes 2024 sección X").
- **Si encuentras estudios académicos chilenos** (CAF, Banco Mundial Chile, OCDE, Casen, Centro de Microdatos) cítalos.
- **Output extenso permitido**.

## Por qué esto vale los USD 5 que cuesta

La diferencia entre un pitch promedio y un pitch ganador es el dato concreto en el slide 2: *"4,3 millones de chilenos dejan CLP 380 mil al año en subsidios sin reclamar"* vs *"hay un problema con literacy financiera"*. Lo primero es defendible ante CMF/SII/SERNAC, lo segundo no. Este reporte construye ese arsenal cuantitativo.

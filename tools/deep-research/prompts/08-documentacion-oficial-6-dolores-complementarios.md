---
titulo: "Documentación oficial chilena para los 6 dolores priorizados en sesión complementaria"
objetivo: "Por cada uno de los 6 dolores marcados como ✅ Incluir en la sesión complementaria del 30-abr (E3-D8 multas SII, E4-D2 subsidios, E4-D3 FOGAPE, E4-D5 PreviRed, E5-D4 suspensión SII / Término de Giro, E5-D5 disolución RES), identificar la documentación oficial chilena que el asistente IA necesita ingerir para responder con autoridad. Mismo formato que el run #07."
agent: "deep-research-max-preview-04-2026"
linea: inclusion-financiera
prioridad: alto
---

# Prompt: Documentación oficial para los 6 dolores complementarios

## Contexto

El equipo **The Clauders** está construyendo **Tu Plata Mipyme**. Tras la reunión del 30-abr-2026 (sesión complementaria), el equipo cerró el alcance del producto V1 con **25 dolores ✅ Incluir** (de 48 totales).

El [run #07](2026-04-30-07-documentacion-oficial-dolores-incluidos.md) ya cubrió los **19 dolores priorizados originalmente**. Este run #08 cubre los **6 dolores adicionales** que se sumaron en la sesión complementaria del mismo 30-abr y que aún no tienen mapeo de documentación oficial.

Output esperado: mismo formato que run #07 (un bloque por dolor con docs esenciales + acceso técnico + brechas + acciones técnicas concretas para MCPs/scrape/RAG).

---

## Los 6 dolores a investigar

### [E3-D8] Primer choque con multas SII

**Resumen:** El microemprendedor recibe el primer "correo rojo" del SII con jerga técnica (ej: "omisión sustantiva") y entra en pánico. Inacción → intereses penales y reajustes que multiplican la multa original. Visita presencial angustiante a oficina local SII.

**Decisión equipo (30-abr complementaria):** ✅ Incluir. Traducir la urgencia de los correos rojos a lenguaje cotidiano + guiar la solicitud de **Condonación de Multas e Intereses** online.

**Documentos a buscar:**
- Procedimiento de Condonación de Multas e Intereses (Circular SII / Resolución Exenta).
- Tipos de notificaciones SII (giro, requerimiento, citación) y plazos críticos.
- Tribunal Tributario y Aduanero (TTA) cuando aplica recurso.
- Tasa de interés y reajustes mensuales por mora.

### [E4-D2] Postulación a Subsidios del Estado (Sercotec/Corfo)

**Resumen:** >50% de las postulaciones se rechazan por mala formulación. Llenado de formularios largos + Modelo Canvas + grabación de pitch en video. Brecha enorme en redacción técnica para NSE D-E. Cofinanciamiento posterior obligatorio si se gana.

**Decisión equipo (30-abr complementaria):** ✅ Incluir. Asistente conversacional que actúa como oráculo: entrevista al usuario y redacta el Modelo Canvas + guion del pitch.

**Documentos a buscar:**
- Bases técnicas de los principales programas Sercotec (Capital Semilla, Crece, Mujer Emprendedora) — criterios de evaluación.
- Bases Corfo (Subsidio Semilla Inicia, Capital Abeja).
- Calendario unificado de convocatorias (si existe en programadps.gob.cl o similar).
- Plantillas oficiales de Modelo Canvas Sercotec.
- Requisitos de cofinanciamiento por programa.
- FOSIS Emprendamos Semilla / Básico / Avanzado (cruce con RSH).

### [E4-D3] Créditos con Garantía Estatal (FOGAPE)

**Resumen:** Solicitud vía banco comercial. Falsa expectativa: usuarios creen que es un regalo del Estado o que se condona si fracasan. La garantía cubre al banco, no al deudor. Rechazo si el riesgo de la pyme es excesivo.

**Decisión equipo (30-abr complementaria):** ✅ Incluir. Desmitificador: la usuaria entiende **antes de firmar** que es aval (no regalo), que el banco evalúa riesgo, y que en caso de mora el cobro recae sobre ella.

**Documentos a buscar:**
- Reglamento FOGAPE vigente (BancoEstado).
- Tipos de garantía FOGAPE (Pyme, Mujer Emprendedora, Reactiva).
- Bancos participantes y sus condiciones específicas.
- Tasas, plazos, garantías exigidas.
- Diferencia con CORFO crédito directo (si lo hay).

### [E4-D5] Pago de Cotizaciones (PreviRed)

**Resumen:** Carga manual de planillas en previred.com los días 10. Multas y presunción legal de deuda si no se pagan. Imposibilidad de licitar con Estado (Ley Bustos).

**Decisión equipo (30-abr complementaria):** ✅ Incluir + recordatorio. Push WhatsApp días previos al 10 + educación clave: *"si no hay caja, declarar sin pago igual evita la multa por Ley Bustos"*. Calendario agendable.

**Documentos a buscar:**
- Manual oficial PreviRed para empleadores Mipyme.
- Ley Bustos (qué dice exactamente sobre la presunción de deuda y la prohibición de licitar).
- Tasas de cotización vigentes (AFP, Salud, AFC, SIS, Mutual, Ley SANNA).
- Plazos legales y multas por atraso.
- Procedimiento "declaración sin pago" — base legal y cómo se hace.
- Formato .ple que pide PreviRed (planilla electrónica).

### [E5-D4] Suspensión Temporal o Término de Giro SII

**Resumen:** El emprendedor "deja botada" la empresa cuando le va mal. SII sigue acumulando F29 no presentados → multas mensuales por omisión. Miedo a avisar al SII que el negocio fracasó.

**Decisión equipo (30-abr complementaria):** ✅ Incluir con **trigger eliminar cuenta** del producto. Cuando la usuaria intenta eliminar su cuenta, el agente le sugiere proactivamente: *"antes de irte, dejá tu empresa en regla"* → guía Aviso de Suspensión Temporal o Término de Giro en SII.

**Documentos a buscar:**
- Aviso de Suspensión Temporal de Actividades (SII) — base legal, requisitos, plazo.
- Término de Giro definitivo (F2121 SII) — pasos, FUT/STUT, certificados requeridos.
- Diferencia conceptual y operativa entre ambos.
- Casos donde una conviene sobre la otra.
- Costos asociados (si los hay).

### [E5-D5] Disolución de Sociedad en RES

**Resumen:** Acta de disolución requiere firma de todos los socios. Notaría con costos variables. Dificultad para coordinar a ex-socios peleados. Quedan "sociedades fantasma" vigentes legalmente pero comercialmente muertas.

**Decisión equipo (30-abr complementaria):** ✅ Incluir. Flujo guiado en RES para disolver SpA/EIRL formalmente. Complementario al Aviso de Suspensión SII (E5-D4).

**Documentos a buscar:**
- Procedimiento de disolución y liquidación de SpA en RES (registrodeempresasysociedades.cl).
- Procedimiento de disolución de EIRL en RES.
- Procedimiento para Sociedades de Responsabilidad Limitada (Ltda) en notario tradicional.
- Requisitos de inscripción en Registro de Comercio del Conservador.
- Acta de disolución — formato y contenido mínimo.
- Casos: socio ausente, socio fallecido, desacuerdo entre socios.

---

## Estructura solicitada al agente — POR CADA DOLOR

Mismo formato del run #07. Cada dolor en su bloque:

```markdown
### [E3-D8] Primer choque con multas SII

**Resumen del dolor:** una frase del problema.

**Documentación esencial (orden de prioridad):**

1. **[Nombre del documento]**
   - **URL:** https://...
   - **Qué cubre:** texto descriptivo.
   - **Vigencia:** fecha o "permanente".
   - **Acceso técnico:** API pública / HTML scrapeable / requiere ClaveÚnica/ClaveSII / PDF descargable / trámite presencial.
   - **Notas:** caveats relevantes.

**Documentación complementaria** (no esencial pero recomendada):
- ...

**Brechas detectadas:**
- ...

**Acciones técnicas concretas que requiere el equipo:**
- MCPs específicos.
- Scrapeos a montar.
- Datasets a curar.
- Casos de handoff humano inevitable.
```

---

## Reglas estrictas para el agente

- **Solo fuentes oficiales chilenas:** BCN (LeyChile), SII, ChileAtiende, MINSAL, Sercotec, Corfo, MIDESO, DIPRES, INE, Banco Central, CMF, Subtel, BancoEstado FOGAPE, PreviRed, RES.
- **NO usar:** Wikipedia, blogs comerciales, foros, sitios de abogados privados (excepto cuando sean la única fuente y declarar la limitación).
- **URLs verificables.** Si la URL está detrás de login (ClaveÚnica/ClaveSII), señalarlo.
- **Distinguir 4 modalidades de acceso:** API pública, HTML scrapeable, login requerido, PDF descargable.
- **Identificar brechas** donde no hay documentación pública o está fragmentada.
- **Acciones técnicas concretas** (no genéricas): "Construir MCP para X usando endpoint Y", "scrape diario de Z", etc.

---

## Por qué este run vale los ~USD 5

Los 6 dolores complementarios cubren áreas donde el agente IA hace una contribución cívica fuerte:
- E3-D8 desestresa el primer encuentro punitivo con SII (alto valor emocional).
- E4-D2 mejora >50% rechazo en CORFO/SERCOTEC (capital público que no llega).
- E4-D3 evita el "pidieron y quebraron" por desinformación FOGAPE.
- E4-D5 evita exclusión de licitaciones por incumplimiento PreviRed (Ley Bustos).
- **E5-D4 + E5-D5 son trigger explícito al "eliminar cuenta"** — un patrón único de agente que protege al usuario incluso al irse del producto.

Sin este mapeo, el equipo construye estos 6 features sin saber qué documentos alimentan el RAG/MCP.

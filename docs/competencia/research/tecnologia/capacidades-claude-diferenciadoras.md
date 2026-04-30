---
title: "Capacidades de Claude que dan ventaja competitiva"
description: "Modelos vigentes, features únicos (Citations, Vision, 1M contexto, MCP, prompt caching) y stack recomendado para 7 días."
autor: "Síntesis sobre research previo del equipo (Estrategia Literacy Regulatoria)"
fecha: 2026-04-29
categoria: tecnologia
linea: transversal
tags:
  - research
  - tecnologia
  - claude
  - stack
---

# Capacidades de Claude que dan ventaja competitiva

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuente externa"
    Sintetizado a partir del [PDF de estrategia Literacy Regulatoria](../../../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf). **Verificar cifras antes de citarlas en el pitch.**

Lo que Claude hace **mejor que cualquier competidor** y nos puede dar el bonus de "Claude & Agentic Thinking (25 % + 5)".

## Fuente

- :material-file-pdf-box: [Estrategia Literacy Regulatoria (PDF)](../../../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf), p. 5.

---

## Modelos vigentes a abril 2026

| Modelo | Estado | Cuándo usarlo |
|---|---|---|
| **Opus 4.7** (16-abr-2026) | Flagship | Razonamiento complejo, generación de pitch, redacción legal |
| **Opus 4.6** | Vigente | Idem (más barato) |
| **Sonnet 4.6** | Workhorse | **Cerebro principal del MVP** — balance velocidad/capacidad |
| Sonnet 4.5 | **Sunset 30-abr-2026** | Migrar antes |
| **Haiku 4.5** | Vigente, $1/$5 por 1 M tokens | Volumen (chat WhatsApp, triage, clasificación) |

> **Recomendación de la estrategia:** Sonnet 4.6 + Haiku 4.5. Sonnet 4.6 entrega **1 M tokens de contexto a precio estándar ($3/$15)** — ningún competidor lo iguala — lo que permite cargar toda la Ley 21.521, las NCG relevantes, las cartillas SERNAC y las circulares CMF en una sola sesión **sin pipeline RAG complejo**.

---

## 5 capacidades diferenciadoras (vs un wrapper genérico)

### 1. Citations API

> Cada respuesta cita **literalmente el artículo / cláusula fuente** — oro para compliance regulado.

- Reduce drásticamente el riesgo de **alucinación regulatoria** (descalificador del lab).
- Construye confianza ante reguladores en el pitch.
- Diferenciación visible en la demo ("¿de dónde sacas esto? — del artículo 17 B de la Ley 19.496, aquí está el texto").

### 2. PDF / Vision nativo

- Hasta **100 páginas** y **32 MB** por documento.
- Sirve para leer cartolas AFP, contratos, cédulas chilenas, boletas SII, papeles de cobranza.
- **Sin pipeline OCR propio** — Claude lo hace nativamente.

### 3. Structured Outputs con `strict: true`

- JSON validado por schema.
- Indispensable para extraer **monto / CAE / fecha / RUT** de un documento ingresado por el usuario.
- Permite construir tools que dependen de tipos exactos sin parsing artesanal.

### 4. Tool use con parallel calls y modo programático

- Conectar a **Khipu, Fintoc, SII, calculadora UF**.
- Permite que el agente invoque varias tools en paralelo (ej: validar RUT en SII *y* consultar deuda CMF al mismo tiempo).

### 5. MCP (Model Context Protocol)

- Permite **exponer la normativa CMF / SII / SERNAC** como **servidores reutilizables**.
- Cada equipo del lab puede hacer su propio MCP custom y este se vuelve activo agéntico de alto valor.
- Facilita conectar bases de URLs maliciosas (CSIRT) si se hace ciberseg.

### Bonus: prompt caching

- **90 % de descuento** en lecturas.
- Cachear toda la normativa una vez y pagar solo por la pregunta del usuario hace el modelo viable a **centavos por consulta**.

---

## Casos enterprise útiles para citar en el pitch

- **Zapia (BrainLogic)** — 2,5 M usuarios en WhatsApp en el primer año con Claude, hyperlocalizado por país, 90 %+ feedback positivo. **Ya validó el patrón en LATAM.**
- **Brex, Ramp, CRED** — fintechs de USA/India con Claude en producción.
- **Citi, Commonwealth Bank of Australia** — banca grande usando Claude.

---

## Líneas rojas (Acceptable Use Policy de Anthropic, sept 2025)

El MVP **NO puede**:

- Tomar decisiones finales de **aprobación crediticia**.
- **Recomendar inversión específica**.
- Operar como **"asesor financiero"** sin disclosure.

El MVP **SÍ puede**:

- **Educar**.
- **Traducir jerga**.
- **Resumir contratos**.
- **Comparar productos públicos**.
- **Llenar formularios**.
- **Detectar cláusulas abusivas** según SERNAC.
- **Calcular CAE / cuotas** con datos públicos.

> **La Línea 1 del lab está perfectamente alineada con lo permitido.** No es accidente — los organizadores la diseñaron así.

---

## Stack recomendado para 7 días

| Capa | Recomendación | Por qué |
|---|---|---|
| Modelo principal | Sonnet 4.6 | Balance + 1 M contexto |
| Modelo volumen | Haiku 4.5 | $1/$5 por 1 M tokens |
| SDK | Anthropic SDK Python | Mejor soporte para agentic |
| Backend | FastAPI | Rápido, async, ecosistema Python |
| Frontend | Next.js 15 + Vercel AI SDK | Streaming + AI UX |
| BaaS | Supabase (Postgres + Auth + RLS + Vector + Storage) | Todo en uno, gratis para 48 h |
| Canal usuario | Twilio WhatsApp Business sandbox | Penetración 95 % en Chile |
| Observabilidad | Langfuse | Tracing de llamadas a LLM |
| Embeddings | Voyage AI | Calidad alta para español |
| Deploy | Vercel + Railway / Fly.io São Paulo | Latencia LATAM aceptable |

---

## Implicancias para nuestras decisiones

| Decisión | Default propuesto | Cuándo desviarse |
|---|---|---|
| **Modelo principal** | Sonnet 4.6 | Si necesitamos razonamiento muy complejo (ADR de Mi Plan B): subir a Opus 4.7 |
| **Backend** | Sonnet 4.6 con prompt caching de toda la normativa | Si el caso requiere chat WhatsApp masivo: Haiku 4.5 con context summary |
| **Citaciones** | API Citations habilitada por defecto | Solo desactivar si no aporta al criterio (raro) |
| **Vision** | Habilitar para casos donde el usuario suba documentos | Skip si el caso de uso es solo conversacional |
| **MCP** | Construir al menos 1 MCP custom (fuente regulatoria) | Si el tiempo aprieta: usar tools directas |
| **Prompt caching** | Habilitar día 1, medir ahorro | Siempre conviene si hay contexto largo |

---

## Backlog técnico para spikes pre-lab

- [ ] Spike 1: Sonnet 4.6 con todo el texto de la **Ley 21.521** cargado vía Files API + Citations habilitadas → medir tokens, latencia y exactitud de cita.
- [ ] Spike 2: Vision sobre 3 contratos retail reales (CMR / Ripley / Cencosud) → medir extracción de CAE y comisiones.
- [ ] Spike 3: MCP custom mínimo que exponga `buscar_articulo(ley, articulo)` a Claude → medir invocación correcta.
- [ ] Spike 4: Twilio WhatsApp sandbox → mensaje recibido, respondido en <10 s.
- [ ] Spike 5: Prompt caching aplicado al system prompt regulatorio → medir reducción de costo en 100 calls.

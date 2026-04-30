---
titulo: "Documentación oficial chilena requerida para los 19 dolores priorizados de Tu Plata Mipyme"
objetivo: "Por cada uno de los 19 dolores marcados como ✅ Incluir, identificar la documentación oficial chilena (leyes, formularios, manuales, circulares, ordenanzas, APIs) que el asistente IA necesita ingerir para resolver el dolor con autoridad. Distinguir entre API pública, HTML scrapeable y trámite presencial. Identificar brechas donde la documentación no está consolidada."
agent: "deep-research-max-preview-04-2026"
linea: inclusion-financiera
prioridad: alto
---

# Prompt: Documentación oficial chilena para los 19 dolores priorizados

## Contexto

El equipo **The Clauders** está construyendo **Tu Plata Mipyme**, un copiloto freemium en WhatsApp + Web que acompaña al microemprendedor chileno desde el sueño hasta la PYME. Tras revisar 48 dolores documentados en el [run #06](2026-04-30-06-entrepreneur-journey-backlog.md), el equipo priorizó en la [reunión del 30-abr-2026](../../../docs/reuniones/2026-04-30-revision-dolores-backlog.md) **19 dolores** que el producto va a atacar (✅ Incluir).

**Necesidad concreta:** antes de empezar a programar, necesitamos saber **exactamente qué documentación oficial chilena debemos ingerir** en el RAG/MCP de cada subagente para que las respuestas sean **citables, verificables y actualizadas**. Sin este mapeo, terminamos haciendo "vibe answers" que las reglas del lab prohíben.

El target del producto son **mujeres microemprendedoras 30-50 años en regiones del sur de Chile** (Araucanía 38% informalidad), por lo que las fuentes deben ser accesibles y aplicables a este segmento (no a grandes empresas).

## Lo que necesito

Para **cada uno de los 19 dolores** listados abajo, mapear la documentación oficial chilena necesaria con la estructura definida en la sección de output.

---

### Listado de los 19 dolores ✅ Incluir

#### E0 — Idea / Sueño (6 dolores)

- **[E0-D2] Miedo irracional al SII** — Decisión equipo: "✅ Incluir (CRÍTICO + transversal)". Comunicación incremental por etapa. La IA debe desmitificar fiscalización temprana.
- **[E0-D3] Ignorancia sobre fijación de precios** — Decisión: "✅ Incluir con disclaimer". Solo teoría simplificada, sin cálculo directo. "No te calculo, te enseño lo que debes saber".
- **[E0-D5] Fricción cognitiva sobre permisos** — Decisión: "✅ Incluir". Documentación municipal + manejo de alimentos + reglamentos.
- **[E0-D6] Soledad del emprendedor / red de apoyo** — Decisión: "✅ Incluir + scrapper". Scrapper diario de Sercotec, Corfo, Startup Chile, FOGAPE, FOSIS. Match con perfil del usuario.
- **[E0-D7] Mezclar finanzas familiares con negocio** — Decisión: "✅ Incluir como pregunta diagnóstica". Recomienda cuentas vista gratuitas (Cuenta FAN BancoChile, etc.).
- **[E0-D8] Desconocimiento del valor del propio tiempo** — Decisión: "✅ Incluir dentro de pricing". Va dentro del flujo de cómo poner precios.

#### E1 — Validación informal (4 dolores)

- **[E1-D1] Sin RUT comercial / no factura B2B** — Decisión: "✅ Incluir". Cuantificar pérdida B2B mensual ("perdiste $200K"). Caso real: cuñada de Felipe vende tortas, director de colegio le pide factura mensual y pierde la oportunidad.
- **[E1-D2] Recepción de pagos en CuentaRUT personal** — Decisión: "✅ Incluir como warning IA". Alerta cuando se acerca el tope mensual o riesgo de bloqueo por presunción de lavado. Open Banking estatal llega 07/2027.
- **[E1-D7] Crecimiento invisible (sin balance real)** — Decisión: "✅ Incluir". Mensaje diario por WhatsApp pidiendo ingresos/gastos. Generar el hábito de registro.
- **[E1-D8] Miedo a perder beneficios sociales** — Decisión: "✅ Incluir como info". Información estática + scrapper de beneficios estatales.

#### E2 — Formalización (7 dolores)

- **[E2-D1] Fricción técnica en Tu Empresa en Un Día (RES)** — Decisión: "✅ Incluir como acompañamiento". "Te ayudamos a completar formularios pero no lo hacemos por ti".
- **[E2-D2] Elección errónea de figura jurídica** — Decisión: "✅ Incluir". Información a la mano (MEF vs EIRL vs SpA + régimen contable Pro-Pyme General/Transparente).
- **[E2-D3] Abismo RES↔SII (Formulario 4415)** — Decisión: "✅ Incluir como continuación de etapa". Construir journey: SPA creada → SII iniciar actividades → activar boleta → activar factura.
- **[E2-D4] Acreditación domicilio tributario** — Decisión: "✅ Incluir como recomendación". Atasco real — Jose lo vivió. Si arriendas y la familia no tiene domicilio propio = trancado.
- **[E2-D5] Patente municipal** — Decisión: "✅ Incluir". Una patente por municipalidad si vende en varias comunas. Nuestro flujo de agentes debe geolocalizar.
- **[E2-D6] Permisos sanitarios SEREMI** — Decisión: "✅ Incluir condicionado". Solo si vende alimentos. El flujo de agentes debe activarlo/excluirlo según el caso.
- **[E2-D8] Sobrecarga de firmas electrónicas (FEA vs simple)** — Decisión: "✅ Incluir como quick win". One-time cada 2 años. Info clave para no comprar Token caro innecesario.

#### E3 — Operación formal (2 dolores)

- **[E3-D1] Declaración mensual F29** — Decisión: "✅ Incluir". Acompañamiento fuerte primeros 3 meses + recordatorio + calendario (algo agendable que reserva el día). "El tremendo deseable de muchos".
- **[E3-D3] Régimen tributario** — Decisión: "✅ Incluir, pero en E2". Es necesario para iniciar actividades — debería estar en flujo previo de formalización.

---

## Estructura solicitada al agente — POR CADA DOLOR

Cada dolor debe tener un bloque con esta estructura exacta:

```markdown
### [E2-D5] Patente municipal

**Resumen del dolor:** una frase del problema (no copiar el contexto, asumir conocido).

**Documentación esencial (orden de prioridad):**

1. **[Nombre del documento]**
   - **URL:** https://...
   - **Qué cubre:** texto descriptivo de qué resuelve este documento del dolor.
   - **Vigencia:** fecha de última actualización conocida (si está disponible).
   - **Acceso técnico:** una de:
       - `API pública disponible` — citar endpoint si lo tienes (ej: API LeyChile BCN).
       - `HTML scrapeable` — sin login.
       - `Requiere ClaveÚnica/ClaveSII` — el usuario debe autenticar.
       - `PDF descargable` — formato fijo, ingestable a RAG.
       - `Trámite presencial` — sin documentación digital usable.
   - **Notas:** caveats relevantes (ej: "ordenanzas pequeñas no están online", "API tiene rate limit").

2. **[Otro documento]**
   - ...

**Documentación complementaria** (no esencial pero recomendada):
- ...

**Brechas detectadas:**
- Casos donde la documentación no existe o está fragmentada.
- Ejemplo: "No existe API consolidada de ordenanzas municipales — requiere scrapeo manual top 50 comunas".

**Acciones técnicas concretas que requiere el equipo:**
- MCPs específicos a construir (ej: "MCP LeyChile para leyes nacionales").
- Scrapeos a montar (ej: "scrape diario sitio sercotec.cl/calendario-postulaciones").
- Datasets a curar manualmente (ej: "tabla de tasas de patente municipal por comuna top 50").
- Casos donde el handoff humano es inevitable (ej: "comunas pequeñas → derivar a contador").
```

---

## Reglas estrictas para el agente

### Fuentes
- **Solo fuentes oficiales chilenas:** BCN (LeyChile), SII (sii.cl, mipyme.cl), ChileAtiende, MINSAL (asdigital), Sercotec, Corfo, MIDESO (Registro Social de Hogares), DIPRES, INE, Banco Central, CMF, Subtel.
- **Municipalidades:** sitios oficiales `.gov.cl` o `.muni.cl`.
- **NO usar:** Wikipedia, blogs comerciales, foros, sitios de abogados privados (excepto cuando sean la única fuente y declarar la limitación).

### Verificabilidad
- **URLs verificables.** Si la URL está detrás de login (ClaveÚnica, ClaveSII), señalarlo explícitamente.
- **Vigencia:** indicar última actualización conocida o "permanente".
- **Si no existe documentación oficial sobre un punto, decirlo.** No inventar fuentes.

### Acceso técnico
- **Distinguir siempre entre 4 modalidades:**
  - API pública (mejor caso, integración limpia con MCP).
  - HTML scrapeable público.
  - Login requerido (HTML/PDF tras autenticación).
  - PDF descargable.
- **Si una API existe, citar el endpoint** (aunque sea estimado).

### Brechas
- **Identificar dónde no hay docs o están fragmentadas.** Esto define dónde el producto necesita scrapeo manual o handoff humano.
- **Ejemplos típicos a buscar:** ordenanzas municipales (fragmentadas), reglamentos sanitarios pequeños, calendarios Sercotec/FOSIS (no APIs), criterios RSH no publicados.

### Acciones técnicas
- **Concretas, no genéricas.** "Construir MCP para LeyChile usando endpoint X" en vez de "integrar info legal".
- **Sugerir el alcance.** ¿Cuántos documentos hay que ingestar? ¿Qué tan grande es el dataset?

---

## Top 5 prioridad si tiempo es limitado

Si por algún motivo el agente no alcanza a cubrir los 19 dolores con profundidad equivalente, priorizar estos 5 (los más complejos y críticos):

1. **[E2-D5] Patente municipal** — fragmentación por comuna, alta complejidad.
2. **[E2-D6] SEREMI alimentos** — reglamento técnico denso, requisitos por escala.
3. **[E2-D2] Figura jurídica** — múltiples leyes a comparar.
4. **[E0-D6] Calendarios Sercotec/Corfo/FOGAPE** — fuentes dispersas, alta utilidad.
5. **[E2-D3] F4415 + activación boleta/factura** — atasco real frecuente.

## Por qué este run vale los ~USD 5

Sin este mapeo, el equipo construye el RAG/MCP "a ojo" y termina con:
- Citas inventadas (alucinación legal).
- Cobertura inconsistente (algunas etapas con docs, otras sin).
- Trabajo duplicado (re-buscar las mismas leyes una y otra vez).

Con este mapeo, el equipo puede:
- Listar los **MCPs concretos a construir** (LeyChile, ChileAtiende, etc.).
- Saber qué **ordenanzas municipales scrapear** (top 50 comunas vs todas).
- Identificar dónde **el handoff humano es la única salida** (alcance del Marketplace).
- Decidir qué documentos **descargar como PDF** y meter al RAG estático vs **conectar via API**.

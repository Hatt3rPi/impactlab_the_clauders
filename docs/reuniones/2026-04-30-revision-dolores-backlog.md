---
title: "Revisión del backlog: dolores E0-E3 del journey"
fecha: 2026-04-30
hora: "09:30"
duracion: "1h 33min"
tipo: "diseño-producto"
participantes:
  - Felipe Abarca
  - Jose Foncea
  - Cristian Astorga
  - Anahi Gonzalez
ausentes: []
tags:
  - reunion
  - backlog
  - tu-plata-mipyme
  - decisiones-producto
---

# Reunión: Revisión del backlog del run #06 (dolores E0-E3)

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Documento generado a partir de la transcripción literal de la reunión del 30-abr-2026 (09:30-11:03). Es fuente primaria de las decisiones del equipo sobre el backlog.

## TL;DR

- El equipo revisó **dolor por dolor** el catálogo del [run #06 Deep Research](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md), decidiendo cuáles atacar y cuáles excluir.
- **Etapa 0 (Idea/sueño):** la barrera es **psicológica, no tecnológica**. El copiloto debe actuar como consejero antes de meter herramientas financieras.
- **Etapa 1 (Validación informal):** "informalidad es un escudo de cristal". La IA debe demostrar empíricamente que **el costo de ser informal ya superó el costo de formalizarse**.
- **Etapa 2 (Formalización):** el equipo confirma que esto **es uno de los fuertes** del producto — la IA es el hilo conductor entre RES → SII → patente municipal → SEREMI → INAPI (este último excluido).
- **Etapa 3 (Operación formal):** acompañamiento fuerte los primeros 3 meses + recordatorios + calendario después. Quedó incompleta la revisión por corte de tiempo.
- **Decisiones de identidad:** lenguaje B1 (8° básico), párrafos cortos, dibujos. Diseño moderno pero serio (Cristian propone alineación con paleta Estado: blanco/azul + naranjo Claude).
- **Pendiente crítico:** confirmar con la organización si el producto del lab debe ser **100% gratuito** o si el modelo freemium es válido.

## Decisiones globales tomadas

| # | Decisión | Razón |
|---|---|---|
| 1 | **Segmento confirmado:** desde idea hasta MIPE/PYME básica (no se sube a mediana empresa). | Antes de los 30M CLP/mes ya empieza a requerir servicios distintos. |
| 2 | **Canal principal: WhatsApp (estilo "llamado telefónico") + Web complementaria con asistente Claude.** | WhatsApp para captura rápida (audio, fotos boletas, ventas del día); web para flujos complejos y como repositorio documental. |
| 3 | **Telegram queda fuera** (aunque Cristian propuso MVP allí por sus botones libres). | WhatsApp es donde está el segmento NSE D-E. Para botones se requerirá cuenta WhatsApp Business de automatización (template de marketing). |
| 4 | **Riesgo de alucinación con LLM: regla dura.** No hacer cálculos numéricos directos como "cobra X precio". Solo dar teoría + rango + disclaimer. | Las reglas del lab exigen que el producto **acompañe**, no haga la tarea. "Te ayudamos pero no lo hacemos por ti." |
| 5 | **Open Banking del Estado llega julio 2027.** Para el lab: reenvío de correos (Banco Chile sí, Santander no) + cartolas mensuales como contexto. | No hay integración transaccional disponible aún. |
| 6 | **Datasets oficiales del lab:** ya hay APIs/MCPs curados por el equipo organizador (canales habilitados especialmente para este proyecto). | Esperan que conectemos un MCP de Cloud a sus fuentes legales/regulatorias. |
| 7 | **Pendiente: confirmar modelo de negocio.** Freemium quedó en duda — no sabemos si el lab requiere gratuidad total. | Acción: consultar a la organización cuanto antes. |
| 8 | **Anahi asume System Design en Cloud** (cuenta propia) + paletas de identidad. | Ya está más adelante en la versión 6 con base de diseño estructural. |
| 9 | **Repo de demo: privado de transición ahora, oficial el 6 de mayo.** Estrategia de commits secuenciales sin "tabú": estructura → landing → features. | Las reglas del lab probablemente prohíben código previo al 6/5. Estrategia: "que parezca rápido pero no se vea pre-cocinado". |

## Decisiones por dolor (etapa por etapa)

Notación: ✅ **incluir** · ❌ **excluir** · 💡 **guiño/futuro** · ⏳ **pendiente revisar**

### E0 — Idea / Sueño

| ID | Dolor | Decisión | Notas del equipo |
|---|---|---|---|
| E0-D1 | Síndrome del impostor ("no soy empresaria") | ❌ Excluir | Jose: "es algo emocional, no se resuelve con un chatbot". |
| E0-D2 | Miedo irracional al SII | ✅ **CRÍTICO + transversal** | "Es lo más importante del proyecto." Comunicación incremental por etapa. |
| E0-D3 | Ignorancia sobre fijación de precios | ✅ Incluir con disclaimer | Solo teoría simplificada, sin cálculo directo. "No te calculo, te enseño lo que debes saber." |
| E0-D4 | Viabilidad de mercado hiperlocal | ❌ Excluir | "Llegamos tarde con este dolor — atendemos a quien ya sabe qué quiere hacer." |
| E0-D5 | Fricción cognitiva sobre permisos | ✅ Incluir | Documentación municipal + manejo alimentos + reglamentos. Costo: tener documentación + responder sobre ella. |
| E0-D6 | Soledad del emprendedor / red de apoyo | ✅ Incluir + scrapper | Scrapper diario de Sercotec, Corfo, Startup Chile, FOGAPE, FOSIS. Match con perfil del usuario. **Posible MVP separado.** |
| E0-D7 | Mezclar finanzas familiares con negocio | ✅ Incluir como pregunta diagnóstica | Pregunta inicial: "¿Tienes cuenta separada?" → si no, recomienda cuentas vista gratuitas (Cuenta FAN BancoChile, etc.). |
| E0-D8 | Desconocimiento del valor del propio tiempo | ✅ Incluir dentro de pricing | No es feature aparte: va dentro del flujo de cómo poner precios. |

**Síntesis E0 acordada:** *"La barrera principal aquí no es tecnológica, es psicológica. El copiloto debe actuar como consejero de confianza antes de introducir herramientas financieras."*

### E1 — Validación Informal

| ID | Dolor | Decisión | Notas del equipo |
|---|---|---|---|
| E1-D1 | Sin RUT comercial / no factura B2B | ✅ Incluir | Cuantificar pérdida B2B mensual ("perdiste $200K"). **Caso real Felipe:** su cuñada vende tortas por Instagram, un director de colegio le compraría todos los meses pero necesita factura → perdiendo oportunidad. |
| E1-D2 | Recepción de pagos en CuentaRUT personal | ✅ Incluir como warning IA | La IA, con contexto del workspace, alerta cuando se acerca el tope mensual o riesgo de bloqueo por presunción de lavado. Open Banking aún no — usar reenvío correos. |
| E1-D3 | Riesgo decomiso fiscalizadores | ❌ Excluir como dolor independiente | Tratado como disclaimer dentro del checklist de permisos. No agregar feature dedicada. |
| E1-D4 | Estafas con pantallazos falsos | ❌ Excluir | "Cae en ciberseguridad y choca con otro pilar del lab. Cotota la idea, pero descartada." |
| E1-D5 | Desorden de inventario básico | ❌ Excluir | "No apunta a la línea del proyecto (inclusión financiera). Es buena idea pero fuera de alcance." |
| E1-D6 | Costos de despacho informal | ❌ Excluir | "Cloud/GPT puede responder eso solo, no necesitamos invertir." |
| E1-D7 | Crecimiento invisible (sin balance real) | ✅ Incluir | Mensaje diario por WhatsApp pidiendo ingresos/gastos. **Generar el hábito de registro.** |
| E1-D8 | Miedo a perder beneficios sociales | ✅ Incluir como info | Información estática + scrapper de beneficios estatales. |

**Síntesis E1 acordada:** *"La informalidad es un escudo de cristal — protege de la burocracia pero expone a estafas, multas y estancamiento. La IA debe demostrar empíricamente que el costo de ser informal ya superó al de formalizarse."*

**Adición del equipo (Felipe):** falta agregar al backlog el dolor de **"obligaciones tributarias post-formalización"** — los formalizados saben que duele, pero a los que están antes del salto les vendemos el lado positivo (beneficios B2B) y omitimos el dolo. Hay que comunicar pros **y** contras.

### E2 — Formalización

| ID | Dolor | Decisión | Notas del equipo |
|---|---|---|---|
| E2-D1 | Fricción técnica en Tu Empresa en Un Día (RES) | ✅ Incluir como acompañamiento | "Te ayudamos a completar formularios pero no lo hacemos por ti." |
| E2-D2 | Elección errónea de figura jurídica | ✅ Incluir | Información a la mano (MEF vs EIRL vs SpA + régimen contable Pro-Pyme General/Transparente). Caso Jose: usó GPT especializado para asesorarse. |
| E2-D3 | Abismo RES ↔ SII (F4415) | ✅ Incluir como continuación de etapa | Construir journey: SPA creada → SII iniciar actividades → activar boleta → activar factura. **Pasos distintos**. |
| E2-D4 | Acreditación domicilio tributario | ✅ Incluir como recomendación | **Atasco real** — Jose lo vivió. Si arriendas, la familia no tiene domicilio propio y no quieres pagar oficina virtual = trancado. |
| E2-D5 | Patente municipal | ✅ Incluir | Una patente por municipalidad si vende en varias comunas. Nuestro flujo de agentes debe geolocalizar. |
| E2-D6 | Permisos sanitarios SEREMI | ✅ Incluir condicionado | Solo si vende alimentos. El flujo de agentes debe activarlo/excluirlo según el caso del usuario. |
| E2-D7 | Protección de marca INAPI | 💡 Guiño / logro futuro | Excluido del alcance principal: "quien piensa en INAPI ya está formado". Tratarlo como "checklist de cosas que podrías hacer en algún momento". |
| E2-D8 | Sobrecarga de firmas electrónicas (FEA vs simple) | ✅ Incluir como quick win | One-time cada 2 años. **Info clave para no comprar Token caro innecesario.** |

**Síntesis E2 acordada:** *"La formalización no es un acto, es un flujo de 4-6 sub-trámites en distintas agencias que no conversan entre sí. La IA debe ser el hilo conductor."* Felipe: **"Es nuestro fuerte hasta el momento."**

### E3 — Operación Formal (revisión incompleta)

| ID | Dolor | Decisión | Notas del equipo |
|---|---|---|---|
| E3-D1 | Declaración mensual F29 | ✅ Incluir | Acompañamiento fuerte primeros 3 meses + recordatorio + **calendario** (no solo pop-up — algo agendable que reserva el día). "El tremendo deseable de muchos." |
| E3-D2 | Facturación electrónica desde WhatsApp | ❌ Excluir generación automática | Afuera por complejidad técnica. Dirigir a soluciones existentes (Bsale, Defontana, SII Mipyme). **Mantenemos rol de información, no de ejecución.** |
| E3-D3 | Elección y comprensión del régimen tributario | ✅ Incluir, **pero en E2** | Es necesario para iniciar actividades — debería estar en el flujo previo de formalización. |
| E3-D4 a E3-D8 | (Resto: F22, certificados, conciliación, honorarios, multas SII) | ⏳ **Pendiente** | La reunión se cortó por compromiso de Felipe a las 11:00. **Revisar en próxima sesión.** |

## Decisiones de producto/contenido

### Lenguaje y tono
- **Nivel:** B1 / 8° básico, no más.
- **Formato:** párrafos cortos para dividir ideas. Dibujos > texto largo. Gráficos solo cuando lo técnico lo amerite.
- **Voz:** "Te recomiendo / piensa en esto / tiende a esto." **Nunca:** "haz esto exactamente."

### Contenido y SEO
- **Generar landing page + blog** (no solo WhatsApp). Razón: la gente busca esto por Google primero, no por IA. Necesitamos presencia SEO.
- Felipe demostró el efecto de blog en Perplexity: 10K impresiones / mes orgánicas con artículos consistentes. **Perplexity premia autoridad y consistencia (>20 artículos buenos).**
- **Anahi:** generar landing pages de pros/contras de formalización + cómo formalizarse paso a paso.

### Identidad visual
- Tendencia hacia **diseño corporativo sobrio** (Cristian + Felipe + Anahi alineados).
- **Inspiración:** transmitir formalidad/seriedad/confianza ("nos basamos en fuentes públicas para responder").
- **Pendiente Anahi:** propuestas de paleta. Tensión entre alinearse con paleta Estado (blanco/azul) + naranjo Claude vs marca propia más diferenciada.

### Audio / voz
- **Eleven Labs vía MCP en Cloud** parece la opción para resúmenes en audio (microemprendedores con poco tiempo de lectura).
- **Regla:** servicios de tercero solo si Cloud no tiene la capacidad nativa.

## Acciones inmediatas

| # | Quién | Qué | Cuándo |
|---|---|---|---|
| 1 | Felipe | Marcar dolores in/out en el backlog del run #06 según decisiones de hoy | Hoy 30-abr |
| 2 | Felipe | Pedir documentación oficial al Deep Research (SII, formalización, boletas, tributarios) | Hoy/mañana |
| 3 | Felipe | Análisis de gap: documentación faltante para los dolores cubiertos | Esta semana |
| 4 | Anahi | System Design en Cloud + propuestas de paletas de identidad | 30-abr / 1-may |
| 5 | Jose | Especificaciones (cuando Felipe avise que tenga el material listo) | Esta semana |
| 6 | Cristian | Revisar APIs/MCPs habilitados por el lab + factibilidad técnica del backlog seleccionado | Esta semana |
| 7 | Equipo | Consultar a la organización si el modelo debe ser 100% gratuito | Lo antes posible |
| 8 | Felipe | Continuar revisión de E3 (D4-D8) + E4 + E5 con el equipo | Próxima reunión |
| 9 | Felipe | Diagrama del journey con hitos visualizables | Esta semana |

## Pendientes / preguntas abiertas

1. **¿Modelo del producto debe ser 100% gratuito para el lab?** (consultar organización).
2. **¿Eleven Labs MCP es oficial en Cloud?** Verificar.
3. **¿Hay datasets adicionales del lab habilitados desde 30-abr?** Revisar canales del organizador.
4. **¿Cómo balanceamos el "te enseño los pros del B2B" con "ojo: te llegan obligaciones tributarias"?** (No engañar al usuario — comunicación honesta).
5. **¿Qué hacemos cuando el negocio crece más allá de PYME básica?** Felipe: "Lo derivamos a un contador real (handoff Marketplace)."

## Citas memorables

> "Pero al final es ofrecer la ayuda a que este gallo deje de pensar y se dedique a emprender." — Felipe

> "Estamos pensando en una persona que tiene escolaridad baja, poco tiempo para leer, y lo que lee le cuesta mucho entenderlo. Un acompañamiento estilo chatbot es una ayuda caída del cielo." — Anahi

> "El servicio terminaría siendo tan bueno que se terminaría siendo un Claude Code gratuito en tu celular vía WhatsApp." — Cristian

> "Es nuestro job y hasta el momento es uno de los fuertes." — Felipe sobre la formalización como hilo conductor.

## Referencias

- [Run #06 Deep Research — Entrepreneur Journey](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md)
- [Backlog Tu Plata Mipyme (60 features)](../tu-plata-mipyme/backlog.md) — actualizar con decisiones de esta reunión.
- [Definición canónica Tu Plata Mipyme](../tu-plata-mipyme/que-es.md)
- [ADR 0004 — WhatsApp-first, freemium, multi-agente](../tu-plata-mipyme/especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md) — el modelo freemium queda en revisión.
- Transcripción literal: `Formalización y Asistente Conversacional Transcripción.txt` (no commiteada).

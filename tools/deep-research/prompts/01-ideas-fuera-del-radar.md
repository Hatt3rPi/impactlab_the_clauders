---
titulo: "Ideas fuera del radar para literacy regulatoria con IA en Chile"
objetivo: "Expandir el espacio de ideas más allá de las 9 candidatas actuales del equipo, buscando ángulos no obvios cruzando datasets sub-utilizados, eventos de vida poco atendidos, canales alternativos y sub-segmentos invisibles. Inspirarse en casos exitosos en otros países que no se han replicado en Chile."
agent: "deep-research-max-preview-04-2026"
linea: inclusion-financiera
prioridad: critico
---

# Prompt: Ideas fuera del radar

## Contexto

Soy parte de un equipo de 4 personas que participará en el **Claude Impact Lab Chile 2026** (6-7 mayo 2026, Espacio Riesco, organizado por Anthropic + Bendita IA + FinteChile). El Track 1 del evento se llama **"Inclusión Financiera y Literacy Regulatoria"** y declara textualmente: *"5 millones de chilenos tienen derechos financieros que no pueden ejercer"*. Esperan asistentes conversacionales y traductores regulatorios sobre normativa real chilena (Ley Fintech 21.521, NCG 514 Open Finance, Ley 21.719 Protección de Datos, Ley 21.673 Antifraude bancario, Ley 21.563 Régimen concursal, etc.).

Los datasets disponibles son normativas y circulares de **CMF** (Comisión para el Mercado Financiero), procedimientos del **SII** (Servicio de Impuestos Internos), marcos de **SERNAC** (Servicio Nacional del Consumidor) y otras instituciones públicas chilenas.

El equipo ya tiene un backlog de 9 ideas pre-evaluadas (todas dentro del esquema "chatbot/RAG sobre regulación + Citations + Vision"):

1. Defensor — copiloto de derechos para morosos en DICOM (cobranza abusiva)
2. Letra Chica / Tu Plata — semáforo visual de contratos financieros con CAE
3. Tu Plata Mipyme — asistente regulatorio para microemprendedores informales
4. Mi Plan B — coach de salida del sobreendeudamiento
5. ConfíaConmigo — traductor de derechos para migrantes
6. Mi Pensión — traductor previsional con simulador
7. Antiestafa / Pillo — verificador antiphishing
8. Mis Datos · ARCOP — copiloto de derechos de protección de datos
9. Open Finance Explainer — consentimiento informado B2B
10. sabidurIA ciudadana — wiki de la vida (idea unificadora que mapea eventos de vida a derechos)

## Lo que necesito

Genera **15-20 ideas adicionales** de productos IA-nativos para literacy regulatoria/financiera en Chile que **explícitamente NO sean** ninguna de las 10 anteriores ni variantes triviales de ellas. Busca ángulos genuinamente no obvios cruzando los siguientes ejes:

### A. Eventos de vida poco atendidos por el ecosistema fintech actual chileno

Ejemplos para inspirarte (no te limites a éstos): nacimiento de hijo y postulación a chile crece contigo, egreso de enseñanza media y postulación FUAS/CAE/becas, primer trabajo formal y elección de AFP, matrimonio/conviviencia civil y régimen patrimonial, adquisición primera vivienda, cesantía y AFC, enfermedad seria y CAEC/GES no usados, fallecimiento de familiar y posesión efectiva + AFP + seguros con beneficiario, violencia intrafamiliar económica, jubilación con foco en PGU y modalidades, salida de prisión y reinserción financiera, deportistas amateur y régimen tributario especial, despido masivo de empresa en quiebra.

### B. Datasets chilenos públicos sub-utilizados

Ejemplos: APIs del Registro Civil (posesión efectiva, defunción), Servicio de Impuestos Internos (propuestas de declaración, regímenes simplificados), Superintendencia de Pensiones (afiliados, multifondos), Superintendencia de Salud (isapres, GES), Superintendencia de Insolvencia y Reemprendimiento, MinDes (Registro Social de Hogares), AFC, Servel, JUNJI, JUNAEB, FOSIS, CONADI, SENADIS, Sename, ChileCompra, ChileAtiende, Banco Central, INE, Subtel.

### C. Canales de distribución alternativos a app/web tradicional

Ejemplos: WhatsApp + voz, SMS, ferias libres, juntas de vecinos, parroquias y comunidades religiosas, sindicatos rurales y portuarios, cooperativas (Coopeuch, COOPEUCH, otras), Hogar de Cristo financiero, Fondo Esperanza, Banigualdad, OMIL municipales, INDAP (campesinos), DGAC, partnerships con BancoEstado/CuentaRUT, Carabineros 600, kioscos físicos, audio/podcast.

### D. Sub-segmentos invisibles con dolor agudo y monto reclamable alto

Ejemplos para inspirarte: privados de libertad reinsertándose, viudas pre-65 antes de PGU, deportistas amateur con régimen tributario especial, vendedores ambulantes regularizados (Ley de Comercio en la Vía Pública), jóvenes egresados de SENAME (vulnerabilidad post-egreso), estudiantes con CAE en mora, trabajadores de plataformas digitales (Uber, Rappi, Cornershop), personas con discapacidad y beneficios tributarios, cuidadores informales de adultos mayores o personas con discapacidad, mujeres víctimas de violencia económica/coacción financiera.

### E. Formatos de output novedosos (no chat de texto plano)

Ejemplos: audio conversacional voice-first, generación de cartas formales en PDF firmable, llenado de formularios oficiales, simuladores interactivos, dashboards visuales para que el usuario "vea" sus derechos, generación de timeline de plazos automatizada, integración con calendar.

## Inspírate en casos análogos en países comparables

Busca productos exitosos en **México, Brasil, Colombia, Perú, India, Reino Unido, Estonia, Singapur, Países Bajos, Estados Unidos** (especialmente productos de welfare reclaim como Stamford CARE, Benefits.gov, Propel Inc, MakeMyMoney; productos cívicos como gov.br Brasil, LifeSG Singapur, eesti.ee Estonia, mygov.in India, SafeMortgage en UK). Para cada uno, identifica el ángulo original y evalúa qué tan replicable es a contexto chileno.

## Formato del output esperado

Para cada idea, devuelve:

1. **Nombre tentativo** (corto y evocador).
2. **Problema concreto** que resuelve (cuál es el dolor del ciudadano y por qué no está atendido).
3. **Sub-segmento prioritario** (sé específico: no "todos los chilenos").
4. **Datasets chilenos requeridos** (sé específico con nombres de instituciones y URLs si las conoces).
5. **Demo imaginado en 60 segundos** (un caso concreto, narrado desde el punto de vista del usuario).
6. **Capacidades de Claude que aprovecha** (Citations, Vision, Tool Use, Structured Outputs, MCP, prompt caching).
7. **Por qué nadie en Chile lo está haciendo** (gap real vs producto inexistente).
8. **Caso análogo en otro país** (con link y referencia).
9. **Riesgo principal** (regulatorio, técnico, de alcance).
10. **Por qué podría diferenciar al equipo en este lab específico** (recordando que hay 200 participantes y 50%+ probablemente intentará un RAG sobre regulación).

## Reglas para el agente

- **Si no encuentras dato oficial verificable, dilo explícitamente**. Prefiero "sin fuente verificable" antes que un dato fabricado.
- **No me devuelvas variantes triviales de las 10 ideas listadas** ("Defensor para arrendatarios", "Letra Chica para isapres") salvo que el ángulo de cruce sea genuinamente nuevo.
- **Cita las fuentes oficiales chilenas que mencionas** con URLs verificables.
- **Si una idea requiere un dato chileno que no existe públicamente, dilo**. No la propongas asumiendo que existe.
- **Prioriza ideas con métrica de impacto cuantificable** (CLP activados, tiempo ahorrado, infracciones evitadas).
- **Estructura el reporte con índice al inicio** y secciones claras por idea.
- **Al final, agrega una sección "Top 5 ideas más prometedoras según impacto × diferenciación × viabilidad en 7 días"** con justificación.

## Por qué esto vale los USD 5 que cuesta

El equipo lleva 24 horas de research y tiene 10 ideas mayormente estructuradas como "RAG sobre regulación". El riesgo real del lab es que las 200 personas converjan a la misma idea. Un set de 15-20 ideas adicionales pensadas desde ángulos no obvios es justo lo que el equipo no tiene capacidad de generar en una mañana, y es donde un agente con 160 queries de búsqueda y exposición a productos cívicos globales aporta valor que el equipo solo no logra.

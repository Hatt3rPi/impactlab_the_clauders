---
title: "Estrategia de pitch y arquitectura para el lab (7-may-2026)"
description: "Recomendaciones operacionales concretas para el pitch y la arquitectura del MVP, derivadas del análisis de ganadores 2025-2026 con LLMs frontera."
autor: "Síntesis del equipo a partir del run Deep Research Max 02-ganadores-hackathons-fintech-ia"
fecha: 2026-04-29
tags:
  - equipo
  - pitch
  - arquitectura
  - estrategia
---

# Estrategia de pitch y arquitectura para el lab del 7 de mayo

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Tácticas extraídas del [run Deep Research del 29-abr-2026](../research/_runs-deep-research/2026-04-29-02-ganadores-hackathons-fintech-ia.md) sobre patrones de ganadores en hackathons fintech IA 2025-2026. **Aún no validadas en práctica por el equipo.**

> Este documento **complementa** las [convenciones de patrones hackathons](../research/mercado/patrones-hackathons-fintech.md) (que sintetizó el PDF de Calibria con datos pre-2024) con datos frescos sobre cómo cambió el listón en los últimos 18 meses con la llegada de Claude 4.x, Gemini 3.1, GPT-5 y los agentes asíncronos.

## La tesis: el listón subió radicalmente en 2025-2026

> **Los proyectos que envuelven una sola llamada a un LLM están sistemáticamente descalificados.** La era del "wrapper" terminó. Los ganadores construyen ecosistemas agénticos B2B/cívicos con MCP, Citations API y demos end-to-end sobre datos sucios reales.

## Anti-patrones que descalifican (datos de postmortems 2025-2026)

| Anti-patrón | Por qué pesa | Caso documentado |
|---|---|---|
| **Wrapper de LLM** sin lógica de enrutamiento ni estado | Filtro de viabilidad inmediato | "Resume mis PDFs legales" perdió toda barrera de entrada |
| **"Agent Porn"** — 15 agentes debatiendo entre sí en bucle infinito sobre problema trivial | Sobre-ingeniería sin foco | Postmortems hackathons 2026: jueces detectan en 30s |
| **Demo que falla en vivo** | Causa #1 de muerte súbita | OpenAI París 2024: "API falló bajo carga, contexto desbordó ventana, drift en system prompt" |
| **Mercado amplio "para todos los chilenos"** | Compite mentalmente contra ChatGPT y pierde | Los ganadores eligen "Permisos ADU en California", "Carreteras rurales", "Volúmenes EBS" |
| **Mockups en lugar de datos reales** | Intolerancia absoluta del jurado | Aceleración del desarrollo con IA hace inexcusable un mockup |
| **Sin Citations** | Mente del jurado descalifica | Estándar normativo en RegTech 2026 |
| **Sin MCP custom** | Pierdes diferenciación visible | "Madurez ingenieril" se mide por servidor MCP propio |

## El estándar técnico de 2026 (no negociable)

| Pre-2024 | 2025-2026 |
|---|---|
| Un solo LLM con prompts en cadena | Redes de agentes asíncronos con enrutamiento especializado |
| Texto plano + chat + PDFs pre-procesados | **Multimodal nativo** sobre documentos sucios no estructurados |
| Ingeniería de prompts ("actúa como experto") | **Citations API obligatoria** + anclaje a fuentes auditables |
| RAGs genéricos experimentales | **Servidores MCP customizados** + API gateways |
| Mockups en Figma + fallos tolerados | **Demo end-to-end con datos reales**; intolerancia a fallos asíncronos |
| "IA B2C" amplia ("chatbot para enseñarte a ahorrar") | Fricción regulatoria B2B profunda y oculta |

## Plantilla de proyecto ganador 2026 — Caso CrossBeam (Anthropic Opus 4.6)

Es la plantilla más limpia documentada. La sigo como referencia táctica:

| Elemento | Cómo lo hizo CrossBeam |
|---|---|
| **Founder** | Solo founder (Mike Brown), abogado sin background CS |
| **Problema** | Permisos ADU California: 90 % rechazados por errores burocráticos |
| **Insight** | Vio problema de proceso, no de tecnología |
| **Stack** | Claude Code + Agents SDK + Next.js 16 + Express + Cloud Run + Vercel sandboxes |
| **Demo** | Arrastrar carta de rechazo gubernamental real → plan de acción con cita exacta del California Government Code §§66310-66342 |
| **Métrica** | "De meses a 20 minutos" |
| **Capacidades Claude** | Vision sobre planos + procesamiento paralelo con sub-agentes + Citations al código gubernamental |
| **Por qué ganó** | Verticalidad absoluta del problema + dominio sobre tecnología |

## 6 tácticas operacionales para nuestro pitch del 7 de mayo

### 1. La narrativa de apertura: dominio sobre tecnología (1,5 min)

- Abrir con **caso humano nombrado + fricción regulatoria hiperespecífica chilena**.
- Plantilla: *"El artículo X de la Ley Y exige a las pymes presentar el formulario Z en un formato que toma N horas. María perdió W por un error humano aquí."*
- **No** abrir con "queremos ayudar a 5M chilenos" — el "dolor aburrido" gana al "dolor genérico".

### 2. Arquitectura del demo en vivo: el "momento de magia" multimodal (2 min)

- Cero maquetas. Arrastrar un **documento real sucio** (formulario SII manchado, contrato de crédito complejo, papel de cobranza).
- **Stack split:**
    - **Claude Haiku 4.5** en paralelo para enrutamiento inicial y extracción rápida.
    - **Claude Sonnet 4.6** para razonamiento legal pesado (con prompt caching).
- **Mencionar verbalmente** la arquitectura asíncrona en el pitch — eso captura el **bonus de +5 puntos por agentic excepcional**.

### 3. Capturar el 20 % de "Uso responsable de datos": Citations + trazabilidad

- UI dividida: izquierda documento original | derecha veredicto del agente.
- Cada afirmación legal con **número de cita interactiva**.
- Click en cita → highlight visual de la línea exacta de la ley en el documento.
- Sin Citations, ni siquiera consideramos defendible la solución.

### 4. Implementar un servidor MCP propio para contexto regulatorio chileno

- Durante los 7 días pre-lab, **compilar la normativa local relevante** (Ley 21.521, Ley 21.719, NCG 514, Ley 21.673, etc.) en una base local.
- Construir **un servidor MCP simple** que la exponga.
- En el pitch decir: *"Desarrollamos un servidor MCP dedicado a la normativa chilena. Esto permite a nuestros agentes consultar regulaciones de forma dinámica reduciendo el riesgo de alucinaciones."*
- Esto golpea directo el **25 % de Claude & Agentic Thinking**.

### 5. Protocolo de contingencia: state-freezing local

- Causa #1 de muerte súbita en hackathons presenciales: **API falla en vivo**.
- Implementar modo **"State-Freezing"**: cachear localmente los payloads exitosos de las consultas complejas durante las pruebas.
- Si en demo la API falla / latencia explota → enrutar a caché local pre-verificado con indicador visual sutil de "modo offline" pero **sin interrupción del flujo visual**.
- Esta sola táctica nos pone delante del 70 % de equipos que asumen que la API responderá.

### 6. Cierre: "Partnership readiness" como marca blanca (1,5 min)

- Posicionar la herramienta como **ecosistema marca blanca integrable** vía API o MCP propio en portales bancarios chilenos existentes.
- Cierre tipo: *"Hemos resuelto la economía unitaria de la inclusión financiera reduciendo el costo de cumplimiento de días a minutos para las instituciones financieras."*
- Esta narrativa hizo ganar a Intuitech en Mastercard FINITIV (precisión >99 %, automatización 95 %, time-to-cash 20 días → 3 días).

## Casos ganadores 2025-2026 destacados

| Proyecto | Hackathon | Stack diferencial |
|---|---|---|
| **CrossBeam** | Anthropic Opus 4.6 | Vision sobre planos + Citations a código gubernamental |
| **Intuitech** | Mastercard FINITIV | Redes agénticas + Human-in-the-loop, demo cargando hipoteca real de 100 páginas |
| **Vera Health** | OpenAI x YC | Voice-first manos libres + Vector store de 60M artículos |
| **camfer** | OpenAI DevDay 2024 | OpenAI o1 + simuladores como tools en bucle de auto-corrección |
| **AgenticAI-MCP-Client** | Kong Hackathon | MCP centralizado en API Gateway |
| **RAG Pipeline V2** | You.com Hackathon | Citations API obsesiva + estructuración de tablas numéricas |
| **GSBD Cloud FinOps Bot** | AWS AIdeas 2026 | Event-driven + Human-in-the-loop para autorizar destrucción |
| **RegulAIte** | Microsoft AI Agents | Reducción drástica de alucinaciones en políticas corporativas |

## Aplicación directa a sabidurIA ciudadana

Si el equipo confirma sabidurIA en el Tollgate 1, esta estrategia se aplica así:

- **Apertura:** caso de María (mujer jefa de hogar, viuda) cuyo cónyuge muere y abandona CLP 8,8 M de saldo AFP por no saber tramitar posesión efectiva. *"El 41 % de los herederos AFP en Chile dejan ese dinero perdido."*
- **Demo:** ella sube foto del certificado de defunción → la IA detecta cobertura GES no usada en últimos meses + saldo AFC del cónyuge + cuota mortuoria + seguros con beneficiario. **CLP X recuperados en pantalla.**
- **Stack:** Haiku para extraer el certificado + Sonnet para razonamiento legal sucesorio + MCP custom de "cl-sucesiones" + Citations a Ley 21.484 (régimen sucesorio) + Reg. Civil.
- **Pantalla dividida:** documento original | árbol de derechos activables con cita.
- **Cierre:** marca blanca para AFPs, BancoEstado, Coopeuch, Hogar de Cristo Financiero — reducimos su "carga de notificación a herederos" de meses a horas.

## Referencias

- [Run Deep Research #02 — Patrones de ganadores 2025-2026](../research/_runs-deep-research/2026-04-29-02-ganadores-hackathons-fintech-ia.md) (reporte crudo, 441 líneas, 46 fuentes).
- [Patrones que ganan hackathons fintech (datos pre-2024)](../research/mercado/patrones-hackathons-fintech.md) — síntesis previa del PDF de Calibria, sigue siendo válida pero **se complementa** con esta nota.
- [Capacidades de Claude diferenciadoras](../research/tecnologia/capacidades-claude-diferenciadoras.md) — stack técnico recomendado.

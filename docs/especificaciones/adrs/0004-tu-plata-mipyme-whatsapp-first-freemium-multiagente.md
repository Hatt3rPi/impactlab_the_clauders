---
title: "ADR 0004 — Tu Plata Mipyme: WhatsApp-first, freemium y multi-agente"
estado: "Aceptado"
fecha: 2026-04-30
autor: "The Clauders (decisión de equipo)"
tags:
  - adr
  - tu-plata-mipyme
  - whatsapp
  - freemium
  - multi-agente
  - canal
---

# ADR 0004 — Tu Plata Mipyme: WhatsApp-first, freemium y multi-agente

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Decisión arquitectónica del equipo The Clauders sobre el producto Tu Plata Mipyme. **Supersede parcialmente al [ADR 0003](0003-plataforma-web-mobile-first.md)** en lo relativo al canal principal del producto (no en lo relativo a la wiki ni a otros productos).

## Contexto

Al concretar el producto **Tu Plata Mipyme** (asistente para microemprendedores informales) tres preguntas arquitectónicas tienen que cerrarse antes de empezar a construir:

1. **¿Cuál es el canal principal de interacción?** (web mobile-first vs. WhatsApp vs. híbrido)
2. **¿Qué modelo de negocio sostiene el producto** sin excluir al segmento que más lo necesita?
3. **¿Cómo se estructura la inteligencia conversacional**? (un agente monolítico vs. multi-agente)

El segmento objetivo opera bajo restricciones específicas:

- **1,08 millones de microemprendedores informales** en Chile (INE EME8); 59 % son mujeres, alta concentración fuera de la RM.
- **NSE D-E predominante**, comprensión lectora bajo nivel 3 PIAAC, tiempo de atención corto en móvil.
- **WhatsApp con > 90 % de penetración** en hogares chilenos, ya instalado y aprendido — la app más usada en la cohorte.
- **Cero capacidad de pago** al inicio, pero con **disposición a pagar real** una vez que ven valor monetario tangible (formalizar, postular a subsidio).
- **El corpus regulatorio relevante** (SII, CORFO, SERCOTEC, FOGAPE) cambia con frecuencia y requiere razonamiento especializado por etapa, no respuesta única.

Esto entra en tensión con el [ADR 0003](0003-plataforma-web-mobile-first.md), que decidió **web mobile-first** y dejó WhatsApp como canal secundario. Esa decisión sigue siendo válida para la **wiki del equipo** y para productos de *consulta puntual* (donde el usuario "busca y encuentra"). Pero **no es la correcta para Tu Plata Mipyme**, que es un producto de *acompañamiento sostenido en el tiempo*, donde la conversación recurrente y asincrónica es el modo natural de uso.

## Decisión

Para **Tu Plata Mipyme** decidimos:

### 1. WhatsApp es el canal principal; la web es complementaria

> Construimos primero el bot de WhatsApp Business y después la web. Toda funcionalidad core debe ser usable solo en WhatsApp. La web amplifica con visualización (gráficos de utilidad, formularios, descargas de PDF), nunca exclusiviza.

- **WhatsApp** = conversación, captura de datos, recordatorios, derivaciones.
- **Web** = landing pública (SEO + AI-citability), tablero visual del emprendedor, formularios largos cuando son inevitables, descargas (carta a banco, checklists).

### 2. Modelo freemium con triggers contextuales de conversión

> El plan **Free** debe ser suficiente indefinidamente. Cobramos sólo cuando el valor monetario del paso siguiente es evidente y monetario para el usuario.

- **Free (Brote):** acompañamiento informal, simulaciones, recordatorios.
- **Pro (Crece, ~$5.000/mes):** asistencia a formalización SII.
- **Plus (Postula, $15-30K por evento):** postulación asistida a CORFO/SERCOTEC.
- **Marketplace de asesores humanos:** comisión, sin margen al usuario.

### 3. Arquitectura multi-agente con supervisor + 4 subagents por etapa del journey

> Implementamos el sistema con Agent SDK como **1 supervisor + 4 subagents especializados** (`mentor-inicio`, `acompanante-informal`, `gestor-formalizacion`, `estratega-crecimiento`), no como un único system prompt monolítico.

- Cada subagent tiene system prompt focalizado < 2k tokens, tools propios y memoria persistente compartida (expediente del emprendedor).
- Handoffs explícitos entre etapas pasan contexto estructurado (JSON), no historia conversacional cruda.
- Caching diferenciado del corpus regulatorio por subagent (>80 % hit objetivo).

## Consecuencias

### Positivas

- **Cobertura del segmento real.** WhatsApp ya está en el bolsillo de la microemprendedora informal. Cero fricción de instalación, cero curva de aprendizaje de UI.
- **Asincronía natural.** La conversación recurrente cuadra con el ritmo del usuario (responde entre tareas, no en sesiones largas), lo que la web no facilita.
- **Freemium alinea incentivos.** Ningún paywall delante del valor base; el cobro aparece donde el usuario ya tiene plata por gastar (banco, subsidio). Reduce acusación de "lucrar con vulnerabilidad".
- **Multi-agente permite calidad y observabilidad.** Cada subagent se evalúa, ajusta y monitorea por separado; los prompts se mantienen pequeños y legibles.
- **Caching diferenciado** abarata el costo Anthropic en >70 % esperado vs. cargar el corpus completo en cada llamada.
- **Diferenciador claro en pitch.** "Multi-agente real con handoffs" + "WhatsApp first para el segmento que el resto ignora" es una historia distinta a la de los demás equipos.

### Negativas / costos

- **Dependencia de Meta / WhatsApp Business API.** Cambios en políticas de templates, costos por mensaje y latencias quedan fuera de nuestro control. Mitigación: arquitectura del orquestador agnóstica al canal (`Channel` interface), poder mover a Telegram/SMS si Meta endurece términos.
- **SEO y AI-citability se degradan como vector de adquisición.** Si WhatsApp es el canal principal, Google Search y AI Overviews dejan de ser el motor central. Mitigación: la **web pública sí mantiene SEO/AI-citability** para captar tráfico orgánico que aterriza en "iniciar conversación por WhatsApp".
- **Demo en vivo más difícil de mostrar al jurado.** Un chat en WhatsApp en pantalla compartida es menos espectacular que una UI rica. Mitigación: combinar pitch con la web tipo dashboard mostrando lo que el agente está haciendo "por debajo".
- **Multi-agente añade complejidad operacional.** Más prompts, más tools, más superficie de error. Mitigación: empezar con UN solo agente operativo (`acompanante-informal`) en Fase 0; sumar los otros en Fase 1.
- **Costo recurrente Anthropic** crece con MAU, no con conversiones. Si la base de Free explota antes que la conversión a Pro, el unit economics se compromete. Mitigación: límite suave de mensajes/mes en Free (generoso pero acotado), Haiku 4.5 para clasificación, batch para tareas no críticas.

### Neutras / a observar

- **Vendor lock-in con Anthropic** (Agent SDK + caching). Aceptado conscientemente por el lab. Reevaluar si el producto crece a producción: la abstracción del orquestador permite swap a otro proveedor con esfuerzo M.
- **Twilio vs. Meta Cloud API directa** para WhatsApp queda diferido a un ADR técnico siguiente. Decisión MVP: **Twilio** por velocidad de integración; migración a Cloud API directa cuando el costo lo justifique.
- **Web framework concreto** (Astro vs. Next.js) sigue abierto desde ADR 0003. Para esta decisión no es bloqueante.

## Alternativas consideradas

### Opción A — Web mobile-first como canal principal (ADR 0003 aplicado tal cual)

- **Pros:** Coherencia con decisión previa; SEO + AI-citability como motor de adquisición; demo más vistosa; sin dependencia de terceros para el canal.
- **Contras:** El segmento informal **no busca activamente** "asesoría tributaria" en Google — está en WhatsApp respondiendo encargos. Forzar a abrir un navegador y entrar a un sitio rompe el patrón de uso natural. Las cohortes objetivo además tienen baja confianza en sitios web nuevos (aprendieron a desconfiar por estafas).
- **Razón de descarte:** prioriza el canal cómodo *para nosotros* sobre el canal cómodo *para el usuario*. La cobertura efectiva sería mucho menor que la teórica.

### Opción B — Híbrido sin priorización (paridad WhatsApp + Web)

- **Pros:** No deja a nadie afuera.
- **Contras:** Doblar superficie de UX duplica costo de construcción y testing; en 7 días de lab, no llegamos a hacer ninguna de las dos bien.
- **Razón de descarte:** "ambos al mismo tiempo" en lab corto = nada terminado. Priorizar WhatsApp y dejar la web como amplificación es la única vía realista.

### Opción C — Solo web (sin WhatsApp)

- **Pros:** Stack único, menos dependencias.
- **Contras:** Pierde el canal donde el segmento ya vive; obliga a flujos de notificación push web que no son confiables en navegadores móviles chilenos.
- **Razón de descarte:** sacrifica precisamente la cualidad que distingue a Tu Plata Mipyme del resto de productos de educación financiera ya existentes.

### Opción D — Modelo de negocio: gratuito total con financiamiento estatal/donaciones

- **Pros:** Cero fricción de cobro, alineamiento total con misión social.
- **Contras:** Dependencia política y de ciclos de financiamiento; sin margen para reinvertir en mejorar el producto; no escalable.
- **Razón de descarte:** el freemium con triggers contextuales captura el "willingness to pay" real que existe en los puntos de inflexión (formalización, subsidio), sin excluir al segmento base.

### Opción E — Modelo de negocio: pago obligatorio con prueba gratuita

- **Pros:** Mejor unit economics teórico.
- **Contras:** Excluye al segmento que más lo necesita; reproduce la barrera económica que es la causa raíz del problema.
- **Razón de descarte:** incompatible con la tesis de impacto del producto.

### Opción F — Inteligencia: un único agente con system prompt grande

- **Pros:** Más simple de implementar y desplegar; menos llamadas entre componentes.
- **Contras:** System prompts > 8k tokens degradan calidad medida en evals internos; sin foco por etapa, el agente confunde a un soñador con una PYME formalizada; caching menos efectivo (un solo prefix grande vs. varios prefixes especializados).
- **Razón de descarte:** sacrifica el diferenciador "agentic thinking" que el lab valora explícitamente, y pierde calidad en el segmento real.

## Referencias

- [Plan de implementación Tu Plata Mipyme](../tu-plata-mipyme-plan.md) — arquitectura, fases, KPIs y roadmap completo.
- [Definición canónica del producto](../../definiciones/tu-plata-mipyme.md).
- [Ficha de idea original](../../ideas/tu-plata-mipyme.md).
- [Comportamiento digital en Chile (DataReportal 2026)](../../research/usuarios/comportamiento-digital-chile-2026.md) — datos macro de penetración WhatsApp y uso de internet móvil.
- [Línea temática Inclusión Financiera](../../lineas-tematicas/inclusion-financiera.md).

## Relacionados

- **Supersede parcialmente:** [ADR 0003 — Plataforma web mobile-first](0003-plataforma-web-mobile-first.md), específicamente en lo relativo al canal principal del producto Tu Plata Mipyme. ADR 0003 sigue vigente para la wiki y para productos de consulta puntual.
- **Relacionado con:** [ADR 0002 — Línea temática (Inclusión Financiera)](0002-linea-tematica-inclusion-financiera.md).
- **ADRs futuros pendientes:**
    - ADR 0005 (tentativo) — gateway WhatsApp: Twilio vs. Meta Cloud API directa.
    - ADR 0006 (tentativo) — framework web (Astro vs. Next.js) para landing y tablero.

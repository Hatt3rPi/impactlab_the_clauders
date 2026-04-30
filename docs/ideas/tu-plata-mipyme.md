---
title: "Idea: Tu Plata Mipyme — co-piloto freemium para microemprendedores"
description: "Plataforma WhatsApp + Web con multi-agente IA que acompaña al microemprendedor por 4 etapas: del sueño a PYME. Freemium."
autor: "Estrategia Literacy Regulatoria"
fecha: 2026-04-29
actualizado: 2026-04-30
linea: inclusion-financiera
estado: activa
prioridad: alta
tags:
  - idea
  - inclusion-financiera
  - pyme
  - sii
  - corfo
  - freemium
  - multi-agente
  - whatsapp
---

# Idea: Tu Plata Mipyme — co-piloto freemium para microemprendedores

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Idea evolucionada el 2026-04-30 — pasa de "asistente regulatorio one-shot" a **plataforma freemium con journey por etapas y multi-agente**. Ver [plan de implementación](../especificaciones/tu-plata-mipyme-plan.md) y [definición canónica](../definiciones/tu-plata-mipyme.md). Origen: [PDF de estrategia](../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf) + [Deep Research de Calibria](../assets/research/2026-04-29-deep-research-calibria.html).

> *Para el microemprendedor informal que sueña con crecer, Tu Plata Mipyme es un **co-piloto en WhatsApp + Web** con agentes IA especializados que lo acompañan etapa por etapa — gratis hasta que vale la pena pagar.*

> :material-rocket-launch: **"Claude co-work para el teléfono"** — democratizar la asesoría de gestión a lo largo de todo el país, eliminando la dependencia de contador, OTEC o sucursal SERCOTEC.

## Problema

- **1,08 millones de microemprendedores informales** (54 % del universo de 2 M; INE EME8).
- Foco en **mujeres (59 % informales)** y regiones del sur (Araucanía 38 % informalidad).
- **No formalizan** porque desconocen Pro-Pyme Transparente, Boleta Electrónica, FOGAPE, FSGarantía, productos CORFO/SERCOTEC.
- Solo **12,2 % accede a financiamiento formal**.

## Hipótesis

Si una microemprendedora puede **describir su negocio en español natural** ("vendo empanadas en feria de Quilicura, gano como 600 lucas al mes"), entonces obtiene un plan personalizado con ruta de formalización + productos CORFO/SERCOTEC para los que califica + simulación de utilidad.

## Propuesta

### Modelo: freemium con journey por etapas

**4 etapas, 4 agentes IA especializados** que se pasan contexto entre sí:

| Etapa | Quién | Tier | Agente |
|---|---|---|---|
| 1 — **Sueño** | Tiene una idea, no ha vendido | Free | `mentor-inicio` |
| 2 — **Informal activo** | Vende sin formalizar (1,08 M en Chile) | Free | `acompanante-informal` |
| 3 — **En formalización** | Decidió formalizar, está en trámite SII | Pro (~$5.000/mes) | `gestor-formalizacion` |
| 4 — **PYME en crecimiento** | Formalizada, postula a subsidios | Plus (pago por evento) | `estratega-crecimiento` |

> El detalle completo del journey, agentes, tools y handoffs está en el [plan de implementación](../especificaciones/tu-plata-mipyme-plan.md).

### Qué hace (visión consolidada)

- **WhatsApp como canal principal**, web como amplificador visual (formularios, links, descargas).
- **Captura conversacional** del estado del negocio: ventas, gastos, ubicación, rubro.
- **Recordatorios personalizados** que empujan hacia formalización sin presionar.
- **Simulación Pro-Pyme** vs régimen general con cifras reales del usuario.
- **Matcher de fondos CORFO/SERCOTEC/FOGAPE** con cálculo de probabilidad.
- **Carta de presentación al banco** generada como PDF.
- **Marketplace de asesores humanos** certificados, por región (post-MVP).
- **Repositorio contable** versionado, propiedad del emprendedor (post-MVP).
- **Telemetría agregada anónima** para reportes a SERCOTEC / Subsecretaría de Economía.

### Qué NO hace

- No tramita formalización por el usuario (lo guía).
- No recomienda banco específico.
- No otorga crédito ni firma declaraciones tributarias.
- No sustituye a SERCOTEC ni a CORFO — los **complementa**.

### Principios de diseño (no negociables)

- **WhatsApp-first** (96 % penetración smartphone, >90 % WhatsApp).
- **Lenguaje 6° básico** (PIAAC nacional bajo nivel 3).
- **1 decisión por pantalla**, mensajes ≤ 160 caracteres.
- **Funciona en 3G**, audio entrante/saliente como primera clase.
- **Cita la fuente normativa siempre**.

## Stack y datos

- **Modelos Claude:** Sonnet 4.6 (agentes principales) + Haiku 4.5 (clasificación e intención). Opus solo en revisión legal crítica.
- **Patrones agénticos:** Agent SDK con un supervisor + 4 subagents especializados, prompt caching del corpus regulatorio (>80 % hit), memory tool sobre Postgres.
- **Tools clave:** validar RUT en SII, simulador Pro-Pyme, matcher CORFO/SERCOTEC, generador de PDF.
- **Canal:** WhatsApp Business API (Twilio en MVP) + Next.js para la web.
- **Datasets:** circulares SII, bases CORFO/SERCOTEC/FOSIS abiertas, ENIF 2025, EME8 INE.

## Demo imaginada (Fase 0 — pitch del lab)

1. **Mensaje 1 (usuario, WhatsApp):** *"vendo empanadas en feria de Quilicura, gano como 600 lucas al mes, tengo 35"*.
2. **Respuesta inmediata (agente `acompanante-informal`):** saluda en chileno cercano, captura 2 datos más en mensajes cortos.
3. **Output visual (web):** simulación Pro-Pyme — *"si formalizas, pagas $X y te quedan $Y netos"*. Botón: *"¿Te ayudo a dar el paso?"*
4. **Handoff a `gestor-formalizacion` (paid):** muestra checklist SII en 3 pasos + genera PDF de carta al banco.
5. **Cierre:** recordatorio agendado a 7 días — *"¿Cómo vas con el Inicio de Actividades?"*

## Scoring (criterios oficiales)

| Criterio | Peso | Score (0-1) | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,85 | 21,25 |
| Uso responsable de datos | 20 | 0,80 | 16,00 |
| Claude & Agentic Thinking | 25 | 0,90 | 22,50 |
| Funcionalidad | 15 | 0,75 | 11,25 |
| Calidad del pitch | 15 | 0,80 | 12,00 |
| **Total** | **100** | | **83,00** |
| Bonus agentic (+5) | 5 | 0,80 | +4,00 |

## Viabilidad en 48 h

- **Esfuerzo:** M.
- **Riesgos:**
    - **Alcance** — acotar a 2 productos top en la demo.
    - **Actualización de bases** CORFO/SERCOTEC — usar RAG con caching.
- **Datos disponibles ya:** sí (todo público).
- **Demo end-to-end factible:** sí.

## Por qué gana

- Cruza **inclusión financiera con formalización** (preocupación SII).
- Tiene a **SERCOTEC y SII como mentores potenciales**.
- Mueve un **dial macroeconómico real** (informalidad → formalización → tributación).

## Próximos pasos para validar

- [ ] Hablar con **3-5 microemprendedoras reales** (perfil mujer 30-50, dolor de formalización).
- [ ] Pedir contactos a SERCOTEC / Hogar de Cristo / Fondo Esperanza.
- [ ] Spike: validar RUT en SII con tool use.
- [ ] Cerrar **decisiones abiertas** del [plan de implementación §10](../especificaciones/tu-plata-mipyme-plan.md#10-decisiones-que-faltan-antes-de-cerrar-fase-0): cuenta WhatsApp Business para demo, presupuesto Anthropic, equipo y roles.

## Solapamiento

- **No solapa** con Defensor / Letra Chica.
- Posible **canal post-lab** distinto: CORFO / SERCOTEC / cooperativas / Fondo Esperanza.

## Documentos relacionados

- [Plan de implementación completo](../especificaciones/tu-plata-mipyme-plan.md) — arquitectura, agentes, fases, KPIs.
- [Definición canónica del producto](../definiciones/tu-plata-mipyme.md) — qué es, qué no es, segmentos.
- [Glosario de términos nuevos](../definiciones/glosario.md#tu-plata-mipyme) — Pro-Pyme, FOGAPE, freemium, multi-agente.

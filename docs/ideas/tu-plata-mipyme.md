---
title: "Idea: Tu Plata Mipyme — asistente regulatorio para microemprendedores"
description: "Asistente que guía formalización SII + productos CORFO + simulación Pro-Pyme."
autor: "Estrategia Literacy Regulatoria"
fecha: 2026-04-29
linea: inclusion-financiera
estado: activa
prioridad: alta
tags:
  - idea
  - inclusion-financiera
  - pyme
  - sii
  - corfo
---

# Idea: Tu Plata Mipyme — asistente regulatorio para microemprendedores informales

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [PDF de estrategia](../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf) y/o el [Deep Research de Calibria](../assets/research/2026-04-29-deep-research-calibria.html). **Aún no validada por el equipo.**

> *Para una microemprendedora de feria que vende empanadas y no sabe si formalizar, Tu Plata Mipyme genera ruta paso-a-paso, identifica productos CORFO/FOGAPE para los que califica, simula utilidad bajo Pro-Pyme Transparente y le redacta una carta de presentación al banco.*

> :material-flag: **Plan C según la estrategia** ([PDF p. 7](../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf)) — *si el equipo tiene contacto con microemprendedores reales para entrevistar*.

## Problema

- **1,08 millones de microemprendedores informales** (54 % del universo de 2 M; INE EME8).
- Foco en **mujeres (59 % informales)** y regiones del sur (Araucanía 38 % informalidad).
- **No formalizan** porque desconocen Pro-Pyme Transparente, Boleta Electrónica, FOGAPE, FSGarantía, productos CORFO/SERCOTEC.
- Solo **12,2 % accede a financiamiento formal**.

## Hipótesis

Si una microemprendedora puede **describir su negocio en español natural** ("vendo empanadas en feria de Quilicura, gano como 600 lucas al mes"), entonces obtiene un plan personalizado con ruta de formalización + productos CORFO/SERCOTEC para los que califica + simulación de utilidad.

## Propuesta

### Qué hace

- **Recibe** descripción del negocio en español natural por WhatsApp o web.
- Devuelve:
    1. **Ruta de formalización** paso a paso (SII, Boleta Electrónica, régimen tributario).
    2. **Productos CORFO/SERCOTEC/FOGAPE** para los que califica con cálculo de probabilidad.
    3. **Simulación de utilidad** bajo Pro-Pyme Transparente (cuánto se queda vs régimen general).
    4. **Carta de presentación a banco** generada como PDF.

### Qué NO hace

- No tramita la formalización por el usuario.
- No recomienda banco específico.

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 con prompt caching del corpus regulatorio.
- **Patrones agénticos:** contexto largo carga toda la Circular SII + reglamento CORFO + bases SERCOTEC, **Tool use** al SII para validar RUT y régimen actual, **Memory tool** para acompañar el proceso semanas después.
- **Datasets:** circulares SII, bases CORFO/SERCOTEC/FOSIS abiertas, ENIF 2025.

## Demo imaginada

1. **Inicio:** mensaje WhatsApp: "vendo empanadas en feria, gano $600.000/mes, tengo 35 años, soy mujer".
2. **Magia:** Tu Plata Mipyme responde con plan en 5 pasos + lista de 3 productos CORFO con probabilidad de aprobación + simulación: "si formalizas en Pro-Pyme Transparente, pagas $XX y te quedan $YY netos".
3. **Cierre:** se muestra el PDF de carta al banco.

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

- [ ] Hablar con **3-5 microemprendedores reales** (tener perfil de mujer 30-50 con dolor de formalización).
- [ ] Pedir contactos a SERCOTEC / Hogar de Cristo / Fondo Esperanza.
- [ ] Spike: validar RUT en SII con tool use.

## Solapamiento

- **No solapa** con Defensor / Letra Chica.
- Posible **canal post-lab** distinto: CORFO / SERCOTEC / cooperativas.

---
title: "Idea: Voz Financiera / InclusiBot — accesibilidad financiera para discapacidad visual"
description: "Vision sobre PDF de contrato + síntesis vocal con énfasis emocional en advertencias para >1M personas con discapacidad visual."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: en-refinamiento
prioridad: media
tags:
  - idea
  - inclusion-financiera
  - accesibilidad
  - discapacidad-visual
  - voice
---

# Idea: Voz Financiera / InclusiBot — el destructor de letra chica

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *Más de 1 millón de chilenos viven con algún grado de discapacidad visual. Para ellos, leer un contrato bancario con su "letra chica" es literalmente imposible. Voz Financiera convierte el PDF a voz con síntesis emocional que enfatiza las cláusulas peligrosas.*

## Problema

- **>1 millón de personas con discapacidad visual** en Chile.
- Los **contratos crediticios son cognitivamente impenetrables e inaccesibles visualmente**, vulnerando la Ley del Consumidor.
- **Sub-segmento:** personas ciegas o con baja visión enfrentándose a contratos de crédito de consumo o automotriz.
- Las iniciativas de "inclusión bancaria" suelen limitarse a **rampas en sucursales**, ignorando que el contrato en sí es la barrera.

## Hipótesis

OCR + síntesis vocal con énfasis emocional sobre las cláusulas peligrosas convierte el contrato en accionable.

## Propuesta

### Qué hace

- Recibe PDF escaneado del contrato.
- **Vision** + OCR extrae la "Hoja Resumen".
- Sintetiza con voz: "Hola Juan. Este crédito es de **dos millones**. Tasa: X%. **Cuidado**: te incluyen seguro de desgravamen no obligatorio por CLP 15.000/mes. Puedes pedir que lo quiten."
- Énfasis prosódico en advertencias.

### Qué NO hace

- No firma por el usuario.
- No reemplaza al abogado del consumidor.

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 (Vision + Citations).
- **Patrones agénticos:** Document parsing de PDFs densos + integración con TTS con síntesis emocional (ElevenLabs o similar).
- **Datasets:** Reglamentos de Sernac Financiero (Sello SERNAC), Ley del Consumidor.

## Demo imaginada

1. "Juan, 65 años, ciego, le ofrecen un crédito de consumo."
2. Recibe PDF por email, lo reenvía al bot.
3. La IA sintetiza con voz: el monto, la tasa, las cláusulas, **con tono de alerta** sobre seguros forzosos.

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,85 | 21,25 |
| Datos | 20 | 0,75 | 15,00 |
| Claude/Agentic | 25 | 0,85 | 21,25 |
| Funcionalidad | 15 | 0,70 | 10,50 |
| Pitch | 15 | 0,80 | 12,00 |
| **Total** | | | **80,00** |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M.
- **Riesgo:** OCR alucinado sobre fotocopias de baja resolución.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| OCR alucinado | Alta | Alto | Verificación cruzada + lectura de "Hoja Resumen" oficial |
| Síntesis vocal genérica sin emoción | Media | Medio | TTS con marcadores de énfasis (SSML) |

## Por qué considerar

- **Caso análogo:** [Be My Eyes](https://www.bemyeyes.com) (integración multimodal con LLMs), aplicado a literacy contractual.
- **Diseño universal genuino** — accesibilidad pura, no solo simplificación lingüística.

## Próximos pasos

- [ ] Probar TTS con SSML para énfasis prosódico.
- [ ] Validar con persona ciega real.

## Notas y referencias

- **Caso análogo:** [Be My Eyes](https://www.bemyeyes.com).
- Catálogo completo: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

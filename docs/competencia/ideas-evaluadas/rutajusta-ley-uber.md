---
title: "Idea: RutaJusta — auditor IA de la Ley Uber chilena"
description: "Vision sobre screenshots de Uber/Rappi/PedidosYa para detectar si el algoritmo viola la Ley 21.431 (1,2× IMM, 12 h desconexión)."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: activa
prioridad: alta
tags:
  - idea
  - inclusion-financiera
  - ley-21431
  - plataformas
  - vision
---

# Idea: RutaJusta / Algoritmo Transparente — auditor IA de la Ley Uber

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *El conductor sube screenshots de su semana en Uber/Rappi. La IA extrae horas y pagos, calcula si la app respetó el piso del 1,2× IMM por hora y las 12 h continuas de desconexión que exige la Ley 21.431. Si detecta infracción, genera el reporte para Dirección del Trabajo.*

## Problema

- La **Ley 21.431** (2022) regula trabajadores de plataformas digitales: piso de **1,2× IMM** por hora, **12 h continuas de desconexión** mínimas.
- **El conductor opera en una caja negra:** no sabe si la tarifa dinámica viola el piso legal.
- El Estado **no tiene capacidad de auditar algoritmos** en tiempo real; depende de denuncias.
- **Sub-segmento:** trabajadores independientes de reparto y transporte (Uber, Rappi, PedidosYa, Cornershop).

## Hipótesis

Si el conductor puede subir screenshots de su historial semanal, la IA puede auditar el cumplimiento legal con precisión y darle herramientas para reclamar.

## Propuesta

### Qué hace

- Recibe screenshots del historial de viajes (tiempos de conexión + ganancias).
- **Vision** extrae horas logueadas y pagos.
- Calcula si se cumplió el umbral 1,2× IMM (~CLP 624.000/mes equivalente).
- Verifica si hubo 12 h continuas de desconexión.
- Si detecta infracción: genera reporte estructurado para presentar ante DT.

### Qué NO hace

- No demanda en nombre del trabajador.
- No automatiza la presentación a DT (el trabajador la presenta).

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 (Vision multimodal robusto).
- **Patrones agénticos:** Vision (procesar UI compleja de apps), Tool use (calculadora vs IMM dinámico), Prompt caching (jurisprudencia DT extensa).
- **Datasets:** [Ley 21.431 BCN](https://www.bcn.cl/leychile/navegar?idNorma=1173502), dictámenes [Dirección del Trabajo](https://www.dt.gob.cl/), circulares SUSESO.

## Demo imaginada (60 s)

1. "**Pedro** trabaja en Rappi. Quiere saber si le están pagando bien."
2. Sube 5 screenshots de su semana.
3. IA: "Trabajaste 47 horas. Te pagaron CLP 285.000 = **CLP 6.063/hora**. El piso legal es **CLP 7.350/hora** (1,2× IMM). **Te deben CLP 60.486 retroactivos.**"
4. "Además, tuviste solo 8 h continuas de desconexión el martes. La Ley 21.431 exige 12. Aquí tu reporte para DT."

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,85 | 21,25 |
| Datos | 20 | 0,80 | 16,00 |
| Claude/Agentic | 25 | 0,95 | 23,75 |
| Funcionalidad | 15 | 0,75 | 11,25 |
| Pitch | 15 | 0,90 | 13,50 |
| **Total** | | | **85,75** |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M-A (alta variabilidad UI de apps).
- **Riesgos:** OCR inconsistente sobre screenshots de distintas apps; jurisprudencia DT compleja.
- **Datos disponibles:** sí (ley pública).
- **Demo end-to-end:** sí, con screenshots reales de un voluntario.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Variabilidad de UI Uber/Rappi/PedidosYa | Alta | Medio | Acotar a 1-2 apps en demo |
| Cálculo erróneo de IMM | Media | Alto | Tool use con calculadora certificada |
| Represalias de la app contra el trabajador | Media | Alto | Reporte anónimo a DT, no exponer al trabajador |

## Por qué gana

- **Narrativa fascinante:** "IA del trabajador audita IA del empleador".
- **Caso análogo verificable:** [Worker Info Exchange (UK)](https://www.workerinfoexchange.org).
- **Diferenciador único** — ningún equipo del lab tocará este vector.

## Próximos pasos

- [ ] Conseguir screenshots reales de Uber/Rappi (5 muestras).
- [ ] Spike Vision sobre 1 app específica.
- [ ] Validar interpretación legal con un abogado laboralista.

## Notas y referencias

- **Caso análogo:** [Worker Info Exchange (UK)](https://www.workerinfoexchange.org).
- Catálogo completo: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

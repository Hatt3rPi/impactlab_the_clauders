---
title: "Idea: Talento Tributa — gerente de bolsillo para deportistas, e-sports y creadores"
description: "Atletas amateur, músicos, jugadores de e-sports y creadores de contenido: la IA traduce ingresos irregulares al lenguaje del SII."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: en-refinamiento
prioridad: baja
tags:
  - idea
  - inclusion-financiera
  - creadores
  - e-sports
  - sii
---

# Idea: Talento Tributa — gerente de negocios de bolsillo

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *Deportistas amateur, músicos emergentes y jugadores de e-sports generan ingresos esporádicos pero quedan excluidos del sistema bancario. Talento Tributa actúa como un gerente de negocios de bolsillo que traduce premios y patrocinios al lenguaje del SII.*

## Problema

- Talento chileno con **ingresos irregulares** (deporte amateur, música emergente, e-sports, creadores de contenido).
- El sistema **bancario los rechaza** por falta de historial formal.
- **Sub-segmento:** atletas alto rendimiento sin contrato laboral, creadores de contenido emergentes, artistas esporádicos.
- Fricción: contadores tradicionales desestiman el nicho por bajo volumen; SII tiene la información pero su lenguaje es inescrutable.

## Hipótesis

IA que traduzca ingresos esporádicos a régimen tributario óptimo + emisión correcta de boletas habilita el historial bancario.

## Propuesta

### Qué hace

- Recibe descripción de los ingresos del talento.
- Diseña hoja de ruta para **emitir boletas de prestación de servicios** por ingresos esporádicos.
- Proyecta cuánto guardar para retención anual.

### Qué NO hace

- No emite boletas por el usuario (lo hace el SII).
- Disclosure: "no soy contador".

## Stack y datos

- **Modelo Claude:** Sonnet 4.6.
- **Patrones agénticos:** Structured Outputs (dashboard financiero), Citations a circulares SII.
- **Datasets:** Regímenes simplificados [SII](https://www.sii.cl), normativas Mindeporte, exenciones Ministerio Culturas.

## Demo imaginada

1. "**Camila**, judoca amateur. Ganó CLP 1 M en torneo en Brasil + auspicio local CLP 200K."
2. IA: "Camila, emite Boleta de Honorarios. Te retienen 13 %. En Operación Renta recuperas CLP X. Te conviene comenzar a aportar voluntariamente para AFP."

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,75 | 18,75 |
| Datos | 20 | 0,70 | 14,00 |
| Claude/Agentic | 25 | 0,75 | 18,75 |
| Funcionalidad | 15 | 0,70 | 10,50 |
| Pitch | 15 | 0,75 | 11,25 |
| **Total** | | | **73,25** |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M.
- **Riesgo:** asesoría tributaria errónea legalmente vinculante.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Asesoría tributaria errónea | Alta | Alto | Disclaimer permanente; derivar al SII para casos específicos |

## Por qué considerar

- **Caso análogo:** [Catch.co (USA)](https://catch.co) — beneficios de freelancers.
- **Expande "trabajador informal"** a creator economy + e-sports.

## Notas y referencias

- **Caso análogo:** Catch.co (USA).
- Catálogo completo: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

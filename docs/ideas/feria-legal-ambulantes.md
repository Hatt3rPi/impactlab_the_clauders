---
title: "Idea: Feria Legal — regularización de comercio ambulante"
description: "Voice-first WhatsApp para vendedores ambulantes: ruta de Microempresa Familiar + ordenanzas municipales + permiso de patente."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: en-refinamiento
prioridad: baja
tags:
  - idea
  - inclusion-financiera
  - ambulantes
  - mef
  - municipalidades
---

# Idea: Feria Legal — regularización en la vía pública

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *El vendedor ambulante interactúa por audio en WhatsApp. La IA explica el régimen de Microempresa Familiar (MEF), genera la lista de requisitos y ubica la oficina de patentes de su municipalidad.*

## Problema

- El **comercio ambulante** es una crisis nacional: muchos vendedores quieren formalizarse para evitar decomisos pero el proceso cruza permisos municipales, sanitarios y tributarios.
- **Sub-segmento:** vendedores ambulantes ("toldos azules") y feriantes no regularizados.
- Fricción: el Estado ataca con policías, no con inclusión proactiva en el lenguaje de la calle.

## Hipótesis

Voice-first + información hiperlocal por comuna + lenguaje accesible desbloquea el primer paso de la formalización.

## Propuesta

### Qué hace

- Recibe audio del usuario.
- Explica **Microempresa Familiar (MEF)**.
- Genera lista de requisitos.
- Ubica oficina de patentes de la municipalidad correspondiente.

### Qué NO hace

- No tramita la patente.

## Stack y datos

- **Modelo Claude:** Haiku 4.5 (latencia + costo) + Sonnet 4.6 si profundiza.
- **Patrones agénticos:** Voice-first, MCP a bases municipales (cuando existan).
- **Datasets:** Ordenanzas municipales modelo (ACHM), guías [SERCOTEC](https://www.sercotec.cl), Ley de Rentas Municipales.
- **Limitación:** datos municipales fragmentados → piloto inicial 2-3 comunas grandes.

## Demo imaginada

1. Audio: "Quiero sacar el permiso pero me piden iniciación de actividades y no sé qué es."
2. IA responde por audio: "Te explico el régimen de **Microempresa Familiar**. Para ti, en la Municipalidad de Maipú, los pasos son: 1)..., 2)..., 3)..."

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,80 | 20,00 |
| Datos | 20 | 0,70 | 14,00 |
| Claude/Agentic | 25 | 0,75 | 18,75 |
| Funcionalidad | 15 | 0,65 | 9,75 |
| Pitch | 15 | 0,75 | 11,25 |
| **Total** | | | **73,75** |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M.
- **Riesgo:** alta fragmentación municipal.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Información desactualizada por comuna | Alta | Medio | Acotar a 2-3 comunas piloto en demo |

## Por qué considerar

- **Caso análogo:** [mygov.in (India)](https://www.mygov.in), módulos de formalización.
- **Sale de la burbuja "Sanhattan"** — aborda problema sociopolítico visible en cada esquina.

## Notas y referencias

- **Caso análogo:** mygov.in (India).
- Catálogo completo: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

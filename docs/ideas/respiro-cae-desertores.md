---
title: "Idea: Respiro CAE — línea de tiempo para desertores universitarios"
description: "Para egresados sin título con CAE en mora: la IA mapea plazos de reprogramación al 10% de renta y evita el shock anual con TGR."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: en-refinamiento
prioridad: baja
tags:
  - idea
  - inclusion-financiera
  - cae
  - desertores
  - tgr
---

# Idea: Respiro CAE — desertores universitarios con deuda CAE

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *Los desertores universitarios con CAE en mora enfrentan el peor escenario: deuda completa acelerada, sin título para generar ingresos, y el Estado retiene su devolución de impuestos cada año. Respiro CAE mapea un timeline exacto de los plazos de reprogramación al 10% de renta antes de Dicom.*

## Problema

- Los **desertores con CAE** (estudiantes que abandonaron sin título) enfrentan deuda acelerada.
- La **Tesorería General de la República (TGR)** retiene su devolución de impuestos anualmente como garantía estatal.
- **Sub-segmento:** estudiantes desertores con CAE en mora.
- Fricción: la literatura bancaria asume titulación, ignorando el infierno de la deserción académica.

## Hipótesis

Mapear los plazos exactos de reprogramación que abre Comisión Ingresa una vez al año + el riesgo de Dicom convierte el desorden en plan accionable.

## Propuesta

### Qué hace

- Recibe situación del usuario.
- Cruza fechas de deserción + plazos legales de ejecución del aval bancario.
- Muestra **timeline visual exacto** de plazos de reprogramación.
- Calcula la cuota al **10 % de la renta** según última info Comisión Ingresa.

### Qué NO hace

- No tramita la reprogramación (el usuario debe ir a Ingresa).

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 (razonamiento temporal complejo / prompt chaining).
- **Patrones agénticos:** Tree-of-thoughts (deducir fechas y plazos), Citations.
- **Datasets:** Manuales de [Comisión Ingresa](https://portal.ingresa.cl), normativas TGR.

## Demo imaginada

1. "**Felipe**, 28. Desertó el 2019 con CAE de CLP 8 M. La TGR le retuvo CLP 250.000 este año en la Operación Renta."
2. IA: "Felipe, **puedes reprogramar al 10 % de tu renta** vía Ingresa antes del 30-jun-2026. Cuota mensual: CLP 41.000 (en lugar de CLP 110.000 actual). Aquí los pasos."

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,80 | 20,00 |
| Datos | 20 | 0,70 | 14,00 |
| Claude/Agentic | 25 | 0,75 | 18,75 |
| Funcionalidad | 15 | 0,70 | 10,50 |
| Pitch | 15 | 0,80 | 12,00 |
| **Total** | | | **75,25** |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M.
- **Riesgo:** políticas CAE son altamente dinámicas (proyecto FES en curso).

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Cambio normativo (FES) | Alta | Alto | Disclaimer "info al [fecha]" |
| Cálculo de reprogramación erróneo | Media | Alto | Tool use + validación Ingresa |

## Por qué considerar

- **Caso análogo:** [StudentAid.gov (USA)](https://studentaid.gov) — orientación sobre planes IDR (Income-Driven Repayment).

## Próximos pasos

- [ ] Validar fechas vigentes de reprogramación con Comisión Ingresa.

## Notas y referencias

- **Caso análogo:** StudentAid.gov (USA).
- Catálogo completo: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

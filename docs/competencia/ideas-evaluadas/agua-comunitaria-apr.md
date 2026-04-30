---
title: "Idea: Agua Comunitaria / APR-Bot — copiloto tarifario para comités rurales"
description: "Foto de boletas → la IA calcula la tarifa óptima del Servicio Sanitario Rural según Ley 20.998 y genera el informe contable trimestral."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: activa
prioridad: alta
tags:
  - idea
  - inclusion-financiera
  - apr
  - ruralidad
  - ley-20998
---

# Idea: Agua Comunitaria / APR-Bot — copiloto tarifario para comités rurales

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *El tesorero de un Comité APR sube fotos de los gastos mensuales (cloro, electricidad). La IA aplica la Ley 20.998 y genera el borrador del informe contable trimestral exigido por la Superintendencia de Servicios Sanitarios. Sin esto, el directorio enfrenta multas o censura.*

## Problema

- **Más de 2 millones de chilenos** se abastecen mediante Servicios Sanitarios Rurales (APR).
- La **Ley 20.998** profesionalizó el sector: obliga a comités comunitarios a calcular tarifas complejas, aprobar con SISS y aplicar leyes recientes de subsidios eléctricos.
- **Dirigentes rurales carecen de conocimiento de ingeniería tarifaria** — son víctimas de multas y censura.
- **Sub-segmento:** dirigentes y tesoreros de Comités y Cooperativas APR.

## Hipótesis

Un copiloto que automatice cálculo tarifario + informe contable trimestral evita multas y desfinanciamiento de servicios de agua comunitarios.

## Propuesta

### Qué hace

- Recibe fotos de gastos (cloro, electricidad, mantención).
- **Vision** extrae costos.
- Aplica principios de la **Ley 20.998** (corredores tarifarios + subsidios eléctricos).
- Genera **borrador del informe contable trimestral** para la SISS.
- Calcula si aplica al **descuento de tarifa eléctrica invernal Ley 21.472**.

### Qué NO hace

- No reemplaza al ingeniero sanitario certificado.
- No presenta el informe ante SISS (lo presenta el directorio).

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 (Vision + cálculo tarifario complejo).
- **Patrones agénticos:** Vision (extracción de boletas rudimentarias), Tool use (calculadora tarifaria), Citations (Ley 20.998 + circulares MOP).
- **Datasets:** [Ley 20.998 BCN](https://www.bcn.cl/leychile/navegar?idNorma=1100062), circulares tarifarias de la Subdirección de Servicios Sanitarios Rurales del MOP.

## Demo imaginada

1. "**Don Manuel** es tesorero del APR de Azapa. Tiene que entregar el informe trimestral en 5 días."
2. Sube 3 fotos de boletas (cloro, electricidad, sueldos).
3. IA: "Tu tarifa óptima es **CLP 8.450/m³**. Tu APR califica al **descuento de tarifa eléctrica invernal** (Ley 21.472, ahorras CLP 1,2 M anuales). Aquí el borrador del informe trimestral."

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,90 | 22,50 |
| Datos | 20 | 0,75 | 15,00 |
| Claude/Agentic | 25 | 0,85 | 21,25 |
| Funcionalidad | 15 | 0,75 | 11,25 |
| Pitch | 15 | 0,90 | 13,50 |
| **Total** | | | **83,50** |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M.
- **Riesgo:** un mal cálculo tarifario podría desfinanciar el APR.
- **Datos disponibles:** sí (ley pública + circulares MOP).
- **Demo end-to-end:** sí, con datos sintéticos de un APR real.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Cálculo tarifario erróneo desfinancia comunidad | Alta | Alto | Validar con ingeniero MOP + disclaimer de "borrador, requiere aprobación SISS" |
| Variabilidad de boletas rurales | Alta | Medio | Acotar a 2-3 formatos comunes (Saesa, CGE, etc.) |

## Por qué gana

- **Desmarque temático absoluto** del lab — nadie más va a hacer fintech rural.
- **Caso análogo verificable:** Gov.br módulo rural (Brasil).
- Aborda nexo vital: **finanzas comunitarias + acceso al agua**.

## Próximos pasos

- [ ] Conseguir 3 boletas de gastos de un APR real.
- [ ] Validar formato de informe trimestral con la SISS.
- [ ] Spike Vision sobre boletas eléctricas chilenas.

## Notas y referencias

- **Caso análogo:** Gov.br módulo rural (Brasil).
- Catálogo completo: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

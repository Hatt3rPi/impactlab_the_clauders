---
title: "Idea: Viuda Protegida — pensión de sobrevivencia AFP para viudas <65"
description: "Diferencia automáticamente si corresponde pensión por accidente laboral (SUSESO) o sobrevivencia AFP, y calcula porcentajes para viuda + hijos."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: en-refinamiento
prioridad: media
tags:
  - idea
  - inclusion-financiera
  - viudez
  - afp
  - pension-sobrevivencia
---

# Idea: Viuda Protegida — pensión de sobrevivencia AFP para viudas pre-65

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *Las viudas que enviudan jóvenes (antes de los 65) y no califican aún para PGU se pierden en el laberinto de la Superintendencia de Pensiones. Viuda Protegida diferencia automáticamente si corresponde pensión por ley de accidentes laborales (SUSESO) o sobrevivencia AFP, calcula los porcentajes y guía la postulación.*

## Problema

- Las **viudas <65 años** caen en un vacío entre **mutuales de accidentes laborales** y **pensión de sobrevivencia AFP**.
- **Sub-segmento:** mujeres viudas menores de 65 sin historial extenso de cotizaciones propias.
- Fricción: la AFP no persigue a la viuda para pagarle. Ella debe ir a exigirlo enfrentando burocracia.

## Hipótesis

Diferenciar automáticamente la causa del fallecimiento + calcular porcentajes + generar borrador de postulación elimina la barrera principal.

## Propuesta

### Qué hace

- Recibe relato de la viuda (texto o voz).
- Determina si la causa de muerte **califica como accidente laboral** (SUSESO) o **muerte natural** (AFP sobrevivencia).
- Calcula porcentaje del sueldo base que corresponde a la viuda y a los hijos menores.
- Genera borrador de postulación con instituciones y plazos.

### Qué NO hace

- No otorga la pensión.
- No reemplaza al asesor previsional.

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 (razonamiento complejo de reglas previsionales).
- **Patrones agénticos:** Tree-of-thoughts (árbol de decisiones legales), Citations a Compendio de Normas del Sistema de Pensiones.
- **Datasets:** Compendio Sup. Pensiones, normativa SUSESO, Ley 16.744 (accidentes laborales).

## Demo imaginada

1. "**Carmen**, 58. Su esposo Juan murió en un accidente de tránsito yendo al trabajo."
2. "Carmen, esto califica como **accidente del trayecto** (Ley 16.744). Te corresponde pensión SUSESO **del 50 % del sueldo base** (CLP X), no la AFP. Aquí los pasos."

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,90 | 22,50 |
| Datos | 20 | 0,75 | 15,00 |
| Claude/Agentic | 25 | 0,80 | 20,00 |
| Funcionalidad | 15 | 0,70 | 10,50 |
| Pitch | 15 | 0,80 | 12,00 |
| **Total** | | | **80,00** |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M.
- **Riesgo:** cálculos actuariales erróneos generan falsas expectativas.
- **Datos disponibles:** sí.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Cálculo erróneo de porcentaje | Media | Alto | Tool use con calculadora certificada Sup. Pensiones |
| Confusión accidente laboral vs común | Alta | Alto | Árbol de decisión documentado + escalamiento a AFP en casos dudosos |

## Por qué considerar

- **Caso análogo:** formularios automatizados de viudedad en Países Bajos.
- **Solapamiento parcial con [Legado Claro](legado-claro-herencias.md)** — podría integrarse como sub-módulo.

## Próximos pasos

- [ ] Validar árbol de decisión con asesor previsional independiente.
- [ ] Spike de razonamiento Claude sobre 5 casos hipotéticos.

## Notas y referencias

- **Caso análogo:** Países Bajos — Sociale Verzekeringsbank.
- **Posible integración con [Legado Claro](legado-claro-herencias.md)** como sub-módulo de "trámites post-fallecimiento".
- Catálogo completo: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

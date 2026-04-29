---
title: "Idea: Retención Alimentos — ejecutor de Ley 21.484 contra deudores"
description: "Para madres con sentencias de alimentos impagas: la IA genera el escrito de retención de fondos y guía paso a paso en Oficina Judicial Virtual."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: en-refinamiento
prioridad: media
tags:
  - idea
  - inclusion-financiera
  - alimentos
  - ley-21484
  - violencia-economica
---

# Idea: Retención Alimentos — ejecutor Ley 21.484

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *La Ley 21.484 creó el Registro Nacional de Deudores de Pensiones de Alimentos pero las madres no saben cómo ejecutar embargos a las cuentas bancarias del deudor. Retención Alimentos genera el "Escrito de solicitud de retención de fondos bancarios" y guía paso a paso por la Oficina Judicial Virtual.*

## Problema

- La **violencia económica intrafamiliar** es la pandemia invisible: madres sufren evasión sistemática de pensiones alimenticias.
- La **Ley 21.484** creó herramientas para castigar a deudores, pero **el tribunal no retiene fondos de oficio**: la víctima debe impulsar procesalmente el embargo.
- **Sub-segmento:** madres con sentencias de alimentos impagas (uno de los grupos con mayor índice de vulnerabilidad crediticia estructural en Chile).

## Hipótesis

Generar el escrito legal exacto + guía visual de la Oficina Judicial Virtual elimina la barrera procesal que impide ejecutar embargos.

## Propuesta

### Qué hace

- Recibe descripción del caso (deudor, monto, sentencia previa).
- Genera **borrador de "Escrito de solicitud de retención de fondos bancarios"** según Ley 21.484.
- Guía visual paso a paso por la **Oficina Judicial Virtual** (mock interface o extensión Chrome).
- Si se confirma violencia económica: deriva a **Corporación de Asistencia Judicial** (gratis).

### Qué NO hace

- No representa legalmente.
- No accede a la Oficina Judicial Virtual con credenciales del usuario (mock para demo).

## Stack y datos

- **Modelo Claude:** Sonnet 4.6.
- **Patrones agénticos:** Document Generation (PDF de escrito), Prompt Caching (Ley 21.484), Citations.
- **Datasets:** [Ley 21.484 BCN](https://www.bcn.cl/leychile/navegar?idNorma=1181057), procedimientos del Poder Judicial ([Oficina Judicial Virtual](https://oficinajudicialvirtual.pjud.cl)).
- **Workaround:** ClaveÚnica restringida → mock interface que guía al usuario sobre los botones exactos a presionar.

## Demo imaginada

1. "**Patricia**, 34, 2 hijos. El padre debe CLP 3 M y aparece en el Registro de Deudores."
2. La IA genera el escrito legal en 30 s + tutorial visual de los 5 pasos en la Oficina Judicial Virtual.
3. "Patricia, si quieres asesoría gratuita: aquí el contacto de la Corporación de Asistencia Judicial."

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,90 | 22,50 |
| Datos | 20 | 0,70 | 14,00 |
| Claude/Agentic | 25 | 0,80 | 20,00 |
| Funcionalidad | 15 | 0,65 | 9,75 |
| Pitch | 15 | 0,90 | 13,50 |
| **Total** | | | **79,75** |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M.
- **Riesgo:** intervención en Poder Judicial + manejo de PII de menores de edad.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| PII sensible (datos de menores) | Alta | Alto | No persistir; anonimizar logs |
| Escrito legal con error formal | Alta | Alto | Validar plantilla con abogada de familia |
| Falsa esperanza de embargo rápido | Media | Medio | Disclosure: "esto es la solicitud, el tribunal decide" |

## Por qué considerar

- **Caso análogo:** plataformas de Child Support en USA que automatizan autogestión de embargos.
- **Toca fibra del feminismo financiero** — empoderamiento legal frente a coacción económica.

## Próximos pasos

- [ ] Validar escrito con abogada de familia.
- [ ] Probar mock interface de Oficina Judicial Virtual.

## Notas y referencias

- **Caso análogo:** Child Support digital (USA).
- Catálogo completo: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

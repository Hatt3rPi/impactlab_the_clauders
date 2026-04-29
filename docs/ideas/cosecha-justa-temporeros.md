---
title: "Idea: Cosecha Justa — denuncia anónima por SMS para temporeros agrícolas"
description: "Audio WhatsApp/SMS desde el campo: la IA cruza con normativa DT y genera reclamo anónimo a Inspección del Trabajo."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: en-refinamiento
prioridad: media
tags:
  - idea
  - inclusion-financiera
  - temporeros
  - dt
  - sms-first
---

# Idea: Cosecha Justa / Sindicalismo IA

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *El temporero envía un audio desde el campo: "nos están cobrando el transporte hacia el predio". La IA cruza con normativa DT, responde que esos costos los asume el empleador, y genera SMS de reporte anónimo a Inspección del Trabajo local.*

## Problema

- El **trabajo agrícola de temporada** opera en los márgenes de la ley laboral: contratos por faena, descuentos abusivos por transporte/alimentación.
- **Sub-segmento:** trabajadores agrícolas temporeros y empacadores de fruta.
- Fricción: **escasez extrema de fiscalización presencial** del Estado en zonas rurales.

## Hipótesis

Canal SMS-first (no WhatsApp data) en zonas con poca conectividad + reporte anónimo desbloquea la denuncia que el campo no hace por miedo a represalias.

## Propuesta

### Qué hace

- Recibe audio o SMS desde el campo.
- Cruza con normativa DT y dictámenes.
- Responde si la situación es ilegal.
- Genera SMS de reporte anónimo a Inspección del Trabajo local.

### Qué NO hace

- No demanda en nombre del trabajador.
- No expone identidad (anonimato estricto).

## Stack y datos

- **Modelo Claude:** Haiku 4.5 (latencia baja, costo $1/$5 per M tokens).
- **Patrones agénticos:** Tool use (calculadora descuentos legales), Structured Outputs (formato exacto reclamo DT).
- **Datasets:** Código del Trabajo, dictámenes [Dirección del Trabajo](https://www.dt.gob.cl).

## Demo imaginada

1. SMS: "Nos están cobrando $5.000 por bus al predio. ¿Es legal?"
2. IA: "**No es legal.** Los gastos de traslado en trabajo de temporada son del empleador (Dictamen DT 4567/156, 2018). Te ayudo a denunciar anónimamente a la Inspección de Curicó. Responde SI."

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,85 | 21,25 |
| Datos | 20 | 0,65 | 13,00 |
| Claude/Agentic | 25 | 0,75 | 18,75 |
| Funcionalidad | 15 | 0,70 | 10,50 |
| Pitch | 15 | 0,80 | 12,00 |
| **Total** | | | **75,50** |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M.
- **Riesgo:** SMS gateway requiere número de Twilio + verificación corporativa.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Represalias patronales | Alta | Alto | Anonimato técnico estricto |
| SMS no llega en zonas remotas | Media | Medio | Multi-canal (WhatsApp si hay señal) |

## Por qué considerar

- **Caso análogo:** [Contratista-app (México)](https://contratista.app) — transparencia comisiones agrícolas.
- **Promueve canales de ultra-baja conectividad** (SMS/WhatsApp), alejado de "apps de Santiago".

## Próximos pasos

- [ ] Validar SMS gateway con Twilio.
- [ ] Conseguir 2-3 dictámenes DT más comunes.

## Notas y referencias

- **Caso análogo:** Contratista-app (México).
- Catálogo completo: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

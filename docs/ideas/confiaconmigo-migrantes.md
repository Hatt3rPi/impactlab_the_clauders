---
title: "Idea: ConfíaConmigo — traductor de derechos para migrantes"
description: "Bot multiidioma que guía onboarding bancario, derechos laborales y financieros para migrantes."
autor: "Estrategia Literacy Regulatoria"
fecha: 2026-04-29
linea: inclusion-financiera
estado: en-refinamiento
prioridad: media
tags:
  - idea
  - inclusion-financiera
  - migrantes
  - multiidioma
---

# Idea: ConfíaConmigo — traductor de derechos para migrantes

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [PDF de estrategia](../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf) y/o el [Deep Research de Calibria](../assets/research/2026-04-29-deep-research-calibria.html). **Aún no validada por el equipo.**

> *Bot multiidioma (español, criollo haitiano básico) que guía el onboarding bancario completo, explica derechos laborales y financieros, y responde en formato audio o texto.*

## Problema

- **1,92 M migrantes** (10 % población); **337 K irregulares**.
- Prioritarios: venezolanos (728 K), haitianos (188 K, barrera idioma), peruanos (260 K).
- **KYC con cédula extranjera**, derechos para abrir CuentaRUT, remesas, reconocimiento de estudios para empleo formal.
- Solo **33 % de migrantes** tiene instrumento financiero.

## Hipótesis

Un migrante recién llegado puede **completar onboarding bancario** y entender **sus derechos laborales y financieros** en menos de 30 minutos vía WhatsApp en su idioma.

## Propuesta

- Bot multiidioma con NLP en español + criollo haitiano básico.
- Vision para leer **permiso temporal / cédula extranjera**.
- Citations a **SJM (Servicio Jesuita Migrante)** y normativa migratoria (Ley 21.325).
- Audio/texto opcional.

## Stack

- **Claude:** Sonnet 4.6 + Vision.
- :warning: **Riesgo declarado por Anthropic:** criollo haitiano tiene **desempeño limitado en LLM**. Validar antes.

## Scoring (criterios oficiales)

| Criterio | Peso | Score (0-1) | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,85 | 21,25 |
| Uso responsable de datos | 20 | 0,75 | 15,00 |
| Claude & Agentic Thinking | 25 | 0,80 | 20,00 |
| Funcionalidad | 15 | 0,70 | 10,50 |
| Calidad del pitch | 15 | 0,80 | 12,00 |
| **Total** | **100** | | **78,75** |

## Por qué considerar

- **Gap real** (33 % bancarización vs 91 % nacional).
- Encaja con grupos prioritarios de la **ENIF 2025**.

## Por qué descartar

- **Galgo y Migrante ya cubren parte** (con licencia CMF y respaldo BID Lab).
- La organización podría verlo como **competencia con sponsor existente**.

## Estado en el equipo

> **En refinamiento.** Mantener en backlog. Ver si se puede combinar con Defensor/Tu Plata Mipyme como sub-segmento.

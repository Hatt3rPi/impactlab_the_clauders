---
title: "Idea: Mis Datos — copiloto ARCOP para ciudadanos"
description: "El usuario describe su problema, la IA identifica al responsable y redacta + trackea solicitud ARCOP."
autor: "Deep Research Calibria"
fecha: 2026-04-29
linea: proteccion-datos
estado: fuera-de-linea
prioridad: alta-en-otra-linea
tags:
  - idea
  - proteccion-datos
  - arcop
  - ley-21719
---

# Idea: Mis Datos — copiloto ARCOP

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [PDF de estrategia](../../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf) y/o el [Deep Research de Calibria](../../assets/research/2026-04-29-deep-research-calibria.html). **Aún no validada por el equipo.**

> :material-alert: **Esta idea pertenece a la línea Protección de Datos**, no a la línea elegida. Si se considera la mejor apuesta, requeriría revisar [ADR 0002](../../tu-plata-mipyme/especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md).

> *Identifica al responsable correcto, redacta la solicitud según tipo (Acceso, Rectificación, Cancelación, Portabilidad, Oposición), la envía y monitorea el plazo de 30 días.*

## Problema (cifras del deep research)

- **67 % de chilenos** no sabe cómo se usan sus datos personales.
- **48,9 %** nunca lee la política de privacidad.
- **67 %** se ha visto obligado a entregar datos contra su voluntad.
- **NO existe** asistente IA para ciudadanos que ayude con derechos ARCOP (deep research, sección 5: "el ciudadano está completamente huérfano").
- **APDP aún sin Consejo Directivo nombrado** a abril 2026.

## Hipótesis

Si el usuario puede **describir** el problema con sus datos en lenguaje natural, entonces obtiene una **carta ARCOP completa** y dirigida al responsable correcto en menos de 5 minutos.

## Propuesta

- Stack: **LLM + Email + Tracking**.
- Identificación automática del responsable (banco, retail, isapre, etc.).
- Generación de carta según tipo de derecho (ARCOP).
- Envío + monitoreo del plazo de 30 días.

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,90 | 22,50 |
| Datos | 20 | 0,95 | 19,00 |
| Claude/Agentic | 25 | 0,85 | 21,25 |
| Funcionalidad | 15 | 0,75 | 11,25 |
| Pitch | 15 | 0,80 | 12,00 |
| **Total** | | | **86,00** |

## Por qué gana (en su línea)

- **Timing perfecto**: 5 meses antes de vigencia plena de **Ley 21.719** (1-dic-2026).
- **Gap CRÍTICO documentado**: no existe nada similar en Chile.
- **Demanda potencial masiva**.
- **Pivot natural a B2B2C** ofreciendo el rail a empresas que necesiten responder DSAR.

## Por qué (de momento) está fuera

- El equipo eligió **Inclusión Financiera**.
- En la reunión kickoff, Felipe mencionó que está vendiendo implementación de Ley de Protección de Datos como freelance pero "no se siente súper cómodo en eso".

## Si pivoteamos a esta idea, qué cambia

- Nuevo ADR superseding 0002.
- Re-foco en **Ley 21.719** y derechos ARCOP.
- Mentor objetivo: **APDP / Derechos Digitales / Datos Protegidos**.
- Posible cliente B2B post-lab: cualquier empresa que necesite responder DSAR a escala.

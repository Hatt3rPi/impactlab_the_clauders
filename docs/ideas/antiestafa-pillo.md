---
title: "Idea: Antiestafa / Pillo — verificador antiphishing para adultos mayores"
description: "Bot WhatsApp que recibe SMS/correo/llamada-transcrita y emite veredicto + protocolo de acción en menos de 10 segundos."
autor: "Estrategia Literacy Regulatoria + Deep Research Calibria"
fecha: 2026-04-29
linea: ciberseguridad
estado: fuera-de-linea
prioridad: alta-en-otra-linea
tags:
  - idea
  - ciberseguridad
  - phishing
  - adultos-mayores
---

# Idea: Antiestafa / Pillo — verificador antiphishing conversacional

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [PDF de estrategia](../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf) y/o el [Deep Research de Calibria](../assets/research/2026-04-29-deep-research-calibria.html). **Aún no validada por el equipo.**

> :material-alert: **Esta idea pertenece a la línea Ciberseguridad Ciudadana**, no a la línea elegida (Inclusión Financiera). Si el equipo la considera la mejor apuesta, requeriría revisar [ADR 0002](../especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md) y cambiar de línea temática.

> *Bot WhatsApp + voz donde el adulto mayor (o un familiar) reenvía un SMS, correo o llamada-transcrita y recibe diagnóstico instantáneo + protocolo de acción + reporte a CSIRT/CMF.*

> Esta ficha **consolida** dos descripciones equivalentes:
>
> - "Antiestafa" del PDF (Idea 6).
> - "Pillo · Verificador antiphishing" del deep research (Quick Win 1, **Impacto 10 / Complejidad 4**).

## Problema (cifras del deep research)

- **94,3 %** de los chilenos ha recibido phishing al menos una vez (USS 2024).
- **27,6 B** intentos de ciberataques en Chile en 2024 (4,6× más que 2023).
- **+125 %** phishing en 2024 (Kaspersky).
- **+213 %** ataques móviles en Chile.
- **29 % de adultos mayores** víctimas.
- **266 K usuarios** afectados por fraude bancario en 2023 (+113 %); BancoEstado concentra 66 %.
- **53 % no sabe usar 2FA**.

## Hipótesis

Un adulto mayor puede **reenviar un SMS o correo sospechoso** por WhatsApp y obtener en menos de 10 segundos un veredicto claro con **protocolo de qué hacer**.

## Propuesta

- WhatsApp + voz.
- Recibe SMS, link o audio.
- Devuelve: **fraude / sospechoso / legítimo** + razón + protocolo de acción + reporte a CSIRT/CMF si corresponde.

## Stack

- Claude Haiku 4.5 (baja latencia, costo).
- **Constitutional AI** mitiga falsos positivos.
- **Tool use** para reportar al SERNAC.
- Integración con feed CSIRT (URLs maliciosas).

## Scoring (criterios oficiales)

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,95 | 23,75 |
| Datos | 20 | 0,75 | 15,00 |
| Claude/Agentic | 25 | 0,80 | 20,00 |
| Funcionalidad | 15 | 0,85 | 12,75 |
| Pitch | 15 | 0,90 | 13,50 |
| **Total** | | | **85,00** |

## Por qué gana (en su línea)

- **Brecha total en Chile**: NO existe app gratuita ciudadana de detección de phishing/SMS/llamadas con IA generativa (deep research, sección 5).
- **Ley 21.663** habilita uso de **IOCs públicos**.
- Voice-first para baja literacy digital.
- Métrica clara: **intentos verificados / fraudes evitados**.

## Por qué (de momento) está fuera

- El equipo eligió **Inclusión Financiera** ([ADR 0002](../especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md)).
- El argumento "atacar el problema raíz" puso a Ciberseguridad como reactiva.
- Si algún spike día 1-2 muestra que Defensor/Letra Chica no convencen, esta es la **apuesta de fallback más fuerte** en otra línea.

## Si pivoteamos a esta idea, qué cambia

- Nuevo ADR superseding 0002.
- Re-foco de research regulatorio en **Ley 21.663 (ciberseguridad)** y **Ley 21.673 (antifraude)**.
- Cambio de mentor objetivo: **CSIRT / SERNAC / PDI** en vez de **CMF / SII**.

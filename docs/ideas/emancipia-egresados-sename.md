---
title: "Idea: EmancipIA / Despegue — simulador post-SENAME contra el sobreendeudamiento"
description: "Roleplay conversacional: Claude actúa como vendedor agresivo de retail con CAE 40 % y el joven debe decidir. Si cae, le muestra el costo real."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: activa
prioridad: media
tags:
  - idea
  - inclusion-financiera
  - sename
  - jovenes
  - roleplay
---

# Idea: EmancipIA / Despegue — simulador post-SENAME

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *Al cumplir 18 años, los jóvenes bajo tutela del Estado son expulsados al mundo adulto sin redes ni alfabetización financiera. EmancipIA es un juego de rol donde Claude asume el papel de un vendedor agresivo de retail ofreciendo una tarjeta con CAE cercana al 40 %. El joven debe decidir.*

## Problema

- **Egresados de SENAME / Mejor Niñez** son **presa fácil del sobreendeudamiento comercial** al cumplir 18 años.
- La **Tasa Máxima Convencional (TMC)** para créditos de consumo bajo 50 UF roza el **40,59-40,90 % anual** ([CMF](https://www.cmfchile.cl/portal/principal/613/w3-propertyvalue-43062.html)).
- **No hay colchón familiar** que amortigüe un error.
- **Sub-segmento:** jóvenes 17-19 egresando de residencias de protección estatal.

## Hipótesis

La alfabetización financiera tradicional asume colchón familiar y no funciona para este perfil. Un **simulador conversacional adversarial** ("ataque virtual") construye resiliencia antes del primer contacto real con el retail.

## Propuesta

### Qué hace

- Roleplay conversacional. Claude asume rol de **vendedor agresivo** ofreciendo tarjeta de retail.
- El joven debe decidir: aceptar / negociar / rechazar.
- Si cae en la trampa virtual: la IA cambia de rol y muestra un **estado de cuenta** con cómo desaparece su sueldo en intereses.
- Cierra como mentor: "Esto es lo que pasó. La próxima vez puedes decir: ..."

### Qué NO hace

- No reemplaza la educación financiera formal.
- No accede a datos reales de la persona joven.

## Stack y datos

- **Modelo Claude:** Opus 4.7 para el roleplay (matiz, persuasión simulada) + Sonnet 4.6 para análisis post-juego.
- **Patrones agénticos:** Roleplay prompting avanzado (Claude como adversario y luego como mentor), Structured Outputs (estado de cuenta sintético).
- **Datasets:** [CMF Educa](https://www.cmfeduca.cl), normativa Sernac Financiero, TMC vigente.

## Demo imaginada (60 s)

1. "**Bastián**, 18 años, egresó de un hogar SENAME hace 1 mes. Trabajo CLP 460.000."
2. "Hola Bastián, te llamo de Tienda XYZ. Vengo a ofrecerte una tarjeta con cupo de CLP 800.000 sin aval..."
3. Bastián acepta.
4. "Tarjeta otorgada. CAE 39,8 %. Dividendo CLP 41.000/mes por 36 meses. Total a pagar: **CLP 1.476.000** por una tarjeta de CLP 800.000."
5. "Bastián, perdiste **76 % en intereses**. Aquí está la lección: ..."

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,90 | 22,50 |
| Datos | 20 | 0,70 | 14,00 |
| Claude/Agentic | 25 | 0,90 | 22,50 |
| Funcionalidad | 15 | 0,70 | 10,50 |
| Pitch | 15 | 0,90 | 13,50 |
| **Total** | | | **83,00** |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M (roleplay requiere prompts cuidadosos para no caer en tono patronizante).
- **Riesgo:** revictimización si el roleplay no se diseña con un trabajador social.
- **Datos disponibles:** sí (TMC público).
- **Demo end-to-end:** sí.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Tono patronizante / revictimizante | Alta | Alto | Validar con trabajador social de Mejor Niñez antes del demo |
| Joven se siente humillado | Media | Alto | Cierre con narrativa de empoderamiento, no de fracaso |
| Datos sensibles si se vincula a perfil real | Baja | Alto | Modo 100 % anónimo, no requiere registro |

## Por qué gana

- **Gamificación conversacional única** — no es chatbot, es simulador adversarial.
- **Caso análogo:** simuladores de riesgo financiero nórdicos (Suecia, Noruega).
- **Diferenciador de UX agéntica** difícil de igualar.

## Próximos pasos

- [ ] Validar guion con trabajador social de Mejor Niñez.
- [ ] Spike de prompting de Claude como vendedor agresivo (sin cruzar líneas éticas).
- [ ] Diseñar 3 escenarios distintos (tarjeta retail, crédito automotriz, casa de empeño).

## Notas y referencias

- **Caso análogo:** simuladores de riesgo financiero nórdicos.
- Catálogo completo: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

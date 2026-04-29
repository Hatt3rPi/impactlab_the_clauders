---
title: "Idea: Re-Inicia — copiloto de reinserción y quiebra personal Ley 21.563"
description: "Para ex-presos y microemprendedores destruidos: la IA mapea ruta de quiebra personal asequible y arma borrador de declaración jurada."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: activa
prioridad: media
tags:
  - idea
  - inclusion-financiera
  - quiebra
  - ley-21563
  - reinsercion
---

# Idea: Re-Inicia — copiloto de reinserción y quiebra

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *Para ex-privados de libertad reinsertándose con deudas acumuladas durante el encierro y para microemprendedores quebrados: Re-Inicia mapea su ruta de quiebra personal según Ley 21.563 (Renegociación y Liquidación), explica bienes inembargables, y arma el borrador de declaración jurada.*

## Problema

- La **Ley 21.563** (Régimen Concursal) ofrece vías de **renegociación o liquidación de deuda personal**, pero sus requisitos son de **alta complejidad técnica**.
- **Abogados de quiebras cobran CLP 20.000-100.000/hora** o porcentajes prohibitivos para personas ya endeudadas.
- **Sub-segmentos:** ex-convictos reinsertándose + microemprendedores en cesación de pagos profunda.
- Fricción raíz: la "muerte civil" por DICOM bloquea acceso al mercado laboral formal y al crédito.

## Hipótesis

Si el usuario puede narrar su situación en lenguaje natural, la IA puede mapear su ruta legal de "borrar la pizarra" (Ley 21.563) sin pagar abogado.

## Propuesta

### Qué hace

- Recibe descripción del usuario (texto o voz).
- Determina si califica para procedimiento concursal con **Superintendencia de Insolvencia y Reemprendimiento (SUPERIR)**.
- Lista **bienes inembargables** según ley.
- Genera **borrador de declaración jurada** lista para firmar.
- Explica plazos y consecuencias en lenguaje claro.

### Qué NO hace

- No representa legalmente al usuario (debe contratar abogado).
- No otorga la quiebra (la otorga el tribunal).
- Disclosure permanente: "soy una IA, no un abogado."

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 (Citations rigurosas a Ley 21.563).
- **Patrones agénticos:** Citations a artículos específicos de Ley 21.563, Document Generation (PDFs de declaración), Structured Outputs (lista de bienes inembargables).
- **Datasets:** Formularios y guías de [SUPERIR](https://www.superir.gob.cl), información del Boletín Comercial.

## Demo imaginada (60 s)

1. "**Carlos** salió de Santiago 1 hace 6 meses. Tiene CLP 12 M en deudas (multitienda + tarjetas)."
2. "Carlos, según Ley 21.563 art. 263, **calificas para procedimiento concursal de liquidación**. Te genero el borrador de declaración jurada."
3. "Tus bienes inembargables incluyen: ropa de uso, herramientas de trabajo, lecho. Lo demás se liquida."
4. "Plazo: 6-12 meses. Después, salida limpia de DICOM."

## Scoring

| Criterio | Peso | Score | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,85 | 21,25 |
| Datos | 20 | 0,75 | 15,00 |
| Claude/Agentic | 25 | 0,90 | 22,50 |
| Funcionalidad | 15 | 0,70 | 10,50 |
| Pitch | 15 | 0,80 | 12,00 |
| **Total** | | | **81,25** |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M.
- **Riesgo:** consejo legal inexacto puede tener consecuencias penales (ocultamiento de bienes).
- **Datos disponibles:** sí (SUPERIR público).
- **Demo end-to-end:** sí.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Consejo legal inexacto | Alta | Alto (penal) | Disclaimer permanente; siempre derivar a Defensoría Penal Pública para casos complejos |
| Ocultamiento de bienes mal asesorado | Media | Alto | No instruir sobre cómo evitar embargo, solo sobre derechos |
| Estigma de la quiebra | Alta | Medio | Narrativa empoderadora, no de "fracaso" |

## Por qué gana

- **Aborda el dolor más crudo** del Track 1: "Derechos financieros que no pueden ejercer".
- **Caso análogo verificable:** [Upsolve (USA)](https://upsolve.org) — plataforma gratuita para declarar bancarrota.
- **Stakeholders:** SUPERIR, Defensoría Penal Pública.

## Próximos pasos

- [ ] Validar plantilla de declaración jurada con un abogado de quiebra.
- [ ] Conseguir 2-3 casos reales (anonimizados) para pulir el roleplay.
- [ ] Spike Citations sobre Ley 21.563.

## Notas y referencias

- **Caso análogo:** [Upsolve (USA)](https://upsolve.org).
- Catálogo completo: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

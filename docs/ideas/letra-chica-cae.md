---
title: "Idea: Letra Chica / Tu Plata — semáforo de contratos con Vision + SERNAC"
description: "Foto de un contrato y la IA devuelve un semáforo por cláusula con costo total real."
autor: "Estrategia Literacy Regulatoria + Deep Research Calibria"
fecha: 2026-04-29
linea: inclusion-financiera
estado: activa
prioridad: alta
tags:
  - idea
  - inclusion-financiera
  - cae
  - vision
  - contratos
---

# Idea: Letra Chica / Tu Plata — semáforo de contratos financieros

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [PDF de estrategia](../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf) y/o el [Deep Research de Calibria](../assets/research/2026-04-29-deep-research-calibria.html). **Aún no validada por el equipo.**

> *El usuario fotografía un contrato (tarjeta retail, crédito de consumo, plan de telco) y la IA le muestra un semáforo verde-amarillo-rojo por cláusula con la ley violada citada y un cálculo de costo total real.*

> :material-flag: **Plan B según la estrategia** ([PDF p. 6-7](../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf)) — *si el equipo prefiere un producto con demo más visual*. También recomendada por el deep research como **Quick Win 2** (Impacto 9 / Complejidad 4).

> Esta ficha **consolida** dos descripciones equivalentes:
>
> - "Letra Chica" del PDF (Idea 2).
> - "Tu Plata · Traductor CAE/CTC" del deep research (Quick Win 2).

## Problema

- **57 % no compara productos** antes de firmar (CAF-CMF 2023).
- **CAE real, comisiones por mantención, seguros desgravamen forzados, cláusulas de mora exponencial** son ilegibles.
- Solo **1 de cada 5** chilenos calcula correctamente la tasa simple del crédito.
- Dolor del **80 %+ de la población** según el deep research.

## Hipótesis

Si el usuario puede **fotografiar** cualquier contrato financiero y obtener en segundos un **semáforo de cláusulas** con cita legal y cálculo de costo total, entenderá lo que firma sin pedir ayuda profesional.

## Propuesta

### Qué hace

- **Recibe** foto o PDF de un contrato.
- Devuelve:
    1. Semáforo visual por cláusula (**verde / amarillo / rojo**) con explicación en lenguaje natural.
    2. Comparación con normativa CMF/SERNAC (**Ley 20.555, NCG 484, Ley 19.496**).
    3. Cálculo de **costo total real** (CAE, comisiones ocultas, seguros, total a pagar).
    4. Comparador con simulador SERNAC y "Conoce tu Deuda".

### Qué NO hace

- No firma por el usuario.
- No recomienda banco/retail específico (línea roja AUP).
- No archiva contratos (privacidad).

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 (Vision + Citations).
- **Patrones agénticos:** PDF/Vision nativo, Citations al artículo violado, Structured Outputs con schema `cláusula → riesgo → ley → cita → severidad`, **Artifacts** para generar simulador HTML interactivo.
- **Datasets:** NCG 484 CMF (comisiones), Ley 20.555, Reglamento Ley Sernac, dataset de 20-30 contratos reales (pedir en LinkedIn).

## Demo imaginada (60 segundos)

1. **Inicio:** alguien presenta un contrato Cencosud/Ripley/CMR.
2. **Acción:** lo fotografía.
3. **Magia:** la IA muestra el contrato con highlights rojos en 4 cláusulas, cada una con su violación legal citada, y al final un total: "este contrato te cuesta CLP $XYZ, no los $ABC que dice la portada".
4. **Cierre:** comparativa contra el simulador SERNAC equivalente.

## Scoring (criterios oficiales)

| Criterio | Peso | Score (0-1) | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,90 | 22,50 |
| Uso responsable de datos | 20 | 0,80 | 16,00 |
| Claude & Agentic Thinking | 25 | 0,90 | 22,50 |
| Funcionalidad | 15 | 0,75 | 11,25 |
| Calidad del pitch | 15 | 0,95 | 14,25 |
| **Total** | **100** | | **86,50** |
| Bonus agentic (+5) | 5 | 0,75 | +3,75 |

## Viabilidad en 48 h

- **Esfuerzo:** M-A (variabilidad visual de contratos).
- **Riesgos:**
    - Calidad de OCR sobre fotos malas.
    - Evaluación legal subjetiva → acotar a infracciones evidentes (no opinables).
- **Datos disponibles ya:** sí (leyes públicas; contratos reales hay que pedirlos).
- **Demo end-to-end factible:** sí.

## Por qué gana

- **Demo es espectacular** ("subo este contrato y aparece todo en rojo") — alto puntaje en pitch.
- Masivo: **cualquier chileno tiene un contrato así**.
- **SERNAC está en la mesa público-privada** del lab → posible LOI.

## Próximos pasos para validar

- [ ] Conseguir **20-30 contratos reales** (LinkedIn / WhatsApp / familia).
- [ ] Spike Vision con 3 contratos diferentes (CMR / Ripley / banco).
- [ ] Listado curado de **infracciones más comunes** según SERNAC.
- [ ] Validar con un abogado del consumidor ("¿estas 5 cláusulas son inequívocamente abusivas?").

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Variabilidad visual de contratos | Alta | Medio | Pre-procesamiento de imagen, manejo de errores |
| Identificar mal una cláusula como abusiva | Alta | Alto | Mostrar **siempre la cita legal** y dejar al usuario juzgar |
| Letra del contrato dañada / cortada | Media | Medio | Pedir múltiples fotos, fallback "no logré leer claramente" |

## Solapamiento con otras ideas

- **Defensor (DICOM)** se foca en cobranza ya activa; Letra Chica se foca en el contrato **antes** de firmar. Complementarias.
- Posible **integración**: Letra Chica como feature dentro de Defensor, o lanzamiento por separado.

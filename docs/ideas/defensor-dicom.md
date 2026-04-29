---
title: "Idea: Defensor — copiloto de derechos para morosos en DICOM"
description: "WhatsApp bot que defiende a personas con deuda de cobranzas abusivas con citación legal."
autor: "Estrategia Literacy Regulatoria (research previo)"
fecha: 2026-04-29
linea: inclusion-financiera
estado: activa
prioridad: estrella
tags:
  - idea
  - inclusion-financiera
  - dicom
  - whatsapp
  - vision
---

# Idea: Defensor — copiloto de derechos financieros para chilenos en DICOM :material-star:

> *Para una mujer jefa de hogar con deuda repactada en retail, que recibe llamadas y SMS abusivos sin entender qué firmó, Defensor es un WhatsApp bot que en minutos le dice qué dice la ley, si hay infracción, le redacta la carta-respuesta y le indica dónde reclamar. Diferenciador: cita el artículo exacto.*

> :material-star-circle: **Idea recomendada por la estrategia** ([PDF p. 6, 8](../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf)). Combina el segmento más numeroso (3,9 M morosos), encaja literalmente con el wording del Track 1, y usa **las cuatro capacidades diferenciales de Claude juntas** (Citations + Vision + ES-CL + Haiku para escala).

## Problema

- **3,92 M de personas** con deuda morosa en DICOM (25 % de los adultos), especialmente quintiles D-E y mujeres jefas de hogar.
- **Desconocen sus derechos** bajo Ley 21.563 (régimen concursal), Ley 21.680 (deuda consolidada), Ley 21.320 (límites a cobranzas), reforma 19.628 (datos personales) y SERNAC Financiero.
- Reciben **llamadas abusivas, repactaciones que duplican deuda, y nunca saben cuándo prescribe**.

## Hipótesis

Si una persona en DICOM puede **reenviar por WhatsApp** un SMS, papel de cobranza o contrato de repactación, entonces obtiene en **menos de 60 segundos** un diagnóstico legal con cita, una **carta-respuesta** lista para enviar y una **ruta de reclamo** clara.

## Propuesta

### Qué hace

- **Recibe en WhatsApp** un SMS, foto de papel de cobranza, o contrato de repactación.
- Devuelve:
    1. **Qué dice la ley** sobre lo que está pasando.
    2. **Si hay infracción** (sí/no/ambiguo + por qué).
    3. **Modelo de carta-respuesta** generada como PDF firmable.
    4. **Ruta de reclamo** a SERNAC / CMF.

### Qué NO hace (alcance fuera)

- No da consejo de "no pagues" (línea roja AUP).
- No actúa como abogado (disclosure permanente).
- No automatiza pagos.

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 (cerebro) + Haiku 4.5 (escala WhatsApp).
- **Patrones agénticos:** RAG con Citations sobre normativa real, Vision para documentos, Tool use para generar PDF de carta.
- **MCPs propuestos:** `cmf-circulares`, `sernac-cartillas`, `ley-fintech-articulos`.
- **Datasets:** cartillas SERNAC, leyes 21.563/21.680/21.320, NCG CMF sobre repactaciones, dataset propio de 50-100 SMS/cartas reales (pedirlos en redes sociales en día 1).

## Demo imaginada (60 segundos)

1. **Inicio:** demo en vivo. Pantalla compartida de WhatsApp.
2. **Acción:** la persona reenvía un SMS de cobranza real ("repacte ahora con 50 % descuento, oferta vence hoy").
3. **Magia:** Defensor responde en 8 segundos con (a) diagnóstico ("esto puede vulnerar Ley 21.320 art. X por presión indebida"), (b) cita textual del artículo, (c) PDF de carta-respuesta listo para descargar.
4. **Cierre:** se muestra la carta y se pulsa "enviar a SERNAC".

## Scoring (criterios oficiales)

| Criterio | Peso | Score (0-1) | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,95 | 23,75 |
| Uso responsable de datos | 20 | 0,80 | 16,00 |
| Claude & Agentic Thinking | 25 | 0,95 | 23,75 |
| Funcionalidad | 15 | 0,80 | 12,00 |
| Calidad del pitch | 15 | 0,90 | 13,50 |
| **Total** | **100** | | **89,00** |
| Bonus agentic (+5) | 5 | 0,80 | +4,00 |

> Scoring inicial heurístico. Ajustar tras spike técnico y entrevistas día 1.

## Viabilidad en 48 h

- **Esfuerzo:** M-L.
- **Riesgos técnicos:**
    - **Disclosure** ("no soy abogado") permanente.
    - **Evitar** sugerir no pagar.
    - **PII**: anonimizar antes de loguear.
- **Datos disponibles ya:** parcial (la ley pública sí; SMS/cartas reales hay que conseguirlos esta semana).
- **Demo end-to-end factible:** sí.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Recomendar acción ilegal o desaconsejable | Media | Alto (descalifica) | Eval set de 30 prompts gold-standard con casos a rechazar |
| Variabilidad de SMS reales (cada banco/retail tiene su jerga) | Alta | Medio | Dataset de 50+ SMS reales antes del lab |
| Falsos positivos de "infracción" | Media | Alto | Schema con severidad explícita + escalamiento a abogado humano para casos rojos |
| Privacidad: usuarios envían PII | Alta | Medio | Anonimización automática en logs |
| Carta-respuesta con error formal | Media | Alto | Validación contra plantillas SERNAC oficiales |

## Por qué gana (según la estrategia)

- Combina **el grupo más grande y políticamente sensible** (3,9 M morosos).
- **Encaja perfecto con "literacy regulatoria"** — wording literal del Track 1.
- **CMF y SERNAC** tienen incentivo directo en presentarlo.
- **Demuestra Claude en su capacidad más pura** (Citations + Vision + ES-CL).
- Cualquier chileno con DICOM **es un usuario validable** en una semana.

## Próximos pasos para validar

- [ ] **5-10 entrevistas reales** en grupos Facebook tipo "Salida de DICOM" (día 1).
- [ ] Spike: prompt v0 que cite **Art. 17 B Ley 19.496** ante un caso de prueba.
- [ ] Spike Vision: leer 3 papeles de cobranza reales y extraer monto, banco/retail, fecha, supuesta deuda.
- [ ] Conseguir **dataset de 50+ SMS reales** vía redes sociales del equipo.
- [ ] Validar con **mentor regulatorio** (CMF/SERNAC) en pasillo del Forum día 6.

## Notas y referencias

- Sub-segmento sugerido por la estrategia: **mujeres jefas de hogar con deuda repactada en retail**.
- Posible cliente B2B post-lab: **Coopeuch (1,2 M socios)**, **Hogar de Cristo financiero**, **Fondo Esperanza**.
- Cubre dolores top del scoring (deep research): #11 (sobreendeudamiento) y se cruza con #3 (caída de respuesta a reclamos).

---
title: Líneas temáticas
description: Comparativa lado a lado de las 3 líneas posibles del lab.
tags:
  - lineas
---

# Líneas temáticas

<!-- AUTO-BANNER -->
!!! note ":material-bank: Información oficial del lab"
    Extraído del sitio oficial del [Claude Impact Lab Chile 2026](https://fintech.benditaia.cl/es) (WebFetch 2026-04-29). Confirmar con la organización antes del 6 de mayo.

El lab ofrece **tres líneas temáticas** y cada equipo elige **una**. Esta sección sirve para comparar y decidir cuál atacamos.

!!! success "Decisión tomada: Inclusión Financiera"
    El equipo eligió **Inclusión Financiera** en la [reunión de kickoff del 29/04](../reuniones/2026-04-29-definicion-problema-setup.md). Ver razones y alternativas en [ADR 0002](../especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md).

    Las páginas de las otras dos líneas se mantienen como referencia, pero el equipo ya no trabaja en ellas.

## Matriz comparativa

| Dimensión | Inclusión financiera | Ciberseguridad ciudadana | Protección de datos |
|---|---|---|---|
| **Problema central** | Regulación incomprensible para el ciudadano | Vulnerabilidad ante fraude digital | Pérdida de control sobre datos personales |
| **Stakeholder regulador** | CMF, SERNAC | CMF, SERNAC, autoridades policiales | CMF, autoridad de protección de datos |
| **Datasets clave** | Ley Fintech 21.521, circulares CMF, FAQs SII | Reportes de fraude, alertas SERNAC | Ley 19.628, derechos ARCO, registros |
| **Tipo de agente** | RAG conversacional sobre regulación | Detector + educador anti-fraude | Asistente de derechos ARCO |
| **Riesgo de alucinación** | Alto (legal sensible) | Medio (educacional) | Alto (legal sensible) |
| **Demo visualmente fuerte** | Media (chat) | Alta (alertas, simulaciones) | Media-alta (visualizaciones) |
| **Differentiation potencial** | Alto si profundizamos en un nicho (ej: emprendedores) | Alto (gamificación, casos reales) | Alto (UI de "tus datos en X institución") |
| **Competencia interna** | Probablemente la más popular | Media | Media-baja (más nicho) |

## Criterios de evaluación aplicados a cada línea

Recordatorio de pesos: Impacto cívico 25 % · Datos 20 % · Claude/Agentic 25 % · Funcionalidad 15 % · Pitch 15 %.

| Criterio | Inclusión financiera | Ciberseguridad | Protección de datos |
|---|---|---|---|
| **Impacto cívico potencial** | :material-circle: :material-circle: :material-circle: | :material-circle: :material-circle: :material-circle: | :material-circle: :material-circle: |
| **Riqueza de fuentes públicas** | :material-circle: :material-circle: :material-circle: | :material-circle: :material-circle: | :material-circle: :material-circle: |
| **Encaje con agentic thinking** | :material-circle: :material-circle: | :material-circle: :material-circle: :material-circle: | :material-circle: :material-circle: :material-circle: |
| **Facilidad de demo en 48 h** | :material-circle: :material-circle: :material-circle: | :material-circle: :material-circle: | :material-circle: :material-circle: |

*(escala visual provisional — actualizar cuando hagamos research por línea)*

## Profundizar

- :material-bank: [Inclusión financiera](inclusion-financiera.md)
- :material-shield-account: [Ciberseguridad ciudadana](ciberseguridad-ciudadana.md)
- :material-lock: [Protección de datos](proteccion-datos.md)

## Cómo decidiremos

1. Cada miembro lee las tres páginas y trae **2 ideas concretas** por línea preferida.
2. Las ideas van al [tablero de ideas](../ideas/index.md) con su scoring.
3. Reunión de selección: comparamos top 3 ideas globales y elegimos línea + idea.
4. Registramos la decisión como [ADR](../especificaciones/adrs/index.md).

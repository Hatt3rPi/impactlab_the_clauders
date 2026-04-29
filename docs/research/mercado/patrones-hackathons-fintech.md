---
title: "Patrones que ganan hackathons fintech (y los que descalifican)"
description: "Lecciones extraídas de 15+ ganadores documentados (BID Lab, CAF LIF, Visa Everywhere, Finnosummit, Mastercard Lighthouse, Santander X, 2016-2026)."
autor: "Síntesis sobre research previo del equipo (Estrategia Literacy Regulatoria)"
fecha: 2026-04-29
categoria: mercado
linea: transversal
tags:
  - research
  - hackathon
  - patrones
  - pitch
---

# Patrones que ganan hackathons fintech

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuente externa"
    Sintetizado a partir del [PDF de estrategia Literacy Regulatoria](../../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf). **Verificar cifras antes de citarlas en el pitch.**

Si vamos a ganar, **imitar lo que ya funciona** y **evitar lo que descalifica**.

## Fuente

- :material-file-pdf-box: [Estrategia Literacy Regulatoria (PDF)](../../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf), p. 4-5.

Base de evidencia: 15 ganadores verificados en BID Lab, CAF LIF, Visa Everywhere, Finnosummit, Mastercard Lighthouse y Santander X (2016-2026).

---

## Lo que ganan los ganadores

### Procesos

- **4 de cada 5 ganadores** parten de **entrevistas reales con su segmento** antes de programar.
- **Casi todos abren el pitch con un caso humano nombrado** ("María vende empanadas en La Pintana...").
- **Pitch > prototipo**, pero **demo funcional en vivo es no-negociable**.

### Categorías que históricamente convierten

- **Scoring alternativo**.
- **Educación financiera embebida (no apps standalone)**.
- **Créditos para informales**.
- **Productos para migrantes**.
- **Onboarding KYC simplificado**.

### Tendencia 2024-2026 (iupana)

> Educación **"invisible" dentro del producto** — exactamente lo que pide el Track 1 del Claude Impact Lab.

### Qué muestran los ganadores 2023-2026 con IA (Nauphilus, Tomín, Leja)

- **No son wrappers**.
- Modelo entrenado sobre datos del **dominio**.
- **Métrica concreta** de mejora.
- Caso donde la IA **es necesaria, no decorativa**.

> Un wrapper de Claude sobre datos genéricos pierde frente a un sistema con **RAG sobre normativa CMF + Citations + Tool use a APIs reales chilenas**.

### Stack que llega a la final

Los ganadores típicos llegan con:

- **One-pager**.
- **Figma navegable**.
- **Frontend funcional** sobre datos mockeados o reales.
- **Video de respaldo de 90 segundos** por si la demo en vivo falla.

---

## Errores que descalifican (predecibles, se repiten)

| Error | Por qué pesa |
|---|---|
| Prototipo **sin problema validado** | Los jueces detectan la falta de research en 30 segundos |
| Demo que **no corre en vivo** | Pierdes ~50 % del puntaje aunque la idea sea buena |
| **Equipo solo técnico** | Sin storytelling y producto, el pitch es plano |
| **Mercado demasiado amplio** ("para todos los chilenos") | Se ve como falta de foco |
| **Pitch lleno de jerga** | El jurado del Lab incluye reguladores no técnicos |
| **Ignorar la tecnología patrocinadora** | En este caso: usar Claude como wrapper sin aprovechar Citations/Vision/MCPs |
| **No tener respuestas a las 5 preguntas duras** | El jurado las usará para diferenciar finalistas |

### Las 5 preguntas duras estándar (preparar respuestas)

1. **¿Por qué no lo hace ya un banco?** (típica respuesta: "no tienen incentivo").
2. **¿Qué pasa si te copia Tenpo / Destácame?** (típica respuesta: "moat de red de ONGs / partnerships").
3. **Unit economics** (costo por consulta, pricing B2C/B2B).
4. **Regulación CMF** (cómo no caemos en asesoría no autorizada).
5. **Escalabilidad** (modelo replicable a otros países LATAM con normativa equivalente).

---

## Criterios de evaluación típicos en hackathons fintech

| Criterio | Peso típico | En este Lab esperamos... |
|---|---|---|
| Innovación | ~22 % | Estándar |
| Impacto / inclusión | ~22 % | **Más peso** dado el énfasis cívico |
| Viabilidad técnica | ~18 % | Estándar |
| Modelo de negocio | ~18 % | Estándar |
| Equipo y pitch | ~12 % | Estándar |
| Uso de tecnología patrocinadora | ~8 % | **Más peso** dado que es Anthropic |

> Recordatorio: criterios oficiales del lab son **Impacto cívico 25 % · Datos 20 % · Claude/Agentic 25 % · Funcionalidad 15 % · Pitch 15 %** + bonus +5. Ver [Criterios de evaluación](../../competencia/criterios-evaluacion.md).

---

## Estructura de pitch recomendada (5 minutos)

7 láminas (deck v1):

1. **Hook humano** (10-15 s) — caso real con nombre.
2. **Problema dimensionado** (cifras + ley violada).
3. **Solución + demo** (en vivo o video).
4. **Diferenciación tech** (Citations + Vision + MCP).
5. **Modelo de negocio** (B2C freemium + B2B SaaS).
6. **Equipo** (perfil + por qué somos los que pueden hacerlo).
7. **Pedido** (presentación a regulador, partnership, sandbox).

---

## Tres movimientos de mayor apalancamiento (recomendados por la estrategia)

1. **Hacer 5-10 entrevistas reales en día 1 antes de escribir una línea de código** — los ganadores de BID, CAF y Visa Everywhere todos lo hacen, los perdedores no.
2. **Explotar las capacidades únicas de Claude** (Citations + Vision + 1M contexto + Haiku barato) en lugar de tratarlo como wrapper.
3. **Conseguir antes del pitch un LOI escrito y un contacto verbal con un regulador** — ambos son asequibles en una semana en Chile y ambos son game-changers en el storytelling final.

---

## Riesgo más alto identificado

> El riesgo más alto **no es técnico ni regulatorio: es de alcance**. Una semana es muy poco para hacer un producto bonito sobre un problema mal definido, y mucho para hacer un producto enfocado sobre un problema dolorosamente específico.
>
> **"Mujeres jefas de hogar con deuda repactada en retail"** vs **"morosos en general"** = diferencia entre top 3 y proyecto olvidable.

---

## Implicancias para nuestro proceso

- [x] Equipo balanceado (técnico + IA + comercial + UX) — ya lo tenemos.
- [ ] 5-10 entrevistas reales antes del lab.
- [ ] One-pager listo el día 3 del sprint pre-lab.
- [ ] Video de respaldo 90 s — listo el día 4.
- [ ] LOI + contacto regulador antes del 6 de mayo.
- [ ] Eval set de 30 prompts gold-standard antes del demo.
- [ ] Las 5 preguntas duras respondidas el día 4.
- [ ] Pitch ensayado mínimo 6 veces el día 6.

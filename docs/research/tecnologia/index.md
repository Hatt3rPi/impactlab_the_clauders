---
title: Research tecnológico
description: Papers, patrones agénticos, benchmarks, librerías y MCPs interesantes.
tags:
  - research
  - tecnologia
---

# Research tecnológico

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../../convenciones-de-contenido.md).

Notas sobre **cómo construir** la solución: patrones agénticos, librerías, MCPs, benchmarks de modelos, evaluación.

## Por qué importa

El criterio **Claude & Agentic Thinking (25 %)** + el **bonus +5** dependen de que apliquemos patrones agénticos sólidos. Necesitamos referencias concretas para argumentar nuestras decisiones.

## Áreas a investigar

### Patrones agénticos

- [ ] Reflection / self-criticism loops.
- [ ] Tool use estructurado vs prompt-driven.
- [ ] Multi-agente: ¿especialización por subtarea o un único agente con muchas tools?
- [ ] RAG agéntico (el agente decide qué y cuándo recuperar).
- [ ] Planning explícito (descomposición de tareas).
- [ ] Verificación de hechos / citación obligatoria.

### Stack Anthropic

- [ ] Lectura del [Agent SDK](../../stack/agent-sdk.md) actualizado.
- [ ] [MCPs disponibles](../../stack/mcps.md) y cómo crear uno custom.
- [ ] **Prompt caching** para reducir costos en chats largos.
- [ ] **Extended thinking** y cuándo conviene.
- [ ] **Citations API** (si está disponible) para citar fuentes con tracking automático.

### Datos y RAG

- [ ] Embeddings: opciones disponibles que se integren bien con Claude.
- [ ] Vector stores ligeros para 48 h (Chroma, Qdrant local, etc.).
- [ ] Chunking de textos legales (estructura por artículos vs tokens).

### Evaluación

- [ ] Cómo evaluar respuestas legales sin un experto disponible.
- [ ] Detección de alucinaciones en respuestas con citación.

## Backlog

- [ ] Una nota por patrón agéntico relevante con ejemplo de código.
- [ ] Spike de prompt caching aplicado a regulación.
- [ ] Spike de RAG sobre Ley Fintech.

## Notas existentes

| Nota | Tema | Autor | Fecha |
|---|---|---|---|
| [Capacidades de Claude diferenciadoras](capacidades-claude-diferenciadoras.md) | Stack + features | Equipo | 2026-04-29 |

> Crear notas adicionales con [`../_template.md`](../_template.md).

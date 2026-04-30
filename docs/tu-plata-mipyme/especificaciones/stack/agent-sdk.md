---
title: Agent SDK
description: Kit oficial para construir agentes con Claude.
tags:
  - stack
  - claude
  - agentic
---

# Agent SDK

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../../../convenciones-de-contenido.md).

Kit oficial de Anthropic para construir **agentes** sobre la API de Claude. Es el centro del criterio **Claude & Agentic Thinking (25 % + bonus +5)**.

## Qué nos da

- Loop estándar de **planning → tool use → reflexión → respuesta**.
- Integración natural con MCPs.
- Manejo de **estado** del agente entre turnos.
- Estructura para **multi-agente** (un coordinador + agentes especializados).

## Patrones agénticos a considerar

### Single-agent con tools

Un agente con varias tools bien diseñadas. Más fácil de pulir en 48 h.

```text
[Usuario] → [Agente] ──┬─ tool: buscar_articulo_ley
                      ├─ tool: traducir_a_lenguaje_claro
                      ├─ tool: generar_carta_arco
                      └─ tool: validar_cita
                       ↓
                    [Respuesta con citas]
```

### Multi-agente con coordinador

Un agente coordinador delega en agentes especializados.

```text
[Usuario] → [Coordinador] ──┬─ [Agente legal]   (RAG sobre leyes)
                           ├─ [Agente redacción] (genera carta)
                           └─ [Agente validador]  (verifica citas)
                            ↓
                       [Respuesta sintetizada]
```

Más potente pero más caro y más complejo de depurar.

### Reflection loop

El agente **revisa su propia respuesta** antes de entregarla. Crítico para el riesgo de alucinación regulatoria.

```text
1. Generar respuesta inicial
2. Verificar: ¿cada afirmación tiene fuente citada?
3. Si no → reformular o pedir más contexto
4. Entregar
```

### RAG agéntico

El agente **decide cuándo y qué buscar**, en vez de un RAG mecánico.

- Necesita una tool de búsqueda (semántica + por keyword).
- Necesita un corpus indexado (Ley Fintech, FAQs, alertas).
- El agente puede hacer múltiples búsquedas hasta tener suficiente contexto.

## Decisiones que probablemente tomemos

- ¿Single-agent o multi-agente?
- ¿Cuántas tools? (Recomendable: empezar con 3-5.)
- ¿Cómo gestionamos memoria entre turnos? (Estado en backend vs solo en prompt.)
- ¿Cómo medimos calidad de las respuestas?

> Cuando se decida, capturar como [ADR](../adrs/index.md).

## Spike sugerido antes del lab

Construir un mini-agente de 2 horas que:

1. Reciba una pregunta de un ciudadano (ej: "¿qué hago si me cobran una comisión que no autoricé?").
2. Use una tool de búsqueda en un texto legal de prueba.
3. Devuelva respuesta + cita.
4. Auto-valide que la cita existe en el texto.

Esto nos da una baseline real de cuánto cuesta el patrón base.

## Recursos

- Skill `claude-api` en este Claude Code.
- Docs oficiales del Agent SDK (verificar versión a la fecha del lab).

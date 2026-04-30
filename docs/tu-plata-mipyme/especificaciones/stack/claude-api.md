---
title: Claude API
description: Modelos disponibles, créditos, recomendaciones de uso.
tags:
  - stack
  - claude
---

# Claude API

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../../../convenciones-de-contenido.md).

## Familias de modelos

La familia 4.X de Anthropic ofrece tres líneas:

| Modelo | Cuándo usarlo | Trade-offs |
|---|---|---|
| **Opus 4.x** | Razonamiento complejo, generación de pitch, redacción legal cuidada | Más caro y más lento |
| **Sonnet 4.x** | Default para la mayoría del flujo agéntico | Balance velocidad/capacidad |
| **Haiku 4.x** | Clasificación, validaciones, tools livianas, alta concurrencia | Más rápido y barato |

> Verificar IDs exactos del momento del lab. Al 2026-01: `claude-opus-4-7`, `claude-sonnet-4-6`, `claude-haiku-4-5-20251001`. Confirmar en docs oficiales antes del kickoff.

## Estrategia recomendada para 48 h

1. **Sonnet** como modelo default del agente principal.
2. **Haiku** para subtareas baratas: clasificar intent, formatear, validar formatos.
3. **Opus** solo para:
    - Redacción del pitch final.
    - Razonamiento jurídico cuando Sonnet no esté seguro.
    - Generación de cartas ARCO formales (si aplica).

## Funcionalidades clave

### Prompt caching

Permite **reutilizar prefijos** de prompts (ej: la ley completa) y reducir costo + latencia.

- Crítico si vamos a meter texto legal extenso en cada llamada.
- Hacer un **spike** temprano para medir ahorro real.

### Tool use

API nativa para que el modelo invoque funciones que definimos.

- Cada tool tiene un JSON schema y una descripción.
- El modelo decide cuándo invocarla.
- Necesario para el **agentic thinking**.

### Extended thinking

Para problemas que requieren razonamiento explícito antes de responder.

- Sopesar costo vs beneficio (es más caro).
- Útil para validación de respuestas legales.

### Citations

Si la API expone citaciones automáticas: usarlas. Reduce drásticamente el riesgo de **alucinación regulatoria** (descalificador del lab).

## Créditos y consumo

- USD 50 por participante. Equipo de 4 = USD 200.
- Estimación gruesa: 1M tokens de entrada en Sonnet ≈ pocos USD; con caching, mucho menos.
- **Habilitar logging** del consumo desde el día 1 para no quedarse sin créditos antes del demo.

## Buenas prácticas

- **Citar la fuente** en cada respuesta del agente que toque regulación.
- **Rechazar elegantemente** ("no tengo información oficial sobre esto") en vez de inventar.
- **Evals manuales** sobre 10-20 preguntas reales antes del pitch.

## Recursos

- Skill `claude-api` disponible en este Claude Code (úsala cuando construyamos).
- [Documentación oficial](https://docs.anthropic.com).

## Decisiones tomadas

> Mover acá las decisiones del equipo cuando se tomen, con link al ADR.

---
title: Stack técnico
description: Vista general del stack disponible y nuestras decisiones técnicas.
tags:
  - stack
---

# Stack técnico

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../convenciones-de-contenido.md).

Vista general de las **herramientas provistas por el lab** y de las **decisiones técnicas del equipo**.

## Provisto por el lab

<div class="grid cards" markdown>

-   :material-api: **[Claude API](claude-api.md)**

    ---

    Acceso a Sonnet, Opus y Haiku. USD 50 en créditos por participante.

-   :material-laptop-account: **[Claude Code](claude-code.md)**

    ---

    IDE con IA integrada (este mismo agente).

-   :material-robot: **[Agent SDK](agent-sdk.md)**

    ---

    Kit oficial para construir agentes con loops, tool use y validación.

-   :material-connection: **[MCPs](mcps.md)**

    ---

    Model Context Protocol para conectar el agente con datos y tools externas.

-   :material-database: **[Datasets](datasets.md)**

    ---

    Datos públicos de CMF, SII, SERNAC.

-   :material-server: **[Infraestructura](infraestructura.md)**

    ---

    Hosting, deploy, secrets, observabilidad.

</div>

## Decisiones técnicas pendientes

> A capturar como [ADRs](../especificaciones/adrs/index.md) cuando se tomen.

- Lenguaje principal: ¿Python o TypeScript?
- Framework UI: ¿qué marco usar para el front?
- Vector store: ¿hace falta? ¿cuál?
- Despliegue del prototipo: ¿hosted o local?
- Estructura del agente: ¿un único agente con muchas tools o multi-agente?

## Convenciones

- Todo el código del **prototipo** vive en otro repositorio (que se inicia el 6 de mayo).
- Este repo es **solo wiki**.
- Los **secrets** (API keys, etc.) **nunca** se commitean. Usar `.env` local + secret manager del provider.

## Costos / créditos

- USD 50 en créditos de Claude por participante × tamaño del equipo.
- Para conservar créditos en la fase exploratoria, usar **Sonnet** por defecto y Opus solo cuando se justifique.
- Activar **prompt caching** desde temprano si manejamos contextos largos (ej: ley completa).

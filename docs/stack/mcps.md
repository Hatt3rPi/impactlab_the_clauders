---
title: MCPs
description: Model Context Protocol — conectar agentes con datos y herramientas externas.
tags:
  - stack
  - mcp
---

# MCPs (Model Context Protocol)

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../convenciones-de-contenido.md).

Protocolo abierto que estandariza **cómo un agente accede a datos y herramientas externas**. Es la pieza que conecta a Claude con el "mundo real".

## Por qué nos importa

- **Punto fuerte de scoring** en Claude & Agentic Thinking.
- Reduce código de pegamento entre el agente y datasets/APIs.
- Permite reusar MCPs existentes (de la comunidad o de los reguladores).

## MCPs candidatos a usar / construir

### MCPs públicos potencialmente útiles

- **Web fetch / browser** para ir a sitios oficiales en tiempo real.
- **Filesystem** para leer corpus locales.
- **SQLite / Postgres** si tenemos una BD local.
- **Search** semántica (vector store con MCP wrapper).

### MCPs propios que podríamos construir

- `cmf-search` — busca en circulares y NCG de la CMF.
- `ley-fintech-rag` — RAG sobre Ley 21.521 con citación por artículo.
- `sii-faq` — busca en FAQs del SII.
- `sernac-alertas` — recupera alertas de fraude por categoría.
- `arco-formulario` — genera carta ARCO completable.

## Cómo decidiremos qué MCPs hacer

1. Definir la idea ganadora.
2. Listar las **3-5 capacidades externas** que el agente necesita.
3. Para cada una: ¿hay un MCP existente o lo construimos?
4. Priorizar los que aportan más al scoring.

## Construir un MCP en ~2 horas

Esquema general:

```text
1. Definir el nombre y las "tools" expuestas (1-3 al inicio).
2. Stub del servidor MCP (Python o TS).
3. Implementar 1 tool end-to-end con datos reales.
4. Probar con Claude Code conectado al MCP local.
5. Iterar prompt y descripción de tools.
```

## Convenciones para el lab

- Cada MCP custom vive en una carpeta `mcps/<nombre>` del repo del prototipo.
- README mínimo en cada MCP con: para qué sirve, cómo instalar, cómo correr.
- Logs de cada call para debugging durante el demo.

## Riesgos

- MCPs custom pueden tener **bugs ocultos** que el modelo enmascara.
- Tools mal descritas hacen que el modelo **no las invoque** o las invoque mal.
- Pasar texto demasiado grande por una tool genera **costos altos** (planear chunking).

## Decisiones tomadas

> Capturar acá los MCPs que decidamos construir o usar.

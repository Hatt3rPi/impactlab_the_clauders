---
title: "RAG · Retrieval Augmented Generation"
description: "Sección con la decisión de stack RAG, corpus inicial de documentación oficial chilena, y plan de implementación. 21 de 26 capacidades del producto V1 dependen del RAG."
tags:
  - tu-plata-mipyme
  - rag
  - retrieval
  - corpus
  - documentación-oficial
---

# 📚 RAG — Retrieval Augmented Generation

!!! info ":material-information: Para qué sirve esta sección"
    Documentación de cómo Impulsa **cita norma oficial chilena** sin alucinar. Incluye la decisión técnica del stack (Supabase + Voyage AI + Anthropic Contextual Retrieval), el catálogo de documentación a indexar agrupado por entidad emisora (SII, BCN, ChileAtiende, etc.), y el plan de ingesta.

> **21 de 26 capacidades del producto V1 (~81%)** dependen del RAG. Sin RAG, el bot improvisa números, fechas y nombres de leyes — riesgo crítico para un producto que asesora sobre formalización legal y tributaria.

## Documentos de la sección

| Doc | Qué contiene |
|---|---|
| [Corpus inicial por entidad](corpus-inicial.md) | Catálogo de **47 documentos** oficiales chilenos agrupados por **13 entidades emisoras** (SII, BCN LeyChile, ChileAtiende, Sercotec, FOGAPE, etc.) con URL, formato, frecuencia de cambio y mapeo a capacidades del producto |
| [Decisión de stack (en repo de código)](https://github.com/Hatt3rPi/impactlab_pre_journeyemprendedor/blob/main/docs/specs/rag-stack-decision.md){target="_blank"} | Análisis comparativo de Supabase pgvector vs alternativas (Pinecone, Qdrant, Weaviate, Chroma). Decisión: Supabase + Voyage AI `voyage-3.5-lite` + hybrid search + Anthropic Contextual Retrieval |

## Resumen de la decisión técnica

| Capa | Tecnología elegida | Por qué |
|---|---|---|
| **Vector store** | Supabase pgvector (Free → Pro al crecer) | Ya está en el stack. RLS unificado entre `users`, `messages`, `doc_chunks`. Una sola plataforma |
| **Embeddings** | Voyage AI `voyage-3.5-lite` (1024 dim) | Recomendado oficialmente por Anthropic. Multilingüe (clave para español chileno). 200M tokens gratis al inicio |
| **Hybrid search** | pgvector + tsvector con Reciprocal Rank Fusion | Salto de precisión 62% → 84% en queries con keywords legales chilenas (ej: "Art. 8 bis", "Ley 21.713") |
| **Contextual Retrieval** | Anthropic technique (Claude Haiku con prompt caching) | Reduce fallos de retrieval -49% solo / -67% con reranker. Costo marginal |
| **Reranking** | Cohere Rerank (opcional, no V1) | Activar solo si la precisión top-5 cae bajo 80% en producción |
| **Plan B** | Qdrant Cloud free tier | Migración ~1 día si Supabase da fricción |

## Costo estimado V1 (~1000 queries/día)

| Concepto | Mensual |
|---|---|
| Supabase Free (hasta 500MB docs) | USD 0 |
| Supabase Pro (cuando crezca) | USD 25 |
| Voyage AI embeddings (200M tokens gratis al inicio) | USD 0 |
| Claude Haiku Contextual Retrieval (one-shot del corpus) | <USD 1 |
| Claude Sonnet 4.6 inferencia con prompt caching | ~USD 230 |
| **Total con Claude inferencia** | **~USD 230-260** |
| Total sin prompt caching (referencia) | ~USD 480 |

!!! warning ":material-alert: Prompt caching obligatorio"
    Activar prompt caching en Claude Sonnet 4.6 reduce el costo de input ~10x. No es opcional — es la diferencia entre USD 230 y USD 480 al mes.

## Cómo se relaciona con otros documentos

| Documento | Para qué |
|---|---|
| Capacidades × etapa *(pendiente cargar — preview HTML en el [repo de código](https://github.com/Hatt3rPi/impactlab_pre_journeyemprendedor/blob/main/docs/preview/capacidades.html){target="_blank"})* | Define qué capacidades requieren RAG vs cuáles son IA pura. 21 de 26 capacidades V1 dependen del RAG |
| [Plan de implementación](../../plan.md) | Arquitectura general del producto (incluye mención al RAG dentro del flow) |
| [Stack tecnológico](../stack/index.md) | Stack general — el RAG es una capa que se monta encima de Supabase + Claude |
| [ADRs](../adrs/index.md) | Las decisiones técnicas formales del producto. La elección de stack RAG eventualmente debería formalizarse como ADR |

## Estado de implementación

!!! warning ":material-clock-outline: Status: propuesto, no implementado"
    La decisión de stack está documentada y aprobada conceptualmente. La ingesta del corpus y la implementación del retrieval en `/api/chat` quedan **post-lab** (5-6 mayo 2026). Estimado: ~2 días de trabajo + tiempo de descarga manual de docs (~6h).

## Próximas iteraciones de la sección

Cuando se implemente, esta sección debería sumar:

- `pipeline-ingesta.md` — script Node + GitHub Action mensual
- `query-flow.md` — diagrama y pseudocódigo del flow desde mensaje del user hasta respuesta citando fuentes
- `observability.md` — qué loguear de cada retrieval (tabla `rag_queries`, dashboards)
- `rerank-decision.md` — si se activa Cohere Rerank (después de medir precisión en producción)

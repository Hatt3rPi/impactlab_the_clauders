---
title: Reuniones
description: Índice cronológico de reuniones del equipo (transcripciones + resúmenes ejecutivos).
tags:
  - reuniones
---

# Reuniones

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../convenciones-de-contenido.md).

Cada reunión queda **versionada en el repo**: transcripción cruda + resumen ejecutivo + decisiones + acciones.

## Cómo registrar una reunión

1. Copiar [`_template.md`](_template.md) a `docs/reuniones/YYYY-MM-DD-titulo-corto.md`.
2. Llenar las secciones (TL;DR, decisiones, acciones, transcripción).
3. Sumar la fila al [índice](#indice-cronologico) de abajo.
4. Si la reunión generó decisiones técnicas relevantes, crear el [ADR](../tu-plata-mipyme/especificaciones/adrs/index.md) correspondiente.

## Convenciones

- **Resumen ejecutivo arriba**, transcripción cruda abajo en `<details>` colapsable.
- **Acciones con responsable y fecha** (formato `[ ] @persona — acción — YYYY-MM-DD`).
- Tagear la reunión con `kickoff`, `seleccion-idea`, `tech-spike`, `retro`, etc.

## Índice cronológico

| Fecha | Título | Tipo | Decisiones clave | Link |
|---|---|---|---|---|
| 2026-04-29 | Definición de problema y setup del hackathon | kickoff | Línea: inclusión financiera · Plataforma: web mobile-first · Roles asumidos | [Ver](2026-04-29-definicion-problema-setup.md) |
| 2026-04-30 | Revisión de dolores E0-E3 + decisiones de backlog | diseño-producto | 21 features ✅ · 6 ❌ · 1 💡 · 32 ⏳ · E2 (formalización) es el fuerte · Pendiente: confirmar freemium con organización | [Ver](2026-04-30-revision-dolores-backlog.md) |

## Acciones abiertas (vivas)

> Idealmente sincronizadas con cada reunión. Mover a "cerradas" cuando se completen.

- [ ] @Equipo — **Validar propuesta de [hoja de ruta](../equipo/proceso-y-hoja-de-ruta.md)** (3 etapas + 2 tollgates) en reunión de hoy 21:00
- [ ] @Equipo — **Tollgate 1**: cerrar problema/segmento y aprobar PRD — objetivo hoy o mañana
- [ ] @Jose — Compartir research inicial (cruce CMF + Impact Lab) en el repo — 2026-04-29
- [ ] @Todos — Centralizar links y fuentes en el repo — continuo
- [ ] @Todos — Diseñar proceso de validación con usuarios vía redes sociales — esta semana
- [ ] @Equipo — **Tollgate 2**: arquitectura + stack definidos antes del 5 de mayo
- [ ] @Equipo — MVP testeado antes del kickoff del lab — 2026-05-06

## Acciones cerradas

- [x] @Felipe — Montar repositorio/wiki como fuente de la verdad (2026-04-29)
- [x] @Jose — Armar hoja de ruta con etapas e hitos (audio + diagrama 2026-04-29 → [propuesta registrada](../equipo/proceso-y-hoja-de-ruta.md))
- [x] @Todos — Levantamiento individual reemplazado por incorporación de research previo + 9 ideas pre-evaluadas (2026-04-29)

---
title: "Tu Plata Mipyme"
description: "Hub central del producto — copiloto freemium en WhatsApp + Web para acompañar al microemprendedor chileno desde el sueño hasta la PYME."
tags:
  - tu-plata-mipyme
  - hub
  - producto
---

# 🚀 Tu Plata Mipyme

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Hub central de la idea ganadora del equipo The Clauders para el Claude Impact Lab Chile 2026.

> **Tu Plata Mipyme** es un copiloto freemium en WhatsApp + Web que acompaña al microemprendedor chileno desde el sueño hasta la PYME, con agentes IA especializados por etapa que hablan en su idioma y citan la norma.

**Target prioritario:** mujeres microemprendedoras 30-50 años en regiones del sur de Chile (Araucanía 38% informalidad · 59% mujeres informales según EME8). Universo: ~1,08M microemprendedores informales.

---

## Tabla de contenidos

### Documentos principales

| Doc | Qué contiene |
|---|---|
| [PRD](PRD.md) | Documento de Requerimiento de Producto consolidado — frame de negocio, alcance, RF priorizados, CA, supuestos, riesgos |
| [PITCH](PITCH.md) | Material de pitch para el Claude Impact Lab Chile 2026 — 10 slides ejecutivos derivados del PRD, listos para presentación al jurado |
| [Qué es y para quién](que-es.md) | Definición canónica, tiers (Free/Pro/Plus/Marketplace), segmentos, qué hace y qué NO hace |
| [**Dolores del journey**](dolores.md) | 48 dolores documentados E0-E5 con 5 puntos cada uno (cómo se resuelve hoy, costo, tiempo, fracaso, brecha IA) + decisión literal del equipo |
| [Plan de implementación](plan.md) | Arquitectura multi-agente (1 supervisor + 4 subagentes), stack, principios duros, KPIs, roadmap 4 fases |
| [Backlog (60 features)](backlog.md) | Catálogo categorizado E0-E5, escenarios de usuario, decisiones del equipo (✅/❌/💡/⏳) |

### Definiciones del producto

- [Glosario](definiciones/glosario.md) — términos del producto y del concurso.
- [Stakeholders](definiciones/stakeholders.md) — actores impactados.
- [Personas](definiciones/personas.md) — arquetipos de usuario.

### Especificaciones técnicas

- [Arquitectura](especificaciones/arquitectura.md) — diseño técnico end-to-end.
- [Prototipo](especificaciones/prototipo.md) — demo interactiva.
- [Stack tecnológico](especificaciones/stack/index.md) — Claude API, Claude Code, Agent SDK, MCPs, datasets, infraestructura.
- [Decisiones (ADRs)](especificaciones/adrs/index.md) — 4 ADRs registrados:
    - `0001` Uso de ADRs · `0002` Línea temática · `0003` Plataforma web · **`0004` WhatsApp-first / freemium / multi-agente** (decisión central).

---

## Estado del backlog (revisión equipo 30-abr-2026)

| Estado | Cantidad |
|---|---|
| ✅ Incluir | **21 features** |
| ❌ Excluir | 6 features |
| 💡 Guiño / futuro | 1 feature (INAPI) |
| ⏳ Pendiente revisión | 32 features (E3 incompleto + E4 + E5) |

**Etapa más madura:** E2 — Formalización (11 de 12 incluidas). El equipo declaró: *"es nuestro fuerte hasta el momento."*

Detalle por etapa: ver [backlog.md](backlog.md).

---

## Decisiones globales tomadas

1. **Canal:** WhatsApp principal + Web complementaria. Telegram fuera.
2. **Modelo:** freemium con triggers contextuales (Free / Pro ~$4.990 CLP/mes / Plus $15-30K / Marketplace 10-15% comisión). **Pendiente confirmar** con la organización si el lab requiere gratuidad total.
3. **Arquitectura:** 1 supervisor + 4 subagentes (mentor-inicio, acompañante-informal, gestor-formalización, estratega-crecimiento).
4. **Riesgo de alucinación:** la IA NO hace cálculos numéricos directos. Solo teoría + rango + disclaimer.
5. **Open Banking:** llega 07/2027. Para el lab: reenvío de correos + cartolas mensuales como contexto.

---

## Próximos hitos

- Completar revisión de etapas E3 (D4-D8), E4 y E5 con el equipo (32 features pendientes).
- Confirmar modelo de negocio con la organización del lab.
- Definir paleta visual (Anahi).
- Spike técnico del supervisor multi-agente.
- Demo script para el lab (6-7 mayo 2026).

## Referencias

- [Reuniones del equipo](../reuniones/index.md) — actas de decisiones.
- [Competencia / concurso](../competencia/index.md) — info del Claude Impact Lab Chile 2026.
- [Equipo](../equipo/miembros.md) — quiénes somos y cómo trabajamos.

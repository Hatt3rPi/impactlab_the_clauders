---
title: Especificaciones técnicas
description: Visión técnica del prototipo, arquitectura y decisiones registradas.
tags:
  - especificaciones
---

# Especificaciones técnicas

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../../convenciones-de-contenido.md).

Esta sección **se llena cuando se decida la idea**. Mientras tanto, estructura lista para recibir contenido.

## Contenido

- [**Arquitectura**](arquitectura.md) — diagrama de componentes, flujos, integraciones.
- [**Prototipo**](prototipo.md) — alcance funcional: qué hace, qué no hace, criterios de aceptación.
- [**ADRs**](adrs/index.md) — Architecture Decision Records: por qué tomamos cada decisión.

## Cuándo llenar cada parte

| Sección | Cuándo |
|---|---|
| Arquitectura | Después de elegir idea + stack base |
| Prototipo | Después de elegir idea (alcance) y antes de codear |
| ADRs | Cada vez que se tome una decisión técnica relevante |

## Convenciones

- **Diagramas** en mermaid (renderizan en MkDocs Material).
- **ADRs** son inmutables: si cambias una decisión, escribes un ADR nuevo que **supersede** al anterior.
- Toda decisión que afecte a más de una persona se documenta.

---
title: Convenciones de contenido
description: Cómo distinguir entre plantilla, síntesis, contenido del equipo e info oficial.
tags:
  - convenciones
  - guia
---

# Convenciones de contenido

Cada página de la wiki nace con uno de **4 estados**, identificado con un *banner* de color al inicio del archivo:

| Banner | Significado | Cuándo aparece |
|---|---|---|
| :material-toy-brick: **Plantilla / esqueleto** | Estructura inicial sin contenido del equipo. **Hay que llenarla o reemplazarla.** | Cuando creé el árbol de carpetas inicial y dejé un esqueleto a llenar (ej: `personas.md`, `roles.md`, índices vacíos). |
| :material-book-open-variant: **Síntesis de fuentes externas** | Resumen estructurado de **fuentes externas** (PDFs, HTMLs, sitios web). Verificar cifras antes de citarlas en el pitch. | Cuando hay un documento original en `docs/assets/` que es la fuente de verdad. |
| :material-check-bold: **Producido por el equipo** | Acta, decisión o documento **generado por el equipo**. Es la fuente primaria para ese tema. | Reuniones, ADRs aprobados, propuestas formales internas. |
| :material-bank: **Información oficial del lab** | Datos extraídos del **sitio oficial** del Claude Impact Lab Chile 2026. | Páginas en `competencia/` y todo lo que reproduce reglas, criterios, premios o líneas oficiales. |

## Cómo se ve

Cada banner es una *admonition* al inicio del archivo, justo después del título:

!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura inicial sin datos del equipo. Reemplazar antes de citar.

!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Sintetizado a partir de [Fuente original](#). Verificar cifras antes de citar en el pitch.

!!! success ":material-check-bold: Producido por el equipo"
    Aprobado en [reunión / ADR / decisión].

!!! note ":material-bank: Información oficial del lab"
    Fuente: sitio oficial del Claude Impact Lab Chile 2026.

## Reglas de uso

1. **Toda página nueva** debe abrir con uno de los 4 banners.
2. Si una página **muta de estado** (ej: una plantilla se llena con datos reales del equipo), se actualiza el banner.
3. Las **plantillas** (`_template.md`) siempre llevan el banner naranjo.
4. Si una página combina contenido de varias fuentes, gana el de **mayor compromiso** (equipo > síntesis > oficial > plantilla).
5. Cuando una página de síntesis se basa en un documento, el banner cita ese documento explícitamente.

## Cómo aplicar el banner

Pegar el bloque al **inicio del cuerpo**, justo debajo del `# Título`:

```markdown
---
title: ...
---

# Título de la página

!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura inicial sin datos del equipo. Reemplazar antes de citar.

(...contenido...)
```

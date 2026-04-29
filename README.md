# The Clauders — Wiki del equipo

Wiki interna del equipo **The Clauders** para el [Claude Impact Lab Chile 2026 — *El puente al ciudadano*](https://fintech.benditaia.cl/es) (Anthropic + BenditaIA + FinteChile, 6-7 de mayo de 2026, Espacio Riesco).

> **Sitio publicado:** <https://theclauders.netlify.app>

Este repositorio contiene research, ideas, definiciones, stack técnico, especificaciones y transcripciones de reuniones del equipo. Está construido con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Cómo usarla (la forma simple)

Tú **no escribes Markdown**. Conectas el repositorio a un agente IA y le pides cosas en lenguaje natural:

> *"Te dejo la transcripción de la reunión de hoy, súbela y actualiza el tablero de ideas según lo que decidimos."*
>
> *"Acá hay un PDF con un research de mercado, incorpóralo donde corresponda."*
>
> *"Decidimos cambiar el stack a Astro, registra el ADR."*
>
> *"¿Qué quedó pendiente del último kickoff?"*

El agente lee la wiki entera, decide dónde va cada cosa (acta de reunión, ficha de idea, ADR, nota de research, etc.), respeta las [convenciones de contenido](docs/convenciones-de-contenido.md) y actualiza tanto el archivo nuevo como los índices, navegación y referencias cruzadas. Tú solo revisas el commit.

### Opción A — Claude Code (recomendado)

[Claude Code](https://claude.com/claude-code) es la CLI/IDE oficial de Anthropic.

1. Instalar Claude Code en tu máquina.
2. `cd` al repo clonado y abrir Claude Code.
3. Pedirle al agente lo que necesites en lenguaje natural. Él se encarga de leer la estructura, editar los archivos correctos, hacer build local para verificar y commitear/pushear (este equipo opera en modo proactivo, así no preguntará para cada commit).

### Opción B — Cowork

Si el equipo prefiere [Cowork](https://cowork.io/) u otra herramienta agéntica con acceso a GitHub, conectar el repo y pedirle lo mismo en lenguaje natural. La idea es la misma: tú dictas en español, el agente edita la wiki y hace commit.

### Opción C — Markdown a mano (fallback)

Si quieres editar directo los `.md`:

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve  # → http://localhost:8000
```

Si agregas una página nueva, súmala al `nav` en `mkdocs.yml`. Para reuniones, ideas o ADRs nuevos, copia la `_template.md` correspondiente. Commit a `main` y la wiki se redespliega sola.

## Estructura

```
docs/
├── competencia/        Información oficial del lab
├── lineas-tematicas/   Las 3 líneas posibles
├── ideas/              Tablero de ideas con scoring
├── research/           Notas de investigación (regulatorio, usuarios, mercado, tech)
├── definiciones/       Glosario, stakeholders, personas
├── stack/              Claude API, Agent SDK, MCPs, datasets
├── especificaciones/   Arquitectura, prototipo, ADRs
├── reuniones/          Transcripciones + resúmenes ejecutivos
├── equipo/             Miembros, roles, ways of working
└── recursos/           Enlaces, mentores, workshops
```

Cada sección tiene su propio `index.md` y, donde aplica, un archivo `_template.md`.

## Convenciones de contenido

Cada página abre con un **banner** que indica su origen: plantilla, síntesis de fuente externa, producido por el equipo, o información oficial del lab. Detalle en [`docs/convenciones-de-contenido.md`](docs/convenciones-de-contenido.md).

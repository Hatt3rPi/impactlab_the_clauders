# The Clauders — Wiki del equipo

Wiki interna del equipo **The Clauders** para el [Claude Impact Lab Chile 2026 — *El puente al ciudadano*](https://fintech.benditaia.cl/es) (Anthropic + BenditaIA + FinteChile, 6-7 de mayo de 2026, Espacio Riesco).

> **Sitio publicado:** <https://theclauders.netlify.app>

Este repositorio contiene research, ideas, definiciones, stack técnico, especificaciones y transcripciones de reuniones del equipo durante la fase de exploración y el lab. Está construido con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) y desplegado en [Netlify](https://www.netlify.com/).

## Quickstart local

```bash
# 1. Crear entorno virtual (opcional pero recomendado)
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows PowerShell

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Levantar servidor de desarrollo con hot-reload
mkdocs serve
# → abrir http://localhost:8000

# 4. (Opcional) Generar el sitio estático
mkdocs build
```

## Estructura

```
docs/
├── competencia/        Información oficial del lab
├── lineas-tematicas/   Las 3 líneas posibles (en exploración)
├── ideas/              Tablero de ideas con scoring
├── research/           Notas de investigación (regulatorio, usuarios, mercado, tech)
├── definiciones/       Glosario, stakeholders, personas
├── stack/              Claude API, Agent SDK, MCPs, datasets
├── especificaciones/   Arquitectura, prototipo, ADRs
├── reuniones/          Transcripciones + resúmenes ejecutivos
├── equipo/             Miembros, roles, ways of working
└── recursos/           Enlaces, mentores, workshops
```

Cada sección tiene su propio `index.md` y, donde aplica, un archivo `_template.md` con la plantilla a copiar.

## Despliegue (Netlify)

El sitio se publica automáticamente en Netlify en cada push a `main`. La configuración vive en [`netlify.toml`](netlify.toml) y `runtime.txt`.

### Setup inicial (una sola vez)

1. Ir a <https://app.netlify.com/> y conectar la cuenta con GitHub.
2. **Add new site → Import an existing project → GitHub →** seleccionar `Hatt3rPi/impactlab_the_clauders`.
3. Netlify lee `netlify.toml` y completa los campos:
    - **Build command:** `pip install -r requirements.txt && mkdocs build`
    - **Publish directory:** `site`
    - **Python version:** 3.12 (vía `runtime.txt` y `PYTHON_VERSION`)
4. **Deploy site.** El primer build tarda ~1 min.
5. (Opcional) **Site settings → Change site name** para personalizar la URL `*.netlify.app`.
6. (Opcional) **Domain management** para apuntar un dominio propio.

### Después

Cada `git push` a `main` dispara un build en Netlify. Los logs y el historial quedan en el dashboard del sitio.

## Cómo contribuir

1. Crea o edita el archivo dentro de `docs/`.
2. Si agregas una página nueva, súmala al `nav` en `mkdocs.yml`.
3. Para reuniones e ideas nuevas, copia la plantilla `_template.md` correspondiente.
4. Commit + push a `main`. El sitio se redespliega automáticamente.

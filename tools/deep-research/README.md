# Deep Research — herramientas del equipo

Cliente Python para invocar el modelo `deep-research-max-preview-04-2026` de Google y guardar los reportes citados directamente en la wiki bajo `docs/research/_runs-deep-research/`.

> **Esto es pre-trabajo del equipo, NO parte del producto del lab.** El demo del 7 de mayo invoca Claude (no Gemini), o sacrificas el bonus de *Claude & Agentic Thinking*.
>
> Documentación operativa de la API: [docs/research/herramientas/deep-research-google.md](../../docs/research/herramientas/deep-research-google.md).

## Setup (una sola vez)

1. **Obtén una API key** en <https://aistudio.google.com/apikey>. Necesitas un proyecto con **billing habilitado** — Deep Research está en *paid tiers*, no hay free tier.

2. **Configura el `.env`** del cliente:

    ```bash
    cd tools/deep-research
    cp .env.example .env
    # editar .env y pegar tu GEMINI_API_KEY
    ```

3. **Instala dependencias:**

    ```bash
    pip install -r tools/deep-research/requirements.txt
    ```

4. **Verifica:**

    ```bash
    python tools/deep-research/run.py --list
    ```

    Debe imprimir los 5 prompts disponibles.

## Uso

**Correr un solo prompt:**

```bash
python tools/deep-research/run.py 01-ideas-fuera-del-radar
```

**Correr varios:**

```bash
python tools/deep-research/run.py 01-ideas-fuera-del-radar 04-money-left-on-the-table
```

**Correr los 5 secuencialmente:**

```bash
python tools/deep-research/run.py --all
```

> Cada task tarda 5-20 minutos. Si corres `--all`, son ~1-2 horas en total. Puedes dejarlo en background y volver a revisar.

## Costos

| Modelo | Por tarea (estimado) | 5 tareas |
|---|---|---|
| Standard | USD 1-3 | USD 5-15 |
| **Max** (default del cliente) | USD 3-7 | **USD 15-35** |

El cliente usa `deep-research-max-preview-04-2026` por defecto (mayor profundidad). Si quieres ahorrar, modifica `DEFAULT_AGENT` en `client.py`.

## Qué pasa cuando corres un prompt

1. El cliente lee el archivo `prompts/<slug>.md` (frontmatter + cuerpo).
2. Lanza un task asíncrono con `background=True`.
3. Hace polling cada 10 s hasta que el status sea `completed` o `failed`.
4. Imprime el `interaction_id` y heartbeats por consola.
5. Al completar, guarda el resultado en `docs/research/_runs-deep-research/YYYY-MM-DD-<slug>.md` con:
    - Frontmatter completo (categoría, fecha, autor = modelo + ID).
    - Banner *"síntesis de fuente externa"* siguiendo las [convenciones](../../docs/convenciones-de-contenido.md).
    - Cuerpo del reporte.
    - Citaciones al final.
    - Imágenes/visualizaciones embebidas en `docs/assets/research/deep-research-runs/`.

Todo queda navegable desde la wiki y commiteable a git.

## Estructura

```
tools/deep-research/
├── README.md              # este archivo
├── client.py              # cliente reusable
├── run.py                 # wrapper CLI
├── requirements.txt       # google-genai + python-dotenv
├── .env.example           # plantilla de credenciales
├── .env                   # (ignorado por git) credenciales reales
└── prompts/
    ├── 01-ideas-fuera-del-radar.md
    ├── 02-ganadores-hackathons-fintech-ia.md
    ├── 03-datasets-chilenos-subutilizados.md
    ├── 04-money-left-on-the-table.md
    └── 05-canales-distribucion-confianza.md
```

## Editar / agregar prompts

Cada prompt es un archivo `.md` con frontmatter:

```markdown
---
titulo: "Título corto del prompt"
objetivo: "Una frase de qué buscamos"
agent: "deep-research-max-preview-04-2026"
linea: inclusion-financiera
prioridad: alto
---

# Prompt: ...

(cuerpo del prompt; el cliente envía todo lo que está después del frontmatter)
```

El **slug** del archivo (`NN-nombre.md`) es lo que pasas como argumento a `run.py`.

## Buenas prácticas

- **Antes de correr un prompt costoso (Max)**, lee el cuerpo del `.md` y ajusta cualquier detalle que esté desactualizado.
- **Si vas a correr `--all`**, asegúrate de tener cuota suficiente en Google Cloud (USD 35-50 en créditos disponibles).
- **Después de correr, revisa los outputs** antes de promover hallazgos a notas estructuradas en `docs/research/<categoria>/`.
- **Las citaciones del agente NO son verdad automática** — el agente puede citar fuentes secundarias. Verifica antes de poner cifras en el pitch.
- **Si un prompt falla** (status = `failed`), el `interaction_id` aparece en consola; puedes investigar el error desde Google AI Studio.

## Cómo se relaciona esto con el resto del repo

- Documentación de la API: `docs/research/herramientas/deep-research-google.md`.
- Outputs versionados: `docs/research/_runs-deep-research/`.
- Imágenes generadas: `docs/assets/research/deep-research-runs/`.
- Convenciones de contenido (banners por origen): `docs/convenciones-de-contenido.md`.

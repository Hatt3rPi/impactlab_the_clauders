---
title: "Deep Research API de Google (Gemini Interactions)"
description: "Documentación operativa para invocar deep-research-max-preview-04-2026 desde el equipo en fase exploratoria."
autor: "Síntesis sobre documentación oficial Google AI for Developers"
fecha: 2026-04-29
categoria: tecnologia
linea: transversal
tags:
  - research
  - tecnologia
  - herramientas
  - deep-research
  - google
  - gemini
---

# Deep Research API de Google — guía operativa

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Sintetizado a partir de la documentación oficial: [Deep Research (es-419)](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) · [Deep Research (en)](https://ai.google.dev/gemini-api/docs/deep-research) · [Deep Research Max model card](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026). Verificar pricing y rate limits antes de operar (preview, sujeto a cambios).

> **Para qué sirve esto en nuestro proyecto.** Deep Research Max es un agente asíncrono de Google que ejecuta hasta 160 queries de búsqueda con grounding y devuelve un reporte citado. Lo usamos **únicamente como pre-trabajo del equipo** para llenar gaps de research específicos. **No es parte del producto del lab** — el demo del 7 de mayo invoca Claude, no Gemini, o sacrificas el bonus de *Claude & Agentic Thinking*. Ver [ADR 0002](../../../tu-plata-mipyme/especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md).

## TL;DR operativo

| Concepto | Valor |
|---|---|
| **Modelo** | `deep-research-max-preview-04-2026` (versión Max, recomendada para nosotros) |
| **API** | [Interactions API](https://generativelanguage.googleapis.com/v1beta/interactions) — async, no `generate_content` |
| **Auth** | API key de [Google AI Studio](https://aistudio.google.com/apikey) en header `x-goog-api-key` |
| **Modo obligatorio** | `background=True` |
| **Tiempo de un task** | 5-20 min típico, **60 min máximo** |
| **Costo Max** | **USD 3-7 por tarea** (estimado preview) |
| **Tokens Max** | ~900k input, ~80k output, ~160 queries de búsqueda |
| **Tools default activos** | Google Search + URL Context + Code Execution |
| **Tools adicionales** | MCP servers, File Search |
| **Output** | Reporte de texto citado + imágenes/charts en base64 |
| **Multimodal input** | Texto, imagen, PDF, audio, video |
| **Idiomas** | Español, inglés y otros (Gemini 3.1 Pro multilingüe) |

## Modelos disponibles

| Modelo | Diseño | Queries | Input tokens | Output tokens | Costo/task |
|---|---|---|---|---|---|
| `deep-research-preview-04-2026` | Velocidad / streaming | ~80 | ~250k | ~60k | USD 1-3 |
| `deep-research-max-preview-04-2026` | Exhaustividad | ~160 | ~900k | ~80k | USD 3-7 |

> **Nuestra elección:** `deep-research-max-preview-04-2026`. Para los 5 prompts dirigidos del Discovery, la diferencia de costo es despreciable (~USD 25 totales) y la profundidad importa.

## Autenticación

1. Crear API key en <https://aistudio.google.com/apikey>.
2. Asociar a un proyecto con **billing habilitado** — Deep Research está en *paid tiers* únicamente.
3. Guardar en variable de entorno `GEMINI_API_KEY`.
4. Pasarla en header `x-goog-api-key: $GEMINI_API_KEY` o configurarla en el SDK.

> **Nunca** commitear la API key al repo. El [`tools/deep-research/.env.example`](#) muestra el formato esperado y `.gitignore` excluye `.env`.

## Endpoint y autenticación

```
POST https://generativelanguage.googleapis.com/v1beta/interactions
GET  https://generativelanguage.googleapis.com/v1beta/interactions/{interaction_id}
```

Header obligatorio: `x-goog-api-key: $GEMINI_API_KEY`.

## Parámetros del request

| Parámetro | Tipo | Requerido | Descripción |
|---|---|---|---|
| `agent` | string | sí | `deep-research-max-preview-04-2026` |
| `input` | string \| array | sí | Texto del prompt o array multimodal |
| `background` | boolean | sí | **Debe ser `true`** para Deep Research |
| `stream` | boolean | no | `true` para streaming en vivo |
| `previous_interaction_id` | string | no | Para follow-ups o aprobar plan |
| `agent_config` | object | no | Ver abajo |
| `tools` | array | no | Override de tools default |

### `agent_config`

```python
{
    "type": "deep-research",
    "thinking_summaries": "auto",       # "auto" | "none". Default: "none"
    "visualization": "auto",            # "auto" | "off". Default: "auto"
    "collaborative_planning": False     # true habilita revisión de plan antes de ejecutar
}
```

> Para nuestros prompts, **conviene activar `thinking_summaries: "auto"`** — vemos los pasos del agente y sirve como input adicional para el equipo. `collaborative_planning: True` es útil cuando queremos revisar el plan antes de gastar los $5 (recomendado para prompts complejos).

## Tools

### Default (activas automáticamente)

```python
tools = [
    {"type": "google_search"},     # Grounding con la web pública
    {"type": "url_context"},       # Lee y resume páginas específicas
    {"type": "code_execution"},    # Ejecuta código para análisis cuantitativo
]
```

### Opcionales

**MCP server:**
```python
{
    "type": "mcp_server",
    "name": "Nombre",
    "url": "https://mcp.example.com/mcp",
    "headers": {"Authorization": "Bearer token"},
    "allowed_tools": ["tool1"]   # opcional, restringe qué tools del MCP usa
}
```

**File Search** (subir corpus propio antes y referenciar):
```python
{
    "type": "file_search",
    "file_search_store_names": ["fileSearchStores/mi-store"]
}
```

> Para nuestro caso, la combinación `google_search + url_context + code_execution` (default) es suficiente. **No** subimos a File Search los PDFs internos del equipo (estrategia, deep research) — son input que va en el prompt, no corpus consultable.

## Polling vs streaming

### Polling (recomendado para batch)

```python
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    input="<prompt aquí>",
    agent="deep-research-max-preview-04-2026",
    background=True,
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
)

while True:
    result = client.interactions.get(interaction.id)
    if result.status == "completed":
        print(result.outputs[-1].text)
        break
    elif result.status == "failed":
        raise RuntimeError(f"Falló: {result.error}")
    time.sleep(10)  # 5-10 s recomendado
```

### Streaming (para UI en vivo)

```python
stream = client.interactions.create(
    input="<prompt>",
    agent="deep-research-max-preview-04-2026",
    background=True,
    stream=True,
    agent_config={"type": "deep-research", "thinking_summaries": "auto"}
)
for event in stream:
    # event.type ∈ {"interaction.start", "content.delta", "interaction.complete", "error"}
    # event.delta_type ∈ {"thought_summary", "text", "image"}
    ...
```

**Reconexión tras desconexión** (importante para tasks largos):
```python
client.interactions.get(
    id=interaction_id,
    stream=True,
    last_event_id=last_event_id   # guardado del stream previo
)
```

## Estados del task

| Status | Significado |
|---|---|
| `in_progress` | Corriendo |
| `completed` | OK; ver `outputs` y `citations` |
| `failed` | Error; ver `error` |

## Formato de la respuesta

```json
{
    "id": "interaction-uuid",
    "status": "completed",
    "outputs": [
        { "type": "text", "text": "Reporte..." },
        { "type": "image", "data": "<base64>" }
    ],
    "citations": ["https://...", "https://..."]
}
```

## Multimodal input

```python
input = [
    {"type": "text", "text": "Analiza este documento y compáralo con..."},
    {"type": "document", "uri": "https://gov.cl/...", "mime_type": "application/pdf"},
    {"type": "image", "uri": "https://..."},
]
```

## Collaborative planning (recomendado para prompts caros)

Permite revisar el plan **antes** de ejecutar las 160 queries (no gastas los $5 si el plan es malo).

```python
# 1. Pedir plan
plan = client.interactions.create(
    input="<prompt>",
    agent="deep-research-max-preview-04-2026",
    background=True,
    agent_config={"type": "deep-research", "collaborative_planning": True}
)

# 2. (Opcional) Refinar plan
refined = client.interactions.create(
    input="Enfócate en X, omite Y",
    agent="deep-research-max-preview-04-2026",
    background=True,
    agent_config={"type": "deep-research", "collaborative_planning": True},
    previous_interaction_id=plan.id
)

# 3. Aprobar y ejecutar
final = client.interactions.create(
    input="El plan está bien, ejecuta",
    agent="deep-research-max-preview-04-2026",
    background=True,
    agent_config={"type": "deep-research", "collaborative_planning": False},
    previous_interaction_id=refined.id
)
```

## Límites y constraints

| Límite | Valor |
|---|---|
| Tiempo máximo de un task | **60 minutos** |
| Tiempo típico | 5-20 minutos |
| `background` | **Obligatorio `true`** para Deep Research |
| `store` | Implícito en `background=true` (tasks persistidos) |
| Function Calling custom | **No soportado** (usar MCP en su lugar) |
| Structured outputs | **No soportado** |
| Beta status | Sí — schemas pueden cambiar |

## Manejo de errores

```python
result = client.interactions.get(interaction.id)
if result.status == "failed":
    # result.error contiene el mensaje
    ...
```

Errores comunes:

- **API key inválida o sin billing** → 401/403.
- **Rate limit** → 429 (preview tier, sin límites publicados).
- **Stream desconectado** → reconectar con `last_event_id`.
- **Task superó 60 min** → status `failed`.

## Consideraciones de seguridad (importantes)

> Citado de la documentación oficial:

- **Risk de inyección por archivo:** documentos maliciosos pueden contener texto oculto que manipule el output. Validar fuentes antes de subirlas.
- **Filtrado de contenido web:** el agente accede a la web pública. Revisar citaciones antes de tomar decisiones.
- **Exfiltración de datos:** no combinar datos sensibles internos con browsing web sin entender el flujo.

Para nuestro caso (research público sobre Chile), el riesgo es bajo. Pero **nunca** poner cifras sensibles del equipo en el prompt.

## Mejores prácticas (resumen Google)

1. **Indica al agente cómo manejar lo desconocido** — "si no encuentras dato oficial, di 'sin fuente verificable'".
2. **Da contexto de fondo en el prompt** — restricciones, alcance, audiencia esperada del reporte.
3. **Usa collaborative planning** para prompts complejos antes de gastar.
4. **Verifica citaciones** — el agente puede citar fuentes secundarias; rastrea hasta la primaria.
5. **Monitorea costos** — Max es ~3× Standard.

## Cómo lo operamos en este proyecto

- **Quien ejecuta:** Felipe (mientras no esté construyendo el producto).
- **Cuándo:** ahora, antes del Tollgate 1.
- **Cliente:** [`tools/deep-research/client.py`](https://github.com/Hatt3rPi/impactlab_the_clauders/tree/main/tools/deep-research) en el repo (no aparece en la wiki porque vive fuera de `docs/`).
- **Prompts:** [`tools/deep-research/prompts/`](https://github.com/Hatt3rPi/impactlab_the_clauders/tree/main/tools/deep-research/prompts), versionados en git para trazabilidad.
- **Outputs:** se guardan automáticamente en `docs/research/_runs-deep-research/YYYY-MM-DD-NN-slug.md` con frontmatter completo y banner de "síntesis de fuente externa". Quedan navegables desde la wiki.
- **Costo estimado total:** USD 25-30 por los 5 prompts iniciales.

## Próximos pasos

1. Felipe configura `tools/deep-research/.env` con su `GEMINI_API_KEY`.
2. Corre `python tools/deep-research/run.py 01-ideas-fuera-del-radar` (o todos en paralelo en background).
3. Mientras corre, sigue con su trabajo. Cada task tarda 10-20 min.
4. Al terminar, los outputs aparecen en `docs/research/_runs-deep-research/` listos para revisar y eventualmente promover a notas estructuradas.
5. Reunión corta del equipo (30 min) para revisar los outputs juntos antes del Tollgate 1.

## Referencias

- [Deep Research overview (es-419)](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419)
- [Deep Research overview (en)](https://ai.google.dev/gemini-api/docs/deep-research)
- [Deep Research Max model card](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026)
- [Deep Research preview model card](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026)
- [Cookbook (notebook Colab)](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_Deep_Research.ipynb)
- [Pricing oficial](https://ai.google.dev/gemini-api/docs/pricing)
- [Anuncio del lanzamiento](https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/)

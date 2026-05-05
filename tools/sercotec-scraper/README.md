# Sercotec scraper — postulaciones abiertas

Extrae las convocatorias activas en `https://www.sercotec.cl/postulaciones-abiertas/`
y las guarda en CSV + JSON con: nombre, fecha de inicio, fecha de cierre, región,
link directo y requisitos.

Hay **dos implementaciones**:

| Script                  | Discovery                              | Engine     | Cuándo usar                                                            |
| ----------------------- | -------------------------------------- | ---------- | ---------------------------------------------------------------------- |
| `scraper.py`            | sitemap_index.xml + parse HTML         | requests   | Rápido, sin browser. Buen default para CI / cron.                      |
| `scraper_playwright.py` | Render del iframe widget (Next.js)     | Playwright | Refleja exactamente lo que ve el usuario en /postulaciones-abiertas/.  |

## Setup

```bash
pip install -r tools/sercotec-scraper/requirements.txt
# Solo si vas a usar scraper_playwright.py:
playwright install chromium
```

`selenium` solo es necesario si pasas `--selenium` a `scraper.py`. `playwright`
solo si usas `scraper_playwright.py`.

## Uso

### A) `scraper.py` (requests + sitemap)

```bash
# Default: discovery vía sitemap + parser HTTP
python tools/sercotec-scraper/scraper.py

# Limitar (debug)
python tools/sercotec-scraper/scraper.py --limit 5

# Forzar Selenium (requiere Chrome + chromedriver en PATH)
python tools/sercotec-scraper/scraper.py --selenium

# Procesar URLs específicas (sin discovery)
python tools/sercotec-scraper/scraper.py \
  --seed https://www.sercotec.cl/convocatoria/capital-semilla-emprende-region-de-nuble-2026/

# Cambiar output
python tools/sercotec-scraper/scraper.py --out outputs/2026-05-postulaciones.csv
```

Outputs: `outputs/postulaciones.csv` (separador `;`, BOM UTF-8 para Excel CL)
y `outputs/postulaciones.json`.

### B) `scraper_playwright.py` (Playwright + iframe widget)

```bash
# Default (headless)
python tools/sercotec-scraper/scraper_playwright.py

# Ver el browser (debug visual)
python tools/sercotec-scraper/scraper_playwright.py --headed

# Limitar
python tools/sercotec-scraper/scraper_playwright.py --limit 5

# Volcar HTML renderizado del widget para inspección
python tools/sercotec-scraper/scraper_playwright.py --debug

# Cambiar output
python tools/sercotec-scraper/scraper_playwright.py --out outputs/postulaciones_pw.csv
```

Outputs: `outputs/postulaciones_pw.csv` y `outputs/postulaciones_pw.json` con
columnas: `nombre, fecha_inicio, fecha_cierre, region, link, requisitos`
(texto plano completo, listo para enviar a un LLM).

#### Cómo funciona (resumen)

1. Playwright abre `https://sctwebwidgets.sercotec.cl/convocatorias` (el iframe
   que `/postulaciones-abiertas/` embebe; es Next.js, no se puede leer con
   `requests` plano).
2. Espera a que aparezcan los anchors `/convocatoria/`, luego ejecuta JS en el
   page para subir por el DOM y capturar nombre, fechas, región y link de cada
   card de forma resiliente a cambios de clases CSS.
3. Por cada link, baja la página de detalle con `requests` (es server-rendered,
   no requiere browser) y extrae el bloque "¿Quiénes pueden acceder?":
   - busca `<button data-bs-target="#collapseX">¿Quiénes pueden acceder?</button>`,
   - obtiene el `<div id="collapseX">` correspondiente,
   - devuelve el texto plano completo del `.accordion-body` (con saltos de línea).
   Fallback: si no hay accordion, busca `<h2>` con texto similar.

## Decisiones de diseño

### 1. Discovery — por qué sitemap y no la página listing

`/postulaciones-abiertas/` solo enlaza a páginas-paraguas de cada **programa**
(p. ej. `/capital-semilla-emprende`). Las **convocatorias** específicas con
fechas y región viven en URLs independientes con patrón
`/convocatoria/{slug}-{region}-{año}/`. Esas URLs no aparecen listadas en
ninguna página HTML pública. Sí están en el sitemap de Yoast (WordPress estándar),
así que el discovery primario es:

```
sitemap_index.xml → sub-sitemaps → URLs que contienen "/convocatoria/"
```

Fallback automático: si el sitemap falla, parsea `/postulaciones-abiertas/`
buscando enlaces `/convocatoria/` embebidos.

### 2. requests vs Selenium

Las páginas de Sercotec son **renderizadas server-side** (WordPress). `requests`
+ `BeautifulSoup` extrae todo correctamente y es ~20× más rápido que un browser
headless. Selenium queda como fallback opcional (`--selenium`) por si Sercotec
migra a SPA o agrega contenido cargado por JS.

### 3. Estrategia para "Requisitos" — la pregunta clave

Inspeccionando varias convocatorias actuales, los requisitos viven en una de
estas variantes de heading:

- `<h2>Requisitos</h2>`
- `<h2>¿Quiénes pueden acceder?</h2>` (formato Capital Semilla 2026)
- `<h2>¿Quiénes pueden postular?</h2>`
- `<h2>¿Quiénes pueden participar?</h2>`

Y el contenido siguiente puede ser `<ul>`, `<p>` o mezcla. Por eso el scraper:

1. **Extrae texto completo** del bloque entre el heading de requisitos y el
   siguiente heading del mismo nivel — no se pierde nada.
2. **Normaliza a bullets** cuando hay `<ul>/<ol>` (más útil para tablas).
3. **Clasifica cada requisito** con regex en categorías:
   - `legal` — RUT, SII, persona natural/jurídica, EIRL, formalización…
   - `financiero` — ventas, UF, deuda, previsional, tributario…
   - `demografico` — mayor de edad, género, joven…
   - `geografico` — comuna, región, residencia…
   - `proyecto` — plan de negocio, rubro, foco, idea…

   Esto sale como `categorias_requisitos` (lista) y permite filtrar
   "¿qué convocatorias exigen ser persona jurídica?" sin leer texto libre.

4. **Adjunta links a PDF de Bases** como `bases_pdf`. La web a veces resume;
   el PDF es la fuente vinculante (se recomienda revisar manualmente para
   decisiones reales).

### 4. Fechas — heurística regex

Sercotec no usa una clase CSS estable para fechas. El scraper busca etiquetas
de texto (`fecha de cierre`, `postulaciones hasta`, `desde el`, `hasta el`,
`plazo de postulación`, etc.) y captura la fecha más cercana hacia adelante
en formatos: `dd/mm/aaaa`, `dd-mm-aaaa`, o `dd de mes [de aaaa]`.

Si el año no aparece junto a la fecha (común en frases tipo "hasta el
13 de mayo"), se devuelve `dd-mm` sin año — la columna `nombre` de la
convocatoria suele incluir el año, así que el contexto se preserva.

Fechas en `No informado` → revisar el PDF de Bases enlazado.

## Estructura del output

CSV (separador `;`):

| columna                 | ejemplo                                              |
| ----------------------- | ---------------------------------------------------- |
| nombre                  | Capital Semilla Emprende Región de Ñuble 2026        |
| fecha_inicio            | 22-04-2026                                           |
| fecha_cierre            | 13-05-2026                                           |
| region                  | Ñuble                                                |
| link                    | https://www.sercotec.cl/convocatoria/…               |
| estado                  | ABIERTA / CERRADA / PRÓXIMAMENTE                     |
| categorias_requisitos   | legal\|demografico\|proyecto                         |
| bases_pdf               | https://…/Bases-…2026.pdf \| https://…recomendaciones |
| requisitos              | (texto plano con saltos `⏎`)                         |

JSON: mismo contenido + `requisitos_bullets` (lista) y `requisitos_texto`
(string con saltos de línea reales).

## Notas operativas

- Throttling: 0.8 s entre requests para no saturar Sercotec. Ajustable en
  la constante `SLEEP_BETWEEN`.
- User-Agent: Chrome desktop. Si Sercotec endurece anti-bot, considerar
  rotar UA o agregar `Referer`.
- El sitemap se cachea por Sercotec con TTL alto, así que es seguro correr
  esto cada hora.
- Para integración con dashboards: leer el JSON; el CSV está pensado para
  abrir en Excel chileno (UTF-8 BOM + `;`).

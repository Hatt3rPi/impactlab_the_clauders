# CORFO scraper — programas y convocatorias

Extrae todas las convocatorias publicadas en
`https://www.corfo.gob.cl/sites/cpp/programasyconvocatorias/` y las guarda en
CSV + JSON con: nombre, fecha de inicio, fecha de cierre, región, link directo,
estado, descripción corta y requisitos completos (texto plano listo para LLM).

## Setup

```bash
pip install -r tools/corfo-scraper/requirements.txt
```

No requiere Playwright ni Selenium — todo se obtiene desde la API pública del
sitio (`admin-ajax.php`).

## Uso

```bash
# Default: descarga todas las convocatorias
python tools/corfo-scraper/scraper.py

# Debug con pocas
python tools/corfo-scraper/scraper.py --limit 5

# Cambiar output
python tools/corfo-scraper/scraper.py --out outputs/2026-05-corfo.csv
```

Outputs: `outputs/convocatorias.csv` (separador `;`, BOM UTF-8 para Excel CL)
y `outputs/convocatorias.json`.

## Decisiones de diseño

### 1. API pública en vez de scraping del DOM

La página `/programasyconvocatorias/` no renderiza las tarjetas en el HTML
inicial: las pinta vía AJAX llamando a:

```
POST /sites/cpp/wp-admin/admin-ajax.php
  action=filter_convocatorias
  post_type=convocatoria
  nonce=<extraído del HTML del listing>
  page=<1, 2, 3, …>
```

La respuesta es JSON con dos campos: `found` (total de convocatorias) y `html`
(las cards de esa página). El nonce es público — está en una variable JS
inline (`convocatoriasAjax = { ..., "nonce": "xxx" }`) y no expira en una
sesión normal.

Esto evita Playwright/Selenium completamente y es ~20× más rápido.

> Nota: existen también endpoints REST `/wp-json/wp/v2/programa` y
> `/wp/v2/convocatoria`, pero **devuelven 403** sin autenticación. Por eso el
> camino válido es `admin-ajax.php`.

### 2. Paginación

`convocatorias-filters.js` usa `pageLength: 10`. El scraper itera `page=1,2,…`
hasta acumular `found` resultados (con tope de seguridad de 200 páginas).

### 3. Cards — selectores estables

Cada card en el HTML del AJAX tiene esta estructura:

```html
<div class="caja-resultados_uno">
  <h4>NOMBRE DE LA CONVOCATORIA</h4>
  <div class="apertura"><span> 04/05/2026 </span></div>
  <div class="cierre"><span> 04/06/2026 </span></div>
  <h5><em>Alcance: Metropolitana</em></h5>
  <h6>Estado: Abiertas</h6>
  <p>descripción corta…</p>
  <div class="foot-caja_result">
    <a href="https://www.corfo.gob.cl/sites/cpp/convocatoria/SLUG/">Más Información</a>
  </div>
</div>
```

### 4. Requisitos — página de detalle

En cada `/sites/cpp/convocatoria/SLUG/` los requisitos viven en:

```html
<h2>¿Quiénes pueden postular?</h2>
<div class="postula_fase2-cuerpodos_fase2"> …texto… </div>
```

El scraper:
1. Borra los `.modal` antes de extraer (los modales de "Bases legales" tienen
   listas de PDFs que no son requisitos).
2. Busca `<h2>` con texto `"¿Quiénes pueden postular?"` (o variantes:
   `"acceder"`, `"participar"`, `"requisitos"`).
3. Toma el siguiente `.postula_fase2-cuerpodos_fase2` y devuelve su texto plano.
4. Fallback: si esa clase no existe, captura todo el contenido entre el `<h2>`
   y el siguiente heading del mismo nivel.

## Estructura del output

CSV (`;` + BOM UTF-8):

| columna             | ejemplo                                              |
| ------------------- | ---------------------------------------------------- |
| nombre              | CONVOCATORIA CDPR METROPOLITANO 2026: VIRALIZA …     |
| fecha_inicio        | 04/05/2026                                           |
| fecha_cierre        | 04/06/2026                                           |
| region              | Metropolitana                                        |
| link                | https://www.corfo.gob.cl/sites/cpp/convocatoria/…    |
| estado              | Abiertas                                             |
| descripcion_corta   | Se busca fortalecer la articulación entre …          |
| requisitos          | (texto plano, saltos de línea como `⏎` en CSV)       |

JSON: mismo contenido pero `requisitos` con saltos de línea reales.

## Notas operativas

- Throttling: 0.5 s entre requests (configurable en `SLEEP_BETWEEN`).
- El nonce se extrae al inicio. Si CORFO migrase a un esquema con expiración
  agresiva, hay que re-fetchear el listing periódicamente.
- Si `parse_cards` deja de devolver resultados pero `found` indica que faltan,
  inspeccionar la respuesta del AJAX: probablemente cambiaron el nombre de la
  clase `.caja-resultados_uno`.

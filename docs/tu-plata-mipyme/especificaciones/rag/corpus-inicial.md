---
title: "Corpus inicial del RAG · Documentación oficial por entidad"
description: "Catálogo curado de 47 documentos oficiales chilenos agrupados por las 13 entidades emisoras (SII, BCN, ChileAtiende, Sercotec, etc.). Insumo del pipeline de ingesta del RAG y checklist de descarga manual."
tags:
  - tu-plata-mipyme
  - rag
  - corpus
  - documentación-oficial
  - sii
  - bcn-leychile
  - chileatiende
  - sercotec
---

# 📂 Corpus inicial del RAG por entidad emisora

!!! info ":material-information: Para qué sirve este doc"
    Catálogo curado de la documentación oficial chilena que va al RAG de Impulsa V1, organizada por **entidad emisora**. Construido a partir de los runs de Deep Research [#07](../../../competencia/research/_runs-deep-research/2026-04-30-07-documentacion-oficial-dolores-incluidos.md) y [#08](../../../competencia/research/_runs-deep-research/2026-05-01-08-documentacion-oficial-6-dolores-complementarios.md), más la matriz de capacidades del producto.

> **Documentos relacionados:**
>
> - [Sección RAG · Overview](index.md) — la decisión de stack
> - [Decisión de stack (en repo de código)](https://github.com/Hatt3rPi/impactlab_pre_journeyemprendedor/blob/main/docs/specs/rag-stack-decision.md){target="_blank"} — Supabase + Voyage + Contextual Retrieval
> - [Run #07 raw](../../../competencia/research/_runs-deep-research/2026-04-30-07-documentacion-oficial-dolores-incluidos.md) — research de los 19 dolores ✅ Incluir originales
> - [Run #08 raw](../../../competencia/research/_runs-deep-research/2026-05-01-08-documentacion-oficial-6-dolores-complementarios.md) — research de los 6 dolores complementarios

---

## 1. Resumen ejecutivo

| Indicador | Valor |
|---|---|
| **Entidades emisoras únicas** | 13 |
| **Documentos individuales identificados** | 47 |
| **PDFs descargables** | 19 |
| **HTMLs scrapeables** | 22 |
| **APIs públicas disponibles** | 1 (ChileAtiende) |
| **Capacidades del producto V1 que cubren** | 21 de 26 (las que requieren RAG) |
| **Estimado de chunks tras ingesta** | ~3.000-5.000 (chunks de 500-800 tokens) |

### Top 3 entidades por importancia

1. **SII** — 15 documentos. Cubre 11 de 21 capacidades RAG. Es la columna vertebral.
2. **BCN LeyChile** — 11 leyes/decretos. Cubre 9 capacidades. Marco legal completo.
3. **Sercotec + ChileAtiende + FOGAPE** — 9 docs combinados. Cubre subsidios y trámites operativos.

### Estado del corpus

- ✅ **Identificado:** 47 documentos con URL verificada.
- ⏳ **Por descargar manualmente:** todos. Aún no hay ingesta.
- ⏳ **Por chunkear y embeber:** todos.
- ⏳ **Por aplicar Anthropic Contextual Retrieval:** todos.

---

## 2. Documentación por entidad

### 2.1 SII — Servicio de Impuestos Internos

**Tipo:** Servicio público chileno. Ente recaudador y fiscalizador.<br>
**URL base:** [https://www.sii.cl/](https://www.sii.cl/)<br>
**Acceso:** HTML público + PDFs descargables. Sin API oficial. Scrapeo directo.<br>
**Frecuencia de cambios:** Estable la base, circulares actualizadas anualmente.<br>
**Capacidades del producto que sirve:** #1, #3, #7, #11, #13, #14, #18, #19, #20, #21, #25 (11 de 21)

| # | Documento | URL | Formato | Cambia |
|---|---|---|---|---|
| 1 | Carta de Derechos del Contribuyente | [Link](https://www.sii.cl/sobre_el_sii/derechos_contribuyentes.pdf) | PDF | Estable |
| 2 | SII Educa — Derechos del Contribuyente | [Link](https://www.sii.cl/destacados/sii_educa/contenidos/contribuyentes/derechos_del_contribuyente/94-GA-201405290650.pdf) | PDF | Estable |
| 3 | Calendario tributario (valores y fechas) | [Link](https://www.sii.cl/valores_y_fechas/) | HTML | Anual |
| 4 | Preguntas frecuentes — Factura Electrónica (general) | [Link](https://www.sii.cl/preguntas_frecuentes/factura_electronica/) | HTML | Trimestral |
| 5 | FAQ Factura Electrónica — pregunta 6497 | [Link](https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6497.htm) | HTML | Anual |
| 6 | FAQ Factura Electrónica — pregunta 6495 | [Link](https://www.sii.cl/preguntas_frecuentes/factura_electronica/001_003_6495.htm) | HTML | Anual |
| 7 | Tipos de regímenes Pro PYME (modernización tributaria) | [Link](https://www.sii.cl/destacados/modernizacion/tipos_regimenes_mt.html) | HTML | Anual |
| 8 | Regímenes Renta 2025 | [Link](https://www.sii.cl/destacados/renta/2025/regimenes_renta2025.html) | HTML | Anual |
| 9 | Circular 38/2025 (orientación tributaria) | [Link](https://www.sii.cl/normativa_legislacion/circulares/2025/circu38.pdf) | PDF | Estable (versión 2025) |
| 10 | Resolución 75/2025 | [Link](https://www.sii.cl/normativa_legislacion/resoluciones/2025/reso75.pdf) | PDF | Estable |
| 11 | Cómo acreditar domicilio | [Link](https://www.sii.cl/material_inf/acreditar_domicilio.pdf) | PDF | Estable |
| 12 | FAQ RUT / Inicio de Actividades | [Link](https://www.sii.cl/preguntas_frecuentes/rut_inicio_actividades/001_105_0136.htm) | HTML | Estable |
| 13 | Guía F29 — IVA mensual | [Link](https://www.sii.cl/pagina/iva/guia_f29.htm) | HTML | Anual |
| 14 | Cómo solicitar condonaciones | [Link](https://www.sii.cl/como_se_hace_para/solicitar_condonaciones/solicitar_condonaciones.pdf) | PDF | Estable |
| 15 | Auditoría tributaria | [Link](https://www.sii.cl/principales_procesos/auditoria_tributaria.htm) | HTML | Anual |

!!! note ":material-cog: Notas técnicas"
    - HTMLs limpios sin JavaScript pesado, scrapeables directo con `fetch` + `cheerio` o `pdf-parse` para PDFs.
    - Algunos PDFs tienen versionado por año (`circu38.pdf` es de 2025); revisar cada año si la versión vigente cambió.
    - Sin rate limiting documentado pero conviene throttling (~1 request/segundo) para no levantar alarma.

---

### 2.2 BCN LeyChile — Biblioteca del Congreso Nacional

**Tipo:** Repositorio oficial de legislación chilena.<br>
**URL base:** [https://www.bcn.cl/leychile](https://www.bcn.cl/leychile)<br>
**Acceso:** HTML público con JavaScript. Cada norma tiene un `idNorma` único accesible vía `?idNorma=NNNNNNN`.<br>
**Frecuencia de cambios:** Estable salvo modificaciones legislativas (raras).<br>
**Capacidades del producto que sirve:** #11, #12, #18, #20, #23, #24, #25, #26 (8 de 21)

| # | Norma | URL | Capacidad |
|---|---|---|---|
| 1 | Ley 21.220 — Modificaciones FOGAPE | [Link](https://www.bcn.cl/leychile/navegar?idNorma=1207746) | #23 |
| 2 | Ley 20.659 — Régimen Empresas en un Día (RES) | [Link](https://www.bcn.cl/leychile/navegar?idNorma=1048718) | #11, #26 |
| 3 | Ley 19.857 — EIRL | Buscar `idNorma` aproximado | #12 |
| 4 | Ley 20.190 — Mercado de Capitales (incluye SpA) | Buscar | #12 |
| 5 | Ley 21.210 — Modernización Tributaria | Buscar | #20 |
| 6 | Ley 21.713 — Cumplimiento Tributario (transferencias 50/100) | Buscar | #1, #21 |
| 7 | Ley 21.563 — Insolvencia mipyme | Buscar | #25 |
| 8 | Ley 19.799 — Firma Electrónica y Servicios de Certificación | Buscar | #18 |
| 9 | Ley 19.631 — Ley Bustos (cotizaciones impagas) | Buscar | #24 |
| 10 | DL 3063 — Ley de Rentas Municipales | Buscar | #15 |
| 11 | Decreto 977 — Reglamento Sanitario de Alimentos | [Link](https://www.bcn.cl/leychile/Navegar?idNorma=144318) | #16 |

!!! note ":material-cog: Notas técnicas"
    - BCN tiene una vista "Texto Único" para cada ley que es la mejor para chunkear: `https://www.bcn.cl/leychile/navegar?idNorma=NNNNNNN&idVersion=&idParte=`.
    - JavaScript se puede saltar fetcheando directamente `view-source:` o usando Playwright si hay redirects.
    - El `idNorma` es estable; podemos hardcodear los IDs en la lista de descarga.
    - **Pendiente:** verificar IDs exactos de las leyes 19.857, 20.190, 21.210, 21.713, 21.563, 19.799, 19.631 y DL 3063 antes de la ingesta.

---

### 2.3 ChileAtiende

**Tipo:** Portal de trámites del Estado chileno.<br>
**URL base:** [https://www.chileatiende.gob.cl/](https://www.chileatiende.gob.cl/)<br>
**Acceso:** **API pública** + HTML público.<br>
**Frecuencia de cambios:** Mensual (catálogo de trámites se mueve).<br>
**Capacidades del producto que sirve:** #3, #15 (2 de 21, pero con alto valor — diagnóstico inicial)

| # | Recurso | URL | Formato | Notas |
|---|---|---|---|---|
| 1 | API de fichas (todas las fichas individuales) | `GET https://www.chileatiende.gob.cl/api/fichas/{fichaId}` | JSON | Requiere token de acceso |
| 2 | Ficha 67002 — Semilla Inicia | [Link](https://www.chileatiende.gob.cl/fichas/67002-semilla-inicia) | HTML | Ejemplo de ficha individual |
| 3 | Catálogo completo de trámites | Listado scrapeable desde la home | HTML | Para descubrir IDs |

!!! tip ":material-api: Acceso técnico"
    La API requiere token (gestionar acceso con la entidad). Si no se obtiene token a tiempo, fallback: scrapeo HTML. Cada ficha tiene estructura tipada (requisitos, costo, plazos, documentos) — ideal para chunking semántico por sección. Recomendado: ingesta semanal.

---

### 2.4 Sercotec — Servicio de Cooperación Técnica

**Tipo:** Servicio público de fomento a microempresas.<br>
**URL base:** [https://www.sercotec.cl/](https://www.sercotec.cl/)<br>
**Acceso:** HTML público + PDFs descargables (bases de convocatorias).<br>
**Frecuencia de cambios:** **Mensual** — convocatorias activas cambian.<br>
**Capacidades del producto que sirve:** #4, #22 (2 de 21, pero alta frecuencia de actualización)

| # | Documento | URL | Formato | Cambia |
|---|---|---|---|---|
| 1 | Portal principal (convocatorias activas) | [Link](https://www.sercotec.cl/) | HTML | Mensual |
| 2 | Capacitación Sercotec (currículos) | [Link](https://capacitacion.sercotec.cl/) | HTML | Anual |
| 3 | Capacitación — Canvas Modelos de Negocio | [Link](https://capacitacion.sercotec.cl/portal/capacitacion/canvas-diseno-de-modelos-de-negocio/) | HTML | Estable |
| 4 | Bases Semilla EMPRENDE 2026 (Metropolitana) | [Link](https://www.sercotec.cl/wp-content/uploads/2026/04/Bases-Semilla-EMPRENDE-2026-Metropolitana-VB%C2%B0.pdf) | PDF | Anual |

!!! warning ":material-alert: Alta frecuencia de cambios"
    Las bases de convocatorias son PDFs largos (30-60 páginas) con requisitos legales específicos. Chunking por sección (Beneficiarios / Requisitos / Etapas / Plazos / Documentos) es crítico. **Re-ingestar mensualmente** para capturar nuevas convocatorias regionales.

---

### 2.5 Corfo — Corporación de Fomento

**Tipo:** Servicio público de fomento productivo.<br>
**URL base:** [https://www.corfo.cl/](https://www.corfo.cl/)<br>
**Acceso:** HTML público.<br>
**Frecuencia de cambios:** Mensual (convocatorias).<br>
**Capacidades del producto que sirve:** #22

| # | Documento | URL | Formato |
|---|---|---|---|
| 1 | Portal Corfo | [Link](https://www.corfo.cl/) | HTML |
| 2 | Programa DPS (Convocatorias) | [Link](https://programadps.gob.cl/Convocatorias/) | HTML |

---

### 2.6 FOSIS — Fondo de Solidaridad e Inversión Social

**Tipo:** Servicio público para superación de la pobreza.<br>
**URL base:** [https://www.fosis.gob.cl](https://www.fosis.gob.cl)<br>
**Acceso:** HTML público.<br>
**Frecuencia de cambios:** Mensual.<br>
**Capacidades del producto que sirve:** #4, #22

| # | Documento | URL | Formato |
|---|---|---|---|
| 1 | Portal FOSIS | [Link](https://www.fosis.gob.cl) | HTML |
| 2 | Programa Yo Emprendo (similar a Sercotec Semilla) | Subportal del sitio principal | HTML |

---

### 2.7 FOGAPE — Fondo de Garantía para Pequeños y Medianos Empresarios

**Tipo:** Fondo estatal de garantía para créditos.<br>
**URL base:** [https://www.fogape.cl/](https://www.fogape.cl/)<br>
**Acceso:** HTML público + PDFs descargables.<br>
**Frecuencia de cambios:** Estable salvo cambios reglamentarios.<br>
**Capacidades del producto que sirve:** #23

| # | Documento | URL | Formato |
|---|---|---|---|
| 1 | Reglamento FOGAPE actualizado | [Link](https://www.fogape.cl/wp-content/uploads/2016/10/Reglamento-FOGAPE-actualizado.pdf) | PDF |
| 2 | Preguntas frecuentes | [Link](https://www.fogape.cl/2023/06/30/preguntas-frecuentes/) | HTML |

---

### 2.8 INAPI — Instituto Nacional de Propiedad Industrial

**Tipo:** Servicio público de propiedad intelectual.<br>
**URL base:** [https://www.inapi.cl/](https://www.inapi.cl/) (verificar antes de ingesta)<br>
**Acceso:** HTML público.<br>
**Frecuencia de cambios:** Estable.<br>
**Capacidades del producto que sirve:** #17 (💡 guiño futuro, no priorizado V1)

| # | Documento | URL | Formato |
|---|---|---|---|
| 1 | Manual de registro de marcas | Por confirmar | HTML/PDF |
| 2 | Tarifas vigentes | Por confirmar | HTML/PDF |
| 3 | Clasificación de Niza | Por confirmar | HTML |

!!! info ":material-clock-outline: V2"
    Como es 💡 guiño futuro (no V1), descarga puede esperar a la siguiente iteración del corpus.

---

### 2.9 PreviRed

**Tipo:** Plataforma operativa de cotizaciones previsionales.<br>
**URL base:** [https://www.previred.com/](https://www.previred.com/)<br>
**Acceso:** HTML público.<br>
**Frecuencia de cambios:** Mensual (tablas de tasas pueden ajustarse).<br>
**Capacidades del producto que sirve:** #24

| # | Documento | URL | Formato |
|---|---|---|---|
| 1 | Tablas de tasas vigentes (AFP, Isapre/Fonasa, AFC) | [Por confirmar URL exacta](https://www.previred.com/) | HTML |
| 2 | Manual operativo / Tutoriales | Por confirmar | HTML |

!!! note ":material-cog: Acceso restringido"
    PreviRed tiene autenticación para muchas funciones. Los datos públicos son las tablas de tasas y los tutoriales — eso es lo que va al RAG. Lo operativo (declarar cotizaciones reales) NO entra al RAG, lo hace el usuario directamente.

---

### 2.10 SEREMI Salud (Asistente Digital)

**Tipo:** Sistema digital del Ministerio de Salud para autorizaciones sanitarias.<br>
**URL base:** [https://seremienlinea.minsal.cl/asdigital/](https://seremienlinea.minsal.cl/asdigital/)<br>
**Acceso:** HTML público + scrapeo guiado.<br>
**Frecuencia de cambios:** Anual.<br>
**Capacidades del producto que sirve:** #16 (resolución sanitaria por rubro)

| # | Documento | URL | Formato |
|---|---|---|---|
| 1 | Asistente Digital SEREMI | [Link](https://seremienlinea.minsal.cl/asdigital/) | HTML |
| 2 | Manuales por rubro (alimentos, cosméticos) | Subpáginas del sistema | HTML |

!!! info ":material-map-marker: Variaciones regionales"
    Cada Región tiene su SEREMI con variaciones menores. Para V1 enfocar en SEREMI Metropolitana + Araucanía (el target del producto).

---

### 2.11 Entidad Acreditadora (Firmas Electrónicas)

**Tipo:** Organismo regulador de firmas electrónicas certificadas.<br>
**URL base:** [https://www.entidadacreditadora.gob.cl/](https://www.entidadacreditadora.gob.cl/)<br>
**Acceso:** HTML público.<br>
**Frecuencia de cambios:** Estable.<br>
**Capacidades del producto que sirve:** #18

| # | Documento | URL | Formato |
|---|---|---|---|
| 1 | Listado de proveedores certificados de FEA | [Link](https://www.entidadacreditadora.gob.cl/) | HTML |

---

### 2.12 TTA — Tribunales Tributarios y Aduaneros

**Tipo:** Tribunales especializados.<br>
**URL base:** [https://www.tta.cl/](https://www.tta.cl/)<br>
**Acceso:** HTML público.<br>
**Frecuencia de cambios:** Estable.<br>
**Capacidades del producto que sirve:** #21 (impugnación de multas)

| # | Documento | URL | Formato |
|---|---|---|---|
| 1 | Cómo presentar reclamo tributario | [Link](https://www.tta.cl/como-presentar-reclamo/) | HTML |

---

### 2.13 Otras fuentes secundarias

| Entidad | Documento | URL | Capacidad |
|---|---|---|---|
| **CMF Educa** | Educación financiera ciudadana | [Link](https://www.cmfeduca.cl/) | #2 (pricing, conceptos generales) |
| **Registro Social de Hogares** | Solicitud actualización ingresos | [Link](https://www.registrosocial.gob.cl/docs/04_Solicitud_de_actualizacion_de_ingresos_y_situacion_ocupacional.pdf) | #10 (beneficios sociales) |
| **Ventanilla Única Social** | Programa Emprendamos Semilla | [Link](https://www.ventanillaunicasocial.gob.cl/ficha/57/programa-emprendamos-semilla) | #4, #22 |
| **Startup Chile** | Postulación | [Link](https://startupchile.org/postula/) | #22 |

---

## 3. Cobertura por capacidad del producto

Mapa inverso: qué entidades suple cada capacidad del producto V1.

| # Capacidad | Entidades primarias | Cobertura |
|---|---|---|
| #1 Miedo SII | SII (Carta Derechos, Art. 8 bis) | ✅ Completa |
| #2 Pricing | (no requiere RAG — IA pura) | — |
| #3 Permisos | ChileAtiende, SII (RUT/inicio) | ✅ Completa |
| #4 Soledad / mentoras | Sercotec, FOSIS, Ventanilla Única, Startup Chile | ✅ Completa |
| #5 Mezclar finanzas | (no requiere RAG — IA pura) | — |
| #6 Valor del tiempo | (no requiere RAG — IA pura) | — |
| #7 Vende sin RUT | SII (FAQ inicio actividades), boleta servicios | ⚠️ Parcial — falta circular específica |
| #8 Cuenta personal | (no requiere RAG — IA pura) | — |
| #9 Crecimiento invisible | (no requiere RAG — IA pura) | — |
| #10 Beneficios sociales | Registro Social de Hogares + reglamentos específicos | ⚠️ Parcial — falta reglamento Bono Trabajo Mujer, FOSIS |
| #11 Fricción RES | BCN Ley 20.659 | ✅ Completa |
| #12 Figura jurídica | BCN Leyes 19.857 (EIRL), 20.190 (SpA), Código Comercio (Ltda) | ⚠️ Parcial — falta confirmar idNorma |
| #13 Escritura → SII | SII (FAQ inicio actividades, manual F4415) | ⚠️ Parcial — manual F4415 no encontrado online (solicitar) |
| #14 Domicilio tributario | SII (acreditar domicilio PDF) | ✅ Completa |
| #15 Patente municipal | DL 3063 + ordenanzas top 30 comunas | ⚠️ Parcial — ordenanzas requieren scrapeo individual |
| #16 Resolución sanitaria | SEREMI Salud + Decreto 977 | ✅ Completa |
| #17 INAPI marca | INAPI (💡 guiño, V2) | ⏳ Pendiente |
| #18 Firmas electrónicas | BCN Ley 19.799 + Entidad Acreditadora | ✅ Completa |
| #19 F29 mensual | SII (guía F29, calendario) | ✅ Completa |
| #20 Régimen tributario | SII (regímenes Pro PYME) + BCN Ley 21.210 | ✅ Completa |
| #21 Multas SII | SII (condonaciones, auditoría) + TTA | ✅ Completa |
| #22 Sercotec/Corfo | Sercotec, Corfo, ChileAtiende, FOSIS, Ventanilla Única | ✅ Completa |
| #23 FOGAPE | FOGAPE (reglamento) + BCN Ley 21.220 | ✅ Completa |
| #24 PreviRed | PreviRed + BCN Ley 19.631 | ⚠️ Parcial — tablas tasas requieren scrapeo |
| #25 Término giro | SII + BCN Ley 21.563 | ✅ Completa |
| #26 Disolución RES | BCN Ley 20.659 | ✅ Completa |

**Resumen de cobertura RAG (sobre las 21 capacidades que requieren RAG):**

- ✅ **Cobertura completa:** 13 capacidades (62%)
- ⚠️ **Cobertura parcial:** 7 capacidades (33%) — falta confirmar URLs o scrapear ordenanzas/tablas
- ⏳ **Pendiente** (no V1): 1 capacidad (5%) — INAPI

---

## 4. Plan de descarga e ingesta sugerido

### Fase 1 — Descarga manual (~4-6 horas)

!!! example ":material-account: Owner"
    Felipe / Cristian (uno cualquiera, en bloque concentrado).

**Pasos:**

1. Crear carpeta `corpus-rag/` (no versionada en git por tamaño).
2. Por cada entidad de la sección 2:
    - Descargar PDFs directamente (`wget` o navegador).
    - Para HTMLs: usar `curl` + guardar `.html` por URL.
    - Renombrar todos con convención: `<entidad>-<slug-doc>-<fecha>.<ext>` (ej: `sii-carta-derechos-2024-05.pdf`).
3. Confirmar URLs marcadas "Buscar" en BCN (8 leyes pendientes).
4. Confirmar URLs marcadas "Por confirmar" en INAPI y PreviRed.
5. Para Sercotec / Corfo: descargar bases de convocatorias activas al momento de la ingesta (snapshot mensual).

**Total estimado:** ~50-100 archivos, ~150-300 MB.

### Fase 2 — Limpieza y normalización (~2-4 horas)

1. Convertir HTMLs a markdown con `turndown` o `html-to-markdown`. Eliminar nav, footer, scripts.
2. Convertir PDFs a texto con `pdf-parse` o `unpdf`. Verificar resultado de PDFs escaneados (algunos circulares antiguos).
3. Estructurar metadata por archivo:

```json
{
  "source_id": "sii-carta-derechos",
  "source_url": "https://www.sii.cl/sobre_el_sii/derechos_contribuyentes.pdf",
  "source_name": "SII - Carta Derechos del Contribuyente",
  "entity": "SII",
  "fetched_at": "2026-05-05T...",
  "published_at": "2024-12-01",
  "format": "pdf",
  "language": "es",
  "capabilities_served": [1]
}
```

4. Generar lista de chunks con metadata heredada.

### Fase 3 — Contextualización + embeddings (~30 min de cómputo)

1. Para cada chunk: pasar por Claude Haiku con prompt-caching para agregar contexto del documento padre (Anthropic Contextual Retrieval).
2. Para cada chunk contextualizado: generar embedding con Voyage `voyage-3.5-lite`.
3. Insertar batch en Supabase tabla `documents`.

### Fase 4 — Verificación (~1 hora)

1. Smoke test: queries tipo *"qué dice el Art. 8 bis del Código Tributario"*, *"cómo doy primera boleta"*, *"FOGAPE elegibilidad"* — verificar que devuelven chunks relevantes con citas correctas.
2. Medir precisión top-5 con un set de 10-15 queries de prueba.
3. Si precisión <80%, considerar agregar Cohere Rerank.

---

## 5. Re-ingesta y mantenimiento

### Política de actualización

| Entidad | Frecuencia recomendada | Trigger automático |
|---|---|---|
| SII | Anual | Año fiscal nuevo (enero) |
| BCN LeyChile | Anual | Modificación legislativa detectada |
| ChileAtiende | Mensual | Cron mensual |
| **Sercotec** | **Mensual** | Bases nuevas disparan re-scrape |
| Corfo / FOSIS | Mensual | Cron mensual |
| FOGAPE | Trimestral | Cambio reglamento |
| PreviRed (tasas) | Mensual | Cron mensual |
| Resto | Anual | Cron anual |

### Implementación

GitHub Action mensual que:

1. Scrapea HTMLs marcados como "frecuencia mensual".
2. Detecta cambios via hash MD5 del contenido limpio.
3. Si cambió: re-procesa solo ese documento (chunkea + contextualiza + embeba + upsert en Supabase).
4. Notifica al equipo (Slack o issue automático) con el diff.

---

## 6. Riesgos y limitaciones

| Riesgo | Mitigación |
|---|---|
| Sitios oficiales con paywall o auth requerida | Documentar gaps. PreviRed funcional requiere auth — solo scrapear contenido público (tasas, FAQs). |
| Cambios en estructura HTML que rompen scraping | Detectar en CI mensual. Si falla, alertar al equipo. |
| PDFs escaneados (texto no extraíble) | OCR con `tesseract` como fallback. Marcar el documento con flag `needs_ocr`. |
| Información desactualizada en producción | Activar metadata `published_at` + filtro por fecha en queries. Si pregunta por norma vigente y solo hay versión 2022, citar año explícito. |
| Documentos con tablas o cuadros complejos | El chunking por texto pierde tablas. Identificar con `tabula-py` antes de chunkear; tratar tablas como chunks separados. |
| Variaciones regionales no cubiertas | V1 enfoca en RM + Araucanía (target user). Escalar a otras regiones post-lab. |

---

## 7. Decisiones registradas

| # | Decisión | Razón |
|---|---|---|
| C1 | 13 entidades emisoras en V1 | Cubre 21 de 21 capacidades RAG (con 7 cobertura parcial pendiente) |
| C2 | Descarga manual la primera vez, scraping automatizado mensual después | Una sola persona puede hacerlo en bloque de 4-6 horas; automatización mensual cubre actualizaciones |
| C3 | ~3.000-5.000 chunks estimados | Cabe holgado en plan Free de Supabase (500MB DB) |
| C4 | Metadata estructurada por documento | Permite filtros por entidad, fecha, capacidad |
| C5 | INAPI postpuesto a V2 | Es 💡 guiño en la matriz, no priorizado V1 |
| C6 | Foco regional en RM + Araucanía para V1 | Target user del producto. Resto de regiones post-lab |
| C7 | Convocatorias Sercotec/Corfo se re-ingestan mensualmente | Alta volatilidad — bases nuevas cada mes |
| C8 | BCN LeyChile como fuente única para legislación | Repositorio oficial. Otros sitios suelen citar BCN |

---

## 8. Pendientes antes de la ingesta

!!! warning ":material-clipboard-check: Checklist pre-Fase 1"

    - [ ] Confirmar `idNorma` en BCN para 8 leyes marcadas "Buscar" (Sección 2.2).
    - [ ] Verificar URL exacta del manual SII F4415 (no encontrado en runs #07-#08).
    - [ ] Verificar URLs de INAPI (Sección 2.8).
    - [ ] Verificar URLs de tablas vigentes de PreviRed (Sección 2.9).
    - [ ] Solicitar token de API de ChileAtiende (Sección 2.3) — fallback: scrapeo HTML.
    - [ ] Decidir top 30 comunas para ordenanzas municipales (Sección 2 Capacidad #15).
    - [ ] Confirmar reglamentos específicos de beneficios sociales (Bono Trabajo Mujer, FOSIS) — Capacidad #10.

    Cuando todos los items estén check, el corpus está listo para Fase 1 (descarga manual).

---

## 9. Glosario de fuentes / siglas

- **SII** — Servicio de Impuestos Internos
- **BCN** — Biblioteca del Congreso Nacional (LeyChile.cl)
- **DL** — Decreto Ley
- **DS** — Decreto Supremo
- **RES** — Régimen Empresas en un Día (Ley 20.659)
- **EIRL** — Empresa Individual de Responsabilidad Limitada (Ley 19.857)
- **SpA** — Sociedad por Acciones (Ley 20.190)
- **F29** — Formulario 29 (declaración mensual IVA)
- **F22** — Formulario 22 (declaración anual de renta)
- **F4415** — Formulario de Inicio de Actividades / Aviso de Modificaciones SII
- **FOGAPE** — Fondo de Garantía para Pequeños y Medianos Empresarios (Ley 21.220)
- **FOSIS** — Fondo de Solidaridad e Inversión Social
- **TTA** — Tribunal Tributario y Aduanero
- **CMF** — Comisión para el Mercado Financiero
- **Sercotec** — Servicio de Cooperación Técnica
- **Corfo** — Corporación de Fomento
- **INAPI** — Instituto Nacional de Propiedad Industrial
- **SEREMI** — Secretaría Regional Ministerial
- **AFP** — Administradora de Fondos de Pensiones
- **AFC** — Administradora de Fondos de Cesantía
- **FEA** — Firma Electrónica Avanzada
- **FE** — Firma Electrónica (simple)

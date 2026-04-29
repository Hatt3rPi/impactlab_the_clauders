---
title: Datasets
description: Datos públicos disponibles de CMF, SII, SERNAC y otros.
tags:
  - stack
  - datasets
---

# Datasets

Inventario de **datos públicos** que podemos usar. La organización promete datasets curados, pero también podemos traer los nuestros.

## Provistos por el lab

> Confirmar formato exacto y acceso durante los workshops pre-lab.

- Datos de **CMF** (Comisión para el Mercado Financiero).
- Datos de **SII** (Servicio de Impuestos Internos).
- Datos de **SERNAC** (Servicio Nacional del Consumidor).

## Inventario de fuentes públicas

### CMF

- [ ] **Texto completo de la Ley Fintech 21.521**.
- [ ] **Circulares y NCG** publicadas (especialmente las relacionadas con Fintech).
- [ ] **Listado de entidades inscritas** en el registro Fintech.
- [ ] **Estadísticas del sistema financiero** (bancos, EIC, fintechs).
- [ ] **CMF Educa** (sitio educativo) — base de FAQs y guías.

### SII

- [ ] **Preguntas frecuentes** publicadas.
- [ ] **Tutoriales y guías** para emprendedores.
- [ ] **Resoluciones y oficios** que crean obligaciones específicas.

### SERNAC

- [ ] **Alertas al consumidor** (catálogo histórico de fraudes).
- [ ] **Boletines** de reclamos por sector.
- [ ] **Material educativo** disponible.

### Otras

- [ ] **Banco Central de Chile** — informes de inclusión financiera, IEF.
- [ ] **CSIRT de Gobierno** — alertas y campañas de ciberseguridad.
- [ ] **Boletín del Congreso** — para tracking legislativo.
- [ ] **PhishTank / Google Safe Browsing** — listas de URLs maliciosas.
- [ ] **Diario Oficial** — versión definitiva de leyes y reglamentos.

## Tabla de datasets reales (a llenar)

| Dataset | Fuente | Tamaño aprox. | Formato | Licencia | Cómo accederlo | Notas |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

## Consideraciones técnicas

- **Encoding:** mucho contenido oficial chileno viene en PDF; preparar pipeline de extracción.
- **Estructura:** las leyes tienen jerarquía artículo-inciso-letra; respetarla en chunking.
- **Frecuencia de actualización:** documentar cuándo se actualizó cada fuente (importante para citaciones).
- **Versiones:** la Ley Fintech ha tenido modificaciones; capturar cuál es la vigente al 2026.

## Buenas prácticas

- **Snapshot local** de cada fuente que vayamos a usar (evita romper el demo si la URL cambia).
- **Metadata** por documento: título, fecha de publicación, fecha de descarga, URL original.
- **Versionado** en el repo del prototipo (en `data/raw/` y `data/processed/`).

## Riesgos

- **Datos desactualizados** → respuestas legalmente incorrectas → descalificación.
- **Datos con derechos de autor** → confirmar qué podemos redistribuir.
- **PDFs mal parseados** → hallucinaciones del modelo.

## Decisiones pendientes

- ¿Qué formato canónico vamos a usar internamente? (Markdown estructurado por artículo es lo más natural.)
- ¿Vector store o búsqueda por keyword o ambos?

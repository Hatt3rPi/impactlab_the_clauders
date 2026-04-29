---
title: "Comportamiento digital en Chile (DataReportal Digital 2026)"
description: "Cifras oficiales de penetración mobile, hábitos de consumo digital y demografía conectada en Chile."
autor: "Síntesis sobre BYYD (cita DataReportal Digital 2026, oct 2025)"
fecha: 2026-04-29
categoria: usuarios
linea: transversal
tags:
  - research
  - usuarios
  - mobile
  - comportamiento-digital
  - datareportal
---

# Comportamiento digital en Chile

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuente externa"
    Sintetizado a partir de [BYYD blog (cita DataReportal Digital 2026)](https://www.byyd.me/en/blog/2025/12/chiles-mobile-market-key-trends-and-digital-insights/). **Verificar cifras antes de citarlas en el pitch.**

Cifras **oficiales** de comportamiento digital chileno. Fuente útil para sustentar [ADR 0003 (plataforma web mobile-first)](../../especificaciones/adrs/0003-plataforma-web-mobile-first.md) y el pitch.

## Fuente

- **DataReportal Digital 2026** (publicado oct-2025).
- Reseñado por **BYYD** (25-dic-2025) en [Chile's mobile market: key trends and digital insights](https://www.byyd.me/en/blog/2025/12/chiles-mobile-market-key-trends-and-digital-insights/).

> Fuente primaria: **DataReportal**. La cifra del 97 % que Anahi mencionó en el [kickoff](../../reuniones/2026-04-29-definicion-problema-setup.md) coincide en magnitud con la oficial: **95,3 % móvil**.

## Cifras macro de conectividad (oct 2025)

| Métrica | Valor |
|---|---|
| Población total Chile | **19,9 M** |
| Usuarios de internet | **18,8 M** (penetración **94,5 %**) |
| **Acceso a internet vía móvil** | **95,3 %** |
| Mujeres / hombres | 50,3 % / 49,7 % |
| Edad promedio | 36,9 años |
| Área urbana | 88,3 % |

## Tiempo conectado

- **52 horas y 49 minutos por semana** en promedio en medios digitales conectados.
- Equivale a más de **7,5 horas diarias** de uso digital.

## Hábitos de consumo digital (% que realiza la actividad)

| Actividad | % |
|---|---|
| **Búsqueda de información** | **73,9 %** |
| Redes sociales / contacto | 68,3 % |
| Streaming de música | 64,3 % |
| Video / TV online | 59,9 % |
| Compras ecommerce (gasto en bienes de consumo ocurriendo en móvil) | 41,1 % |

> :material-lightbulb: **Implicancia para nuestra solución:** la actividad #1 que hacen los chilenos en internet es **buscar información**. Esto refuerza la decisión de optimizar para SEO + AI Overviews + ChatGPT/Perplexity, no para "instalar una app".

## Implicancias directas para el proyecto

### 1. Confirma ADR 0003 con fuente verificable

> *"95,3 % de los chilenos accede a internet por móvil"* — cita textual con fuente oficial. Útil en el pitch del 7 de mayo.

### 2. Refuerza estrategia de SEO + AI-citability

El **73,9 %** que busca información lo hace en su mayoría desde móvil (95,3 % de los conectados). Si la solución no está bien indexada en Google y citable por Claude/ChatGPT/Perplexity, **no es encontrable**.

### 3. Confirma que el canal natural NO es una app

- El usuario chileno pasa ~7,5 h/día en digital pero su actividad principal es **buscar**, no descubrir apps nuevas.
- Pedir instalación es fricción innecesaria contra el flujo natural.

### 4. Para segmentos vulnerables: cuidado con la generalización

DataReportal **no desglosa** por NSE, edad o región. Los datos macro **no garantizan** que adultos mayores >60 (uno de nuestros sub-segmentos potenciales en Defensor / Antiestafa) tengan los mismos hábitos. Buscar fuente específica para ese sub-segmento.

## Datos que NO están en esta fuente (gaps a cubrir)

| Dato necesario | Estado | Dónde buscarlo |
|---|---|---|
| Penetración de WhatsApp | No incluido | Statista, We Are Social, encuestas Subtel |
| Brecha digital adultos mayores | No incluido | INE, ENUT, ClaroVTR-Criteria Personas Mayores 2024 |
| Penetración mobile por NSE | No incluido | CADEM, GfK, Subtel |
| Uso de mobile banking / fintech | No incluido | CMF, Banco Central, BancoEstado, Fintual |
| Web vs app nativa preferida | No incluido | Estudios SimilarWeb / App Annie |
| Diferencias regionales (RM vs regiones) | No incluido | INE, Subtel |

## Quotes utilizables en el pitch

> *"95,3 % de los chilenos accede a internet desde su móvil"* (DataReportal Digital 2026).
>
> *"73,9 % usa internet principalmente para buscar información"* (DataReportal Digital 2026).
>
> *"Los chilenos pasan 52h 49min por semana conectados"* (DataReportal Digital 2026).

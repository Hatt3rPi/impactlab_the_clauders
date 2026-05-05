---
title: "SEO, landing y organización de tareas para el hackathon"
fecha: 2026-05-05
hora: "04:37"
duracion: "22 min"
tipo: "sync"
participantes:
  - Felipe Abarca
  - Jose Foncea
  - Cristian Astorga
  - Anahi Gonzalez
ausentes: []
tags:
  - reunion
  - seo
  - landing
  - documentacion
  - hackathon
  - organizacion
---

# Reunión: SEO, landing y organización de tareas para el hackathon

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Documento generado a partir de la transcripción literal de la sesión del 05-may-2026 (04:37 UTC). Sesión corta de cierre (~22 min). Continuación directa de la sesión principal de 3 horas.

## TL;DR

- Felipe propone **landing en Astro con blog SEO** (10 artículos iniciales) para posicionamiento en Google + ChatGPT/Perplexity, con robot.txt y LLM.txt configurados. Anahi lo refuerza como parte del journey de demo.
- **Roles confirmados**: Felipe + Cristian → bases de datos y agentes; Jose + Anahi → frontend web, UX, diseño de marca y pitch.
- **Centralización de documentación**: tarea crítica para el día siguiente — reunión de trabajo a las 09:00 h para levantar y organizar fuentes (SII, municipalidades, organismos relevantes) usando Deep Research + IA.
- Cristian propone usar **Google Embeddings** como motor de base de conocimiento.
- Sesión de trabajo presencial programada para mañana a las 09:00 h.

## Objetivo

Cerrar la distribución de tareas antes de dormir y definir la dinámica de trabajo del día siguiente (miércoles 6-may), el día clave de desarrollo del hackathon.

## Decisiones tomadas

| # | Decisión | Razón |
|---|---|---|
| 1 | **Landing en Astro** para la interfaz pública no autenticada | Astro es indexable nativamente por Google, documentado y SEO-friendly. Permite blog con artículos. |
| 2 | **10 artículos de blog iniciales** (Felipe: 5 sobre servicio tributario/PutInterno + 2 sobre formalización) | Mínimo viable para posicionamiento SEO y credibilidad técnica ante jurados. |
| 3 | **Configurar robot.txt + LLM.txt en la landing** | Suma puntos con jueces técnicos y permite indexación en modelos de lenguaje (ChatGPT, Perplexity, Claude). |
| 4 | **Reunión de trabajo a las 09:00 h del día siguiente** | Centralizar documentación antes de que backend tome la posta. Felipe: "son un par de horitas de trabajo." |
| 5 | **Dinámica de la reunión de mañana**: trabajar en conjunto, dividir organismos/fuentes y usar Deep Research para acelerar la recolección | Cristian ya tiene el flujo probado — un prompt estructurado puede generar la base documental inicial. |
| 6 | **Felipe lidera documentación técnica; Cristian de apoyo** | Cristian: "Deberían tener más relación a los problemas — van a tener identificada la documentación y pasarla a una fuente de conocimiento." |

## Acciones

| # | Responsable | Acción | Fecha límite | Estado |
|---|---|---|---|---|
| 1 | Felipe | Armar y entregar 5 artículos sobre PutInterno + 2 sobre formalización para el blog SEO | 06-may | abierta |
| 2 | Felipe | Liderar levantamiento de documentación del repositorio + centralización en la wiki | 05-may 09:00 h | abierta |
| 3 | Cristian | Apoyar documentación técnica (bases de datos, agentes) en la sesión de mañana | 05-may 09:00 h | abierta |
| 4 | Jose | Construir landing pública en Astro + módulo web autenticado | 06-may | abierta |
| 5 | Jose | Coordinar y facilitar la sesión de documentación de mañana | 05-may 09:00 h | abierta |
| 6 | Anahi | Trabajar en UX/UI visual, diseño de marca y pitch junto a Jose | 06-may | abierta |
| 7 | Anahi | Poner alarma y confirmar puntualidad para las 09:00 h | 05-may | abierta |
| 8 | Equipo | Usar Deep Research + IA para recolección y filtrado de documentación oficial | 05-may 09:00 h | abierta |

## Discusión

### SEO y landing pública

Felipe propuso que la landing no autenticada se construya en **Astro** por su indexación nativa en Google. La estrategia SEO incluye un blog con al menos 10 artículos publicados antes del Demo Day — suficiente para demostrar al juez técnico que el posicionamiento digital está pensado.

También mencionó que para aparecer en ChatGPT y Perplexity basta con indexarse correctamente y configurar el robot.txt + LLM.txt. Esto suma credibilidad técnica incluso si los resultados de posicionamiento real no son visibles aún en el Demo Day (el posicionamiento orgánico tarda ~3 meses, pero la arquitectura ya estará instalada).

Anahi sugirió integrar esta landing al journey del demo en vivo: buscar en Google → aparece la landing → el usuario entra → comienza el flujo de WhatsApp.

### División de roles (confirmación)

El equipo confirmó la distribución acordada en la sesión anterior:

- **Felipe + Cristian**: bases de datos, agentes, backend, estructura documental.
- **Jose + Anahi**: web (landing + pantallas internas), experiencia del usuario, diseño visual y pitch.

Anahi resumió la lógica: *"Felipe y Cristian van a estar en bases de datos y agentes. Nosotros [Jose y yo] vamos a preocuparnos del viaje dentro de la web que tiene más visual — diseño de marca, experiencia del usuario y el pitch."*

### Centralización de documentación

Jose identificó que la documentación de fuentes que el asistente necesita (SII, municipalidades, organismos) aún no está centralizada ni en el repositorio. Hay contenido en la wiki del proyecto pero incompleto.

Cristian propuso usar **Deep Research con un prompt bien estructurado** para acelerar la recolección. Felipe confirmó que ya había generado información con Deep Research anteriormente, y que mañana habría que hacer el ejercicio con contexto más refinado (dolores ya acotados a los incluidos en el MVP).

La dinámica acordada para mañana a las 09:00 h: reunión de trabajo (no de revisión), dividir organismos/fuentes entre los miembros, usar IA para filtrar y estructurar, y luego pasar la documentación a la base vectorial. Felipe estimó "un par de horitas."

### Base de conocimiento: Google Embeddings

Cristian reforzó la decisión de usar **Google Embeddings** como motor de la base de conocimiento, anticipando que el flujo sería sencillo: *"Si ocupamos Google Embedding es tomar los documentos y meterlo en la licuadora."* Esto alineado con la decisión de Supabase PG Vector tomada en la sesión anterior.

## Preguntas abiertas

1. **¿Tenemos dominio propio disponible?** Se mencionó que el dominio actual es dinámico. Para SEO real se necesita dominio estático.
2. **¿Los artículos del blog se generan con IA o son redactados manualmente?** No se cerró — Felipe dijo que Claude los puede generar rápido.
3. **¿La documentación del repositorio existente (wiki del proyecto) cubre los casos de uso del demo?** Felipe: "Quizás hay que pedirle al Claude que lo concentre."

## Próximos pasos

- Todos en la sesión de trabajo a las 09:00 h del 05-may.
- Felipe trae el primer set de artículos y la documentación de SII priorizada.
- Cristian llega con el prompt de Deep Research ya estructurado para la recolección.
- Jose y Anahi, en paralelo, inician bocetos de la landing y pantallas internas.
- A las 14:00-15:00 h: punto de control de personalización de sugerencias (ver sesión anterior).

## Material de apoyo

- Transcripción Fireflies: [ver en Fireflies](https://app.fireflies.ai/view/01KQV6VMZ83AJ14N20SYDD4NHE)
- Sesión previa (~3 h): [Arquitectura multi-agente y definición de producto](2026-05-05-arquitectura-producto-definicion.md)

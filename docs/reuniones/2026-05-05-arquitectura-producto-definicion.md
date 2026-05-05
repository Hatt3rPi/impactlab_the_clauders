---
title: "Arquitectura multi-agente y definición de producto"
fecha: 2026-05-05
hora: "01:37"
duracion: "181 min (~3 h)"
tipo: "diseño-producto"
participantes:
  - Felipe Abarca
  - Jose Foncea
  - Cristian Astorga
  - Anahi Gonzalez
ausentes: []
tags:
  - reunion
  - arquitectura
  - producto
  - hackathon
  - tu-plata-mipyme
  - stack
---

# Reunión: Arquitectura multi-agente y definición de producto

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Documento generado a partir de la transcripción literal de la reunión del 05-may-2026 (01:37 UTC / noche del 4-may en Santiago). Sesión de ~3 horas. Es fuente primaria de las decisiones de arquitectura, stack y alcance de producto.

## TL;DR

- El equipo **define por primera vez el alcance acotado del producto**: microemprendedores en etapas Validación informal → Formalización → Operación formal. Etapa "Idea" excluida.
- **Stack confirmado**: WhatsApp vía Open Cloud (no Twilio — marca propia), multi-agente con Claude Opus para agentes especializados + Sonnet/Haiku para orquestador, Supabase PG Vector con Google Embedding para la base documental.
- **Arquitectura multi-agente**: orquestador central → agentes especializados (tributario/SII, financiamiento/postulaciones) + agente explorador (RAG) + agente notificador proactivo.
- **Tres dolores priorizados**: (1) registro SII + trámites de formalización, (2) contabilidad sistémica / flujo de caja, (3) acceso a instrumentos de fomento (Corfo, SERCOTEC, Startup Chile).
- **División de roles**: Felipe + Cristian en backend/agentes; Jose + Anahi en frontend/landing/UX. Punto de control mañana a las 14:00-15:00 h para evaluar personalización de sugerencias.

## Objetivo

Cerrar la definición de producto antes del hackathon (6 de mayo) y acordar el stack técnico, la arquitectura y la distribución de trabajo para el Demo Day.

## Decisiones tomadas

| # | Decisión | Razón |
|---|---|---|
| 1 | **Migrar WhatsApp de Twilio a Open Cloud** | Twilio muestra logo y colores de Twilio en el chat → "mata el efecto wow" del pitch. Open Cloud permite marca propia. Felipe lo tiene listo en ~30 min. |
| 2 | **Descartar etapa "Idea" del alcance del MVP** | El usuario objetivo es quien ya tiene una idea masticada y quiere formalizarse o gestionar mejor. Atacar la etapa Idea amplía demasiado el scope. |
| 3 | **Tres dolores core: SII/formalización + contabilidad + instrumentos de fomento** | Suficientemente acotados para ser resueltos con precisión en el tiempo disponible. El resto se descarta o queda como futuro. |
| 4 | **Descartar dolor "permisos" del MVP** | Demasiado heterogéneo por municipalidad, sector y rubro. No confiable para generalizar. |
| 5 | **Descartar dolor "fijación de precios" del MVP** | Muy amplio y googleable. Los propios fondos dan capacitación al respecto. |
| 6 | **Base documental: Google Embedding + Supabase PG Vector** (no Obsidian) | Obsidian es más preciso pero más complejo de implementar para Demo Day. Supabase tiene config híbrida documentada. |
| 7 | **Arquitectura multi-agente**: orquestador (Sonnet/Haiku) + agentes especializados (Opus) | A mayor contexto y herramientas, mayor alucinación (estudios Vercel). Separar contextos reduce el problema y el gasto de tokens. |
| 8 | **Sugerencia informativa de fondos (no personalizada con evaluación de elegibilidad)** | La personalización agrega una capa de complejidad considerable. Punto de control mañana para reevaluar. |
| 9 | **Backend idéntico para WhatsApp y web** | Diferencia solo en renderizado de la interfaz. Simplifica desarrollo. |
| 10 | **División de roles: Felipe + Cristian → backend/agentes; Jose + Anahi → frontend** | Felipe lidera arquitectura de agentes; Cristian, web scraping y system prompts; Jose y Anahi, pantallas web y UX. |
| 11 | **Herramienta colaborativa: Lucid** (no wiki, que generaba conflictos) | Wiki tiene conflictos de edición simultánea. Lucid permite coeditar en tiempo real. |
| 12 | **No considerar los 50 créditos de API ofrecidos por el convocante** | Llegarán después del hackathon. El equipo opera con sus propias cuentas. |

## Acciones

| # | Responsable | Acción | Fecha límite | Estado |
|---|---|---|---|---|
| 1 | Felipe | Migrar WhatsApp a Open Cloud | 05-may | abierta |
| 2 | Felipe | Liderar arquitectura de agentes + backend funcional | 06-may (Demo Day) | abierta |
| 3 | Felipe | Trasvasijar commits al repo para evidenciar trabajo en 48 h | continuo | abierta |
| 4 | Felipe | Punto de control a las 14:00-15:00 h para evaluar personalización de sugerencias | 05-may | abierta |
| 5 | Cristian | Montar web scraping de postulaciones (Corfo, SERCOTEC, Startup Chile) | 05-may | abierta |
| 6 | Cristian | Definir y construir system prompts de agentes especializados | 06-may | abierta |
| 7 | Cristian | Configurar Supabase PG Vector con Google Embedding | 05-may | abierta |
| 8 | Cristian | Completar diagrama de arquitectura en Lucid | 05-may | abierta |
| 9 | Jose | Liderar frontend de la app web + landing pública | 06-may | abierta |
| 10 | Jose | Crear template de flujo de caja (estructura y formato) | 05-may | abierta |
| 11 | Jose | Definir preguntas del onboarding y sus implicancias para el system prompt | 05-may | abierta |
| 12 | Jose | Subir documentación de organismos (SII, municipalidades, Corfo/SERCOTEC) | 05-may | abierta |
| 13 | Anahi | Frontend y diseño UX/UI de pantallas internas | 06-may | abierta |
| 14 | Anahi | Redacción del perfil del usuario objetivo (perspectiva de género, regiones remotas, mobile-first) | 05-may | abierta |
| 15 | Equipo | Subir documentación a plataforma del Impact Lab antes del jueves | jueves 07-may | abierta |
| 16 | Equipo | Confirmar tickets para Espacio Riesgo (miércoles y jueves) | 05-may | abierta |

## Discusión

### Bloque 1 — Briefing post-reunión con Pacheco (organizador)

El equipo recibió del organizador Pacheco las reglas operativas del hackathon:

- Los **50 créditos de API** no se consideran en el desarrollo — llegarán después.
- **Espacio Riesgo**: miércoles = desarrollo e interacción con mentores (CMF, Caja de los Andes, etc.). Jueves mañana el staff elige 12-13 equipos para presentar pitch y de esos elige 3 ganadores.
- Plazo de documentación: hasta el jueves, pero la selección se basa en lo subido. Conclusión operativa: **un día útil efectivo** (miércoles) para desarrollar.
- Llevar computadores cargados — no hay enchufes disponibles en el espacio asignado.

Jose sintetizó el criterio estratégico del equipo: *"Un equipo puede haber adelantado toda la pega técnica, pero si el problema no hace match con lo que convencer al jurado, van a cagar igual. Lo más importante es que la narrativa entre el problema y lo que generemos, cierre."*

### Bloque 2 — Estado del stack WhatsApp: Twilio → Open Cloud

Felipe tenía montado un esqueleto funcional en **Twilio**, pero identificó un problema crítico para el demo: en Twilio el logo y colores que aparecen en el chat son de Twilio, no de la marca del producto. Eso destruye el efecto visual en el pitch.

La alternativa es **Open Cloud**: permite WhatsApp con marca propia. Felipe estimó ~30 minutos para dejarlo funcionando. El equipo acordó la migración de inmediato.

Adicionalmente, el flujo de onboarding actual tenía fricciones: errores en el registro (correo + password), botones de acción poco visibles y confirmación de correo no evidente para el usuario. Pendiente de pulir antes del Demo Day.

### Bloque 3 — Arquitectura multi-agente (diagrama Cristian)

Cristian presentó una arquitectura multi-agente fundamentada en estudios de Vercel sobre rendimiento de agentes:

> *"Los agentes cuando tienen demasiado contexto, ya sea porque leyeron mucho o porque tienen demasiadas herramientas, pierden efectividad y empiezan a alucinar. Separar contextos reduce el problema."*

La arquitectura acordada:

```
Usuario (WhatsApp / Web)
        ↓
Copiloto / Orquestador / Traductor  ← Claude Sonnet o Haiku
        ↓
┌───────────────────────────────────────────┐
│  Agente especializado: Tributario / SII   │  ← Claude Opus
│  Agente especializado: Financiamiento     │  ← Claude Opus
│  Agente explorador (RAG / base documental)│
│  Agente notificador proactivo             │
└───────────────────────────────────────────┘
        ↑
Capa web scraping: Corfo, SERCOTEC, Startup Chile, etc.
Base documental: Supabase PG Vector + Google Embedding
```

Fundamento técnico: separar el contexto de cada agente especializado mantiene la precisión y evita que el exceso de información de un dominio contamine respuestas de otro.

### Bloque 4 — Base documental: RAG vs Obsidian vs vectorización

Debate sobre la tecnología para la base de conocimiento:

- **Obsidian**: lee archivos Markdown por encabezados, más preciso pero más complejo de implementar para el Demo Day.
- **RAG tradicional**: riesgo de alucinaciones.
- **Google Embedding + Supabase PG Vector**: vectorización híbrida. Tiene instructivo disponible en la documentación del Impact Lab. Cristian lo puede dejar funcionando rápido.

Acuerdo: **Google Embedding + Supabase PG Vector** para Demo Day. Fuente de datos principal de partida: **Bendita IA** (entrega buena base, aunque no cubre Corfo, SERCOTEC, Startup Chile ni Endeavor → web scraping complementario a cargo de Cristian).

Datos sintéticos: descartados para información pública (googleable); aceptados solo donde una conexión real sería muy compleja (ej. datos bancarios).

### Bloque 5 — Definición del problema real (ejercicio colaborativo en Lucid)

Este fue el momento clave de la sesión. Jose propuso migrar el ejercicio al Lucid porque la wiki generaba conflictos de edición. El equipo mapeó dolores por etapa del journey del emprendedor.

**Etapas del viaje identificadas:**
Idea → Validación informal → Formalización → Operación formal → Crecimiento → Recuperación y Cierre.

**Decisión de alcance**: el MVP atiende Validación informal, Formalización y Operación formal. La etapa Idea se excluye. El usuario objetivo es el microemprendedor que ya tiene una idea masticada y quiere dar el paso.

**Dolores analizados y resultado:**

| Dolor | Decisión | Razón |
|---|---|---|
| Miedo al SII | ✅ **CRÍTICO — transversal** | "Es lo más importante del proyecto." |
| Fijación de precios | ❌ Excluir | Muy amplio, googleable, los fondos lo cubren. |
| Permisos (sanitarios, municipales) | ❌ Excluir | Demasiado heterogéneo por rubro/municipalidad. |
| Contabilidad sistémica / flujo de caja | ✅ Incluir — core | Hábito de registro + template + visualización. |
| Acceso a instrumentos de fomento | ✅ Incluir | Scrapper + notificación + match con perfil. |
| Red de apoyo / soledad del emprendedor | ⏳ Evaluación futura | Buena idea, no en el MVP. |

Jose lo verbalizó directamente: *"El producto no estaba definido. No, porque el problema no estaba definido. Tenemos mucho contexto, problema, no sé."* Esta sesión fue la que cerró esa brecha.

### Bloque 6 — Propuesta de valor consolidada

Anahi sintetizó el posicionamiento del producto como un puente con dos caras:

> *"Por un lado entregamos orden, acompañamiento y claridad para los usuarios. A las empresas y al Estado les entregamos datos, una plataforma unificadora y un plan de fomento a la formalización. Somos eso — somos el puente."*

Felipe amplió la visión del producto como acompañante proactivo:

> *"Con eso logramos que la persona, ya sea startupero, ya sea un agricultor, ya sea doña Juanita de la Sopaipilla, se sienta acompañadísima, porque es como el compañero Mateo: primero te guía el paso a paso y segundo te da los respaldos de lo que va requiriendo en cada etapa."*

**Perfil de usuario final acordado**: emprendedores en sectores de comida/alimentos, artesanías/producción, agricultura y servicios (peluquería, manicure, cuidado de personas). Énfasis en regiones remotas y zonas rurales → **mobile-first, WhatsApp como canal principal**.

### Bloque 7 — Canales: WhatsApp vs Web

- **WhatsApp**: instantaneidad, registro de ventas y gastos en terreno, consultas rápidas, notificaciones proactivas, onboarding.
- **Web**: dashboard financiero, calendario, módulo del journey del emprendedor, historial de conversaciones, descarga de PDFs.
- Backend idéntico para ambos canales; diferencia solo en renderizado.

Debate sin cierre definitivo: si el onboarding se hace desde WhatsApp o solo desde web. Felipe ve riesgos de seguridad en Open Cloud. Cristian defiende inclusividad (usuarios solo-móvil). Posición operativa para Demo Day: onboarding desde la app web para simplificar; capacidad por WhatsApp se declara como feature del producto.

### Bloque 8 — Notificaciones y sugerencias

- **Notificaciones proactivas**: cuando se abre un fondo (Corfo, SERCOTEC, Startup Chile), el agente notificador envía una notificación al usuario con explicación y relevancia.
- **Debate**: sugerencia informativa (¿hay un fondo abierto relevante para tu sector?) vs. sugerencia personalizada con evaluación de elegibilidad del usuario.
- Felipe marcó la complejidad de la personalización como riesgo: *"Siento que hay una capa de complejidad no menor."* Decisión: ir por sugerencia informativa para Demo Day. Punto de control mañana a las 14:00-15:00 h para reevaluar.

### Bloque 9 — Logística tokens

Felipe alertó sobre la restricción de créditos del equipo: él tiene cuenta de $200/mes, Jose y Anahi de $20/mes. Si los de $20 se quedan sin tokens durante el desarrollo intensivo, la carga recae sobre Felipe. Se identificó como riesgo operativo a monitorear.

## Preguntas abiertas

1. **¿Se puede implementar personalización de sugerencias** (evaluación de elegibilidad por perfil) en el tiempo disponible? → punto de control 05-may 14:00-15:00 h.
2. **¿El onboarding puede hacerse desde WhatsApp** o solo desde web para el Demo Day? (debate no cerrado).
3. **¿Qué pasa cuando el negocio crece más allá de PYME básica?** Felipe propone handoff a contador real (marketplace).
4. **¿Cómo balancear el "te enseño los beneficios del B2B" con las obligaciones tributarias** que vienen con la formalización? (comunicación honesta vs. motivar el salto).
5. **¿Los datos sintéticos** son aceptables para casos donde la conexión real es muy compleja?

## Próximos pasos

- Felipe migra WhatsApp a Open Cloud (hoy).
- Cristian monta scraping de postulaciones (~1 hora estimada).
- Jose y Anahi inician frontend en paralelo cuando el backend tenga base.
- Sesión de trabajo de documentación mañana a las 09:00 h (ver reunión del 05-may sesión 2).
- Punto de control de personalización de sugerencias: 05-may 14:00-15:00 h.
- Todos los commits en el repo antes del Demo Day del 06-may.

## Señales de riesgo

| Tipo | Señal | Interpretación |
|---|---|---|
| Scope | Etapas E4 y E5 del journey no revisadas | Quedaron fuera del análisis de esta sesión — risk de feature creep si se retoman. |
| Timing | Solo un día útil (miércoles) para desarrollar | El volumen de trabajo definido en esta sesión requiere ejecución paralela sin fricción. |
| Decisión | Personalización de sugerencias aplazada | Si el punto de control de mañana dice "sí se puede", agrega carga de último minuto. |
| Técnico | Riesgo de tokens ($20 vs $200) | Jose y Anahi pueden quedarse sin tokens durante el desarrollo intensivo. |
| Personal | Hiperfoco de Felipe → retraso propio | Lo autodiagnosticó: "Siempre tiendo a perfeccionar lo que entrego, pero me atrasa." |

## Citas memorables

> *"El producto no está definido. No, porque el problema no está definido."* — Jose

> *"Lo que estamos entregando es la democratización de esta información en lenguaje simple."* — Felipe

> *"Somos el puente."* — Anahi (propuesta de valor síntesis)

> *"Los agentes cuando tienen demasiado contexto pierden efectividad y empiezan a alucinar — separar contextos reduce el problema."* — Cristian

> *"Lo perfecto es enemigo de lo bueno. Llevo 15 años rigiéndome por eso."* — Felipe

## Referencias

- [Arquitectura Tu Plata Mipyme](../tu-plata-mipyme/especificaciones/arquitectura.md) — actualizar con decisiones de esta sesión.
- [Stack tecnológico](../tu-plata-mipyme/especificaciones/stack/index.md) — confirmar Supabase PG Vector + Google Embedding.
- [ADR 0004 — WhatsApp-first / freemium / multi-agente](../tu-plata-mipyme/especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md) — actualizar con decisión Open Cloud.
- [Dolores del journey](../tu-plata-mipyme/dolores.md) — actualizar con resultados del ejercicio Lucid.
- [Backlog Tu Plata Mipyme](../tu-plata-mipyme/backlog.md) — actualizar con decisiones de alcance de esta sesión.
- Transcripción Fireflies: [ver en Fireflies](https://app.fireflies.ai/view/01KQTWGERK4TJS5EAGB8ZHFW2M)

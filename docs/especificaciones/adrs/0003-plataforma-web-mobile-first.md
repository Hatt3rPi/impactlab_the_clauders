---
title: "ADR 0003 — Plataforma: web mobile-first (no app nativa)"
estado: "Parcialmente superado"
fecha: 2026-04-29
actualizado: 2026-04-30
autor: "The Clauders (decisión de equipo en reunión kickoff)"
tags:
  - adr
  - plataforma
  - frontend
  - parcialmente-superado
---

# ADR 0003 — Plataforma: web mobile-first (no app nativa)

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Documento generado por el equipo The Clauders. Es fuente primaria para este tema.

!!! warning ":material-alert-circle: Parcialmente superado por ADR 0004 (2026-04-30)"
    El [ADR 0004](0004-tu-plata-mipyme-whatsapp-first-freemium-multiagente.md) decidió que **para el producto Tu Plata Mipyme el canal principal es WhatsApp**, no la web. Este ADR 0003 sigue vigente para:

    - La **wiki del equipo** (este sitio).
    - **Productos de consulta puntual** (donde el usuario busca y encuentra una vez).

    Para productos de **acompañamiento sostenido** (recurrente, asincrónico) el canal principal es WhatsApp y la web pasa a rol de amplificador (landing pública, tablero visual, descargas). Ver ADR 0004 §"Decisión 1" y §"Alternativa A descartada".

## Contexto

Independiente de la línea temática elegida, el equipo necesita decidir **qué tipo de plataforma** usar para llegar al usuario final. Las opciones realistas en 48 h:

- **Web responsive / mobile-first** (HTML/CSS/JS).
- **App nativa** (iOS/Android).
- **PWA** (web instalable).
- **Asistente embebido** en plataforma de terceros (WhatsApp, Telegram).

Anahi presentó datos sobre uso de tecnología en Chile que fueron **verificados con fuente oficial** (DataReportal Digital 2026, vía BYYD dic-2025):

- **95,3 %** de los chilenos accede a internet vía dispositivos **móviles**.
- **73,9 %** usa internet principalmente para **buscar información**.
- Tiempo promedio conectado: **52 h 49 min por semana**.
- Compras móviles: 41,1 % del gasto en bienes de consumo.

> Fuente verificada: [Comportamiento digital en Chile (DataReportal Digital 2026)](../../research/usuarios/comportamiento-digital-chile-2026.md).

## Decisión

**Construimos una página web mobile-first**, accesible desde el navegador (móvil y desktop) sin instalación.

Requisitos derivados:

- **Mobile-first** en diseño y performance — el 95-97 % del tráfico esperado entra por celular.
- **Encontrable en Google** — SEO técnico básico bien hecho.
- **Rastreable por crawlers IA** (Google AI Overviews, ChatGPT, Perplexity, ClaudeBot) — el ciudadano busca y muchas veces termina en una respuesta IA antes que en un sitio. Si la IA cita nuestra página, ganamos visibilidad.
- **Sin login obligatorio para empezar** — fricción mínima para el primer uso.

## Consecuencias

### Positivas

- **Cobertura máxima del usuario chileno** (95,3 % móvil, no requiere instalar nada).
- **Pitch alineado con datos de comportamiento real**, no con preferencias de equipo.
- **El 73,9 % usa internet para buscar información** → SEO + AI-citability genera tráfico orgánico continuo, no solo el del lab.
- **Diferenciador potencial:** otros equipos probablemente irán por chatbot embebido o app — una web indexable para AI Overviews puede ser más original.
- **Tiempo de iteración más corto** — deploy continuo (Netlify) en cada push.
- **Funciona como wiki + producto** — la misma stack web sirve para documentar y para entregar valor.

### Negativas / costos

- **Sin acceso a APIs nativas** (notificaciones push, biometría, cámara fácil) — no son críticas para el caso de uso planteado.
- **Dependencia del navegador del usuario** — algunos chilenos usan navegadores in-app (Facebook, WhatsApp) con bugs; testear en esos contextos.
- **SEO/AI-citability requiere trabajo deliberado** — no se obtiene gratis. Hay que invertir en metadata, schema.org, contenido estructurado, posibles `llms.txt`.

### Neutras / a observar

- **Framework concreto:** Felipe propuso **Astro** (justifica por experiencia previa con SEO + AI rendering en su otro producto Presencia Digital). No queda cerrado en este ADR — se decide en un ADR separado de stack frontend.
- **Mascota / branding:** Anahi propuso una mascota para generar empatía y confianza. Queda como decisión de UX abierta, dependiente del problema y sub-segmento finales.

## Alternativas consideradas

### Opción A — App nativa (iOS/Android)

- **Pros:** notificaciones, mejor performance percibida, sensación premium.
- **Contras:** instalación es enorme fricción para usuario "a pie"; tiempos de aprobación en stores no caben en 48 h; doble esfuerzo iOS/Android.
- **Razón de descarte:** no podemos pedirle al ciudadano que instale algo para entender un derecho que ya tiene; agrega fricción justo donde el usuario está confundido.

### Opción B — Asistente embebido en WhatsApp/Telegram

- **Pros:** WhatsApp es el canal #1 en Chile; cero instalación adicional; experiencia conversacional natural.
- **Contras:** dependencia de plataformas de terceros; APIs de WhatsApp Business tienen costo y aprobación; pitch al jurado se ve menos en vivo (sin demo visual rica); SEO/AI-citability inexistente.
- **Razón de descarte:** queremos que el usuario nos encuentre cuando *busca* (Google + IA), no solo cuando alguien le comparte un contacto. WhatsApp queda como **canal secundario** potencial.

### Opción C — PWA (Progressive Web App)

- **Pros:** combinación de web + instalable.
- **Contras:** poca diferencia con web mobile-first bien hecha; instalación de PWA tiene fricción real en iOS.
- **Razón de descarte:** la web mobile-first ya cubre el 95 % del valor sin la complejidad extra de PWA.

## Referencias

- Reunión: [kickoff 2026-04-29](../../reuniones/2026-04-29-definicion-problema-setup.md).
- [Comportamiento digital en Chile (DataReportal Digital 2026)](../../research/usuarios/comportamiento-digital-chile-2026.md) — fuente primaria verificada para las cifras macro.

## Relacionados

- ADR 0002 (Línea temática) — independiente, aplica con cualquier línea.
- **Superado parcialmente por:** [ADR 0004 — Tu Plata Mipyme: WhatsApp-first, freemium y multi-agente](0004-tu-plata-mipyme-whatsapp-first-freemium-multiagente.md).
- ADR futuro pendiente — stack frontend concreto (Astro u otro).

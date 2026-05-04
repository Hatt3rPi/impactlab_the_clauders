---
title: "Design System (resumen citable)"
description: "Tokens, escalas y reglas del Design System v0.1 de Impulsa, en formato markdown para referenciar desde el PRD, plan, backlog y otros docs."
tags:
  - tu-plata-mipyme
  - diseño
  - design-system
  - tokens
---

# Design System — Resumen citable

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Versión markdown del Design System v0.1 de Impulsa para citar desde otros docs del wiki. Para la versión visual interactiva ver [Design System (HTML)](../../../assets/diseno/impulsa-design-system.html){target="_blank"}. Resumen ejecutivo en [diseño/index.md](index.md).

## 1. Colores

### 1.1 Primarios

| Token | Hex | Uso semántico |
|---|---|---|
| `--blue` | `#2563EB` | Primario · Acción · Confianza |
| `--amber` | `#D97706` | Secundario · Alertas · CTA |
| `--green` | `#16A34A` | Éxito · Completado · Crecimiento |
| `--purple` | `#7C3AED` | Gamificación · XP · Logros |

### 1.2 Variantes claras (backgrounds suaves)

| Token | Hex | Uso |
|---|---|---|
| `--blue-light` | `#EFF6FF` | Fondo de cards/badges azules |
| `--blue-lighter` | `#DBEAFE` | Borde + fondo de cards seleccionables |
| `--amber-light` | `#FFFBEB` | Fondo de tags ámbar |
| `--green-light` | `#F0FDF4` | Fondo de tags éxito |
| `--green-lighter` | `#DCFCE7` | Variantes de gradiente |
| `--purple-light` | `#F5F3FF` | Fondo de tags violeta |
| `--purple-lighter` | `#EDE9FE` | Variantes de gradiente |
| `--red-light` | `#FEF2F2` | Fondo de errores/avisos |
| `--amber-mid` | `#FEF3C7` | Variantes de gradiente |
| `--yellow` | `#FCD34D` | Acento highlight (gradientes) |

### 1.3 Semánticos / neutros

| Token | Hex | Uso |
|---|---|---|
| `--red` | `#DC2626` | Urgencia · Errores |
| `--dark` | `#0F172A` | Títulos · Texto principal · Sidebar |
| `--mid` | `#475569` | Texto secundario |
| `--muted` | `#64748B` | Subtítulos · Metadata |
| `--soft` | `#94A3B8` | Etiquetas · Apagado |
| `--border` | `#E2E8F0` | Bordes de cards e inputs |
| `--fog` | `#F8FAFC` | Fondo · Superficie de página |
| `--blue-deep` | `#1E40AF` | Final de gradientes hero |

## 2. Tipografía

### 2.1 Familias

- **Display + Body:** `'Plus Jakarta Sans', sans-serif` (Google Fonts, pesos 400-800)
- **Mono / código:** `'JetBrains Mono', monospace` (Google Fonts, pesos 400, 600)

### 2.2 Escala

| Nombre | Tamaño | Peso | Tracking | Uso |
|---|---|---|---|---|
| Título Display | 48px | 800 | -1.5px | Hero del landing |
| Título Principal | 34px | 800 | -0.8px | H2 de secciones |
| Título Sección | 24px | 700 | -0.4px | Subtítulos importantes |
| Subtítulo / Card | 18px | 700 | — | Títulos de cards |
| Cuerpo Destacado | 15px | 600 | — | Énfasis en body |
| Cuerpo | 14px | 400 | line-height 1.7 | Texto corrido |
| Etiqueta | 12px | 500 | uppercase, tracking 1px | Metadata |
| Micro | 9-11px | 400-700 | — | Labels mini, chips |

### 2.3 Reglas de escritura

**✓ Usar:**
- Frases de máximo 8-10 palabras por acción.
- Primera persona del usuario (*"Tu negocio"*).
- Verbos de acción directos (*"Formaliza"*, *"Postula"*).
- Emojis funcionales como apoyo visual.
- Números y datos concretos (*"en 5 minutos"*).

**✗ Evitar:**
- Términos tributarios sin explicación.
- Párrafos de más de 3 líneas.
- Tono institucional o gubernamental.
- Siglas sin expansión (SII → explicarlo la primera vez).
- Lenguaje condicional o vago (*"podría ser"*).

## 3. Espaciado y radios

### 3.1 Escala de espaciado (base 4px)

| Token | Valor | Uso |
|---|---|---|
| `--space-1` | 4px | Micro separación |
| `--space-2` | 8px | Gap tight |
| `--space-3` | 12px | Gap standard |
| `--space-4` | 16px | Padding sm |
| `--space-5` | 20px | Padding md |
| `--space-6` | 24px | Padding lg |
| `--space-8` | 32px | Section gap |
| `--space-12` | 48px | Section padding |
| `--space-16` | 64px | Hero padding |

### 3.2 Border radius

| Token | Valor | Uso |
|---|---|---|
| `--r-sm` | 8px | Botones small, tags |
| `--r-md` | 12px | Botones, inputs |
| `--r-lg` | 16px | Cards principales |
| `--r-xl` | 20px | Hero cards, modals |
| `--r-full` | 9999px | Pills, badges, chips |

## 4. Componentes

### 4.1 Botones — variantes principales

| Variante | Estilo | Uso |
|---|---|---|
| **Primary CTA** | Azul `#2563EB` · texto blanco · 11px 24px · radius 10px · weight 700 · emoji al inicio | Acción principal del flujo |
| **Secondary CTA** | Ámbar `#D97706` · igual estructura | Acciones tipo "postular ahora" |
| **Success CTA** | Verde `#16A34A` · igual estructura | "Marcar completo", confirmaciones |
| **Outline** | Transparente · borde 1.5px azul · texto azul | Secundario, "¿cómo funciona?" |
| **Soft** | Fondo `#EFF6FF` · texto azul · 8px 16px · 12px | "Ver más →" |
| **Hero CTA** | Oscuro `#0F172A` · texto blanco · 14px 40px · 16px · weight 800 | CTA gigante con microcopy "Sin tarjeta · 100% gratuito" |

**Reglas:**
- Siempre incluir emoji o ícono al inicio del CTA principal.
- CTA primario en azul o color de sección.
- Microcopy en CTA final: *"Sin tarjeta · 100% gratuito"*.
- Botones full-width en mobile, auto en desktop.

### 4.2 Cards — variantes

| Variante | Estilo | Uso |
|---|---|---|
| **Card estándar** | Fondo `#FFF` · borde `#E2E8F0` · radius 16px · sombra suave | Contenido general |
| **Card hero** | Gradiente `#2563EB → #1E40AF` · texto blanco · radius 16px | Secciones destacadas |
| **Card de acción** | Fondo `#EFF6FF` · borde 2px `#DBEAFE` · radius 16px · badge "RELEVANTE PARA TI ⭐" | Items seleccionables |

### 4.3 Progress bars

- **Container:** `height: 8-12px · background: #E2E8F0 · radius: 10px · overflow: hidden`
- **Fill (variantes):**
  - Avance del journey: gradiente `#16A34A → #2563EB`
  - XP del nivel: gradiente `#FCD34D → #D97706`
  - Compatibilidad fondo: `#16A34A` sólido
  - Onboarding: `#2563EB` sólido
- **Label sup:** título a la izq · valor a la der (ej: *"68% · 340/500 XP"*).

## 5. Sistema de gamificación

### 5.1 Niveles — *El árbol del emprendedor*

| Emoji | Nivel | XP | Significado | Color |
|---|---|---|---|---|
| 🌱 | **Semilla** | 0–200 | Inicio del camino | Verde `#16A34A` |
| 🌿 | **Brote** | 200–500 | Primeros trámites | Azul `#2563EB` |
| 🌳 | **Árbol** | 500–1.000 | Negocio formalizado | Ámbar `#D97706` |
| 🌲 | **Bosque** | 1.000+ | Empresa consolidada | Violeta `#7C3AED` |

### 5.2 XP por acción

| Acción | XP | Nivel necesario |
|---|---|---|
| Completar diagnóstico inicial | +30 | Semilla |
| Inicio de actividades SII | +50 | Semilla |
| Acreditar domicilio tributario | +60 | Brote |
| Emitir primera boleta | +80 | Brote |
| Obtener patente municipal | +70 | Brote |
| Separar cuenta empresa | +60 | Brote |
| Postular a un fondo | +100 | Árbol |
| Completar un curso | +40 | Cualquiera |
| Registro de marca | +150 | Bosque |

### 5.3 Medallas (12 totales)

🧾 Primera boleta · 🏛️ SII activo · 🏦 Cuenta empresa · 🚀 Primer fondo · 📊 30 días activa · 👥 Primer empleado · 🌐 Sitio web · 💳 Pago digital · 📦 10 ventas · 🏆 Marca registrada · 📚 Primer curso · 🌟 Embajadora.

**Estilo:** activas con fondo `#F5F3FF` + borde 2px `#7C3AED`; inactivas con fondo `#F8FAFC` + borde `#E2E8F0` + opacity 0.45.

## 6. Voz y tono

### 6.1 Atributos (5)

| Emoji | Atributo | Definición |
|---|---|---|
| 🤝 | Cercano | Como un amigo que sabe del tema |
| 💪 | Motivador | Celebra cada avance, por pequeño que sea |
| 🎯 | Directo | Frases cortas, sin rodeos |
| 🧠 | Simple | Sin tecnicismos, sin letra chica |
| 🇨🇱 | Local | Habla chileno, usa el registro del usuario |

### 6.2 Ejemplos antes/después

| ✗ Antes | ✓ Impulsa |
|---|---|
| *"El contribuyente deberá proceder a la iniciación de actividades."* | *"Para vender con boleta, necesitas hacer un trámite en el SII. ¡Es gratis!"* |
| *"Complete el formulario adjunto para iniciar el proceso."* | *"Cuéntanos de tu negocio. Son 5 preguntas rápidas. 🏪"* |
| *"El monto asignado depende de la evaluación de antecedentes."* | *"Si te aceptan, te dan hasta $3.500.000 para tu negocio. 💰"* |

## 7. Principios (5)

### 7.1 👁️ Visual primero

Cada concepto se apoya en un emoji, ícono o ilustración antes del texto. Nunca párrafos sin apoyo visual.

> 💡 Usar emojis funcionales antes de etiquetas. Íconos de 40-52px en cards. Ilustraciones en onboarding.

### 7.2 🎮 Gamificación útil

La gamificación no es decorativa. Cada XP y medalla tiene una acción real detrás que beneficia al emprendedor.

> 💡 Siempre mostrar el beneficio concreto junto al XP. *"Postula y gana +100 XP"* no es el objetivo; el fondo sí lo es.

### 7.3 🧠 Carga cognitiva mínima

Máximo 3 opciones por pantalla. Máximo 8-10 palabras por frase de acción. Una sola CTA primaria por vista.

> 💡 Usar steps/steppers para flujos complejos. Dividir información en tabs en vez de mostrar todo junto.

### 7.4 🤝 Empowerment

Cada interacción debe hacer que el usuario sienta que puede hacerlo. Nunca juzgar el estado actual del negocio.

> 💡 Celebraciones visuales al completar hitos. Tono siempre motivacional. Errores explicados con siguiente paso claro.

### 7.5 ⚡ Mobile primero

El usuario principal tiene alta familiaridad con el celular y WhatsApp. El diseño se piensa desde 390px hacia arriba.

> 💡 Botones mínimo 44px de altura. Texto mínimo 14px. Touch targets holgados. Contenido crítico en el primer scroll.

## 8. Trazabilidad

| Fuente | Ubicación |
|---|---|
| Versión visual interactiva | [`assets/diseno/impulsa-design-system.html`](../../../assets/diseno/impulsa-design-system.html){target="_blank"} |
| Prototipo navegable (6 pantallas) | [`assets/diseno/impulsa-prototipo.html`](../../../assets/diseno/impulsa-prototipo.html){target="_blank"} |
| Tokens en código (CSS variables) | [`impactlab_pre_journeyemprendedor/tokens.css`](https://github.com/Hatt3rPi/impactlab_pre_journeyemprendedor/blob/main/tokens.css) |
| Tokens en código (Tailwind preview) | [`impactlab_pre_journeyemprendedor/tailwind.config.preview.js`](https://github.com/Hatt3rPi/impactlab_pre_journeyemprendedor/blob/main/tailwind.config.preview.js) |
| Resumen ejecutivo (con highlights y links) | [`diseno/index.md`](index.md) |

**Versión:** v0.1 · 3-may-2026 · Autora: Anahi González · Hackathon MVP.

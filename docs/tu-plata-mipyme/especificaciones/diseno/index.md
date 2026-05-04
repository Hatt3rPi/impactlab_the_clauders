---
title: "Diseño · Sistema visual y prototipo"
description: "Design System y prototipo web del producto, entregados por Anahi (3-may-2026)."
tags:
  - tu-plata-mipyme
  - diseño
  - design-system
  - prototipo
---

# Diseño — Sistema visual y prototipo

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Material de diseño entregado por **Anahi González** el **3-may-2026** vía WhatsApp. Versión `v0.1` del Design System + prototipo web interactivo de 6 pantallas. Branding tentativo: **"Impulsa"** (decisión final de naming pendiente — ver [decisiones pendientes](../../index.md#decisiones-pendientes)).

## Documentos

| Archivo | Descripción | Tamaño |
|---|---|---|
| [📐 **Design System** (HTML interactivo)](../../../assets/diseno/impulsa-design-system.html){target="_blank"} | Paleta, tipografía, componentes, gamificación, voz/tono, principios | 230 KB |
| [🎨 **Prototipo Web** (HTML interactivo)](../../../assets/diseno/impulsa-prototipo.html){target="_blank"} | 6 pantallas navegables: Landing, Onboarding, Checklist, Finanzas, Convocatorias, Logros | 1.4 MB |
| [📋 Design System (resumen markdown)](design-system.md) | Tokens, escalas y reglas en formato citable desde otros docs del wiki | — |

> Ambos HTMLs son standalone (todos los assets embebidos en base64). Abren directamente en el navegador, no requieren servidor ni dependencias.

## Highlights del entregable

### Branding

- **Nombre tentativo:** Impulsa
- **Logo:** 🌱 sobre cuadrado azul `#2563EB` con borde redondeado
- **Tagline:** *"Sistema de diseño para la plataforma de acompañamiento a microemprendedores chilenos"*
- **Hero copy:** *"¿Vendes, pero no facturas? Te ayudamos a dar el paso."*

### Paleta principal

| Color | Hex | Rol |
|---|---|---|
| 🔵 Azul Impulsa | `#2563EB` | Primario · Acción · Confianza |
| 🟠 Ámbar Energía | `#D97706` | Secundario · Alertas · CTA |
| 🟢 Verde Logro | `#16A34A` | Éxito · Completado · Crecimiento |
| 🟣 Violeta Nivel | `#7C3AED` | Gamificación · XP · Logros |
| 🔴 Rojo Alerta | `#DC2626` | Urgencia · Errores |
| ⚫ Oscuro | `#0F172A` | Títulos · Texto principal |

### Tipografía

**Plus Jakarta Sans** (display + body, Google Fonts) + **JetBrains Mono** (código). Escala de 9-48px en 6 niveles. Reglas claras de "usar / evitar" en el design system.

### Sistema de gamificación — *El árbol del emprendedor*

| Nivel | XP | Significado |
|---|---|---|
| 🌱 Semilla | 0–200 | Inicio del camino |
| 🌿 Brote | 200–500 | Primeros trámites |
| 🌳 Árbol | 500–1.000 | Negocio formalizado |
| 🌲 Bosque | 1.000+ | Empresa consolidada |

**XP por acción** (extracto): completar diagnóstico (+30), inicio actividades SII (+50), primera boleta (+80), postular fondo (+100), registro de marca (+150). 12 medallas en grid (Primera boleta, SII activo, Cuenta empresa, Primer fondo, etc.).

### 5 principios de diseño

1. **👁️ Visual primero** — emoji/ícono antes del texto. Nunca párrafos sin apoyo visual.
2. **🎮 Gamificación útil** — cada XP/medalla tiene una acción real detrás. La gamificación no es decorativa.
3. **🧠 Carga cognitiva mínima** — máximo 3 opciones por pantalla. Máximo 8-10 palabras por frase de acción. Una sola CTA primaria por vista.
4. **🤝 Empowerment** — celebrar cada hito. Tono motivacional. Errores con siguiente paso claro. Nunca juzgar el estado actual del negocio.
5. **⚡ Mobile primero** — diseño desde 390px. Botones ≥44px. Texto ≥14px. Touch targets holgados.

### Voz y tono — 5 atributos

- 🤝 **Cercano** — como un amigo que sabe del tema
- 💪 **Motivador** — celebra cada avance, por pequeño que sea
- 🎯 **Directo** — frases cortas, sin rodeos
- 🧠 **Simple** — sin tecnicismos, sin letra chica
- 🇨🇱 **Local** — habla chileno, registro del usuario

**Ejemplo antes/después:**
> ✗ *"El contribuyente deberá proceder a la iniciación de actividades."*
> ✓ *"Para vender con boleta, necesitas hacer un trámite en el SII. ¡Es gratis!"*

### Las 6 pantallas del prototipo

1. **Landing** — hero + value props + how it works + testimonios reales (Luz Marinao costurera Temuco; Rodrigo Fuentes carpintero Valparaíso; Ana González repostera Santiago).
2. **Onboarding** — 5 preguntas simples sobre el negocio.
3. **Checklist** — hoja de ruta de formalización personalizada.
4. **Finanzas** — registro de ventas/gastos.
5. **Convocatorias** — fondos disponibles y compatibilidad con perfil.
6. **Logros** — gamificación con árbol del emprendedor + medallas.

## Cómo se relaciona con el resto del producto

- **Frontend (`impactlab_pre_journeyemprendedor`):** los tokens CSS y la paleta del design system se materializaron en [`tokens.css`](https://github.com/Hatt3rPi/impactlab_pre_journeyemprendedor/blob/main/tokens.css) + [`tailwind.config.preview.js`](https://github.com/Hatt3rPi/impactlab_pre_journeyemprendedor/blob/main/tailwind.config.preview.js) como base para el spike técnico.
- **PRD:** la sección [§2.1 Estado futuro deseado](../../PRD.md#21-estado-futuro-deseado) describe la web complementaria; este DS le da forma visual concreta.
- **PITCH:** el slide de demo y el panel "agentic thinking" se beneficiarán de la paleta + componentes definidos.
- **Backlog:** las features de E0-E5 [marcadas ✅ Incluir](../../backlog.md) se renderizarán con estos tokens.
- **Naming:** "Impulsa" es propuesta de Anahi. **Decisión pendiente** del equipo (ver [hub](../../index.md#decisiones-pendientes)).

## Próximos pasos

- [ ] Resolver naming definitivo (sesión equipo, antes del pitch).
- [ ] Validar con casos reales del segmento (entrevistas pre-lab si las hay).
- [ ] Adaptar prototipo desktop a vista mobile (segmento target = mobile-first).
- [ ] Revisar accesibilidad: contraste, tamaño de touch, zoom 200%.
- [ ] Sincronizar con el agente WhatsApp: continuidad visual cuando el usuario pasa de chat a web.

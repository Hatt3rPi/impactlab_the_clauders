---
title: "Manuales operativos"
description: "Recetas paso a paso para extender el producto: gamificación, tools del chat, integraciones."
tags:
  - tu-plata-mipyme
  - manuales
  - operación
---

# 📘 Manuales operativos

Recetas paso a paso para extender el producto sin tener que re-leer todo el código. Pensados para que cualquier miembro del equipo (Felipe, Cristian, Jose, Anahi) pueda aplicar cambios siguiendo una guía concreta.

## Manuales disponibles

| Manual | Para qué |
|---|---|
| [Extender el sistema de gamificación](extender-gamificacion.md) | Agregar checklist items, tipos de milestone, tools nuevas, ajustar XP, cambiar niveles del árbol del emprendedor |

## Convenciones

- Cada manual incluye **archivos a tocar**, **código copiable**, y **comandos de verificación**.
- Cuando una receta requiere migration de DB, lo dice explícito y referencia el patrón de `supabase/migrations/`.
- Cuando una receta cambia el comportamiento del modelo (system prompt), se valida con un test manual descrito.

## Cuándo escribir un manual nuevo

Si en una sesión te encontrás explicando lo mismo más de 2 veces (a Claude o a un humano), conviértelo en manual. Heurística:

1. ¿Es una operación recurrente que el equipo va a repetir? → manual.
2. ¿Es una decisión one-shot del producto? → ADR.
3. ¿Es un dolor estructural del journey? → entra a `dolores.md`.
4. ¿Es la spec de cómo se construye una pieza por primera vez? → `docs/specs/` del repo de código (no acá).

Los manuales viven en la wiki para que sean **citables y editables** desde el navegador. Las specs técnicas detalladas viven en el repo de código junto al código que especifican.

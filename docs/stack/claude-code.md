---
title: Claude Code
description: IDE con IA integrada para acelerar el desarrollo.
tags:
  - stack
  - claude
  - claude-code
---

# Claude Code

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../convenciones-de-contenido.md).

CLI/agente oficial de Anthropic que actúa como par de programación dentro del editor (Cursor, VS Code, terminal).

## Para qué lo usaremos

- Escribir y refactorizar código del prototipo durante las 48 h.
- Mantener esta wiki (sí, este mismo agente la generó).
- Investigar libs, leer docs, generar tests.

## Setup recomendado para el lab

- Cada miembro instala Claude Code en su máquina antes del 6 de mayo.
- Compartir un **CLAUDE.md** del prototipo con convenciones del repo.
- Para builders: integrarlo con VS Code o JetBrains.
- Para vibecoders: usar la CLI directa o la app de Anthropic.

## Hooks y permisos útiles

Settings frecuentes para acelerar:

- **Permisos automáticos** (allowlist) para comandos seguros (`git status`, `npm install`, etc.) → ver skill `fewer-permission-prompts`.
- **Hooks** que validen automáticamente antes de cada commit (lint, format).

## Skills disponibles que sirven en el lab

Listado de skills globales que ya tenemos:

- `claude-api` — guía y best practices para apps con Claude API (incluye prompt caching).
- `frontend-design` — generar interfaces frontend con calidad de producto.
- `init` / `claude-md-management:revise-claude-md` — mantener el `CLAUDE.md` del prototipo.
- `simplify` — revisar y simplificar código.
- `seo-*` — útiles solo si construimos un sitio público.

## Convenciones cuando trabajemos en el prototipo

- Cada PR pasa por `simplify` o equivalente antes de merge.
- Hay un `CLAUDE.md` en la raíz del repo del prototipo con: stack, comandos, anti-patrones, glosario interno.
- Logs de Claude Code no se commitean.

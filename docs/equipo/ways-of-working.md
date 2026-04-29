---
title: Ways of working
description: Cómo trabajamos juntos: convenciones, comunicación, git, decisiones.
tags:
  - equipo
  - convenciones
---

# Ways of working

Reglas mínimas para trabajar bien en un sprint corto.

## Comunicación

- **Canal principal:** {{WhatsApp / Slack / Discord — definir}}
- **Status diario** corto (1 mensaje): qué hice ayer / qué haré hoy / bloqueos.
- **Reuniones síncronas** solo cuando hace falta decidir algo entre todos.
- Si una conversación se vuelve "decisión grande", **mover a reunión** + registrarla en [Reuniones](../reuniones/index.md).

## Decisiones

- **Decisiones técnicas que afectan a más de uno:** ADR.
- **Decisiones de producto:** se discuten, se anotan en la reunión, y la decisión final queda en la página de la idea seleccionada.
- **Empate persistente:** decide el Owner del equipo; explicar por qué en el ADR/reunión.
- Una vez decidido, **no re-discutimos** salvo que cambie el contexto. Si cambia, ADR nuevo.

## Git y wiki

- Branch único `main` con commits frecuentes.
- Mensajes de commit descriptivos: `wiki: agrega nota research sobre Ley Fintech`.
- Cualquier cambio en la wiki dispara redeploy automático a GitHub Pages.
- **Para el código del prototipo** (otro repo, a partir del 6 de mayo): PRs con review aunque sea rápido.

## Documentación

- **Lo que cuesta entender dos veces** se documenta.
- **Glosario vivo:** si tuviste que googlear un término, súbelo a [Glosario](../definiciones/glosario.md).
- **Reuniones:** transcripción + resumen ejecutivo.
- **Decisiones técnicas:** ADRs.
- **Ideas:** plantilla con scoring.

## Tiempos

- Sesiones de trabajo de **bloques de 90 minutos** con descansos.
- **Demo gates** durante el lab: cada 8 horas mostramos el progreso al resto del equipo.
- **Stop loss:** si una rama técnica no funciona en 2 horas, abandonar y probar otra.

## Calidad mínima del prototipo

- Funciona end-to-end (aunque sea con datos parciales).
- Cita fuentes en cada respuesta del agente.
- Tiene fallback cuando no encuentra información ("no tengo información oficial sobre esto").
- No expone secrets.
- Demo grabada como respaldo.

## Cuidado del equipo

- Comer y dormir son no-negociables.
- Si alguien está agotado, **rotar tareas**.
- En el pitch, **todos suben** aunque hable solo uno.

## Anti-patrones acordados

- No reinventar lo que ya existe en MCPs/librerías oficiales.
- No agregar features fuera de scope sin reunión.
- No hacer cambios mayores en las últimas 6 horas (riesgo de romper la demo).
- No commitear secrets ni datos personales.

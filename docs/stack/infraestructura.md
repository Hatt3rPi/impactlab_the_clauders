---
title: Infraestructura
description: Hosting, deploy, secrets y observabilidad del prototipo.
tags:
  - stack
  - infra
---

# Infraestructura

Decisiones sobre **dónde corre** el prototipo, cómo se despliega y cómo lo monitoreamos.

## Restricciones del lab

- **48 horas** netas para construir + presentar.
- Demo se hace **en vivo** en el venue (con internet del lugar — asumir flaky).
- Necesitamos **fallback offline** o backup grabado.

## Opciones de hosting

| Opción | Pros | Contras | Recomendado para |
|---|---|---|---|
| **Local + ngrok / Cloudflare Tunnel** | Setup más rápido, sin deploy | Depende de la máquina del demo | Demo en vivo |
| **Vercel / Netlify (front)** | Deploy automático, gratis | Front estático o serverless | Front del prototipo |
| **Render / Fly.io / Railway (back)** | Deploy simple de un servicio Python/Node | Free tier limitado | Backend del agente |
| **AWS / GCP / Azure** | Producción real | Setup tarda; no necesario para 48 h | No |

## Stack tentativo

> A confirmar en [ADR](../especificaciones/adrs/index.md) cuando se decida.

- **Front:** algo simple — Next.js, SvelteKit o Streamlit/Gradio si queremos ir rápido.
- **Back:** Python (FastAPI) o TypeScript (Hono / Express).
- **Vector store:** Chroma o LanceDB local (sin servidor).
- **Hosting:** combo Vercel (front) + Render/Fly (back) con tunnel local como plan B.

## Secrets

- API keys de Claude **nunca** en el repo.
- Usar `.env.local` ignorado por git.
- Cada miembro tiene su propio key (USD 50 c/u).
- Para deploy: variables de entorno del provider.

```bash
# .env.example (este sí va al repo)
ANTHROPIC_API_KEY=
DATABASE_URL=
```

## Observabilidad

Mínimo viable para 48 h:

- **Logs** estructurados de cada call al modelo (modelo, latencia, tokens, costo).
- **Trace** de cada turno del agente (qué tools llamó, qué devolvió, qué generó).
- **Alerta visual** en consola si una llamada falla.

Si queda tiempo:

- Dashboard tipo Streamlit con tokens consumidos en tiempo real.
- Replay de sesiones para debug.

## Plan de contingencia para el demo

1. **Demo grabada** (~2 min) lista en YouTube/Drive como fallback.
2. **Snapshots de respuestas** del agente en JSON para mostrar sin internet.
3. **Hotspot del celular** como red secundaria.
4. **Pipa de errores** (try/catch global) para que la app no se caiga visiblemente en el pitch.

## Decisiones pendientes

- Dónde corre el front durante el demo.
- Vector store concreto.
- Si publicamos el prototipo o solo el video del demo.

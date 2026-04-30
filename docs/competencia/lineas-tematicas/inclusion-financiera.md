---
title: Inclusión financiera
description: Línea 1 — Hacer la regulación comprensible al ciudadano vía agentes conversacionales.
tags:
  - lineas
  - inclusion-financiera
---

# Inclusión financiera

<!-- AUTO-BANNER -->
!!! note ":material-bank: Información oficial del lab"
    Extraído del sitio oficial del [Claude Impact Lab Chile 2026](https://fintech.benditaia.cl/es) (WebFetch 2026-04-29). Confirmar con la organización antes del 6 de mayo.

> *Hacer la regulación comprensible mediante agentes conversacionales en lenguaje claro.*
> — Descripción oficial del lab.

!!! success "Línea elegida"
    El equipo eligió esta línea el [29/04](../../reuniones/2026-04-29-definicion-problema-setup.md). Ver [ADR 0002](../../tu-plata-mipyme/especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md). Estamos ahora en levantamiento de problemas concretos dentro de esta línea.

## Problema según el lab

- La **Ley Fintech 21.521** y sus circulares están escritas en lenguaje técnico-legal denso.
- El ciudadano no sabe cuáles son sus **derechos y obligaciones** (apertura de cuenta, comisiones, deudas, productos financieros).
- Los **emprendedores** sufren confusión tributaria y de cumplimiento (SII, requisitos para registrarse como Fintech, etc.).

## Stakeholders

| Stakeholder | Rol |
|---|---|
| **Ciudadano** | Usuario final del agente |
| **CMF** | Regulador del sistema financiero |
| **SII** | Autoridad tributaria |
| **SERNAC** | Defensor del consumidor |
| **FinteChile** | Gremio de la industria |
| **Emprendedor / PyME** | Sub-segmento con dolor agudo |

## Fuentes / datasets relevantes (a explorar)

- Ley Fintech 21.521 (texto íntegro publicado).
- Circulares y normas de carácter general de la **CMF**.
- FAQs y guías de **SII** sobre tributación digital.
- Alertas y boletines de **SERNAC**.
- Tasas de bancarización y exclusión financiera (datos públicos del Banco Central).

> Profundizar en [Stack · Datasets](../../tu-plata-mipyme/especificaciones/stack/datasets.md).

## Tipos de solución típicos

- **Chatbot RAG** sobre la Ley Fintech con citación obligatoria de fuente.
- **Agente que traduce** un contrato bancario o caja de cumplimiento a lenguaje claro.
- **Simulador** de "qué le aplica a mi caso" (ej: emprendedor que quiere ofrecer crowdfunding).
- **Asistente de cumplimiento** para PyMEs (qué tengo que reportar a SII y cuándo).

## Pros para nuestro equipo

- Datasets disponibles y abundantes.
- Encaje claro con RAG agéntico + citación.
- Es la línea **central** del lab según la narrativa oficial.

## Contras / riesgos

- Probablemente la línea **más popular** → más competencia interna.
- **Alucinación legal** es altísimo riesgo: descalifica.
- Demos de chatbot pueden verse genéricas.

## Diferenciadores posibles

- Foco en un **nicho subatendido** (ej: emprendedoras, adultos mayores, comunidades migrantes).
- **Multimodal**: voz + texto, accesibilidad.
- **Workflow agéntico** que va más allá del chat (genera documentos, agenda, completa formularios).

## Ideas del equipo

> Por ahora vacío. Agregar ideas en [Ideas](../ideas-evaluadas/index.md) etiquetadas con `inclusion-financiera`.

## Research relacionado

> Ver [Research · Regulatorio](../research/regulatorio/index.md) y [Research · Usuarios](../research/usuarios/index.md).

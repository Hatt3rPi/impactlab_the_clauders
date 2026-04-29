---
title: Ciberseguridad ciudadana
description: Línea 2 — Proteger al ciudadano de fraudes digitales con herramientas accesibles de IA.
tags:
  - lineas
  - ciberseguridad
---

# Ciberseguridad ciudadana

> *Proteger a los ciudadanos del fraude digital con herramientas de IA accesibles.*
> — Descripción oficial del lab.

## Problema según el lab

- Vulnerabilidad ciudadana ante **phishing, smishing, fraudes con QR, suplantación de identidad, estafas con IA**.
- **Asimetría informativa:** el ciudadano no sabe distinguir señales de fraude.
- Crecimiento de fraudes financieros digitales reportados por SERNAC y bancos.

## Stakeholders

| Stakeholder | Rol |
|---|---|
| **Ciudadano** | Víctima potencial / usuario final |
| **SERNAC** | Recibe denuncias y emite alertas |
| **CMF** | Supervisa fraude en sistema financiero |
| **PDI / Brigada del Cibercrimen** | Persecución penal |
| **Bancos / Fintechs** | Implementan controles |

## Fuentes / datasets relevantes (a explorar)

- Alertas de fraude publicadas por **SERNAC**.
- Reportes de incidentes de **CSIRT de Gobierno**.
- Estadísticas de fraude bancario (públicas o agregadas).
- Tipologías de fraude documentadas por la **PDI**.
- Bases de URLs / dominios maliciosos (PhishTank, Google Safe Browsing).

> Ver [Stack · Datasets](../stack/datasets.md).

## Tipos de solución típicos

- **Analizador de mensajes**: pegas un SMS/email/WhatsApp y la IA dice si es fraude + por qué + qué hacer.
- **Simulador entrenador**: usuario practica detectar fraudes en un entorno seguro, IA califica.
- **Agente de denuncia asistida**: te guía paso a paso a denunciar a SERNAC/banco/PDI.
- **Verificador de identidad de un emisor**: el agente revisa si el correo/dominio/cuenta bancaria que te contactó es legítimo.

## Pros para nuestro equipo

- **Demo visualmente fuerte** (alertas rojas, casos reales, gamificación).
- Tema **socialmente urgente**, fácil pitch emocional.
- Encaje natural con **agentic thinking** (el agente investiga, valida, recomienda).

## Contras / riesgos

- **Falsos negativos** son costosos (si decimos "este SMS es seguro" y no lo es, hay daño real).
- Datasets de fraude reales pueden estar **menos estructurados** que la regulación.
- Tentación de hacer un "anti-virus" que en 48 h no se logra.

## Diferenciadores posibles

- Foco en un **vector específico** (ej: solo fraudes con IA generativa, deepfakes de voz).
- **Vínculo directo a denuncia** (no solo detectar, sino acompañar).
- **Educación adaptativa** según el perfil del usuario (adulto mayor vs joven).

## Ideas del equipo

> Por ahora vacío. Agregar ideas en [Ideas](../ideas/index.md) etiquetadas con `ciberseguridad`.

## Research relacionado

> Ver [Research · Mercado](../research/mercado/index.md) y [Research · Usuarios](../research/usuarios/index.md).

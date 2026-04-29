---
title: Protección de datos
description: Línea 3 — Empoderar al ciudadano con sus derechos ARCO sobre datos financieros.
tags:
  - lineas
  - proteccion-datos
---

# Protección de datos

<!-- AUTO-BANNER -->
!!! note ":material-bank: Información oficial del lab"
    Extraído del sitio oficial del [Claude Impact Lab Chile 2026](https://fintech.benditaia.cl/es) (WebFetch 2026-04-29). Confirmar con la organización antes del 6 de mayo.

> *Empoderar a las personas para controlar sus datos financieros mediante guías interactivas y agentes de derechos ARCO.*
> — Descripción oficial del lab.

!!! warning "Línea descartada"
    El equipo descartó esta línea el [29/04](../reuniones/2026-04-29-definicion-problema-setup.md). Razón: actúa *después* de que el usuario ya está dentro del sistema; preferimos atacar el problema raíz (inclusión financiera). Ver [ADR 0002](../especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md). Esta página queda como referencia y la portabilidad de información personal sigue siendo una idea interesante para futuras iteraciones.

## Problema según el lab

- El ciudadano **no sabe qué datos suyos** están en el sistema financiero ni quién los tiene.
- Los **derechos ARCO** (Acceso, Rectificación, Cancelación, Oposición) son **invisibles** en la práctica.
- La **Ley 19.628** de protección de datos personales y la nueva normativa (en consolidación) son técnicas y poco aprovechadas.
- **Open Finance** (parte de la Ley Fintech) introduce mecanismos de portabilidad que el público desconoce.

## Stakeholders

| Stakeholder | Rol |
|---|---|
| **Ciudadano / titular del dato** | Sujeto de derechos |
| **Bancos, Fintechs, comercios** | Tratan los datos |
| **CMF** | Regula Open Finance y datos en el sistema financiero |
| **Autoridad de Protección de Datos** | Ente fiscalizador (en formación bajo nueva ley) |
| **DICOM / Equifax** | Burós que mantienen historial financiero |

## Fuentes / datasets relevantes (a explorar)

- **Ley 19.628** (protección de datos personales).
- Normativa CMF sobre **Open Finance** y portabilidad.
- Texto de la Ley Fintech 21.521, secciones sobre portabilidad.
- Modelos de **solicitud ARCO** publicados por organismos.
- Casos publicados por **SERNAC** sobre tratamiento indebido.

> Ver [Stack · Datasets](../stack/datasets.md).

## Tipos de solución típicos

- **Mapa de "tus datos en X institución"**: a partir de inputs del usuario, el agente explica qué tipos de datos típicamente tiene cada institución.
- **Generador de cartas ARCO**: el usuario describe el problema, la IA redacta la solicitud formal y le indica dónde enviarla.
- **Agente que monitorea cambios** en políticas de privacidad de servicios financieros del usuario.
- **Wallet de consentimientos**: el usuario ve qué consentimientos ha dado y cómo revocarlos.

## Pros para nuestro equipo

- **Línea menos popular** → menos competencia interna probablemente.
- Excelente encaje con **agentes** (investigan, redactan, agendan).
- **Diferenciación clara** vs apps comerciales existentes.
- **Impacto cívico medible**: número de cartas ARCO enviadas.

## Contras / riesgos

- **Tema más abstracto** para el usuario común — pitch debe ser muy concreto.
- **Riesgo legal** si la carta generada contiene errores formales.
- Datasets más dispersos.

## Diferenciadores posibles

- Foco en un **caso de dolor agudo** (ej: dejar DICOM, eliminar dato erróneo, salir de marketing).
- **Visualización única** del flujo de datos del usuario.
- **Integración con Open Finance** del lado de portabilidad.

## Ideas del equipo

> Por ahora vacío. Agregar ideas en [Ideas](../ideas/index.md) etiquetadas con `proteccion-datos`.

## Research relacionado

> Ver [Research · Regulatorio](../research/regulatorio/index.md).

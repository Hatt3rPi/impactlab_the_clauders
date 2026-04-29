---
title: "ADR 0002 — Selección de línea temática: Inclusión Financiera"
estado: "Aceptado"
fecha: 2026-04-29
autor: "The Clauders (decisión de equipo en reunión kickoff)"
tags:
  - adr
  - linea-tematica
---

# ADR 0002 — Selección de línea temática: Inclusión Financiera

## Contexto

El Claude Impact Lab Chile 2026 ofrece tres líneas temáticas y exige elegir **una**:

1. **Inclusión financiera** — regulación comprensible vía agentes conversacionales.
2. **Ciberseguridad ciudadana** — herramientas accesibles contra fraude digital.
3. **Protección de datos** — derechos ARCO y portabilidad de información personal.

El equipo (Felipe, Jose, Cristian, Anahi) discutió las tres en la reunión de kickoff del 2026-04-29 con base en:

- **Perfil del equipo:** mezcla de planificación financiera (Felipe), producto (Jose), apoyo técnico (Cristian) y UX/análisis de datos (Anahi). No somos un equipo full técnico ni full ciberseguridad.
- **Research previo de Jose** (cruce CMF + Impact Lab + otras fuentes) que identifica como problemas grandes en Chile: reclamos en SERNAC (~700K), ciberataques, morosidad y **alfabetización financiera**.
- **Tesis articulada en la reunión:** "Chile tiene la legislación financiera y de privacidad más alineada (a estándares internacionales), pero carece de traducción operativa. Las leyes dibujan un consumidor protegido, pero en la práctica no sabe ejercer."

## Decisión

**Elegimos *Inclusión financiera* como línea temática.**

- Atacamos el **problema raíz** del ciudadano financiero chileno: no comprende sus derechos ni el sistema.
- Las otras dos líneas (ciberseguridad y protección de datos) actúan *después* de que el usuario ya está dentro del sistema; queremos intervenir antes de que se generen problemas downstream.
- Es la línea donde el equipo siente más comodidad (Felipe y Cristian explícitamente la prefieren; Anahi y Jose neutrales pero alineados con el argumento del problema raíz).

## Consecuencias

### Positivas

- **Mayor superficie de ideas** ("hay un montón de carne", según Felipe). Espacio amplio para diferenciarnos por sub-segmento.
- **Más datasets disponibles** y bien estructurados (Ley Fintech 21.521, normativa SII, FAQs públicas) → menor riesgo de alucinación si hacemos RAG bien.
- **Encaje natural con criterio de Impacto Cívico (25 %)** — la conexión "ciudadano abrumado por la regulación → solución que traduce" es directa de pitchear.
- **Mejor alineación con el perfil del equipo** — combinación de research de producto, UX y building técnico, sin necesidad de profundo expertise en seguridad.

### Negativas / costos

- **Es la línea probablemente más popular del lab.** Riesgo de competir contra muchos equipos haciendo "RAG sobre regulación financiera". Mitigación: foco temprano en sub-segmento específico y diferenciador agentic, no solo conversacional.
- **Riesgo alto de alucinación regulatoria** (descalificador del lab). Mitigación: citación obligatoria en cada respuesta, fallback explícito ("no tengo información oficial sobre esto"), validación manual antes del pitch.
- **Demos de chatbot pueden verse genéricas.** Mitigación: workflow agéntico que vaya más allá del chat (genera documentos, agenda, completa formularios reales).

### Neutras / a observar

- Necesitamos **definir el sub-segmento concreto** (PyMEs, emprendedores, adultos mayores, jóvenes con DICOM, mujeres, migrantes...) en las próximas reuniones. La línea elegida no agota la decisión.
- La **portabilidad de información personal** (idea de Felipe inspirada en la nueva Ley de Protección de Datos) queda en el backlog como diferenciador potencial si encaja con la solución final.

## Alternativas consideradas

### Opción A — Ciberseguridad ciudadana

- **Pros:** demo visualmente fuerte (alertas, simulaciones de fraude); tema socialmente urgente; encaje natural con agentic thinking.
- **Contras:** requiere expertise técnico-de-seguridad que no tenemos; falsos negativos son costosos y sensibles; ciberseguridad es campo que cambia muy rápido (Blue/Red teams con IA).
- **Razón de descarte:** explícita en la reunión: *"no me siento cómodo con ciberseguridad porque es muy técnico, muy sensible"* (Cristian) y *"con nuestra inexpertiza técnica creo que no"* (Jose).

### Opción B — Protección de datos

- **Pros:** menos popular → menos competencia interna; excelente encaje con agentes (investigan, redactan cartas ARCO, agendan); diferenciación clara vs apps comerciales.
- **Contras:** tema más abstracto para el ciudadano común (pitch más difícil); riesgo legal si la carta ARCO generada contiene errores formales; datasets más dispersos.
- **Razón de descarte:** actúa sobre usuarios que ya están dentro del sistema, no en la raíz; equipo prefiere intervenir antes. La portabilidad de datos personales queda como **idea backlog** dentro del proyecto principal.

## Referencias

- Reunión: [kickoff 2026-04-29](../../reuniones/2026-04-29-definicion-problema-setup.md).
- Línea elegida: [Inclusión financiera](../../lineas-tematicas/inclusion-financiera.md).
- Research base: [Research · Regulatorio](../../research/regulatorio/index.md) (research de Jose pendiente de subir).

## Relacionados

- ADR 0003 (Plataforma web mobile-first) se decidió en la misma reunión y es independiente de la línea elegida — aplica a cualquiera de las tres.

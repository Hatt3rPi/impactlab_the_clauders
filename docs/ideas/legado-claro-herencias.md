---
title: "Idea: Legado Claro / Herencia Bot — el mapeo post-mortem"
description: "Sube el certificado de defunción y la IA genera un cronograma visual de los trámites para reclamar AFP, seguros, acreencias y cuota mortuoria sin perder plazos."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: activa
prioridad: estrella
tags:
  - idea
  - inclusion-financiera
  - herencia
  - posesion-efectiva
  - afp
---

# Idea: Legado Claro / Herencia Bot — el mapeo post-mortem :material-star:

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md) y validada con cifras del [run #04 (transferencias no activadas)](../research/usuarios/transferencias-no-activadas-chile-2026.md). **Aún no validada por el equipo.**

> *Cuando muere un familiar, el deudo enfrenta plazos vencidos y burocracia ciega para reclamar AFP, seguros, cuotas mortuorias y acreencias. Legado Claro recibe el certificado de defunción y genera un cronograma visual día por día con borradores listos de cada trámite.*

> :material-star-circle: **Cubre directamente el dolor más explosivo del [run #04](../research/usuarios/transferencias-no-activadas-chile-2026.md)**: gap del **41 % en herencias AFP** = **CLP 93.000 millones (USD 98 M)** abandonados, 220.000 afiliados fallecidos sin trámite. Es **9× el promedio de gaps**.

## Problema

- **220.000 afiliados AFP fallecidos** con saldos remanentes; el **41 %** de las familias **no ejerce ninguna acción de cobro** ([Asociación de AFP](https://aafp.cl)).
- Promedio dejado sin cobrar por causante: **CLP 8,8 a 17,6 millones**.
- **CLP 94.444-106.845 millones (2025)** en acreencias bancarias caducables, en su mayoría de fallecidos, que pasarán a Bomberos.
- Seguros de vida con primas bajo 200 UF **no son reportados centralmente** — los beneficiarios ignoran su existencia.
- Saldos a favor en tarjetas de crédito **son absorbidos** por las emisoras tras el fallecimiento.

**Fricción raíz:**

1. **Costo del trámite intermedio:** la posesión efectiva (necesaria si el saldo excede 5 UTA ≈ CLP 2,6 M) cuesta sobre CLP 100.000 + abogado + notario, justo cuando la viuda no tiene liquidez.
2. **Desconocimiento:** los herederos no saben que los fondos AFP son heredables.
3. **Fragmentación institucional:** el Estado notifica el fallecimiento pero **no consolida proactivamente** los activos financieros distribuidos en el sistema mixto (público/privado).

## Hipótesis

Si el deudo puede subir una foto del **certificado de defunción** y obtener un **cronograma visual ordenado por urgencia** con borradores listos para cada trámite, no perderá los activos por desconocimiento o plazos vencidos.

## Propuesta

### Qué hace

- **Recibe** foto / PDF del certificado de defunción.
- **Vision** extrae nombre del causante, RUT, fecha y causa de muerte.
- **Cruza** asíncronamente:
    - Base CMF de Acreencias Bancarias (RUT del fallecido).
    - Sistema [Conoce tu Seguro CMF](https://www.cmfchile.cl/conoce-tu-seguro/) (seguros con beneficiarios).
    - Información de cuota mortuoria de las AFPs.
    - Pensión de sobrevivencia (cónyuge, hijos menores).
- **Genera cronograma estructurado** (timeline visual):
    - **Día 1:** solicitar Posesión Efectiva (borrador del formulario).
    - **Día 15:** con la posesión, ir a CMF Conoce tu Seguro a cobrar seguros de desgravamen.
    - **Día 30:** rescatar la cuota mortuoria en AFP.
    - **Día 45:** si el saldo excede 5 UTA, posesión efectiva ante notario.
- **Genera artefactos:** PDFs prellenados, eventos `.ics` con fechas límite, cartas tipo.

### Qué NO hace

- No tramita por el deudo (ClaveÚnica restringida a privados).
- No asesora legalmente (disclosure permanente).
- No identifica seguros bajo 200 UF si la prima no fue declarada centralmente.

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 (Vision + razonamiento sucesorio + Citations).
- **Patrones agénticos:**
    - **Vision:** extracción de datos del certificado de defunción.
    - **Tool use** paralelo: 4 fuentes consultadas simultáneamente (CMF Acreencias, Conoce tu Seguro, AFP info, Sup. Pensiones).
    - **Structured Outputs:** schema timeline `[{dia, tramite, institucion, monto_estimado, plazo_caducidad, accion_link}]`.
    - **Citations** a Ley 21.484, Código Civil herencias, normativa Sup. Pensiones.
- **Workaround ClaveÚnica:** mock OAuth + JWT sintético, narrativa "delegación bajo mandato del usuario via integradores B2B como [e-cert](https://www.e-cert.cl/)" (ver [Datasets sub-utilizados](../research/tecnologia/datasets-subutilizados-y-cruces.md)).

## Demo imaginada (60 segundos)

1. **Inicio:** "María perdió a su esposo Juan hace 2 meses. No sabe qué tramitar."
2. **Acción:** sube el certificado de defunción al WhatsApp del bot.
3. **Magia:** en 8 segundos:
    - "Juan tenía **CLP 8,2 millones** en su cuenta AFP Habitat, **heredables**."
    - "Tiene un seguro de desgravamen con BancoEstado por **CLP 4,5 M**, beneficiaria: María."
    - "Hay **CLP 312.000** en una cuenta vista de Banco de Chile **caducables el 14-mar-2027**."
    - "Cronograma de trámites:" → calendar visual con 4 hitos.
4. **Cierre:** botón "descargar borrador de posesión efectiva".

## Scoring (criterios oficiales)

| Criterio | Peso | Score (0-1) | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,95 | 23,75 |
| Uso responsable de datos | 20 | 0,80 | 16,00 |
| Claude & Agentic Thinking | 25 | 0,95 | 23,75 |
| Funcionalidad | 15 | 0,75 | 11,25 |
| Calidad del pitch | 15 | 0,90 | 13,50 |
| **Total** | **100** | | **88,25** |
| Bonus agentic (+5) | 5 | 0,90 | +4,50 |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M-L (4 fuentes paralelas + cronograma + borradores legales).
- **Riesgos técnicos:**
    - ClaveÚnica no es API pública → mock o extensión Chrome.
    - Privacidad de datos de personas fallecidas (PII sensible).
    - Variabilidad del certificado de defunción según comuna.
- **Datos disponibles ya:** parcial (CMF público; Sup. Pensiones agregada; AFP individual cerrada).
- **Demo end-to-end factible:** sí, con datos de prueba o un caso real anonimizado.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Privacidad: certificado contiene datos sensibles | Alta | Alto | No persistir imagen original; anonimizar logs |
| Falsa esperanza si no hay activos identificables | Media | Medio | Disclaimer permanente: "esto es preliminar, valide con la institución" |
| Borrador de posesión efectiva con error formal | Media | Alto | Validar plantilla con notario o abogado del consumidor antes del demo |
| ClaveÚnica restringida bloquea integración real | Alta | Medio | Mock OAuth para demo; pitch del "post-lab" con e-cert |

## Por qué gana

- **Cubre la cifra más explosiva del research** (gap 41 % AFP).
- **Transforma un dolor emocional inmenso** (luto + burocracia) en un proceso mecánico empático — *empatía algorítmica*.
- **Caso análogo verificable:** [LifeSG (Singapur)](https://www.life.gov.sg) concentra servicios gubernamentales por hitos de vida, con módulos específicos para herencias.
- **Stakeholders alineados:** AFPs (no quieren custodiar fondos sin reclamar), CMF (Acreencias), Reg. Civil (defunciones), Sup. Pensiones — todas tienen incentivo en presentar esto.

## Próximos pasos para validar

- [ ] Conseguir 3 certificados de defunción reales (anonimizados) para spike Vision.
- [ ] Spike Tool use paralelo: cruzar 1 RUT contra CMF + Conoce tu Seguro en <5 s.
- [ ] Validar plantilla de posesión efectiva con un notario.
- [ ] Entrevistar a 3 viudas recientes para validar el cronograma propuesto.
- [ ] Conseguir LOI con AFP Modelo o Habitat (gerencias de innovación).

## Notas y referencias

- **Caso análogo internacional:** [LifeSG (Singapur)](https://www.life.gov.sg) — concentración de servicios gubernamentales por hitos de vida.
- **Como módulo de [sabidurIA ciudadana](sabiduria-ciudadana.md):** este es el **segundo de los 3 módulos perfectos** para el demo del 7 de mayo (junto con Rescate Ciudadano y un tercero a elegir).
- **Cruce con runs:** valida cifras del [#04 transferencias no activadas](../research/usuarios/transferencias-no-activadas-chile-2026.md) y datasets del [#03 sub-utilizados](../research/tecnologia/datasets-subutilizados-y-cruces.md).
- Catálogo completo de origen: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

---
title: PITCH — Tu Plata Mipyme
description: Material de pitch para el Claude Impact Lab Chile 2026 — narrativa ejecutiva del problema, solución, impacto y diferenciador del equipo The Clauders.
tags:
  - tu-plata-mipyme
  - pitch
  - lab
---

# PITCH — Tu Plata Mipyme

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Material de pitch del equipo The Clauders para el [Claude Impact Lab Chile 2026](../competencia/index.md). Cada slide responde una pregunta del jurado y se sostiene en datos del [PRD](PRD.md), del [run #06 de deep research](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md) y del [plan técnico](plan.md). Sin tecnicismos en la primera línea — el problema y el valor primero, la tecnología después.

| | |
|---|---|
| **Versión** | 1.0 |
| **Fecha** | 2026-04-30 |
| **Equipo** | The Clauders (Felipe · Jose · Cristian · Anahi) |
| **Pitch final** | 7 de mayo de 2026 · 12:00 · Espacio Riesco · 5 minutos |
| **Documentos relacionados** | [PRD](PRD.md) · [Plan de implementación](plan.md) · [Backlog](backlog.md) · [Dolores](dolores.md) · [ADR-0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md) |

> **Cómo leer este documento.** Cada *slide* corresponde a un mensaje del pitch — el título de cada slide es la conclusión, no el tema. La narrativa va de **problema cuantificado → solución como capacidad habilitada → impacto proyectado en 3 escenarios → diferenciador → cierre con recomendación al jurado**. Los slides 1-5 son el bloque que se presenta en vivo (≈4 minutos); los slides 6-10 son material de back-up para preguntas y contexto del jurado.

---

## Slide 1 — Hook

### "1,08 millones de chilenas y chilenos sostienen su negocio en la informalidad. La asesoría que necesitan ya existe — pero está fuera de su alcance."

**Subtítulo:** Tu Plata Mipyme es el copiloto que la pone en su WhatsApp.

**Soporte de slide (visual):**

- Cifra grande: **1,08 M** *(microemprendedores informales en Chile, INE EME8)*
- Banner inferior: *59 % son mujeres · 38 % de informalidad en Araucanía · brecha de ingresos -43,7 % en Los Ríos*

**Por qué este hook funciona.** Un solo dato del INE convierte el "problema social genérico" en magnitud concreta. No abre con tecnología; abre con la persona afectada. El jurado entiende en 10 segundos qué problema atacamos y a qué escala.

*Fuente:* [que-es.md](que-es.md) · [run #06](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md)

---

## Slide 2 — Problema: el costo del statu quo

### "El costo de la informalidad no es solo no pagar impuestos. Es perder ingresos, plata pública asignada y oportunidades de crecimiento."

**3 dimensiones cuantificables del costo actual** (referencia [PRD §1.3.1](PRD.md#131-cuantitativos)):

| Dimensión | Cifra | Significa |
|---|---|---|
| **Plata dejada en la mesa** | **>50 % de las postulaciones a SERCOTEC/CORFO se rechazan** por mala formulación. **44 %** declara financiamiento como su barrera #1. | Capital público existe pero no llega a quien debía llegar. |
| **Sobrepago tributario** | Dueños únicos pagan **27 %** de primera categoría cuando calificarían a **0 %** en Pro-Pyme Transparente (Art. 14 D N°8). | Sistema diseñado para protegerlos los castiga por desconocimiento. |
| **Mortalidad temprana** | **~60 %** de las ideas informales mueren **antes de la primera venta**. **35-40 %** de los borradores RES (Tu Empresa en Un Día) no se firman. | El emprendedor abandona en la rampa, no en la pista. |

**Y el efecto cualitativo crítico** (que ningún dato cuantifica solo): **miedo irracional al SII** transversal a todo el journey. *"El SII me va a multar antes de empezar"* es el bloqueo psicológico que cierra la puerta de entrada antes de que el emprendedor haga nada.

**Resumen de slide.** El problema no es "informalidad como problema cultural". Es un sistema de asesoría caro, geográficamente concentrado, lingüísticamente denso, y un canal digital que asume que el usuario "buscará un sitio web" — cuando el segmento vive en WhatsApp. *(Detalle completo en [PRD §1.3](PRD.md#13-impactos-observables))*

---

## Slide 3 — Solución: la capacidad habilitada

### "Un copiloto que conversa por WhatsApp, acompaña al ritmo del usuario y lo deriva al instrumento estatal correcto. Cuatro especialistas, un solo hilo."

**Lo que el usuario obtiene** (no la tecnología — la capacidad):

1. **Conversa por WhatsApp** en su idioma, con mensajes ≤ 160 caracteres y una idea por mensaje. Cero instalación. Cero curva de aprendizaje de UI.
2. **Lo acompaña, no lo sustituye.** Captura ventas y gastos día a día, muestra utilidad real, recuerda plazos. *"No te calculo, te enseño lo que debes saber"* es la regla anti-alucinación.
3. **Cuatro especialistas según su etapa.** `mentor-inicio` cuando recién está soñando · `acompanante-informal` cuando ya vende sin formalizar · `gestor-formalizacion` cuando da el paso al SII · `estratega-crecimiento` cuando postula a CORFO/SERCOTEC.
4. **Cita la norma — siempre.** Cada respuesta tributaria o legal lleva link verificable a SII, CORFO, SERCOTEC o CMF. Sin cita, no responde.
5. **Gratis hasta que pagar conviene.** Free indefinido para soñador e informal activo. Pro ($4.990/mes) cuando se formaliza. Plus ($15.000-30.000/postulación) cuando aplica a subsidio. Marketplace de asesores humanos (10-15 % comisión) cuando el caso lo requiere.

**Soporte visual del slide.** Diagrama TO-BE del [PRD §2.1](PRD.md#21-estado-futuro-deseado) con los 4 agentes, sus tools clave y el handoff JSON entre etapas.

*Fuente:* [plan.md §3](plan.md#3-journey-del-emprendimiento-4-etapas-4-agentes) · [ADR-0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md)

---

## Slide 4 — Diferenciador

### "Mientras los demás equipos hacen RAG sobre PDF de la CMF, nosotros construimos el copiloto donde el usuario ya vive."

**4 ejes de diferenciación** frente a los ~200 equipos del lab:

| Eje | Lo que hará la mayoría | Lo que hace Tu Plata Mipyme |
|---|---|---|
| **Canal** | Web o app — el usuario tiene que llegar | WhatsApp — el copiloto está donde el usuario ya está (95,3 % penetración mobile) |
| **Arquitectura IA** | 1 agente con system prompt monolítico >8k tokens | 4 subagentes con prompts <2k tokens cada uno + supervisor + handoffs JSON estructurados (Agent SDK) |
| **Trazabilidad** | RAG genérico que cita "según el documento" | MCP propio sobre corpus regulatorio chileno con caching >80 %, cita link verificable a SII/CORFO/SERCOTEC |
| **Modelo económico** | Demo bonito, sin economía real | Freemium con triggers contextuales — Free indefinido, cobro en eventos de valor monetario evidente. Capta WTP real sin reproducir la barrera económica |

**Cita del equipo que resume la apuesta** *(Cristian, [reunión 30-abr](../reuniones/2026-04-30-revision-dolores-backlog.md))*:

> *"El servicio terminaría siendo tan bueno que se terminaría siendo un Claude Code gratuito en tu celular vía WhatsApp."*

---

## Slide 5 — Demo plan: un caso, end-to-end, en 90 segundos

### "Una microemprendedora de Quilicura que vende tortas. La acompañamos desde 'vendí 30 mil' hasta 'aquí está tu carta a banco'."

**Flujo dorado de la demo** (RF-04, RF-06, RF-07, RF-08 del [PRD §4.3](PRD.md#43-tabla-de-requerimientos-funcionales-fase-0)):

```
Día 0   → "Hola, me llamo María, vendo tortas, ¿me ayudas?"
          [acompanante-informal asume el caso]

Día 1-7 → "Vendí 30 mil hoy" · "Compré 12 mil de huevos"
          [registra ventas/gastos · expediente persistente en Postgres]

Día 8   → Reporte semanal:
          "Esta semana ganaste $48.000. Si formalizaras en Pro-Pyme,
           pagarías $0 de primera categoría. ¿Te ayudo a dar el paso?"
          [trigger contextual de upgrade, sin presionar]

Día 8+  → [handoff JSON a gestor-formalizacion]
          "Tu negocio cumple los requisitos para Pro-Pyme Transparente.
           Estos son los 4 pasos: Inicio Actividades SII → Boleta
           Electrónica → Patente Quilicura → SEREMI (no aplica)."

Día N   → [genera carta a banco PDF descargable]
          "Aquí está tu carta de presentación con tus 6 meses de
           historial. Llevasela al banco."
```

**Lo que el jurado ve en el slide.** Captura en mobile (modo retrato) de los mensajes WhatsApp + side-panel "thinking" de la web mostrando los handoffs y tools llamados. *Detalle de la implementación en [plan.md §7 Fase 0](plan.md#fase-0-demo-del-lab-7-dias-hasta-2026-05-07).*

---

## Slide 6 — Impacto proyectado: tres escenarios

### "Si ganamos el lab, el impacto a 12 meses se mide en formalizaciones inducidas, subsidios bien postulados y capital público activado."

Aplicamos la lógica de 3 escenarios del [PRD §2.2.1](PRD.md#221-cuantitativos) para proyectar resultados a 12 meses post-lab (Fase 1 → cierre Fase 2). Las cifras se derivan de las metas del [plan.md §8](plan.md#8-metricas-e-impacto).

| Métrica | Pesimista (-20 %) | Conservador (base plan.md) | Optimista (+20 %) |
|---|---|---|---|
| **MAU al cierre Fase 1** (mes 3) | 40 emprendedoras | **50 emprendedoras** | 60 emprendedoras |
| **MAU al cierre Fase 2** (mes 9) | 400 emprendedoras | **500 emprendedoras** | 600 emprendedoras |
| **Retención semana 4** | 32 % | **40 %** | 48 % |
| **Conversión Free → Pro** | 6 % | **8 %** | 10 % |
| **Tasa avance E2 → E3** (formalización inducida) | 4 %/mes | **5 %/mes** | 6 %/mes |
| **Tasa avance E3 → E4** (postulación inducida) | 12 %/mes | **15 %/mes** | 18 %/mes |
| **Reducción rechazo CORFO/SERCOTEC en cohorte asistida** | de >50 % a 35 % | de >50 % a **<25 %** | de >50 % a 18 % |

**Lectura del jurado.**

- **Pesimista.** Adopción más lenta por dependencia de entrevistas reales no cumplidas en el lab. Aún así: 40 microemprendedoras formalizadas + ahorro tributario por activación Pro-Pyme + reducción de multas municipales.
- **Conservador (la apuesta).** Las metas explícitas del [plan.md §8.1-8.2](plan.md#8-metricas-e-impacto). Primer reporte público a SERCOTEC al cierre del trimestre 1.
- **Optimista.** Endorsement de Fondo Esperanza + Hogar de Cristo en Fase 1 → reclutamiento más rápido de las 50-100 emprendedoras objetivo.

**El supuesto crítico que sostiene los 3 escenarios.** Que la organización del lab acepte el modelo freemium para Tu Plata Mipyme (Free indefinido + cobro contextual). Si exige gratuidad total, el escenario muta hacia financiamiento público (riesgo R-13 del [PRD §7](PRD.md#7-riesgos)).

---

## Slide 7 — Cumplimiento de los 5 criterios oficiales del lab

### "Diseñamos para los 5 criterios. Cada decisión del producto suma puntos en al menos dos de ellos."

Mapeo explícito a los criterios oficiales del [Claude Impact Lab Chile 2026](../competencia/criterios-evaluacion.md). Los pesos son los oficiales del lab.

| Criterio | Peso | Cómo lo cumple Tu Plata Mipyme | Auto-score interno |
|---|---|---|---|
| **Impacto** | 25 % | Atacamos un dolor con universo medido (1,08 M) y métricas de impacto cuantificadas (formalizaciones, subsidios, ahorro tributario). El impacto es de tercera dimensión: usuario + Estado + sistema fintech. | 22 / 25 |
| **Datos** | 20 % | Datasets oficiales SII (crítico), SERNAC (parcial), CMF (agregados). Research previo del equipo con 6 deep research runs (incluido el run #06 con 48 dolores cuantificados). MCP propio sobre corpus regulatorio chileno. | 17 / 20 |
| **Claude / Agentic** | 25 % | Multi-agente real (no monolítico): 1 supervisor Sonnet 4.6 + 4 subagentes especializados con system prompts <2k tokens, handoffs JSON estructurados vía Agent SDK + Haiku 4.5 para clasificación + caching >80 % del corpus regulatorio. | 23 / 25 |
| **Funcionalidad** | 15 % | Demo end-to-end de 90 segundos con flujo dorado verificable. 13 RF Must Have implementados; fallback offline pre-grabado para los 2 casos demo principales. Cumplimiento Ley 19.628 + Ley 21.719 desde Fase 0 (consentimiento granular + ARCO). | 13 / 15 |
| **Pitch** | 15 % | Narrativa Problema → Demo → Roadmap en 5 minutos cronometrados con mentores el 5 de mayo. Hook con dato shock + cierre con call to action al jurado. | 13 / 15 |
| **Total auto-score** | **100 %** | | **88 / 100** |

**Meta interna.** ≥ 85/100. Si bajamos de ese umbral en ensayo del 5-may, ajustamos lo que perdió puntos antes del pitch.

---

## Slide 8 — Roadmap post-lab

### "El demo del lab es Fase 0. Las Fases 1-3 ya están planificadas y son ejecutables si ganamos."

Tomado directo de [PRD §3.4](PRD.md#34-roadmap-post-lab-fases-1-3) + [plan.md §7](plan.md#7-roadmap-por-fases):

| Fase | Ventana | Alcance | Hito clave |
|---|---|---|---|
| **0 — Demo del lab** | 7 días previos + 48h del lab | 1 agente operativo (`acompanante-informal`), 2 tools, memoria persistente, demo 90s | Pitch 7-may 12:00 |
| **1 — Piloto cerrado** | mes 1-3 post-lab | Los 4 agentes operativos · MCP SII real · 50-100 emprendedoras reclutadas vía Fondo Esperanza / Hogar de Cristo · marco ARCO/privacidad pulido con asesoría legal | Primer reporte público a SERCOTEC |
| **2 — Apertura** | mes 4-9 | Tier Pro activado (Webpay/Mercado Pago) · Marketplace de asesores en 3 regiones piloto · Reportes anonimizados a SERCOTEC | Primera adjudicación CORFO/SERCOTEC asistida confirmada |
| **3 — Crecimiento** | mes 10+ | Repositorio contable Git-like · Tier Plus generalizado · Integraciones bancarias vía Open Finance (Ley 21.521) | Cohorte ≥ 1.000 emprendedoras |

**Acelera AI Fintech Sandbox.** Si ganamos el lab, los 60 días de aceleración (junio 2026+) se ejecutan dentro de Fase 1.

---

## Slide 9 — Riesgos y mitigaciones

### "El riesgo no es construir mal. Es construir lento o presentar débil. Tenemos un plan para los dos."

Los 4 riesgos críticos del [PRD §7](PRD.md#7-riesgos) que pueden hundir el pitch, con la mitigación ya cableada:

| # | Riesgo | Probabilidad | Impacto | Mitigación cableada |
|---|---|---|---|---|
| R-02 | **Alucinación legal** | Media | Crítico | Toda respuesta normativa pasa por verificador con tool de cita. Sin cita, no responde. *Owner: Cristian.* |
| R-07 | **Falla de Claude API durante el pitch** | Media | Crítico | Fallback offline pre-grabado para los 2 casos demo principales. *Owner: Felipe.* |
| R-10 | **Sobreestimación del alcance: 4 agentes no caben en 48 h** | Alta | Alto | Fase 0 ya recortada a 1 solo agente (`acompanante-informal`). Los otros 3 quedan en Fase 1. *Owner: Jose.* |
| R-12 | **Pitch no transmite la narrativa en 5 minutos** | Media | Crítico | Ensayo cronometrado con mentores el 5 de mayo + ajuste antes del 6. *Owner: Jose.* |

**Lo que el jurado verá si pregunta.** Que cada riesgo ya tiene plan B operativo y owner asignado. *(Tabla completa en [PRD §7](PRD.md#7-riesgos), 14 riesgos · 6 del plan técnico + 8 nuevos del PRD).*

---

## Slide 10 — Recomendación al jurado

### "Tu Plata Mipyme resuelve un problema con métrica nacional, en el canal correcto, con stack agentic real. Vale la pena financiar Fase 1."

**Resumen del argumento al jurado** (cierre del pitch):

1. **El problema es real, medido y nacional.** 1,08 M de microemprendedores informales. >50 % de rechazo en SERCOTEC/CORFO. 35-40 % de borradores RES sin firmar. ~60 % de mortalidad pre-venta.
2. **La solución no es genérica.** Es WhatsApp-first porque el segmento vive ahí; multi-agente porque cada etapa del journey requiere expertise distinta; freemium porque el segmento no puede pagar al inicio pero sí en puntos de inflexión.
3. **El stack es agentic real.** No es RAG sobre PDF. Es Sonnet 4.6 supervisor + Haiku 4.5 clasificador + 4 subagentes Agent SDK + MCPs propios sobre corpus regulatorio chileno con caching >80 %.
4. **El roadmap es ejecutable.** Fase 0 acotada al demo del lab. Fases 1-3 con hitos verificables, partners identificados (Fondo Esperanza, Hogar de Cristo, SERCOTEC) y métricas públicas.
5. **El equipo es disciplinado.** Working tree del repo limpio, ADRs documentados, research previo con 6 deep research runs, PRD y plan técnico publicados antes del lab. *Hay un repo público con todo lo que hicimos.*

**Cita del equipo que cierra el pitch** *(Felipe, [reunión 30-abr](../reuniones/2026-04-30-revision-dolores-backlog.md))*:

> *"Al final es ofrecer la ayuda a que este gallo deje de pensar y se dedique a emprender."*

---

## Anexos

### A. Trazabilidad de cada slide a los datos del repo

| Slide | Mensaje principal | Fuentes principales |
|---|---|---|
| 1 — Hook | Magnitud del problema | [que-es.md](que-es.md) · [run #06](../competencia/research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md) |
| 2 — Problema | 3 dimensiones cuantificadas + miedo SII | [PRD §1.3.1](PRD.md#131-cuantitativos) · [PRD §1.3.2](PRD.md#132-cualitativos) |
| 3 — Solución | Capacidad habilitada por 4 agentes | [PRD §2.1](PRD.md#21-estado-futuro-deseado) · [plan.md §3](plan.md#3-journey-del-emprendimiento-4-etapas-4-agentes) · [ADR-0004](especificaciones/adrs/0004-whatsapp-first-freemium-multiagente.md) |
| 4 — Diferenciador | 4 ejes vs. 200 equipos | [estrategia de pitch](../equipo/estrategia-pitch-lab.md) · [reunión 30-abr](../reuniones/2026-04-30-revision-dolores-backlog.md) |
| 5 — Demo | Flujo dorado de 90s | [PRD §4.3 RF-04, RF-06, RF-07, RF-08](PRD.md#43-tabla-de-requerimientos-funcionales-fase-0) · [plan.md §7 Fase 0](plan.md#fase-0-demo-del-lab-7-dias-hasta-2026-05-07) |
| 6 — Impacto 3 escenarios | Proyección Conservador/Optimista/Pesimista | [PRD §2.2.1](PRD.md#221-cuantitativos) · [plan.md §8](plan.md#8-metricas-e-impacto) |
| 7 — Cumplimiento criterios | Auto-score 88/100 | [criterios-evaluacion](../competencia/criterios-evaluacion.md) |
| 8 — Roadmap | Fases 1-3 + Acelera Sandbox | [PRD §3.4](PRD.md#34-roadmap-post-lab-fases-1-3) · [plan.md §7](plan.md#7-roadmap-por-fases) |
| 9 — Riesgos | 4 riesgos críticos + mitigaciones | [PRD §7](PRD.md#7-riesgos) · [plan.md §9](plan.md#9-riesgos-y-mitigaciones) |
| 10 — Cierre | 5 puntos al jurado | Síntesis del PRD |

### B. Material adicional para preguntas del jurado

- **Si pregunta por privacidad/ARCO** → [plan.md §4.4 Cumplimiento Ley 19.628 + 21.719](plan.md#44-cumplimiento-ley-19628-ley-21719-datos-personales)
- **Si pregunta por modelo de datos** → [plan.md §4.3 Modelo de datos](plan.md#43-modelo-de-datos-nucleo)
- **Si pregunta por system prompts** → [plan.md §5.2 Esqueleto de system prompts](plan.md#52-system-prompts-esqueleto)
- **Si pregunta por costos Anthropic** → [PRD §2.3.3 KPIs técnicos](PRD.md#233-tecnicos) · target < $0,30 USD/usuario activo/mes con caching >80 %
- **Si pregunta por las otras ideas que descartamos** → [PRD §3.5 Out of scope](PRD.md#35-out-of-scope-exclusiones-explicitas) · 24 ideas evaluadas listadas
- **Si pregunta por evidencia en el repo** → [README del repo](https://github.com/Hatt3rPi/impactlab_the_clauders) · ADRs 0001-0004 · 6 deep research runs · PRD + Plan + Backlog + Dolores publicados

### C. Versión y revisiones

| Versión | Fecha | Cambios |
|---|---|---|
| 1.0 | 2026-04-30 | Versión inicial — derivada del PRD v1.0 aplicando lógica de business case (problema cuantificado → solución como capacidad → impacto en 3 escenarios → recomendación al jurado) |

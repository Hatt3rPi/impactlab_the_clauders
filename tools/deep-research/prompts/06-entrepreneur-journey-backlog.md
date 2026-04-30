---
titulo: "Entrepreneur Journey Chile: dolores, soluciones actuales y backlog de funcionalidades para Tu Plata Mipyme"
objetivo: "Levantar el universo (no priorizar) de dolores reales del microemprendedor chileno a lo largo del journey completo y traducirlo en un catálogo extenso de funcionalidades candidatas para el backlog de Tu Plata Mipyme."
agent: "deep-research-max-preview-04-2026"
linea: inclusion-financiera
prioridad: alto
---

# Prompt: Entrepreneur Journey + Backlog Tu Plata Mipyme

## Contexto

El equipo **The Clauders** ya aterrizó la idea ganadora para el **Claude Impact Lab Chile 2026**: **Tu Plata Mipyme**, un copiloto freemium en WhatsApp + Web que acompaña al microemprendedor chileno desde el sueño hasta la PYME, con agentes IA especializados por etapa que hablan en su idioma y citan la norma.

El público objetivo prioritario son **microemprendedores informales chilenos**, con foco en mujeres 30-50 años en regiones del sur (Araucanía 38% de informalidad, 59% de mujeres informales según EME8). El universo es ~1,08M de microemprendedores informales.

El equipo definió 4 subagentes (mentor-inicio, acompañante-informal, gestor-formalización, estratega-crecimiento) y 4 tiers (Free $0, Pro ~$4.990 CLP/mes, Plus $15-30K CLP/evento, Marketplace asesores 10-15% comisión). Pero el **backlog de funcionalidades aún está incompleto** — por ejemplo, no se ha planteado explícitamente acompañar al usuario en empresaenundia.cl de forma personal o con derivación a tercero (contador/abogado).

Este run busca **expandir y enriquecer el backlog** mapeando el journey completo, levantando los dolores reales por etapa, viendo cómo se resuelven hoy y proponiendo funcionalidades concretas que el equipo pueda priorizar en una segunda iteración.

## Lo que necesito

### Sección 1 — Mapeo del journey en 6 etapas

Por cada etapa, mínimo **8-12 dolores documentados** (con fuente: encuestas EME8 INE, Casen, Sercotec, Ministerio de Economía, IPS, Mujeres Sumando, OCDE, BCN):

#### E0 — Idea / sueño
Fricciones cognitivas (¿es viable mi idea?, ¿cuánto cobro?, miedo al SII), apoyo familiar, falta de mentor, mitos vs realidad, autopercepción de "no soy emprendedor".

#### E1 — Validación informal
Vendiendo sin RUT (Mercado Libre, Instagram, ferias, kiosco vecinal, ventas a vecinos), gestión de cobros (transferencias, MACH, Mercado Pago, efectivo), riesgos (decomisos por Carabineros, multas municipales, estafas, falta de respaldo), separar plata personal vs negocio.

#### E2 — Formalización
- **empresaenundia.cl** (paso a paso real, errores comunes, qué automatiza, qué requiere humano).
- Cuándo conviene **MEF** (Microempresa Familiar) vs **EIRL** vs **SpA**.
- Costos ocultos (notario, capital social, contador inicial).
- **Iniciación de actividades en SII** (formulario 4415, errores frecuentes).
- **Patente municipal** (variabilidad por comuna, costos, fricciones).
- **Permisos sanitarios** SEREMI (alimentos, cosmética, etc.).
- **Registro de marca INAPI**.
- Decisión "¿lo hago solo o con contador / abogado / asesor?".

#### E3 — Operación formal
- **Facturación electrónica** (SII Mipyme gratuito vs Bsale/Defontana/Toku/Nubox).
- **F29 mensual** (IVA, retenciones, errores típicos, multas por atraso).
- **F22 anual** (renta).
- **Régimen Pro-Pyme General vs Pro-Pyme Transparente** — implicancias.
- **Boletas de honorarios** propias.
- Cotizaciones previsionales del trabajador independiente (operación renta obligatoria).
- Primer error con SII (multas, recargos, intereses) — ¿cómo se resuelve?

#### E4 — Crecimiento
- **Financiamiento:** FOGAPE, BancoEstado Microempresas, Banigualdad, Fondo Esperanza, Cumplo, factoring, Mutuales, Capital Semilla Sercotec, Capital Abeja Corfo.
- **Primer empleado** (contrato indefinido vs honorarios, PreviRed, finiquito, Ley Karin).
- **Expansión** geográfica/digital (segunda sede, e-commerce, marketplace, exportar).
- **Marketing y ventas** (¿cómo se llega a más clientes?).
- **Gestión inventario y proveedores**.

#### E5 — Recuperación / cierre / pivot
- **Quiebra personal** Ley 21.563 (procedimiento simplificado, costos, estigma).
- **Suspensión temporal de actividades** SII.
- **Cambio de giro**.
- **Reinvención post-fracaso** (qué pasa con DICOM, cómo volver al sistema).
- **Deuda morosa** (renegociación, Sernac Financiero, mediación).
- **Disolución de SpA / EIRL**.

### Sección 2 — Por cada dolor identificado, documentar

1. **Cómo se resuelve hoy** (servicio público, privado, ONG, asesor humano, autogestión, redes sociales, YouTube).
2. **Costo actual** (gratis, monto en CLP, % de facturación).
3. **Tiempo y fricción** (días/semanas, formularios requeridos, requisitos previos como ClaveÚnica).
4. **Tasa de fracaso/abandono documentada** si existe (ej: % de iniciaciones de actividad que terminan en multa por F29 atrasado, % de Capital Semilla que se postula pero no se rinde).
5. **Brecha explotable por un copiloto IA en WhatsApp** — qué puede resolver una IA conversacional que un PDF/web/contador no resuelve.

### Sección 3 — Inventario de servicios públicos/privados a integrar

Investigar qué APIs, formularios públicos, MCPs candidatos o flujos asistidos existen en cada producto. Por cada uno: alcance, costos, integraciones técnicas (API/scraping/MCP), casos donde un asistente IA ya esté embebido o sea factible:

**Servicios públicos:**
- **empresaenundia.cl** (Min Economía) — qué automatiza, qué deja al usuario, ¿permite asistencia con terceros (gestor, abogado, contador)?, ¿API pública?
- **SII** — Mipyme.cl, F29, F22, registro de boletas honorarios, simulador renta, ¿API pública o requiere ClaveSII?
- **Sercotec** — Capital Semilla, Crece, Mujer Emprendedora, Centros de Negocios (cobertura por región, evaluación impacto).
- **Corfo** — Subsidio Semilla Inicia, Capital Abeja, Reactívate.
- **FOGAPE** y bancos asociados (proceso real, tiempo de aprobación).
- **ChileAtiende, ClaveÚnica, INAPI** (registro de marca paso a paso).
- **Pro-Pyme** SII (régimen tributario simplificado).

**Banca / fintech pyme:**
- BancoEstado Microempresas (CuentaRUT empresarial, créditos).
- EME8 (encuesta INE, no producto, pero clave para sizing).
- Banigualdad, Fondo Esperanza (microfinanzas).
- Tenpo Empresas, MACH (productos para pymes).

**Pasarelas de pago:**
- MACH, Mercado Pago, Tenpo, Toku, Khipu, Flow, Transbank Onepay, Webpay.

**Facturación electrónica:**
- Bsale, Defontana, Toku, SII Mipyme, Nubox, Manager.

**Contabilidad:**
- Toku, Nubox, Defontana, contador humano (rangos de precio promedio en Chile).

### Sección 4 — Catálogo de funcionalidades candidatas (BACKLOG)

**Lista exhaustiva (apuntar a 60-100 ítems)** en formato:

```
- [E2-FORM-12] Acompañamiento paso-a-paso en empresaenundia.cl con handoff a contador humano (marketplace) cuando el usuario se atasca.
  - Dolor: 38% de las iniciaciones de empresa en empresaenundia.cl quedan a medias por dudas técnicas (ej: capital social, giros).
  - Servicio que apalanca: empresaenundia.cl + marketplace de contadores Tu Plata Mipyme.
  - Tier sugerido: Free (acompañamiento básico) + Plus (sesión 1:1 con contador).
  - Complejidad: M (requiere scraping del flujo + UI conversacional).
```

**Agrupado por etapa** (E0-E5) y subcategoría:
- **FORM** (formalización)
- **OPER** (operación día-a-día)
- **FIN** (financiamiento)
- **LEGAL** (laboral, contratos, quiebra)
- **CRECE** (marketing, ventas, expansión)
- **RIESGO** (multas, decomisos, estafas)
- **EMOCIONAL** (motivación, mentor, comunidad)

Cada feature debe declarar:
- **Dolor que resuelve** (con cifra si existe).
- **Servicio público/privado que apalanca o reemplaza**.
- **Tier sugerido** (Free / Pro / Plus / Marketplace).
- **Complejidad implementación** (S/M/L).

### Sección 5 — Casos análogos LATAM

Productos similares en otros países y qué features del journey resolvieron primero, cuáles abandonaron, qué tiers cobraron, qué lecciones se pueden importar:

- **Brasil:** Stone, MEI Fácil, Bling, Conta Azul, Sebrae digital.
- **México:** Konfío, Clip, MEX-EPS, Bind ERP, Crehana Empresas.
- **Colombia:** Bold, Sempli, Alegra, Siigo Mipyme.
- **Perú:** Yape Empresas, Culqi, Niubiz Solo.

Por cada uno: features estrella, modelo de negocio, qué les funcionó y qué no, métricas de adopción si están públicas.

### Sección 6 — Recomendación final

Cierra con:

1. **Top 15 features diferenciadoras + factibles** para Tu Plata Mipyme (no las más obvias, las que más mueven la aguja en NSE D-E mujeres 30-50 sur de Chile). Ordenadas por impacto cívico esperado.
2. **5 features que parecen obvias pero no recomiendas** (ya las hace mejor un actor existente, o no resuelve un dolor real).
3. **3 sleeper features** — funcionalidades poco glamorosas pero que el agente cree pueden ser el diferenciador real de Tu Plata Mipyme en el lab.

## Reglas para el agente

- **No priorizar el backlog** — solo levantar el universo. La priorización la hacemos nosotros después.
- **Cifras con fuente verificable**. EME8 INE, Casen, Sercotec, OCDE, BCN, Ministerio de Economía. Si no tienes verificación, dilo.
- **Distinguir entre lo que existe gratis en papel y lo que el usuario realmente paga** (lugar real). Ej: la MEF existe hace 20 años pero la usan poco — explica por qué.
- **Si un servicio público existe pero nadie lo usa, explícalo** (fricción burocrática, desconocimiento, requisito previo difícil).
- **Honesto con la viabilidad técnica** — qué es API real pública, qué requiere ClaveÚnica/ClaveSII del usuario, qué es scraping, qué requiere humano en el loop.
- **Foco en NSE D-E** — feedback feature debe ser viable para una persona con literacy regulatoria baja, smartphone gama media, conexión 3G/4G intermitente, lenguaje natural informal.
- **Cita la norma** — cuando se mencione un trámite, apuntar a la ley/resolución que lo regula (no solo el servicio).

## Por qué esto vale los USD 5 que cuesta

El equipo ya tiene la idea (Tu Plata Mipyme + WhatsApp-first + freemium + multi-agente) pero el backlog de funcionalidades aún es ad-hoc. Con un mapeo exhaustivo del journey y un catálogo de 60-100 features candidatas, el equipo puede:
1. Priorizar con criterio (no por gusto del momento).
2. Identificar el MVP del lab del 7 de mayo con más confianza.
3. Tener un roadmap post-lab sólido para conversar con sponsors/inversionistas.
4. Detectar features sleeper que la competencia (Tenpo Empresas, MACH Pyme, Defontana) no ha cubierto.

Sin este run, el equipo arriesga construir lo obvio y perder el diferencial cívico. Con este run, tenemos catálogo accionable + casos LATAM para sustentar cada decisión en el pitch.

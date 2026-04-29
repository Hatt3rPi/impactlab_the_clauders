---
titulo: "Datasets públicos chilenos sub-utilizados con potencial de cruce"
objetivo: "Identificar APIs y datasets oficiales chilenos vigentes (abril 2026) que estén sub-utilizados por el ecosistema fintech, y mapear cruces inéditos que revelen oportunidades de producto."
agent: "deep-research-max-preview-04-2026"
linea: inclusion-financiera
prioridad: alto
---

# Prompt: Datasets chilenos sub-utilizados

## Contexto

Soy parte de un equipo en el **Claude Impact Lab Chile 2026** (Anthropic + Bendita IA + FinteChile, 6-7 mayo 2026). El track elegido es **Inclusión Financiera y Literacy Regulatoria**.

El equipo ya tiene mapeados los datasets obvios:

- CMF — Ley Fintech 21.521, NCG 502/514/559, Registro Prestadores, Conoce tu Deuda, circulares.
- SII — propuestas de declaración, Pro-Pyme Transparente, Boleta Electrónica, FAQs.
- SERNAC — Cuenta Pública, alertas de fraude, comparadores, sello de calidad.
- CSIRT/ANCI — alertas ciberseguridad.

Pero hay **muchos más datasets públicos** en el Estado chileno que casi nadie en el ecosistema fintech está usando como insumo para producto. Es ahí donde está la oportunidad de diferenciación.

## Lo que necesito

### Sección 1 — Inventario exhaustivo de datasets / APIs públicos chilenos

Mapea con la mayor exhaustividad posible los datasets, APIs, registros y portales públicos chilenos vigentes a abril 2026 de las siguientes instituciones (no te limites a éstas si encuentras otras relevantes):

**Reguladores financieros y previsionales:**
- CMF (financiero)
- Superintendencia de Pensiones
- Superintendencia de Salud
- Superintendencia de Insolvencia y Reemprendimiento
- Banco Central de Chile

**Tributario y empresarial:**
- SII
- ChileCompra (compras públicas)
- Servicio de Cooperativas (DAES)
- CMF — Registro Prestadores Servicios Fintech

**Vivienda y subsidios sociales:**
- MinDes — Registro Social de Hogares (RSH), beneficios sociales
- MinVu / Serviu — subsidios habitacionales
- IPS (Instituto de Previsión Social) — beneficios, BPS
- AFC (Administradora de Fondos de Cesantía)
- FOSIS
- CONADI

**Salud:**
- FONASA
- Superintendencia de Salud — isapres, GES, CAEC

**Trabajo y empleo:**
- Mintrab — DT (Dirección del Trabajo), denuncias
- OMIL municipales
- SENCE — capacitación

**Educación:**
- Mineduc — FUAS, CAE
- JUNAEB — beneficios estudiantiles
- JUNJI — educación parvularia

**Civil y registros:**
- Registro Civil — defunciones, nacimientos, matrimonios
- Servel — padrón electoral
- Servicio de Registro Civil — posesión efectiva

**Seguridad y justicia:**
- Sename / Mejor Niñez
- Gendarmería
- Defensoría Penal Pública
- Tribunales (Poder Judicial)
- PDI Cibercrimen

**Discapacidad:**
- SENADIS — Registro Nacional de Discapacidad
- Senda — Servicio Nacional para la Prevención y Rehabilitación

**Migración:**
- Servicio Nacional de Migraciones
- Dirección General de Asuntos Consulares

**Productividad y desarrollo:**
- CORFO
- SERCOTEC
- INDAP (campesinos)

**Infraestructura digital:**
- ChileAtiende
- ClaveÚnica
- Subtel (Subsecretaría Telecomunicaciones)
- CGR (Contraloría General)

**Estadísticas:**
- INE (Instituto Nacional de Estadísticas)
- Casen (Encuesta Caracterización Socioeconómica)

### Sección 2 — Para cada dataset / API, documentar

1. **Nombre exacto** del dataset/API.
2. **Institución** propietaria.
3. **Qué expone** (tipo de datos, granularidad, frecuencia de actualización).
4. **Formato técnico** (REST API, descarga CSV/Excel, scraping necesario, formulario web, ninguno).
5. **URL oficial** verificable.
6. **Licencia / términos de uso** (público abierto, requiere registro, restringido).
7. **Calidad de la documentación** (excelente, decente, mínima, inexistente).
8. **Casos de uso conocidos por terceros** (productos comerciales, ONGs, papers académicos que lo usan — busca evidencia real).
9. **Estado a abril 2026** (operacional, en transición, legacy, deprecado).
10. **Saturación** — ¿lo usan muchas fintechs/productos? (alta = saturado, baja = sub-utilizado).

### Sección 3 — Cruces inéditos con potencial

Identifica **5-10 cruces de datasets** que revelen información inédita o accionable. Ejemplos para inspirarte:

- RSH (MinDes) × Registro de Beneficios Sociales (IPS) → quién es elegible para qué subsidio y no lo está cobrando.
- Conoce tu Deuda (CMF) × Padrón Electoral (Servel) → distribución regional de morosidad por edad/género.
- Posesión Efectiva (Reg. Civil) × Multifondos AFP (Sup. Pensiones) → herencias AFP no reclamadas.
- Boleta Electrónica (SII) × AFC → trabajadores informales que recién formalizan y no saben de AFC.
- Comparador SERNAC × Conoce tu Deuda CMF → arbitraje de tasas para refinanciamiento.
- Reclamos CMF × Reclamos SERNAC → empresas problemáticas que el ciudadano debería evitar.

Para cada cruce, declara:
- **Qué información nueva surge** del cruce.
- **Quién se beneficia** (sub-segmento ciudadano).
- **Producto IA-nativo posible** sobre ese cruce.
- **Bloqueos legales o técnicos** del cruce (acceso restringido, datos sensibles, RGPD-equivalente, etc.).

### Sección 4 — Recomendación

Cierra con un **ranking de los 5 datasets más prometedores** para que un agente IA construya producto sobre ellos en 7-10 días, y **5 cruces que abrirían oportunidades de producto que ningún otro equipo del lab estará viendo**.

## Reglas para el agente

- **Verifica que cada dataset existe y está operacional a abril 2026**. Muchos portales chilenos cambian de URL; valida con búsquedas frescas.
- **Si una institución cita una API en su sitio pero no es accesible públicamente, márcalo**.
- **Distingue "dato disponible online" de "API consultable programáticamente"** — para producto necesitamos lo segundo.
- **Si encuentras casos de productos comerciales que ya usan el dataset, mencionálos por nombre** (Destácame, Comparaonline, Galgo, Tenpo, Mach, Floid, Fintoc, etc.).
- **No inventes URLs** — si no las verificaste, dilo.
- **Output esperado**: tabla maestra de datasets (40+ filas) + análisis cualitativo + ranking final.

## Por qué esto vale los USD 5 que cuesta

El equipo viene tras un research que fue exhaustivo en regulación pero superficial en datasets operacionales. La diferenciación frente a 200 equipos viene de **construir sobre datos que nadie está cruzando**. Este mapeo es justo lo que el equipo no tiene tiempo de hacer manualmente esta semana.

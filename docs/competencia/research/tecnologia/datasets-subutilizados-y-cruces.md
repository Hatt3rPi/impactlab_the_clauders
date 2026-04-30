---
title: "Datasets chilenos sub-utilizados + 5 cruces inéditos de alto impacto"
description: "Inventario operativo de APIs/datasets chilenos con saturación comercial baja, cruces algorítmicos con potencial diferenciador, y workarounds prácticos para barreras técnicas (ClaveÚnica, scraping)."
autor: "Síntesis del equipo a partir del run Deep Research Max 03-datasets-chilenos-subutilizados"
fecha: 2026-04-29
categoria: tecnologia
linea: inclusion-financiera
tags:
  - research
  - datasets
  - apis
  - cruces
  - sabiduria
---

# Datasets chilenos sub-utilizados + 5 cruces inéditos

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Promoción a forma curada del [run Deep Research del 29-abr-2026](../_runs-deep-research/2026-04-29-03-datasets-chilenos-subutilizados.md). 44 fuentes oficiales chilenas (Banco Central, CMF, SUPERIR, MinDes BIDAT, FONASA, IPS, Poder Judicial, INE, ChileCompra OCDS, ClaveÚnica, etc.). **Verificar disponibilidad técnica de cada API antes de comprometerse.**

> Esta nota **complementa** la nota previa de [datasets oficiales (PDF Calibria)](../../research/regulatorio/marco-regulatorio-chile-2026.md) con un inventario MUCHO más profundo (40+ datasets) categorizado por **saturación comercial** y **estado técnico operativo**.

## Reframing del producto que el agente propone

> *"Pasar de **Open Finance** a **Open Government for Financial Health**: el Estado Abierto como motor de bienestar financiero."*

Esta narrativa es **defendible ante CMF/SII/SERNAC en el pitch** y diferencia de los 200 equipos que hablarán de "fintech para inclusión".

## Top 5 datasets sub-utilizados (saturación comercial baja-cero)

| # | Dataset | Institución | Estado | Saturación | Por qué importa |
|---|---|---|---|---|---|
| 1 | **Observatorio Estadístico** | SUPERIR | Operacional | Baja | Lanzado fines 2024. Comportamiento pre-quiebra estructurado. Casi nadie lo usa. |
| 2 | **BIDAT (Banco Integrado de Datos)** | MinDes | Operacional | Baja | CASEN, pobreza comunal, RSH agregados. Granularidad territorial para credit scoring. |
| 3 | **Poder Judicial en Números** | Poder Judicial | Operacional | Baja | Termómetro social predictivo: cobros ejecutivos, embargos, demandas familiares. |
| 4 | **Portal Datos Abiertos FONASA** | FONASA | Operacional | Baja | PAD/GRD: gasto hospitalario por familia. **Health-Fintech inexplorada en Chile.** |
| 5 | **Microdatos Censo 2024** | INE | Operacional (publicado dic-2025) | Baja | **Parquet + REDATAM Web**, granularidad manzana. Recién liberado. Ventaja competitiva por timing. |

## Datasets de saturación CERO (oportunidad si encajan)

Casi nadie en el ecosistema fintech chileno los toca:

- **ENDISC** (Estudio Nac. Discapacidad, MinDes/SENADIS) — solo papers médicos.
- **DAES** (Registro Cooperativas, Min. Economía).
- **MinVu Estadísticas Habitacionales** — solo constructoras.
- **FOSIS Programas Emprendimiento** — solo consultoras.
- **CONADI Registro Calidad Indígena** — solo academia.
- **Defensoría Penal Pública Estadísticas** — solo ONGs.
- **Gendarmería Estadísticas Penitenciarias**.
- **Sename / Mejor Niñez Anuario**.
- **JUNJI Microdatos Matrícula CEDOC**.
- **A. Consulares Registro Chilenos en el Exterior** (diáspora).
- **INDAP Línea Base Agricultura Familiar Campesina**.

## Inventario completo por categoría

> Tabla completa con saturación, estado, formato técnico, URL verificable y casos de uso conocidos en el [reporte crudo](../_runs-deep-research/2026-04-29-03-datasets-chilenos-subutilizados.md). Acá un resumen:

### Reguladores y Macroeconomía (10 datasets)

Banco Central API SieteRestWS (saturación alta), CMF Registro Fintech / Reclamos / Acreencias, **SUPERIR Observatorio**, Sup. Pensiones, SII Rutificador, DAES Cooperativas, ChileCompra OCDS API.

### Salud, Desarrollo Social, Vivienda (9 datasets)

**MinDes BIDAT**, ENDISC, **FONASA Portal Datos Abiertos**, IPS Consulta BPS, AFC Estadísticas, MinVu Habitacionales, Sup. Salud GES/CAEC, FOSIS, CONADI.

### Empleo, Educación, Civil (10 datasets)

DT Boletín Infractores (alta saturación pero **inestable**), Reg. Civil API PIEE, Servel Padrón, Mineduc Datos Abiertos, Comisión Ingresa CAE, JUNAEB, JUNJI, SENCE, OMIL, **INE Microdatos Censo 2024**.

### Seguridad, Justicia, Transparencia (9 datasets)

**Poder Judicial en Números**, CPLT InfoLobby/InfoProbidad (API SPARQL), Defensoría Penal, Gendarmería, Sename, Servicio Migraciones, CGR Transparencia, Subtel Telecom, PDI Cibercrimen.

### Productividad, Internacional, Identidad (6 datasets)

CORFO DataInnovación, SERCOTEC Explorador Territorial, INDAP, SENDA, A. Consulares, **ClaveÚnica API** (restringida).

## Workarounds críticos para nuestro hackathon

### 1. ClaveÚnica NO es API abierta para privados

Restringida estrictamente a **instituciones públicas** o privados con funciones públicas acreditadas (notarías electrónicas, AFC). **No es Google Login.**

**Estrategia:** mock endpoint que simula el callback OAuth 2.0 → retorna JWT sintético. En el pitch decir: *"La IA opera bajo mandato del usuario delegando temporalmente el acceso, utilizando integradores B2B validados como **e-cert** o constructos legales similares."*

### 2. Boletín DT y consultas IPS son inestables

**Estrategia BYOD (Bring Your Own Data):** el usuario descarga personalmente sus cartolas oficiales (PDF de RSH, certificados, cartolas previsionales) y las inyecta. La IA aplica OCR localmente. **Evita scraping y posibles bans de IP.**

## 5 Cruces inéditos de alto impacto

### 1. :material-star: Herencia Fácil (cruza con run #04 transferencias)

- **Cruce:** Posesión Efectiva (Reg. Civil) × Acreencias Bancarias (CMF, **CLP 94-98 mil M en pozo**, 117.000 acreencias) × Multifondos AFP (Sup. Pensiones).
- **Beneficiario:** Herederos directos NSE D-E.
- **Producto:** Agente de Recuperación Patrimonial. Procesa Posesión Efectiva → cruza RUT del causante con CMF → levanta cuotas mortuorias AFP → genera reporte + formularios.
- **Estatus:** **Match perfecto con sabidurIA** (módulo Legado Claro). Cruza directo con el gap 41 % AFP del [run #04](../usuarios/transferencias-no-activadas-chile-2026.md).

### 2. Triage de Estrés Financiero Hospitalario

- **Cruce:** GRD/PAD (FONASA Datos Abiertos) × Boletín DT × Oferta Crédito Ley Fintech (CMF).
- **Problema:** ciudadanos toman créditos al 40,60-50 % TMC para urgencias médicas inmediatas.
- **Producto:** Asesor de Liquidez de Salud. Chatbot al momento de admisión clínica → estima costo GRD/PAD → chequea inestabilidad laboral del paciente vía DT → mapea oferta CMF → previene microcrédito usurero.

### 3. Radar de Resiliencia PYME B2G (Factoring Ético)

- **Cruce:** ChileCompra OCDS API (tiempo real) × Boletín DT × Observatorio SUPERIR × InfoLobby.
- **Producto:** Credit Scoring B2G Predictivo. Oráculo automatizado consume feed OCDS → cruza RUT de adjudicado con SUPERIR + DT → analiza InfoLobby para anomalías → semáforo de riesgo a financieros.

### 4. SubsidioBot (Take-up gap del Estado)

- **Cruce:** RSH (MinDes) × Beneficios Previsionales BPS/IPS × Beneficios SENCE/FOSIS.
- **Beneficiario:** Mujeres jefas de hogar, adultos mayores, trabajadores informales.
- **Producto:** Bot WhatsApp. Usuario fotografía cartola RSH → OCR extrae tramos → cruza con reglas de **50+ subsidios** → identifica los que califica y no cobra → alertas.
- **Estatus:** Match con la idea **CuidaDerechos** del run #01 + cifras del run #04.

### 5. Refinanciamiento Preventivo Anti-Violencia Económica

- **Cruce:** Poder Judicial en Números × Conoce tu Deuda CMF × Registro Nacional Deudores Alimentos (Reg. Civil).
- **Beneficiario:** Madres solteras (mayor índice de vulnerabilidad crediticia estructural).
- **Producto:** Plataforma bancaria detecta zonas calientes de demandas familiares + estrés de caja en clientas (ausencia abonos compatibles con alimentos) → IA empática ofrece preventivamente reestructuración → deriva a Corporación de Asistencia Judicial si hay violencia.

## Implicancias para sabidurIA ciudadana

| Hallazgo | Impacto en la idea |
|---|---|
| **Microdatos Censo 2024** recién liberados | Geointeligencia de sub-segmento por manzana → diferenciación demo |
| **SUPERIR Observatorio** sub-utilizado | Detección temprana de pre-quiebra → módulo Mi Plan B reforzado |
| **FONASA PAD/GRD** inexplorada por fintechs | Vertical Health-Fintech única en demo (módulo de cuidado/enfermedad) |
| **ClaveÚnica restringida** | Plan B obligatorio: BYOD + mock OAuth desde día 1 del sprint |
| **DT inestable** | No depender de scraping en runtime; usuario sube cartola |
| **Herencia Fácil = match perfecto** | Sub-módulo del demo confirmado por dato + capacidades + gap 41 % |

## Backlog técnico (para el spike pre-lab del equipo)

- [ ] **Probar API SieteRestWS Banco Central** (registrar usuario, obtener UF/UTM/USD).
- [ ] **Descargar dataset CMF Acreencias 2026** vía Transparencia (CSV anual, evita CAPTCHA).
- [ ] **Explorar Observatorio SUPERIR** (CSV, dashboard) y validar formato consultable.
- [ ] **Verificar disponibilidad de Microdatos Censo 2024** en Parquet (REDATAM Web).
- [ ] **Probar ChileCompra OCDS API** (registro ClaveÚnica + parsing JSON anidado).
- [ ] **Construir mock endpoint OAuth ClaveÚnica** que retorne JWT sintético.
- [ ] **Pipeline OCR local** para cartolas RSH/AFP/Fonasa (entrada usuario, no scraping).
- [ ] **CPLT API SPARQL** para InfoLobby (compliance/AML B2B).

## Limitaciones declaradas por el agente

- URLs y endpoints están sujetos a fluctuaciones de modernización estatal (validar antes de comprometer un dataset).
- La granularidad de causas individuales en el Poder Judicial requiere RIT/ROL específico → solo macro-estadística disponible.
- Los datos de DT son inestables; han caído anteriormente.
- Privacidad: datos sensibles (salud, antecedentes) requieren anonimización o bases sintéticas para hackathon (Ley 19.628 + Ley 20.584).

## Referencias

- [Run Deep Research #03 — Datasets sub-utilizados](../_runs-deep-research/2026-04-29-03-datasets-chilenos-subutilizados.md) (reporte crudo, 304 líneas, 44 fuentes).
- [Datos del run #04 — Transferencias no activadas](../usuarios/transferencias-no-activadas-chile-2026.md) — cifras complementarias.
- [Estrategia de pitch (run #02)](../../../equipo/estrategia-pitch-lab.md) — táctica MCP custom.

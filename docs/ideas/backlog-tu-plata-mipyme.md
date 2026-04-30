---
title: "Backlog de funcionalidades — Tu Plata Mipyme"
description: "Catálogo de 60 features candidatas organizadas por etapa del journey (E0-E5) y subcategoría, con tier sugerido, complejidad y servicio que apalanca. Síntesis del run Deep Research #06."
autor: "Síntesis del equipo a partir del run Deep Research #06 (entrepreneur-journey-backlog)"
fecha: 2026-04-30
linea: inclusion-financiera
estado: en-refinamiento
prioridad: alta
tags:
  - backlog
  - tu-plata-mipyme
  - features
  - journey
  - inclusion-financiera
---

# Backlog de funcionalidades — Tu Plata Mipyme

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Catálogo construido a partir del [run Deep Research #06](../research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md). **Aún no validado por el equipo.** Las prioridades, tiers y complejidades son las propuestas del agente — el equipo debe revisar y ajustar.

> *60 funcionalidades candidatas categorizadas por etapa del journey del microemprendedor chileno (E0-E5) y subcategoría (FORM/OPER/FIN/LEGAL/CRECE/RIESGO/EMOCIONAL). Insumo para priorizar el MVP del Lab del 7 de mayo y el roadmap post-lab.*

## Resumen

- **48 dolores documentados** a lo largo de 6 etapas del journey (idea → cierre).
- **60 features candidatas** distribuidas en 4 tiers: Free, Pro (~$4.990 CLP/mes), Plus ($15-30K CLP/evento), Marketplace (10-15% comisión).
- **17 casos análogos LATAM** estudiados (Brasil, México, Colombia, Perú).
- **Diagnóstico clave del agente:** la informalidad es un "escudo de cristal" inicial — protege de la burocracia pero expone a estafas, multas y estancamiento. El copiloto debe demostrar empíricamente que el costo de ser informal **ya superó** el costo de formalizarse.

## Cómo leer este backlog

Cada feature tiene:

- **ID** `[Etapa-Subcategoría-Número]` — ej: `[E2-FORM-18]` = Etapa 2, subcategoría Formalización, feature #18.
- **Subcategorías:** FORM (formalización), OPER (operación), FIN (financiero), LEGAL (legal/laboral), CRECE (crecimiento/marketing), RIESGO (multas/estafas), EMOC (emocional).
- **Tier:** Free, Pro, Plus, Marketplace.
- **Complejidad:** S (small, días), M (medium, semanas), L (large, mes+).

## Tabla maestra (las 60 features)

### E0 — Idea / Sueño (8 features)

| ID | Feature | Tier | Compl. | Dolor que ataca |
|---|---|---|---|---|
| [E0-EMOC-01] | El Espejo Mágico (test arquetipo) | Free | S | Síndrome del impostor socioeconómico |
| [E0-EMOC-02] | Mata-Mitos SII (V/F sobre fiscalización) | Free | S | Miedo irracional al SII |
| [E0-FIN-03] | Calculadora "Sueldo Justo" | Free | M | Autoexplotación / no cobrar tiempo |
| [E0-OPER-04] | Pizarrón de Costeo de Producto | Free | S | Fijación de precios copiando ciegamente |
| [E0-CRECE-05] | Validador de Idea Express | Pro | M | Parálisis viabilidad hiperlocal |
| [E0-RIESGO-06] | Simulador de Multas Realista | Free | S | Ignorancia sobre costos de decomiso |
| [E0-EMOC-07] | Comunidad Audio-Foro (testimonios sur) | Free | M | Soledad emprendedora rural |
| [E0-OPER-08] | Separador Financiero Conceptual | Free | S | Caos cuenta personal vs negocio |

### E1 — Validación Informal (8 features)

| ID | Feature | Tier | Compl. | Dolor que ataca |
|---|---|---|---|---|
| [E1-OPER-09] | Caja Zapatos Digital (NLP por audio) | Free | S | Ceguera financiera / sin registro |
| [E1-OPER-10] | Alerta Tope CuentaRUT (Open Banking) | Pro | M | Bloqueo de cuenta por sobre-uso |
| [E1-FIN-11] | Generador Link de Pago (MP/Flow) | Free | M | Pérdida de ventas sin tarjeta |
| [E1-RIESGO-12] | Botón del Pánico Fiscalizador | Free | S | Decomiso/inspección sorpresa |
| [E1-CRECE-13] | Catálogo Web Instantáneo (URL) | Pro | M | Mandar fotos manualmente a clientes |
| [E1-OPER-14] | Cotizador/Comprobantes (con disclaimer SII) | Free | S | Profesionalizar venta informal |
| [E1-EMOC-15] | Reporte Pérdida B2B mensual | Pro | S | Imposibilidad vender a empresas |
| [E1-OPER-16] | Caza-Estafas Visual (OCR pantallazos) | Pro | L | Estafas con pantallazos falsos |

### E2 — Formalización (12 features)

| ID | Feature | Tier | Compl. | Dolor que ataca |
|---|---|---|---|---|
| [E2-FORM-17] | Triage Jurídico MEF vs EIRL vs SpA | Free | S | Elección equivocada de figura jurídica |
| [E2-FORM-18] | **Traductor Tu Empresa en Un Día (Vision)** | Free | M | 35-40% abandono por jerga legal |
| [E2-FORM-19] | Redactor Objeto Social Amplio | Free | S | Bloqueo futuras líneas de negocio |
| [E2-FORM-20] | Buscador de Giros SII (diccionario inverso) | Free | S | Errores de clasificación que impiden patente |
| [E2-FORM-21] | Acompañamiento Inicio Actividades F4415 | Free | M | Creer que RES habilita facturar |
| [E2-FORM-22] | Búsqueda Fonética INAPI | Pro | M | Plagio accidental de marca |
| [E2-FORM-23] | Asesor Domicilio Tributario | Free/Pro | M | Rechazo SII por papel mal notariado |
| [E2-FORM-24] | **Handoff a Contador Pyme** | Marketplace | M | Casos borde técnicos imposibles |
| [E2-FORM-25] | Simulador Gastos de Formalización | Free | S | Sorpresa financiera intermedia |
| [E2-FORM-26] | Pre-chequeo SEREMI Alimentos | Pro | M | Rechazo recurrente arquitectónico |
| [E2-FORM-27] | Asesor Patentes Municipales | Plus | L | Falta transparencia ordenanzas |
| [E2-FORM-28] | Orientador Firmas Electrónicas | Free | S | Compra errónea de Token avanzado |

### E3 — Operación Formal (11 features)

| ID | Feature | Tier | Compl. | Dolor que ataca |
|---|---|---|---|---|
| [E3-OPER-29] | **Facturador WhatsApp (ApiGateway/Pana)** | Pro | L | Interfaz tosca SII Mipyme |
| [E3-OPER-30] | Emisor e-Boletas exprés | Pro | L | Fricción app e-Boleta del Estado |
| [E3-OPER-31] | Recordatorio Empático F29 | Free | S | Olvido declaración → multas |
| [E3-OPER-32] | Declarador "Sin Movimiento" (F29 cero) | Free | M | Multas por mes sin ventas |
| [E3-FIN-33] | Calculador Honorarios Líquido↔Bruto | Free | S | Confusión retención freelancer |
| [E3-OPER-34] | Monitor Compras RCV (alerta facturas) | Plus | L | Facturas sorpresa al RUT |
| [E3-RIESGO-35] | **Traductor Notificaciones SII (correos rojos)** | Free | S | Pánico jerga fiscalizadora |
| [E3-FIN-36] | Simulador Pro-Pyme Transparente (IGC) | Plus | L | Ceguera impuestazo abril |
| [E3-OPER-37] | Descargador Carpeta Tributaria | Pro | M | Banco exige certificado complejo |
| [E3-OPER-38] | Handoff Operación Renta F22 | Marketplace | M | F22 demasiado complejo para IA sola |
| [E3-FIN-39] | Conciliador Bancario Visual (OCR cartolas) | Plus | L | Cobros olvidados / desorden |

### E4 — Crecimiento (12 features)

| ID | Feature | Tier | Compl. | Dolor que ataca |
|---|---|---|---|---|
| [E4-FIN-40] | Scout de Subsidios Sercotec/Corfo | Free | M | Desconocimiento calendarios |
| [E4-FIN-41] | **Borrador Modelo Canvas Sercotec** | Pro/Plus | M | >50% rechazo por mala formulación |
| [E4-FIN-42] | Asistente Pitch Video (90s) | Pro | S | Vergüenza escénica ante cámara |
| [E4-FIN-43] | Recomendador Microcréditos (Banigualdad/F.Esp) | Free/Mkt | M | Miedo a tasas usureras |
| [E4-FIN-44] | Desmitificador FOGAPE | Free | S | "FOGAPE no se paga si me va mal" (falso) |
| [E4-LEGAL-45] | Generador Contrato de Trabajo seguro | Pro | M | Demandas laborales por contrato Google |
| [E4-LEGAL-46] | Guía Previred Exprés | Pro | S | Portal Previred poco amigable |
| [E4-LEGAL-47] | Simulador Finiquito básico | Plus | M | No saber cuánto cuesta despedir |
| [E4-LEGAL-48] | Generador Protocolo Ley Karin | Free | S | Consultoras cobran $$$ por PDF |
| [E4-CRECE-49] | Bot Analista Precios Proveedores | Pro | L | Pyme absorbe inflación insumos |
| [E4-CRECE-50] | Creador Textos Instagram (RAG copy) | Pro | S | No saben redactar redes |
| [E4-CRECE-51] | Filtro Compra Ágil <30 UTM (Mercado Público) | Plus | L | Burocracia ChileProveedores |

### E5 — Recuperación / Cierre / Pivot (9 features)

| ID | Feature | Tier | Compl. | Dolor que ataca |
|---|---|---|---|---|
| [E5-LEGAL-52] | Asesor Ley 21.563 Reorganización Mipyme | Free | M | Embargos sobre patrimonio personal |
| [E5-LEGAL-53] | **El "Torniquete" (suspensión SII asistida)** | Pro | M | Empresas zombi acumulando F29 |
| [E5-EMOC-54] | Botón de la Vergüenza (educación DICOM) | Free | S | Estigma + mafias de "borrado" |
| [E5-LEGAL-55] | Derivación Quiebra Simplificada | Plus/Mkt | M | Muerte económica de por vida |
| [E5-EMOC-56] | Diario Post-Mortem (lecciones del fracaso) | Free | S | Duelo no procesado |
| [E5-LEGAL-57] | Renegociación 2da Categoría (honorarios) | Free | S | Default profesional post-pandemia |
| [E5-LEGAL-58] | Disolución Sociedad RES | Pro | S | Sociedades zombi legales |
| [E5-FIN-59] | Invocación Sernac Financiero | Free | S | Cobranza abusiva sobre Mipyme caída |
| [E5-EMOC-60] | Ruta Reinvención (re-empezar como MEF) | Free | S | Trauma del fracaso paraliza retorno |

---

## Recomendaciones del agente

### Top 15 features diferenciadoras + factibles (prioridad sugerida)

**Ordenadas por impacto cívico esperado en mujeres NSE D-E sur de Chile:**

1. **[E0-FIN-03]** Calculadora "Sueldo Justo" — ataca la brecha de género (-43.7% en Los Ríos).
2. **[E3-OPER-29]** Facturador WhatsApp — *killer feature*, factura "50 lucas" desde texto.
3. **[E2-FORM-18]** Traductor Empresa en Un Día con Vision AI — fricción documentada 35-40%.
4. **[E2-FORM-17]** Triage Jurídico MEF vs SpA — resuelve consulta de $50K en 3 min.
5. **[E2-FORM-21]** Acompañamiento F4415 — evita la trampa "ya tengo SpA, puedo vender".
6. **[E4-FIN-41]** Borrador Canvas Sercotec — empareja la cancha (>50% rechazo por formulación).
7. **[E1-OPER-16]** Caza-Estafas Visual OCR — combate directo a estafas vecinales.
8. **[E1-RIESGO-12]** Botón del Pánico Fiscalizador — alto valor emocional, contención real-time.
9. **[E3-FIN-33]** Calculador Honorarios Líquido↔Bruto — aritmética semanal en todo Chile.
10. **[E1-OPER-09]** Caja Zapatos Digital NLP — control financiero por audio para feria.
11. **[E3-RIESGO-35]** Traductor Notificaciones SII — desestresa "correos rojos".
12. **[E5-LEGAL-52]** Asesor Ley 21.563 — evita embargos, educa post-pandemia.
13. **[E5-LEGAL-57]** Renegociación 2da Categoría — atiende a recién beneficiados por la ley.
14. **[E1-EMOC-15]** Reporte Pérdida B2B — *nudging* conductual hacia formalidad.
15. **[E2-FORM-24]** Handoff a Contador Pyme — valida modelo de ingresos del Marketplace.

### 5 features que parecen obvias pero NO se recomiendan

1. **Reemplazar 100% al contador (auto-F29 complejo).** Legalmente suicida — un error de IA en IVA destruye reputación.
2. **Sistema de gestión de inventario con SKUs y bodegas múltiples.** Las microempresarias D-E no mantienen bases sincronizadas al milímetro.
3. **App móvil nativa descargable.** El espacio en el celular gama media es sagrado en NSE D-E. Vivir nativo en WhatsApp.
4. **Lectura automatizada vía ClaveÚnica para todos.** Pasar ClaveÚnica al LLM por WhatsApp rompe protocolos del Estado.
5. **Red social interna de emprendedores.** *Cold-start* costoso — los usuarios ya viven en grupos de WhatsApp/Facebook.

### 3 sleeper features (joyas para el pitch)

1. **[E5-LEGAL-53] El "Torniquete" (Término de Giro asistido).** Ninguna startup hace marketing ayudando a cerrar negocios — pero evita el "impuesto a la ignorancia" de $2M en F29 acumulados.
2. **[E2-FORM-20] Buscador de Giros Inverso.** Si elige "Agricultura" en vez de "Elaboración de Alimentos", el SEREMI la paraliza 6 meses. NLP que cruza con diccionario oficial SII previene cuello de botella fatal.
3. **[E1-OPER-10] Alerta Tope CuentaRUT.** Cuando "pega un palo" en ventas por Instagram, BancoEstado le congela la cuenta. Avisar 24h antes = retención brutal.

---

## Lecciones de casos análogos LATAM

### Brasil (5 casos)
- **Stone:** transición de POS físico → ERP integrado (Linx) + StoneBank. Hubs hiperlocales generaron confianza profunda. **Lección:** "soporte físico + foco micropyme" es replicable en regiones del sur.
- **MEI Fácil (Neon):** plataforma para Microempreendedor Individual (MEI). Freemium: gestión fiscal gratis, monetiza préstamos y tarjetas. **Lección:** publicidad empoderadora ("era empleado, ahora soy dueño") + resolver burocracia inicial = lock-in.
- **Conta Azul (Visma):** ERP cloud con colaboración estrecha PYME-contador. **Open Banking aprobaba créditos en 4h vs 15 días.** Adquirida 2025. **Lección:** integrar contador humano en la misma plataforma = retención brutal.
- **Bling (Locaweb):** ERP e-commerce con 300K+ usuarios. Adquirida USD 97.5M. **Lección:** simplificar fiscalidad compleja para vendedores online.
- **Sebrae Digital:** educación gratuita con validación estatal. **Lección:** democratización de contenidos formales.

### México (5 casos)
- **Konfío:** crédito a pymes evaluando facturas electrónicas del SAT directamente. **Lección:** **modelo a imitar con PFX chileno** — análisis tributario en tiempo real.
- **Clip:** mPOS líder. Tap to Pay on iPhone eliminó el hardware. **Lección:** llevar el cobro a cero fricción (sin comprar máquina).
- **MEX-EPS / RESICO:** régimen tributario simplificado a cambio de formalización absoluta. **Lección:** "menos impuestos a cambio de aparecer en el SAT" — patrón a evangelizar con Pro-Pyme.
- **Bind ERP:** facturación CFDI 4.0 + control inventario. 6K+ usuarios. **Lección:** UX amigable para dueños sin contabilidad formal.
- **Crehana Empresas:** capacitación B2B (Perú→México). Pivot exitoso pandemia. **Lección:** reskilling > venta de cursos sueltos.

### Colombia (4 casos)
- **Bold:** mPOS para informales con RUT provisorio. **Lección:** "vender hoy" antes de exigir contabilidad.
- **Sempli:** primera tarjeta crédito 100% pyme sin cuota manejo. USD 36M levantados. **Lección:** atender el rango "desatendido" USD 10K-100K.
- **Alegra:** contabilidad cloud + 30 IA nativas. 40K pymes Colombia / 100K México / 300-400K LATAM. Alianzas Cámara Comercio Bogotá + Mastercard. **Lección:** automatizar sin que el contador lo perciba como amenaza.
- **Siigo Mipyme:** gigante ERP corporativo. **Lección negativa:** demasiado complejo para target informal temprano.

### Perú (3 casos)
- **Yape Empresas (BCP):** billetera P2P → 14M+ usuarios, 2.95% ventas QR. Separación dueño/cajero exitosa. **Lección:** la separación de roles dentro del mismo producto = adopción operativa.
- **Culqi:** depósitos mismo día (CulqiFull). **Lección:** velocidad de caja brutal para supervivencia.
- **Niubiz Solo (VendeMás):** transición corporativo → pyme con QR/links. **Lección:** alianzas masivas con billeteras ya establecidas.

---

## Servicios públicos/privados a integrar

### Estado chileno
- **Tu Empresa en un Día (RES):** sin API transaccional pública. **Integración:** flujo asistido + Vision AI sobre la web.
- **SII / Pro-Pyme:** APIs limitadas + PFX requerido. **Gateways:** ApiGateway.cl, TuPana.ai (scraping autorizado). **Alta factibilidad** vía gateway con PFX.
- **Sercotec / Corfo:** sin API. **Integración:** scraping bases de postulación → RAG.
- **ChileAtiende / ClaveÚnica:** OAuth 2.0 reservado a convenios. **Integración:** redirecciones seguras o delegación limitada (no se puede capturar ClaveÚnica en WhatsApp).
- **INAPI:** buscador público. **Integración:** scraping simple para búsquedas fonéticas.
- **FOGAPE:** vía bancos. **Integración:** solo informativa (calculadoras + explicación garantías).

### Banca / fintech / microfinanzas
- **EME8 (INE):** estática, ~1.08M informales con concentración femenina sur. **Integración:** training set demográfico.
- **Fondo Esperanza:** ~140K clientes, tasa base ~5%. **Integración:** derivación referencial.
- **Banigualdad:** ~60K clientes, hasta $1M, ~1.52% mensual, grupos de 18 personas. **Integración:** derivación.
- **Tenpo / MACH / BancoEstado Microempresas:** Open Banking vía Fintoc/Prometeo (cartolas, conciliación, alertas).

### Pasarelas
- **Mercado Pago, Flow, MACH Pay, Tenpo, Toku, Khipu, Transbank Onepay, Webpay:** APIs REST documentadas. **Generar links de cobro en WhatsApp = democratizar tarjeta de crédito.**

### ERPs (competencia/alianzas)
- **Bsale, Defontana, Manager, Nubox, Toku, SII Mipyme:** 1-2 UF/mes, complejos para D-E. **Posicionamiento:** Tu Plata Mipyme es *wrapper* sobre SII Mipyme gratuito + **handoff** a estos partners cuando el usuario crece.

---

## Próximos pasos

1. **Revisar y validar** el top 15 con el equipo (sesión 1h).
2. **Cruzar con MVP del Lab** — ¿qué features están en ámbito de las 48h del lab vs el roadmap post-lab?
3. **Identificar features con dependencia técnica común** (ej: PFX habilita E3-OPER-29, E3-OPER-30, E3-OPER-34, E3-OPER-37 simultáneamente).
4. **Priorizar 5-8 features para el demo del 7 de mayo** que cuenten una historia narrativa coherente (de E0 a E5 en 90s).
5. **Convertir features priorizadas en tickets** con criterios de aceptación específicos.

## Notas y referencias

- Reporte fuente: [run #06 Deep Research](../research/_runs-deep-research/2026-04-30-06-entrepreneur-journey-backlog.md).
- 58 fuentes citadas: ver [run-06-entrepreneur-journey](../recursos/enlaces/run-06-entrepreneur-journey.md).
- Definición canónica del producto: [Tu Plata Mipyme](../definiciones/tu-plata-mipyme.md).
- Plan de implementación: [tu-plata-mipyme-plan](../especificaciones/tu-plata-mipyme-plan.md).
- ADR base: [ADR 0004 — WhatsApp-first, freemium, multi-agente](../especificaciones/adrs/0004-tu-plata-mipyme-whatsapp-first-freemium-multiagente.md).

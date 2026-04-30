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
- **Escenario:** micro-historia que muestra el dolor en acción. Personajes recurrentes son mujeres microemprendedoras 30-50 años en regiones del sur de Chile (María en Pucón, Carmen en Temuco, Patricia en Curanilahue, Roxana en Valdivia, Ana en Osorno, Luisa en Puerto Montt) — alineadas con el target prioritario.

## Tabla maestra (las 60 features)

### E0 — Idea / Sueño (8 features)

| ID | Feature | Tier | Compl. | Escenario |
|---|---|---|---|---|
| [E0-EMOC-01] | El Espejo Mágico (test arquetipo) | Free | S | María lleva 5 años haciendo mermeladas en Pucón pero piensa "yo no soy empresaria, solo cocino, no podría". |
| [E0-EMOC-02] | Mata-Mitos SII (V/F sobre fiscalización) | Free | S | Carmen escuchó en el almacén que "el SII te embarga si declarás más de $300 lucas". Mejor no formalizarse. |
| [E0-FIN-03] | Calculadora "Sueldo Justo" | Free | M | Patricia vende empanadas a $1.500. Trabajó 8 horas amasando. Cobra solo los ingredientes y nunca su tiempo. |
| [E0-OPER-04] | Pizarrón de Costeo de Producto | Free | S | Roxana copia el precio del kuchen del local de al lado: $3.500. No sabe que pierde $800 por unidad vendida. |
| [E0-CRECE-05] | Validador de Idea Express | Pro | M | Ana quiere abrir un taller de costura en Curanilahue pero no sabe si en su barrio hay clientas suficientes. |
| [E0-RIESGO-06] | Simulador de Multas Realista | Free | S | Luisa cree que vender en la feria sin permiso es "normal" hasta que le decomisaron $80K en mercadería. |
| [E0-EMOC-07] | Comunidad Audio-Foro (testimonios sur) | Free | M | Patricia teje en el campo cerca de Pucón. No conoce a nadie más que esté emprendiendo y se siente sola. |
| [E0-OPER-08] | Separador Financiero Conceptual | Free | S | María paga el supermercado con la misma CuentaRUT donde le abonan los pedidos. No sabe cuánto gana realmente. |

### E1 — Validación Informal (8 features)

| ID | Feature | Tier | Compl. | Escenario |
|---|---|---|---|---|
| [E1-OPER-09] | Caja Zapatos Digital (NLP por audio) | Free | S | María vendió 3 mermeladas y compró azúcar. A fin de mes no se acuerda y cree que "ganó" porque hay plata. |
| [E1-OPER-10] | Alerta Tope CuentaRUT (Open Banking) | Pro | M | Ana vendió bien en diciembre. BancoEstado le congeló la CuentaRUT por superar el tope mensual. Sin liquidez. |
| [E1-FIN-11] | Generador Link de Pago (MP/Flow) | Free | M | Carmen pierde 2 ventas al día porque sus clientas "no andan trayendo plata efectiva" y ella no acepta tarjeta. |
| [E1-RIESGO-12] | Botón del Pánico Fiscalizador | Free | S | Luisa estaba vendiendo en feria libre. Llegó un inspector. Se paralizó: "¿qué firmo?, ¿qué digo?, ¿corro?". |
| [E1-CRECE-13] | Catálogo Web Instantáneo (URL) | Pro | M | Patricia manda 30 fotos de joyería por WhatsApp a cada clienta nueva. Le agota el día y desordena el chat. |
| [E1-OPER-14] | Cotizador/Comprobantes (con disclaimer SII) | Free | S | Roxana le tiene que pasar un "documento" al jefe de su clienta para que rinda el gasto. No tiene cómo. |
| [E1-EMOC-15] | Reporte Pérdida B2B mensual | Pro | S | Una clienta del restaurante le pidió factura por $200K. María dijo "no puedo" y perdió la venta y todas las que vendrán. |
| [E1-OPER-16] | Caza-Estafas Visual (OCR pantallazos) | Pro | L | Carmen recibió pantallazo de transferencia por $45K. Entregó la mercadería. La plata nunca llegó. |

### E2 — Formalización (12 features)

| ID | Feature | Tier | Compl. | Escenario |
|---|---|---|---|---|
| [E2-FORM-17] | Triage Jurídico MEF vs EIRL vs SpA | Free | S | María entró a empresaenundia.cl y se quedó pegada en "EIRL vs SpA". ¿Cuál le conviene si trabaja en la casa, sola? |
| [E2-FORM-18] | **Traductor Tu Empresa en Un Día (Vision)** | Free | M | Roxana ve el campo "objeto social" en RES y no entiende qué tiene que escribir. Cierra la pestaña y abandona. |
| [E2-FORM-19] | Redactor Objeto Social Amplio | Free | S | Patricia escribió solo "venta de pan" en el RES. Luego quiso vender kuchenes y no podía: tenía que modificar estatutos. |
| [E2-FORM-20] | Buscador de Giros SII (diccionario inverso) | Free | S | Ana eligió giro "Agricultura" en SII pensando que vendía verduras. La SEREMI de Salud la paralizó 6 meses por elaboración de alimentos. |
| [E2-FORM-21] | Acompañamiento Inicio Actividades F4415 | Free | M | María creó la SpA en RES, vendió 3 facturas. SII la multó: nunca hizo el inicio de actividades F4415. |
| [E2-FORM-22] | Búsqueda Fonética INAPI | Pro | M | Carmen quiere registrar "La Patagona" para sus tejidos. No sabe que ya existe "La Patagonia": rechazo seguro. |
| [E2-FORM-23] | Asesor Domicilio Tributario | Free/Pro | M | Luisa lleva el contrato de arriendo al SII. Rechazado: faltaba el rol de la propiedad. Vuelta a la municipalidad. |
| [E2-FORM-24] | **Handoff a Contador Pyme** | Marketplace | M | María se atascó configurando régimen tributario. La IA le dice "aquí necesitas un humano" y le agenda una hora con contadora certificada. |
| [E2-FORM-25] | Simulador Gastos de Formalización | Free | S | Patricia empezó la formalización pensando que era gratis. Se topó con $40K en firma electrónica + notario. Abandona. |
| [E2-FORM-26] | Pre-chequeo SEREMI Alimentos | Pro | M | Roxana pagó el arancel SEREMI sin saber que su cocina no tenía lavamanos separado. Rechazo, $35K perdidos. |
| [E2-FORM-27] | Asesor Patentes Municipales | Plus | L | Carmen pidió patente en La Pintana. Se cambió a Maipú. Cada comuna le pide papeles distintos y no hay claridad. |
| [E2-FORM-28] | Orientador Firmas Electrónicas | Free | S | María compró un Token Avanzado físico de $40K. Solo necesitaba la firma simple online de $2K para RES. |

### E3 — Operación Formal (11 features)

| ID | Feature | Tier | Compl. | Escenario |
|---|---|---|---|---|
| [E3-OPER-29] | **Facturador WhatsApp (ApiGateway/Pana)** | Pro | L | Patricia está vendiendo en feria. La clienta le pide factura por $50K. Tiene que dejar todo, ir a la casa y abrir el computador. |
| [E3-OPER-30] | Emisor e-Boletas exprés | Pro | L | Roxana usa la app del SII pero le quema datos en el campo y a veces simplemente no carga. Pierde la venta. |
| [E3-OPER-31] | Recordatorio Empático F29 | Free | S | María se olvidó del F29 de marzo entre los pedidos. Multa $35K + intereses. Cada mes igual: el F29 se le pasa. |
| [E3-OPER-32] | Declarador "Sin Movimiento" (F29 cero) | Free | M | Ana no vendió nada en abril por una enfermedad. Cree que "no hay que declarar". Acumuló 3 multas seguidas. |
| [E3-FIN-33] | Calculador Honorarios Líquido↔Bruto | Free | S | Carmen acordó con su sobrina pagarle $300K líquidos por diseñar el logo. No sabe cuánto retener ni cómo declararlo. |
| [E3-OPER-34] | Monitor Compras RCV (alerta facturas) | Plus | L | Luisa abrió el SII y vio una factura de $2M de un proveedor que nunca contrató. ¿Fraude? ¿Error? No sabe a quién llamar. |
| [E3-RIESGO-35] | **Traductor Notificaciones SII (correos rojos)** | Free | S | María recibió un correo del SII con palabras como "omisión sustantiva". Pánico. No abrió el correo por 2 semanas. |
| [E3-FIN-36] | Simulador Pro-Pyme Transparente (IGC) | Plus | L | Patricia retiró $5M durante el año sin saber que tributaba en su renta personal. En abril le tocó pagar $800K y no tenía la plata. |
| [E3-OPER-37] | Descargador Carpeta Tributaria | Pro | M | Roxana fue al banco a pedir crédito. El ejecutivo le pidió "su carpeta tributaria". ¿Qué es eso?, ¿de dónde la baja? |
| [E3-OPER-38] | Handoff Operación Renta F22 | Marketplace | M | María llegó a marzo con su F22 a medias. La IA dice: "esto excede lo que puedo resolver, derivémoslo a un contador" y agenda. |
| [E3-FIN-39] | Conciliador Bancario Visual (OCR cartolas) | Plus | L | Carmen cobró 80 transferencias en diciembre vía MACH y CuentaRUT. No tiene idea cuáles eran de qué clienta ni si hay morosos. |

### E4 — Crecimiento (12 features)

| ID | Feature | Tier | Compl. | Escenario |
|---|---|---|---|---|
| [E4-FIN-40] | Scout de Subsidios Sercotec/Corfo | Free | M | Patricia se enteró del Capital Semilla 2 días antes del cierre por una vecina. Imposible postular bien con esos plazos. |
| [E4-FIN-41] | **Borrador Modelo Canvas Sercotec** | Pro/Plus | M | Ana llenó el modelo Canvas como pudo en la pega. Le rechazaron por "propuesta de valor poco clara". Postulaba por tercera vez. |
| [E4-FIN-42] | Asistente Pitch Video (90s) | Pro | S | María tiene que grabar 90 segundos para Sercotec. Se traba al minuto 30. Le da vergüenza la cámara. Re-graba 8 veces. |
| [E4-FIN-43] | Recomendador Microcréditos (Banigualdad/F.Esp) | Free/Mkt | M | Carmen necesita $1M para insumos. El banco le dice no por DICOM viejo. ¿Banigualdad? ¿Fondo Esperanza? No sabe ni a cuál ir. |
| [E4-FIN-44] | Desmitificador FOGAPE | Free | S | Luisa pidió un FOGAPE creyendo que "si no me va bien, lo paga el Estado". Incumplió y ahora el banco la cobra a ella. |
| [E4-LEGAL-45] | Generador Contrato de Trabajo seguro | Pro | M | Roxana contrató a su primera ayudante. Bajó un PDF de Google. La ayudante la denunció a tutela laboral por causales mal redactadas. |
| [E4-LEGAL-46] | Guía Previred Exprés | Pro | S | Patricia quiere pagar las cotizaciones de su empleada pero el portal Previred le pide "archivo .ple". ¿Qué es eso? |
| [E4-LEGAL-47] | Simulador Finiquito básico | Plus | M | María tiene que despedir a su garzón del local. No sabe si le debe 1 o 3 sueldos. No despide por miedo y la ahorca financieramente. |
| [E4-LEGAL-48] | Generador Protocolo Ley Karin | Free | S | Carmen tiene 2 empleadas. La consultora le cotiza $250K por "implementar protocolo Ley Karin". Es un PDF genérico. |
| [E4-CRECE-49] | Bot Analista Precios Proveedores | Pro | L | Roxana lleva 3 meses pagando harina más cara y vendiendo el pan al mismo precio. Quiebra invisible: no se da cuenta. |
| [E4-CRECE-50] | Creador Textos Instagram (RAG copy) | Pro | S | Patricia tiene cuenta de Instagram con 800 seguidores pero solo sube fotos. No vende porque no sabe qué texto poner. |
| [E4-CRECE-51] | Filtro Compra Ágil <30 UTM (Mercado Público) | Plus | L | Ana podría venderle al CESFAM local por <30 UTM. Pero ChileProveedores le pide 50 formularios. Desiste. |

### E5 — Recuperación / Cierre / Pivot (9 features)

| ID | Feature | Tier | Compl. | Escenario |
|---|---|---|---|---|
| [E5-LEGAL-52] | Asesor Ley 21.563 Reorganización Mipyme | Free | M | María tiene $8M en deudas bancarias que no puede pagar. El banco la quiere embargar el auto. No sabe que la Ley 21.563 la protege 40 días. |
| [E5-LEGAL-53] | **El "Torniquete" (suspensión SII asistida)** | Pro | M | Carmen "cerró" el negocio hace 2 años. Sin avisar al SII. Acumuló $1.8M en multas F29 sin saberlo. La empresa sigue "viva". |
| [E5-EMOC-54] | Botón de la Vergüenza (educación DICOM) | Free | S | Patricia está en DICOM hace 4 años. Le ofrecen "borrar el DICOM por $50K". Es una estafa pero ella no lo sabe. |
| [E5-LEGAL-55] | Derivación Quiebra Simplificada | Plus/Mkt | M | Roxana arrastra deudas hace 5 años. No sabe que la liquidación simplificada le permitiría extinguir el saldo y volver a operar limpia. |
| [E5-EMOC-56] | Diario Post-Mortem (lecciones del fracaso) | Free | S | María cerró su panadería hace 6 meses. Llora todas las noches. No quiere ni hablar del tema con nadie. Duelo en silencio. |
| [E5-LEGAL-57] | Renegociación 2da Categoría (honorarios) | Free | S | Luisa emite boletas a honorarios por terapias. Está ahogada con cuotas vencidas. Cree que la quiebra "no aplica para ella". Sí aplica. |
| [E5-LEGAL-58] | Disolución Sociedad RES | Pro | S | Carmen y su ex-socio crearon SpA hace 3 años. Ya no se hablan. La SpA sigue "viva" acumulando obligaciones tributarias. |
| [E5-FIN-59] | Invocación Sernac Financiero | Free | S | Patricia recibe llamadas de cobranza 5 veces al día desde un call center que la insulta y la amenaza con su madre. |
| [E5-EMOC-60] | Ruta Reinvención (re-empezar como MEF) | Free | S | María quiere volver a emprender pero piensa "ya fracasé una vez, no me la creo de nuevo". MEF sería el primer paso seguro. |

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

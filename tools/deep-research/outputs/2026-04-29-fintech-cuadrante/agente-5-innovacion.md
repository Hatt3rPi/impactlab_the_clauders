# AGENTE 5 — PATRONES DE INNOVACIÓN FINTECH CHILE

**Equipo:** The Clauders · Claude Impact Lab Chile 2026
**Fecha:** 2026-04-29
**Verticales cubiertas:** Inclusión Financiera · Ciberseguridad Ciudadana · Protección de Datos
**Restricción cumplida:** ecosistema 100% chileno (sin BID Lab, CAF, Visa Everywhere, Finnosummit, Mastercard Lighthouse, Y Combinator regional ni casos globales).

---

## RESUMEN EJECUTIVO (≤ 300 palabras)

(a) **Patrones ganadores Chile encontrados: 7.** Cubren los tres verticales y se anclan en empresas registradas en CMF, financiadas por VCs chilenos (Magma, Manutara) o emergidas de Start-Up Chile / BancoEstado.

(b) **Los 3 patrones más replicables en hackathon 48h:**
1. **PATRÓN-G3 — Traductor de cartola/letra chica chilena (Vision + Citations)**: leer documentos físicos chilenos (liquidación, cartola, contrato CAE/CTC) y devolver explicación con cita exacta de NCG CMF y SERNAC. Sin licencia CMF requerida si se mantiene en plano informativo/educativo (delimitación NCG 502).
2. **PATRÓN-G5 — Asistente anti-phishing ciudadano (Vision + memoria)**: el ciudadano envía screenshot de SMS/WhatsApp/correo sospechoso y obtiene veredicto + protocolo Ley 20.009 (60 días, denuncia penal obligatoria desde Ley 21.673/2024).
3. **PATRÓN-G7 — Tramitador derechos ARCO Ley 21.719 (Structured outputs + memoria)**: genera y hace seguimiento de la solicitud ARCO ante el responsable de datos (plazo 30 días), con escalamiento automático a la Agencia de Protección de Datos.

(c) **Capacidad Claude que más ventaja crea en Chile: Vision + Citations API combinadas.** La realidad chilena obliga a leer PDFs, cartolas escaneadas y screenshots de WhatsApp; Citations cierra el riesgo regulatorio (cita NCG, no recomienda). Dolores donde es necesaria, no decorativa: (1) interpretación de contrato de crédito con CAE/CTC mal explicado, (2) detección de phishing con suplantación de banco chileno, (3) extracción de datos personales tratados sin consentimiento desde un correo o app.

(d) **Ediciones previas Claude Impact Lab Chile:** **NO existen.** Esta es la **primera edición** (6-7 mayo 2026, Espacio Riesco, 200 builders, 3 tracks). Chile fue elegido entre 9 países globales para activar Claude Impact Lab. Host: Bendita IA / Felipe Pacheco. NO inventé ganadores previos.

(e) **Path del reporte:** `C:\Users\jfonc\Documents\Claude\Projects\impact_lab\tools\deep-research\outputs\2026-04-29-fintech-cuadrante\agente-5-innovacion.md`

---

## FASE 1 — DESCOMPOSICIÓN

### Propósito reformulado
Mapear qué patrones de solución fintech están ganando en el ecosistema chileno (CMF, FinteChile, Start-Up Chile, VCs locales) y cuáles fracasan por restricción regulatoria CMF/SERNAC, para que The Clauders elija un ángulo en el Claude Impact Lab Chile que (i) sea técnicamente replicable en 48h, (ii) use capacidades nativas de Claude que crean ventaja sobre lo que ya existe en Chile y (iii) no caiga en zona de licencia obligatoria CMF.

### Dimensiones de decisión
| Dimensión | Opciones |
|---|---|
| Tipo de patrón | Scoring alternativo · Open Finance B2C · Pagos A2A · Crowdfunding/Lending · Anti-fraude ciudadano · Tutela de derechos (ARCO/portabilidad/Ley 20.009) · Interpretación regulatoria |
| Vertical | Inclusión financiera · Ciberseguridad ciudadana · Protección de datos |
| Replicabilidad 48h | Alta (UI + 1 API pública chilena + Claude) / Media (requiere dato semi-público o scrape) / Baja (requiere acuerdo banco o licencia CMF) |
| Capacidad Claude que da ventaja | Vision · Citations API · Structured outputs · Tool use + MCP · Memoria largo plazo |

### Preguntas de investigación (8)
1. ¿Existen ediciones previas de Claude Impact Lab Chile y qué ganaron?
2. ¿Qué fintechs chilenas se inscribieron en el RPSF de la CMF y por qué (servicios regulados)?
3. ¿Qué proyectos fintech chilenos apoyó Corfo / Start-Up Chile / BancoEstado en 2024-2026?
4. ¿Cómo opera el patrón "scoring alternativo para no bancarizados" en Chile (Destácame, Galgo)?
5. ¿Cómo opera el patrón "Open Finance B2C" en Chile (Fintoc, Floid, Khipu)?
6. ¿Qué patrones NO funcionan en Chile por restricción CMF (asesoría de inversión sin licencia, recomendación, finfluencer)?
7. ¿Qué capacidades específicas de Claude (Vision, Citations, Tool use con MCPs, memoria) crean ventaja sobre lo que ya existe en Chile?
8. ¿Cuáles son los dolores ciudadanos chilenos más fértiles para innovación 2026 (phishing, ARCO Ley 21.719, portabilidad Ley 21.236, tutela Ley 20.009)?

---

## FASE 2 — BITÁCORA DE INVESTIGACIÓN

### Búsquedas web (12)
1. `"Claude Impact Lab Chile" Anthropic hackathon ganadores`
2. `CMF Chile sandbox regulatorio fintech empresas 2024 2025 2026`
3. `Fintech Chile asociación gremial radiografía ecosistema 2025 2026`
4. `Destácame scoring alternativo Chile no bancarizados inclusión financiera`
5. `Fintoc Floid open finance Chile API agregación bancaria`
6. `Start-Up Chile Corfo fintech portafolio 2024 2025 SAF SSAF Semilla`
7. `Galgo Chile crédito automotriz scoring fintech`
8. `CMF asesoría financiera no autorizada multa fintech recomendación inversión Chile`
9. `Magma Partners Manutara Ventures portafolio fintech Chile inversión`
10. `phishing estafas bancarias Chile 2025 2026 ciberseguridad ciudadana`
11. `Ley 21.719 protección datos personales Chile derechos ARCO Agencia Datos`
12. `"Ley 21.236" portabilidad financiera Chile`
13. `"Impact Lab" Chile Anthropic Bendita IA hackathon 2025 ganadores equipos`
14. `BancoEstado innovación lab fintech CuentaRUT Chile AI`
15. `"Conoce tu Deuda" CMF API consulta deudas Chile`
16. `Comparador SERNAC Chile crédito consumo API datos`
17. `CMF sandbox regulatorio "piloto" empresas inscritas autorización 2025`
18. `Xepelin factoring Chile fintech IA scoring pymes`
19. `"finfluencer" Chile NCG CMF norma carácter general 100000 seguidores`
20. `"Khipu" pagos transferencia Chile fintech`
21. `DICOM Equifax Chile salir limpiar deudas comportamiento positivo`
22. `"Ley 20.009" Chile fraude tarjetas devolución bancos abuso autoreporte`
23. `phishing whatsapp chile bancos clave dinámica engañan adultos mayores 2025`
24. `Cumplo crowdfunding Chile crédito P2P fintech Broota`
25. `"finanzas abiertas" Chile OF NCG 514 implementación retraso 2027 2028`

### Web fetches (6)
- Luma — página oficial Claude Impact Lab Chile
- FinteChile — nota "168 entidades inscritas y 165 autorizadas"
- FinteChile — homepage (estado del ecosistema y empresas miembro)
- CMF Chile — portal Fintec (estado Ley Fintech)

### Hallazgos clave de Fase 2
- **Claude Impact Lab Chile = primera edición, 6-7 mayo 2026.** No hay ganadores previos. Premios: USD 500/track ganador (3 tracks), Mac Mini, 60 días en sandbox de incubación, presentación a reguladores. Datos públicos curados: CMF, SII, SERNAC.
- **Chile NO tiene sandbox regulatorio CMF tradicional.** La CMF declaró que un sandbox no le ofrece ventajas; en su lugar, está construyendo el "ambiente de prueba SFA" (Open Finance) que arrancará 9 meses antes de la entrada en vigencia de la NCG 514.
- **NCG 514 (Sistema de Finanzas Abiertas) postergada a julio 2027** (originalmente julio 2026). Implementación gradual hasta 2029. FinteChile criticó la postergación; bancos y retail financiero la celebraron.
- **Registro RPSF**: 168 entidades inscritas, 165 autorizadas (datos dic-2024), >300 solicitudes en trámite. Mayoría son **asesores de inversión**.
- **Mapa Fintech Chile 2024**: 485+ empresas (incluyendo extranjeras operando en Chile). EY presenta Mapa Fintech 2026 el 7 de mayo en Chile Fintech Forum.
- **Ley 20.009 reformada por Ley 21.673 (mayo 2024)**: redujo plazo retroactividad fraude de 120 → 60 días, restitución bancaria 10 días hábiles, denuncia penal obligatoria.
- **Ley 21.719 (Protección Datos Personales)**: publicada 13-dic-2024, entra en vigencia **1-dic-2026** (durante el hackathon esto es inminente). Crea Agencia de Protección de Datos. Multas hasta 20.000 UTM o 4% de ingresos.
- **Phishing en Chile 2025**: 41.703 causas por fraude (récord, +64,4% YoY); 6,3 millones de intentos de phishing bloqueados ene-oct 2025; canal principal migró a WhatsApp y llamadas con voz IA.
- **NCG 502 — finfluencers**: divide en >100k seguidores (gobierno corporativo + gestión riesgos) vs <100k (transparencia conflictos interés). Excepción: contenido "objetivo, neutral, educativo" NO es asesoría.

---

## SECCIÓN 1 — PATRONES GANADORES EN CHILE (7)

### PATRÓN-G1: Scoring alternativo con datos de comportamiento positivo

- **DESCRIPCIÓN:** Modelo crediticio que reemplaza el scoring tradicional (DICOM/Equifax) por señales de comportamiento de pago positivo (cuentas básicas, cuentas de servicios, pagos puntuales) reportadas a la Cámara de Comercio de Santiago. Funciona en Chile porque hay **4 millones de morosos** y **~1 millón de sobreendeudados** que el sistema bancario tradicional excluye.
- **EJEMPLOS REALES CHILENOS:** **Destácame** (campaña "Hombre Invisible", servicio Destácame PRO+ con microcréditos por tramos y educación financiera), **Galgo** (ex-"Migrante", scoring para migrantes y trabajadores informales con crédito moto/auto, levantó USD 40,8M en 2023, alianza con IFC).
- **RESULTADO DOCUMENTADO:** Galgo = mayor levantamiento fintech chileno 2023. Destácame = fintech chilena referente en inclusión financiera, opera bajo Ley Fintech con difusión pública. Ambas en directorio FinteChile.
- **VERTICAL:** Inclusión Financiera.
- **REPLICABILIDAD 48H:** **Media** — requiere fuente de datos alternativa. Se puede aproximar usando Conoce tu Deuda CMF (gratis, pública) + cartola PDF subida por el usuario.
- **VENTAJA SI USA CLAUDE:** **Vision** lee cartola física + **Tool use** consulta API CMF Conoce tu Deuda + **Structured outputs** genera el "informe de comportamiento positivo" sin recomendar. Ventaja sobre Destácame: Destácame requiere registro y almacenamiento; Claude puede operar one-shot, sin persistir datos sensibles.

---

### PATRÓN-G2: Open Finance B2C / agregador de cuentas (pre-NCG 514)

- **DESCRIPCIÓN:** Conectar la cuenta bancaria del usuario chileno (con su consentimiento, vía credenciales) y devolver datos consolidados de saldo, movimientos y productos. Hoy opera por scraping consentido + iniciación de pagos A2A. La Ley Fintech (Ley 21.521) lo formaliza, pero la NCG 514 se postergó a julio 2027.
- **EJEMPLOS REALES CHILENOS:** **Fintoc** (Y Combinator, Series A USD 7M, 2024, expandió a México), **Floid** (Open Banking + APIs CMF/SII), **Khipu** (3M+ chilenos pagando, 11k pagos/hora récord en Cyber, alianza Western Union 2024).
- **RESULTADO DOCUMENTADO:** Fintoc procesa pagos A2A en producción Chile. Khipu integrado a >4.000 comercios. Todos miembros FinteChile.
- **VERTICAL:** Inclusión Financiera + Datos.
- **REPLICABILIDAD 48H:** **Baja para B2C nuevo** (porque requiere acuerdos bancarios o scraping con riesgo legal). **Alta** si se usa la **API pública de Conoce tu Deuda CMF** (vía Floid widget) o el comparador SERNAC.
- **VENTAJA SI USA CLAUDE:** **Tool use con MCPs** que envuelvan API CMF + SERNAC + ChileAtiende permite agregación sin scraping bancario. **Citations** entrega cada dato con cita oficial (NCG, ID de informe CMF). Esto resuelve la principal objeción de la CMF: trazabilidad regulatoria.

---

### PATRÓN-G3: Traductor de cartola / letra chica chilena (zona segura sin licencia CMF)

- **DESCRIPCIÓN:** El usuario sube fotografía o PDF de su contrato de crédito, cartola, liquidación o póliza, y la solución descompone el costo real (CAE, CTC, comisiones, seguro de desgravamen), citando la NCG correspondiente. **Es zona segura porque la NCG 502 / FAQ jul-2024 excluye explícitamente "comunicación meramente informativa o educativa" del concepto de asesoría de inversión.**
- **EJEMPLOS REALES CHILENOS:** Comparador SERNAC (créditos de consumo) muestra el patrón pero solo simula a partir de filtros (monto/plazo/desgravamen). Destácame y CMF Educa publican glosarios. Falta una herramienta que lea **el documento real del usuario**.
- **RESULTADO DOCUMENTADO:** Comparador SERNAC es la herramienta oficial; SERNAC reportó diferencias de >$132.000 entre ofertas para el mismo préstamo de $1MM a 12 meses. La brecha de comprensión es masiva.
- **VERTICAL:** Inclusión Financiera + Datos.
- **REPLICABILIDAD 48H:** **Alta** — Vision + Citations + Comparador SERNAC público. No requiere acuerdo con bancos.
- **VENTAJA SI USA CLAUDE:** **Vision** procesa scans/fotos de cartolas chilenas con formato de cada banco (Estado, Chile, Santander, BCI) + **Citations API** ancla cada cifra a la NCG correspondiente. Ningún Comparador chileno hoy lee el documento físico del usuario; todos exigen tipeo manual de filtros.

---

### PATRÓN-G4: Factoring digital con scoring IA para pymes

- **DESCRIPCIÓN:** Plataforma 100% digital que aprueba factoring/confirming en 24-48h usando scoring crediticio basado en IA propia, alimentada por SII (boletas/facturas) y comportamiento de pago histórico.
- **EJEMPLOS REALES CHILENOS:** **Xepelin** (premio plata Fintech América 2026 categoría IA), **Cumplo** (>USD 116M financiados, 1.000 empresas, 4.000+ créditos), **Broota** (equity crowdfunding), **RedCapital**.
- **RESULTADO DOCUMENTADO:** Xepelin reconocida regionalmente por uso de IA. Cumplo es la mayor plataforma de crowdlending chilena. Todos miembros FinteChile.
- **VERTICAL:** Inclusión Financiera (pymes).
- **REPLICABILIDAD 48H:** **Media** — requiere datos SII (no son públicos sin clave del contribuyente) o cartola de cuenta corriente.
- **VENTAJA SI USA CLAUDE:** **Tool use** sobre el SII (cuando el dueño da consentimiento con su clave) + **Vision** sobre la factura escaneada + **Structured outputs** que genera el dossier de scoring. Hoy Xepelin tiene IA propia entrenada in-house; un equipo de hackathon difícilmente compite ahí en 48h. **Patrón menos atractivo para el lab** que G3, G5, G7.

---

### PATRÓN-G5: Asistente anti-phishing ciudadano (Ley 20.009)

- **DESCRIPCIÓN:** El ciudadano reenvía un SMS/WhatsApp/email sospechoso, y la solución dictamina si es phishing, identifica la suplantación específica (BancoEstado, SII, ChileAtiende) y entrega el protocolo exacto bajo Ley 20.009 (modificada por Ley 21.673/2024): aviso 24/7 al banco, 60 días retroactividad, denuncia penal obligatoria, restitución 10 días hábiles.
- **EJEMPLOS REALES CHILENOS:** No existe una herramienta consolidada chilena que combine veredicto + protocolo. CSIRT Gobierno publica alertas, ANCI publica recomendaciones, bancos tienen formularios. **Hueco grande**.
- **RESULTADO DOCUMENTADO:** 41.703 causas de fraude en 2025 (récord, +64,4% YoY); 6,3M intentos de phishing bloqueados ene-oct 2025. Adultos mayores son el target primario.
- **VERTICAL:** Ciberseguridad Ciudadana.
- **REPLICABILIDAD 48H:** **Alta** — Vision + Citations a Ley 20.009 + protocolo estructurado. No requiere API privada.
- **VENTAJA SI USA CLAUDE:** **Vision** procesa screenshot de WhatsApp con logo del banco + **Citations API** cita Ley 20.009 art. específico + **Memoria largo plazo** sigue al usuario en los 60 días: recordatorio de denuncia penal, plazos de respuesta del banco, escalamiento a SERNAC si la entidad no restituye en 10 días hábiles. Ningún producto chileno cubre el ciclo completo hoy.

---

### PATRÓN-G6: Acelerador de portabilidad financiera (Ley 21.236)

- **DESCRIPCIÓN:** Automatizar la solicitud del Certificado de Liquidación + cotización con el nuevo proveedor + ejecución de la portabilidad. Ley 21.236 (vigente desde 2020) reduce ~60% el costo de refinanciamiento (de $700k a $280k para crédito de 1.000 UF).
- **EJEMPLOS REALES CHILENOS:** Bancos ofrecen portabilidad, pero el proceso sigue siendo opaco para el ciudadano. No existe una herramienta neutral que empuje la decisión. SERNAC publica simulador, pero no ejecuta el flujo.
- **RESULTADO DOCUMENTADO:** "A 5 años de la Portabilidad Financiera" (DOE) reporta uso muy por debajo del potencial.
- **VERTICAL:** Inclusión Financiera.
- **REPLICABILIDAD 48H:** **Media** — el flujo de portabilidad real exige firma electrónica avanzada del cliente. En 48h se puede prototipar la fase de **diagnóstico + simulación + redacción de la solicitud**.
- **VENTAJA SI USA CLAUDE:** **Structured outputs** genera el formulario de solicitud de Certificado de Liquidación que el ciudadano firma. **Citations** referencia Ley 21.236. **Memoria** sigue al cliente en los 7-10 días que toma el banco actual responder.

---

### PATRÓN-G7: Tramitador de derechos ARCO (Ley 21.719, vigencia 1-dic-2026)

- **DESCRIPCIÓN:** Asistente que ejerce los derechos ARCO + portabilidad de datos personales del ciudadano frente a un responsable de tratamiento (banco, retailer, AFP, plataforma fintech). Genera la solicitud, hace seguimiento de los 30 días corridos de respuesta, y si el responsable niega/no responde, formula reclamación a la Agencia de Protección de Datos en los 30 días hábiles siguientes.
- **EJEMPLOS REALES CHILENOS:** Hoy NO existe en Chile. La Ley 21.719 entra en vigencia **1-dic-2026** — el hackathon (mayo 2026) es el momento óptimo para construir esta herramienta antes de que el mercado se sature.
- **RESULTADO DOCUMENTADO:** Multas hasta 20.000 UTM (~CLP 1.300M) o 4% de ingresos anuales. Nuevas atribuciones de la Agencia.
- **VERTICAL:** Protección de Datos.
- **REPLICABILIDAD 48H:** **Alta** — solo requiere conocer la Ley 21.719 y los formularios estándar. No depende de APIs privadas.
- **VENTAJA SI USA CLAUDE:** **Structured outputs** genera la solicitud ARCO formal (con todos los campos exigidos por la ley). **Citations** cita art. específico de la Ley 21.719. **Memoria largo plazo** es esencial: el flujo dura mínimo 60 días (30 + 30) y puede llegar a 6 meses si la Agencia interviene. **Tool use** con MCPs futuros para enviar la solicitud por correo certificado / Mercurio. **Este patrón es el que más se alinea con la primera edición del Impact Lab**: aprovecha capacidad nativa de Claude que en Chile nadie está usando aún.

---

## SECCIÓN 2 — ANTI-PATRONES EN CHILE (5)

### ANTI-PATRÓN-A1: Recomendación de inversión sin licencia (asesor de inversión NCG 502)

- **POR QUÉ FALLA EN CHILE:** Desde 3-feb-2024, ninguna entidad puede prestar servicio de asesoría de inversión sin estar inscrita en el RPSF y autorizada por la CMF. Construir un "robo-advisor" o "AI que sugiere portafolio" en hackathon = bandera roja inmediata.
- **EJEMPLO CHILENO REAL DE FALLA:** La CMF advirtió que las entidades que prestaban servicios fintech sin presentar inscripción al 3-feb-2024 debían **cesar operaciones**. Ya hubo procedimientos sancionatorios (CMF persigue a finfluencers > 100k seguidores que no se registraron).
- **SEÑAL DE ALERTA:** El producto contiene los verbos **"te recomiendo", "deberías invertir en", "este fondo es mejor", "compra X"** o entrega ranking de instrumentos sugerido al usuario. Si el output es **una decisión** y no **un cálculo o cita**, está en zona regulada.

---

### ANTI-PATRÓN-A2: Recomendación crediticia sin licencia (asesoría de crédito NCG 502)

- **POR QUÉ FALLA EN CHILE:** Igual que A1, pero para crédito. La Ley Fintech tipifica "asesoría crediticia" como servicio regulado. Decir "te conviene tomar el crédito Banco X a 24 meses" sin estar registrado = infracción.
- **EJEMPLO CHILENO REAL DE FALLA:** El Comparador SERNAC se cuida explícitamente: muestra cifras y CAE, pero **no recomienda**. Ese es el modelo a copiar.
- **SEÑAL DE ALERTA:** El bot dice "te conviene" / "es mejor para ti" / "elige este crédito". Reformular como: "Según la NCG CMF, los costos comparados son: [tabla]. La decisión es tuya."

---

### ANTI-PATRÓN-A3: Custodia de credenciales bancarias del usuario

- **POR QUÉ FALLA EN CHILE:** Almacenar la clave de internet banking del usuario para hacer scraping persistente queda fuera del alcance del "consentimiento expreso de Ley Fintech" si la NCG 514 no está vigente (julio 2027). Adicionalmente, los bancos chilenos persiguen activamente a quienes hacen scraping no consentido (vulnera términos y condiciones, riesgo de bloqueo y eventual demanda).
- **EJEMPLO CHILENO REAL DE FALLA:** Khipu y Floid evolucionaron justamente para alejarse del scraping puro hacia A2A (transferencia iniciada). Fintoc se posiciona como "instant payments API", no como aggregator persistente. **El sandbox SFA no existe aún para el público hackathon**: se habilitará 9 meses antes de julio 2027.
- **SEÑAL DE ALERTA:** El proyecto pide al usuario su clave de coordenadas / clave dinámica / contraseña de banco para "automatizar". Reformular: usar Conoce tu Deuda CMF (clave única, no bancaria) o que el usuario suba PDF/screenshot de su cartola.

---

### ANTI-PATRÓN-A4: Solución que requiere Ley Fintech / NCG 514 vigente para funcionar

- **POR QUÉ FALLA EN CHILE:** La NCG 514 (Sistema de Finanzas Abiertas) se postergó de julio 2026 a **julio 2027**, con implementación gradual hasta 2029 e información real fluyendo recién en 2028. Cualquier producto que asuma que el SFA está operativo en mayo 2026 = no se puede demostrar funcionando.
- **EJEMPLO CHILENO REAL DE FALLA:** FinteChile se enfrentó públicamente con la CMF por la postergación; bancos y retail financiero la celebraron. Esto significa que el campo está bloqueado.
- **SEÑAL DE ALERTA:** El pitch dice "cuando el Open Finance Chile esté en producción, esto va a funcionar". Reformular: usar APIs ya públicas (Conoce tu Deuda CMF, Comparador SERNAC, ChileAtiende, Banco Central de Chile API).

---

### ANTI-PATRÓN-A5: Auto-reporte fraudulento Ley 20.009

- **POR QUÉ FALLA EN CHILE:** La Ley 21.673 (mayo 2024) reformó la Ley 20.009 endureciendo el régimen: redujo retroactividad a 60 días, hizo obligatoria la denuncia penal, y **mantiene la sanción penal para quien simula fraude para obtener restitución indebida** (mismas penas que el fraude real). Construir una herramienta que "ayude" al ciudadano a declarar fraudes para recuperar dinero está bordeando ilegalidad.
- **EJEMPLO CHILENO REAL DE FALLA:** La Corte Suprema, en noviembre 2025, fijó criterio estricto: en engaños telemáticos donde el ciudadano "entregó voluntariamente" sus credenciales, el banco puede no restituir. Hay un debate vivo.
- **SEÑAL DE ALERTA:** La solución incentiva al usuario a "marcar como fraude" cualquier transacción que no recuerde. Reformular: la solución debe (a) verificar que efectivamente fue suplantación, (b) acompañar el aviso y la denuncia penal, (c) NO reclasificar transacciones legítimas.

---

## SECCIÓN 3 — CAPACIDADES CLAUDE QUE CREAN VENTAJA EN CHILE

### Vision — leer documentos físicos chilenos

Dolores donde es **necesaria, no decorativa**:
1. **Cartola de cuenta corriente / cuenta vista chilena** (BancoEstado, Chile, Santander, BCI, Itaú, Scotiabank). Cada banco tiene formato distinto, hay millones de chilenos que reciben PDF mensual y no saben leerlo.
2. **Liquidación de sueldo chilena** (Previred, formatos AFP/isapre/Fonasa). Necesaria para scoring alternativo, postulación a crédito, validación de ingreso.
3. **Screenshot de phishing por WhatsApp/SMS** suplantando BancoEstado, ChileAtiende, SII, retail (Falabella CMR, Líder, Ripley). El logo es la señal — nadie le pide al ciudadano transcribir el SMS, le piden subirlo.

### Citations API — citar fuentes regulatorias chilenas

Dolores donde es **necesaria**:
1. **Comparador de créditos SERNAC** — cuando el bot entrega un cálculo de CAE, debe citar la fuente y fecha del Comparador para que el ciudadano lleve evidencia al banco.
2. **NCG CMF citada en cifras de costos** — la diferencia entre "te recomiendo" (zona regulada) y "según NCG CMF X esto cuesta" (zona segura) literalmente la marca la cita.
3. **Ley 21.719 art. específico** al ejercer derecho ARCO — la solicitud sin cita legal exacta puede ser rechazada por el responsable de datos.

### Structured outputs — generar formularios chilenos

Dolores donde es **necesaria**:
1. **Solicitud de portabilidad Ley 21.236** — formulario con campos exactos: monto adeudado, costo prepago, comisiones, fecha curse. Si se omite un campo el banco lo rechaza.
2. **Denuncia SERNAC online** — esquema con datos del proveedor, fecha del hecho, tipo de infracción (Ley 19.496, Ley 21.521).
3. **Solicitud ARCO Ley 21.719** — campos obligatorios: identificación titular, derecho ejercido (acceso/rectificación/cancelación/oposición/portabilidad), datos específicos, vía de respuesta.

### Tool use + MCPs — consultar APIs chilenas

Dolores donde es **necesaria**:
1. **Conoce tu Deuda CMF** (gratis, requiere ClaveÚnica + 2FA email desde dic-2025) — ningún producto chileno hoy lo orquesta vía Claude.
2. **Comparador SERNAC** (web pública, no API formal — scraping respetuoso permitido) — datos actualizados mensualmente.
3. **ChileAtiende** (catálogo de trámites) — para responder "cómo salir de DICOM", "cómo postular Bono Trabajo Mujer", "cómo pedir mi informe de deudas".
4. **API Banco Central de Chile** (UF, UTM, dólar observado) — para cálculos de costo real en pesos.

### Memoria de largo plazo — seguimiento procesos chilenos multi-etapa

Dolores donde es **necesaria**:
1. **Ciclo Ley 20.009 anti-fraude** — 60 días retroactividad + denuncia penal + 10 días hábiles restitución. Sin memoria, el ciudadano olvida los plazos y pierde el derecho.
2. **Ciclo ARCO Ley 21.719** — 30 días corridos respuesta + 30 días hábiles para reclamar a la Agencia + hasta 6 meses para resolución. Es el caso de uso de memoria más fuerte de los tres.
3. **Postulación a Bono Trabajo Mujer / IPS / pensión** — flujos de varios meses con notificaciones intermedias.

---

## SECCIÓN 4 — ANÁLISIS DE RIESGO REGULATORIO CHILENO

### Tabla de respuestas PROHIBIDAS vs PERMITIDAS

| ZONA REGULADA (necesita licencia CMF) | ZONA SEGURA (informativa/educativa) |
|---|---|
| "Te recomiendo tomar el crédito de Banco X" (asesoría crediticia, NCG 502) | "Según la NCG CMF y el Comparador SERNAC, los CAEs vigentes son: [tabla con cita y fecha]. La decisión es tuya." |
| "Compra acciones de Falabella, va a subir" (asesoría de inversión, NCG 502) | "Cifras del último estado financiero presentado a la CMF (ID hecho esencial: X, fecha): ingresos Y, deuda Z. No es recomendación." |
| "Tu mejor AFP es Capital" (asesoría previsional, requiere autorización Superintendencia Pensiones) | "Según los datos publicados por la Super de Pensiones a [fecha], la rentabilidad acumulada del Fondo X en cada AFP es: [tabla]." |
| "Reclama este movimiento como fraude así te devuelven la plata" (incentivo a auto-reporte fraudulento Ley 21.673) | "La Ley 20.009 (modificada por Ley 21.673/2024) establece protocolo: aviso 24/7 al banco + denuncia penal obligatoria. Verifica primero si reconoces la operación. Auto-reportar fraude inexistente tiene las mismas penas que el fraude." |
| "Yo te ejerzo el derecho ARCO en tu nombre" sin mandato escrito (suplantación de titular) | "Genero la solicitud para que la firmes y envíes tú al responsable de datos. Si no responde en 30 días corridos, te ayudo a escalar a la Agencia." |

### Reglas operativas para el equipo The Clauders

1. **Nunca usar verbos imperativos** sobre decisiones financieras: invierte, compra, vende, toma, contrata, elige.
2. **Siempre cerrar con "la decisión es tuya"** o equivalente.
3. **Usar Citations API** sobre toda cifra que provenga de regulador chileno (CMF, SERNAC, Banco Central, SII).
4. **Si la solución requiere intermediar dinero o tomar custodia** → necesita licencia → salir del alcance del hackathon.
5. **Si la solución acompaña al ciudadano en ejercicio de un derecho ya consagrado** (Ley 20.009, Ley 21.236, Ley 21.719) → zona segura, alta replicabilidad.

---

## FUENTES NUMERADAS

1. Luma — Claude Impact Lab Chile, 6-7 mayo 2026 — https://luma.com/claudeimpactlabchile
2. Bendita IA — La Bendita Hackathon IA x Teletón 2025 — https://bendita-hackathon-ia.lovable.app/
3. AI Tinkerers — Anthropic Ambassador Chile — https://nyc.aitinkerers.org/talks/rsvp_HCvohBDd5hs
4. CMF Chile — Portal Fintec — https://www.cmfchile.cl/portal/principal/613/w3-propertyvalue-43589.html
5. CMF Chile — NCG 502, NCG 514, comunicados — https://www.cmfchile.cl/normativa/ncg_502_2024.pdf
6. CMF Chile — Conoce tu Deuda — https://conocetudeuda.cmfchile.cl/
7. CMF Chile — Ley 20.009 — https://www.cmfchile.cl/portal/principal/613/w3-article-29132.html
8. CMF Chile — Open Finance System regulation — https://www.cmfchile.cl/portal/principal/613/w3-article-82752.html
9. CMF Chile — Aplazamiento NCG 514 — https://www.cmfchile.cl/portal/prensa/615/w3-article-100482.html
10. FinteChile — Homepage y noticias — https://www.fintechile.org/
11. FinteChile — "168 entidades inscritas y 165 autorizadas" — https://www.fintechile.org/noticias/168-entidades-inscritas-y-165-autorizadas-asi-avanza-el-proceso-de-inscripcion-de-prestadores-fintech-en-la-cmf
12. FinteChile — Postergación SFA — https://www.fintechile.org/noticias/fintechs-alertan-por-nuevo-retraso-en-finanzas-abiertas-implementacion-se-postergaria-a-2027
13. La Tercera — Chile Fintech Forum 2026 — https://www.latercera.com/emprendimiento/noticia/mas-de-6-mil-asistentes-y-90-speakers-de-todo-el-mundo-los-detalles-del-chile-fintech-forum-2026/
14. CNN Chile — Destácame Chile Sin Deudas — https://www.cnnchile.com/empresas2050/destacame-aplicacion-morosos-deudas-chile_20200905/
15. Chócale — Destácame Hombre Invisible — https://chocale.cl/2025/10/campana-del-hombre-invisible-destacame/
16. Diario Financiero — Inclusión financiera Chile — https://www.df.cl/mercados/chile-se-convierte-en-el-pais-con-mejor-nivel-de-inclusion-financiera-en
17. TechCrunch — Fintoc Series A — https://techcrunch.com/2024/04/25/fintoc-a2a-payments-chile-mexico/
18. Floid — Open Finance Chile — https://www.floid.io/
19. Khipu — Open Finance Chile — https://www.khipu.com/en-us/
20. LatamFintech — Galgo USD 40,8M — https://www.latamfintech.co/articles/fintech-galgo-cierra-ronda-por-us-40-8m-convirtiendose-en-el-mayor-levantamiento-chileno-de-2023
21. Galgo — Crédito automotriz inteligente — https://www.galgo.com/blog/educacion-financiera/credito-inteligente
22. Xepelin — Top 10 fintech Chile — https://xepelin.com/blog/pymes/top-10-fintech-chile
23. Gerencia.cl — Xepelin reconocimiento IA — https://www.gerencia.cl/inteligencia-artificial/fintech-chilena-xepelin-obtiene-reconocimiento-regional/
24. Magma Partners — Portafolio LATAM Chile — https://magmapartners.com/
25. Manutara Ventures — Portafolio Chile (Tracxn) — https://tracxn.com/d/venture-capital/manutara-ventures/
26. Diario Financiero — BancoEstado USD 50M startups 2025 — https://www.df.cl/mercados/bancoestado-estima-entregar-us-50-millones-para-el-financiamiento-de
27. BancoEstado — Compraquí brazo fintech — https://www.df.cl/df-lab/transformacion-digital/la-estrategia-de-compraqui-el-brazo-fintech-de-bancoestado-para
28. SERNAC — Comparador Créditos Consumo — https://www.sernac.cl/portal/619/w3-article-84607.html
29. SERNAC — Diferencias en costo crédito $1MM — https://www.sernac.cl/portal/604/w3-article-87349.html
30. SERNAC — Especial Ley de Fraudes — https://www.sernac.cl/portal/604/w3-propertyname-791.html
31. Diario Constitucional — CS criterio Ley 20.009 nov-2025 — https://www.diarioconstitucional.cl/2025/11/14/corte-suprema-fija-criterio-sobre-fraude-bancario-y-reafirma-aplicacion-estricta-de-la-ley-n20-009-frente-a-enganos-telematicos/
32. Carey — Ley 21.719 publicación — https://www.carey.cl/publican-la-ley-n-21-719-que-modifica-la-ley-n-19-628-sobre-proteccion-de-la-vida-privada-en-el-diario-oficial
33. Contreras Cantuarias — Derechos ARCO Ley 21.719 — https://contrerascantuarias.com/2025/08/15/tus-datos-tus-derechos-entendiendo-los-derechos-arco-bajo-la-nueva-ley-21-719-en-chile/
34. CMF Chile — Ley 21.236 Portabilidad Financiera — https://www.cmfchile.cl/portal/principal/613/w3-article-29779.html
35. BCN — Ley 21.236 Portabilidad — https://www.bcn.cl/leychile/navegar?idNorma=1146340
36. Carey — CMF perfecciona regulación NCG 502 — https://www.carey.cl/cmf-perfecciona-regulacion-sobre-prestadores-de-servicios-financieros-de-la-ley-fintech
37. CMF Chile — Parámetros finfluencer — https://www.cmfchile.cl/portal/prensa/615/w3-article-82812.html
38. Fast Check — Finfluencer acreditado CMF — https://www.fastcheck.cl/2024/08/03/su-influencer-financiero-esta-acreditado-la-exigente-prueba-que-deben-rendir-los-finfluencer-y-la-nueva-disposicion-de-la-cmf/
39. Diario Financiero — CMF influencers asesores inversión — https://www.df.cl/mercados/banca-fintech/cmf-influencers-que-brinden-recomendaciones-financieras-deberan
40. La Tercera — Phishing Chile — https://www.latercera.com/piensa-digital/noticia/phishing-la-amenaza-a-la-ciberseguridad-que-mas-ha-aumentado-a-chile/DXTKMP4GKBFFRN7YO33DGUZ474/
41. CutSecurity — Phishing en Chile 2025 ANCI — https://cutsecurity.cl/blog/phishing-en-chile-2025-segun-la-anci/
42. Revista Seguridad & Defensa — Récord histórico fraudes 2025 — https://revistaseguridad.cl/2026/01/27/registros-historicos-de-fraudes-en-chile-suplantacion-migra-a-whatsapp-y-llamadas/
43. CSIRT Gobierno de Chile — Alertas — https://csirt.gob.cl/alertas/
44. ChileAtiende — Informe deudas sistema financiero — https://www.chileatiende.gob.cl/fichas/2614-informe-de-deudas-del-sistema-financiero
45. ChileAtiende — Comparador créditos consumo — https://www.chileatiende.gob.cl/fichas/16219-comparador-de-creditos-de-consumo
46. Hacienda — Plataforma Conoce tu Deuda lanzamiento — https://www.hacienda.cl/noticias-y-eventos/noticias/ministro-marcel-y-cmf-presentan-plataforma-conoce-tu-deuda
47. Cumplo — Crowdfunding/crowdlending Chile — https://cumplo.com/us/
48. LedgiFi — CMF plan regulatorio 2026-2027 — https://blog.ledgifi.com/cmf-2026-2027-plan-regulatorio-pagos-fintech-chile/
49. InfoCheck — 2025 año clave consolidación fintech Chile — https://www.infocheck.cl/blog/2025-el-a%C3%B1o-clave-para-la-consolidaci%C3%B3n-de-la-industria-fintech-en-chile
50. LexLatin — Regulación fintech Chile CMF — https://lexlatin.com/reportajes/regulacion-fintech-chile-cmf-desafios-empresas

---

**Fin del reporte Agente 5.**

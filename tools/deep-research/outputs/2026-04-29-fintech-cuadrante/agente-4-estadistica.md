# AGENTE 4 — ESTADÍSTICA Y EVIDENCIA
## Claude Impact Lab Chile 2026 — Equipo The Clauders
**Fecha**: 2026-04-29
**Misión**: cuantificar dolores ciudadanos chilenos en Inclusión Financiera, Ciberseguridad Ciudadana y Protección de Datos.

---

## FASE 1 — DESCOMPOSICIÓN

### Propósito reformulado
Cuantificar con datos chilenos verificables (preferentemente 2023-2026) la magnitud de los dolores ciudadanos en las tres verticales del proyecto, para priorizar oportunidades fintech por # personas afectadas y $ CLP en juego, y validar/invalidar hipótesis surgidas en investigación etnográfica y competitiva.

### Dimensiones de decisión
- **Inclusión**: bancarización × quintil × género × condición migratoria; deuda × tramo etario; comprensión productos × edad.
- **Ciberseguridad**: # denuncias × canal (PDI / SERNAC / CMF / CSIRT); $ defraudado × tipo (phishing / suplantación / vishing); tasa restitución × banco; perfil víctima × género × edad.
- **Datos personales**: % ciudadanos que conoce ARCO; # solicitudes ARCO Chile; % empresas con DPO designado; preparación ante Ley 21.719.

### Preguntas de investigación
1. ¿Cómo se distribuye la bancarización por estrato/quintil de ingreso en Chile según EFH 2024 del Banco Central?
2. ¿Cuál es el nivel de alfabetización financiera en Chile según OECD/INFE 2023 aplicado por CMF?
3. ¿Cuántos fraudes digitales/bancarios se denunciaron en Chile 2024-2025 (PDI BRICIB, SERNAC, CMF, CSIRT/ANCI)?
4. ¿Cuántas solicitudes ARCO se han ejercido vs ciudadanos con derecho a hacerlo, según CPLT?
5. ¿Cuál es la magnitud de beneficios estatales no reclamados (AFC, AFP herencia, PGU)?
6. ¿Cuál es la brecha de género en acceso al crédito chileno (rechazo, monto, hipotecario)?
7. ¿Cuántos microemprendedores informales no formalizan ante el SII y qué obliga la Ley 21.713?
8. ¿Qué % de jóvenes deudores chilenos comprende correctamente el CAE?
9. ¿Cuántos chilenos están en mora en 2025 y cuál es el monto total de la deuda morosa?
10. ¿Cuál es el grado de preparación de Chile para la Ley 21.719 que entra en vigencia el 1-dic-2026?

---

## FASE 2 — BITÁCORA DE INVESTIGACIÓN

### Búsquedas (WebSearch ejecutados, 13 totales)
1. "Encuesta Financiera Hogares Banco Central Chile 2023 bancarización quintil ingreso" — 2026-04-29
2. "CMF Chile inclusión financiera 2024 informe bancarización adultos" — 2026-04-29
3. "PDI BRICIB fraude digital Chile 2024 2025 denuncias estadísticas" — 2026-04-29
4. "SERNAC reclamos fraude bancario phishing Chile 2024 estadísticas" — 2026-04-29
5. "CSIRT Chile incidentes ciberseguridad 2024 ciudadanos reporte anual" — 2026-04-29
6. "DICOM Chile 2025 morosos número personas deuda total Equifax" — 2026-04-29
7. "CAE comprensión deudores Chile estudio educación financiera créditos" — 2026-04-29
8. "PGU Chile beneficios no reclamados Pensión Garantizada Universal cobertura" — 2026-04-29
9. "AFC Chile seguro cesantía no cobrado fondos no reclamados 2024" — 2026-04-29
10. "brecha género acceso financiero Chile mujeres crédito rechazo 2024" — 2026-04-29
11. "SII Chile microemprendedores informales formalización tributaria 2024" — 2026-04-29
12. "CPLT Consejo Transparencia Chile solicitudes datos personales ARCO 2024" — 2026-04-29
13. "Ley 21.719 datos personales Chile vigencia diciembre 2026 preparación empresas" — 2026-04-29
14. "Findex Banco Mundial Chile 2021 2022 inclusión financiera adultos cuenta" — 2026-04-29
15. "alfabetización financiera Chile OECD 2023 estudio CMF puntaje" — 2026-04-29
16. "Ley 20.009 Chile fraude tarjetas devoluciones bancos 2024 monto" — 2026-04-29
17. "migrantes Chile bancarización inclusión financiera acceso cuenta 2024" — 2026-04-29
18. "Encuesta Financiera Hogares 2024 Banco Central Chile resultados deuda" — 2026-04-29
19. "CMF Chile reclamos consumidores fraude 2024 monto defraudado bancos" — 2026-04-29
20. "CASEN 2022 Chile pobreza adultos mayores autovalencia financiera" — 2026-04-29
21. "Chile estafas digitales 2025 monto perdido víctimas Subsecretaría Prevención Delito" — 2026-04-29
22. "CMF informe género Chile sistema financiero 2024 deudoras mujeres" — 2026-04-29
23. "AFP Chile herencias no cobradas saldos cuenta capitalización fallecidos" — 2026-04-29
24. "Chile pago suplantación identidad bancos 2025 ANCI agencia ciberseguridad incidentes" — 2026-04-29
25. "Chile política privacidad bancos lectura usuarios encuesta protección datos 2024" — 2026-04-29
26. "Chile sobreendeudamiento 2024 tarjetas consumo morosidad por edad joven" — 2026-04-29

### Fetches completos (WebFetch)
- F1: `cmfchile.cl/portal/prensa/615/articles-76205_doc_pdf.pdf` — PDF binario, no parseable.
- F2: `sernac.cl/portal/618/articles-86590_archivo_01.pdf` — PDF binario, no parseable.
- F3: `equifax.com/.../informe_deuda_morosa_marzo_2025.pdf` — PDF binario, no parseable.
- F4: `biobiochile.cl/.../reclamos-al-alza-sernac-...shtml` — datos extraídos OK.
- F5: `politicaspublicas.uc.cl/.../EducacionInclusionFinanciera_CPP_BF.pdf` — PDF binario.
- F6: `biobiochile.cl/.../banco-central-hace-zoom-al-bolsillo-de-los-hogares...shtml` — datos EFH 2024 extraídos OK.

Nota metodológica: cuando los PDFs no fueron parseables, las cifras se obtuvieron desde las síntesis de prensa (Diario Financiero, Emol, BioBíoChile, Diario Estrategia, Cooperativa, Economía y Negocios) que citan los informes originales del Banco Central, CMF, SERNAC, USS-Equifax y Hacienda.

---

## ESTADÍSTICAS CHILENAS (≥25)

### STAT-1: Hogares chilenos con deuda 2024
- **DATO**: 51% de los hogares chilenos mantiene algún tipo de deuda
- **INDICADOR**: % de hogares con al menos un producto crediticio activo (consumo, hipotecario, educación, automotriz)
- **FUENTE**: Banco Central de Chile, Encuesta Financiera de Hogares (EFH) 2024, publicada 30-sep-2025. URL: bcentral.cl/areas/encuestas-economicas/encuesta-financiera-de-hogares
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: alta carga financiera y vulnerabilidad ante shocks de ingreso
- **FECHA DEL DATO**: trabajo de campo julio-diciembre 2024
- **SEÑAL DE TENDENCIA**: a la baja (era 57% en 2021 y 66% en 2017)

### STAT-2: Carga financiera del hogar representativo
- **DATO**: 26% del ingreso mensual destinado a pago de deudas (hogar representativo, ingreso ~$1.168.760)
- **INDICADOR**: razón pago mensual deuda / ingreso mensual líquido
- **FUENTE**: BCCh, EFH 2024 (vía BioBíoChile, 30-sep-2025)
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: estrés financiero y baja capacidad de ahorro
- **FECHA DEL DATO**: 2024
- **SEÑAL DE TENDENCIA**: estable respecto a 2017

### STAT-3: Carga financiera quintil más bajo
- **DATO**: 25% del ingreso mensual en pago de deuda (Estrato 1, 50% más pobre)
- **INDICADOR**: pago mensual / ingreso para hogares de menores ingresos
- **FUENTE**: BCCh, EFH 2021 (Emol y Libertad y Desarrollo, oct-2022)
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: hogares pobres pagan proporcionalmente más por deuda
- **FECHA DEL DATO**: 2021 (último dato desagregado por estrato disponible públicamente)
- **SEÑAL DE TENDENCIA**: estable

### STAT-4: Sobreendeudados con carga >50% ingreso
- **DATO**: 950.000 personas con carga financiera superior al 50% del ingreso mensual
- **INDICADOR**: # deudores en sobreendeudamiento (RDI > 50%)
- **FUENTE**: CMF, Radiografía del endeudamiento, jun-2024 (Cooperativa.cl, 16-ene-2025)
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: incapacidad de pago, ciclo de refinanciamiento
- **FECHA DEL DATO**: junio 2024
- **SEÑAL DE TENDENCIA**: a la baja (16,5% del total deudores en 2024 vs 19,1% en 2023; -83.000 personas)

### STAT-5: Personas con deudas morosas
- **DATO**: 3.909.120 personas con deudas impagas en Chile
- **INDICADOR**: # adultos +18 con al menos una obligación en mora
- **FUENTE**: USS-Equifax, 48° Informe de Deuda Morosa Q1 2025
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: exclusión del sistema crediticio formal, registro DICOM
- **FECHA DEL DATO**: enero-marzo 2025
- **SEÑAL DE TENDENCIA**: a la baja (-3,4% en 12 meses)

### STAT-6: Tasa de morosidad nacional
- **DATO**: 24,8% de los chilenos +18 con deudas se encuentra en mora
- **INDICADOR**: tasa de morosidad de la población adulta endeudada
- **FUENTE**: USS-Equifax, 48° Informe Deuda Morosa Q1 2025
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: 1 de cada 4 adultos endeudados no logra pagar
- **FECHA DEL DATO**: marzo 2025
- **SEÑAL DE TENDENCIA**: a la baja (-1,1 pp en 12 meses)

### STAT-7: Monto total deuda morosa Chile
- **DATO**: USD 9.416 millones (≈ 2,81% del PIB chileno)
- **INDICADOR**: stock total de deuda en mora del sistema
- **FUENTE**: USS-Equifax, 48° Informe Deuda Morosa Q1 2025
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: magnitud agregada del problema de impago
- **FECHA DEL DATO**: marzo 2025
- **SEÑAL DE TENDENCIA**: a la baja anual

### STAT-8: Mora promedio individual
- **DATO**: $2.278.942 CLP por persona morosa
- **INDICADOR**: monto promedio de deuda en mora por individuo
- **FUENTE**: USS-Equifax, 48° Informe Q1 2025
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: deuda significativa (~5 sueldos mínimos) por persona
- **FECHA DEL DATO**: marzo 2025
- **SEÑAL DE TENDENCIA**: estable (-0,2% en 12 meses)

### STAT-9: Alfabetización financiera Chile (OECD/INFE)
- **DATO**: índice de alfabetización financiera Chile = 45% del puntaje máximo (3,15 sobre 7,0)
- **INDICADOR**: puntaje agregado conocimiento + actitud + comportamiento (metodología OECD/INFE 2022)
- **FUENTE**: CMF, 2ª Encuesta Capacidades Financieras, presentada por Solange Berstein, 2023. URL: cmfchile.cl/portal/prensa/615/w3-article-76235.html
- **VERTICAL**: Inclusión Financiera / Datos
- **DOLOR ASOCIADO**: Chile bajo el promedio OECD y latinoamericano
- **FECHA DEL DATO**: 2023 (encuesta cara-a-cara a 1.212 personas, abril-junio 2023)
- **SEÑAL DE TENDENCIA**: estable / preocupante

### STAT-10: Conocimiento del CAE en jóvenes
- **DATO**: solo 31% de jóvenes 18-29 años sabe qué es el CAE
- **INDICADOR**: % de jóvenes que reconoce y comprende el Crédito con Aval del Estado
- **FUENTE**: estudio educación financiera, repositorio U. Chile (referido por El Mostrador y Centro Políticas Públicas UC, 2024)
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: deudores que firman sin entender
- **FECHA DEL DATO**: 2023
- **SEÑAL DE TENDENCIA**: estable

### STAT-11: Niveles de conocimiento financiero
- **DATO**: 42% chilenos baja alfabetización financiera, 37% intermedia, solo 21% alta
- **INDICADOR**: distribución de conocimiento financiero adulto
- **FUENTE**: Repositorio U. Chile / Centro Políticas Públicas UC (2024)
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: 4 de cada 10 chilenos vulnerables ante decisiones financieras
- **FECHA DEL DATO**: 2023-2024
- **SEÑAL DE TENDENCIA**: estable

### STAT-12: Stock CAE — deudores acumulados
- **DATO**: 1.110.000 estudiantes han usado el CAE (acumulado a fines 2021)
- **INDICADOR**: stock acumulado beneficiarios CAE desde 2006
- **FUENTE**: Mineduc, Primer Informe CAE Jul-2022 (educacionsuperior.mineduc.cl)
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: cohorte masiva endeudada con producto que no comprende
- **FECHA DEL DATO**: 2021
- **SEÑAL DE TENDENCIA**: al alza (continúa otorgándose)

### STAT-13: Mora judicial CAE
- **DATO**: 18% de los deudores CAE en cobranza judicial (2020) vs 10% en 2019
- **INDICADOR**: % deudores en cobranza judicial / total deudores activos
- **FUENTE**: Mineduc, Primer Informe CAE 2022; CIPER Chile
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: aceleración del impago tras pandemia
- **FECHA DEL DATO**: 2020
- **SEÑAL DE TENDENCIA**: al alza

### STAT-14: Reclamos por fraude SERNAC
- **DATO**: 19.834 reclamos por fraude en 2024 vs 9.494 en 2023 (+109%)
- **INDICADOR**: # reclamos formales por fraude financiero ingresados al SERNAC
- **FUENTE**: SERNAC, "Agenda Antifraudes" jul-2025; BioBíoChile 14-jul-2025
- **VERTICAL**: Ciberseguridad Ciudadana
- **DOLOR ASOCIADO**: explosión de fraude digital en banca
- **FECHA DEL DATO**: año 2024 calendario
- **SEÑAL DE TENDENCIA**: al alza (+109% interanual)

### STAT-15: Monto reclamado por fraudes
- **DATO**: $275.000 millones CLP reclamados en 2024 vs $243.000 millones CLP en 2023 (+13%)
- **INDICADOR**: $ CLP en disputa por fraudes ante SERNAC
- **FUENTE**: SERNAC 2025 (BioBíoChile)
- **VERTICAL**: Ciberseguridad Ciudadana
- **DOLOR ASOCIADO**: el dinero efectivamente reclamado supera el cuarto de billón anual
- **FECHA DEL DATO**: 2024
- **SEÑAL DE TENDENCIA**: al alza

### STAT-16: Perfil de género de víctimas de fraude
- **DATO**: 55% de los reclamos por fraude SERNAC ingresados por mujeres; 2 de cada 3 víctimas de phishing son mujeres
- **INDICADOR**: distribución de reclamantes por género
- **FUENTE**: SERNAC 2025
- **VERTICAL**: Ciberseguridad Ciudadana / Inclusión
- **DOLOR ASOCIADO**: brecha de género también opera en victimización por fraude
- **FECHA DEL DATO**: 2023-2024
- **SEÑAL DE TENDENCIA**: al alza

### STAT-17: Perfil etario víctimas
- **DATO**: 40% de los reclamos por fraude provienen de personas <30 o >60 años
- **INDICADOR**: % víctimas en grupos etarios extremos
- **FUENTE**: SERNAC 2025
- **VERTICAL**: Ciberseguridad
- **DOLOR ASOCIADO**: jóvenes y adultos mayores son el blanco preferente
- **FECHA DEL DATO**: 2023-2024
- **SEÑAL DE TENDENCIA**: estable

### STAT-18: Reclamos suplantación identidad
- **DATO**: 2.396 reclamos por suplantación de identidad en 2024
- **INDICADOR**: # casos específicos suplantación dentro del total fraudes
- **FUENTE**: SERNAC 2025
- **VERTICAL**: Ciberseguridad / Datos
- **DOLOR ASOCIADO**: robo de identidad como vía de entrada al fraude
- **FECHA DEL DATO**: 2024
- **SEÑAL DE TENDENCIA**: al alza

### STAT-19: Reclamos contra bancos en CMF
- **DATO**: 80.798 reclamos en CMF en 2024; 71% dirigidos a bancos e instituciones financieras
- **INDICADOR**: total reclamos al regulador financiero
- **FUENTE**: CMF, Memoria/Comunicado 2025; Chócale 04-2025
- **VERTICAL**: Inclusión / Ciberseguridad
- **DOLOR ASOCIADO**: insatisfacción masiva con la banca
- **FECHA DEL DATO**: 2024
- **SEÑAL DE TENDENCIA**: al alza

### STAT-20: Pérdidas por phishing/vishing/smishing
- **DATO**: pérdidas superiores a $40.000 millones CLP (2024) por phishing/vishing/smishing
- **INDICADOR**: monto perdido por familias chilenas vía ingeniería social
- **FUENTE**: CMF y PDI, citados en bctecnologia.com / análisis sector 2024
- **VERTICAL**: Ciberseguridad
- **DOLOR ASOCIADO**: dinero efectivamente extraído de cuentas ciudadanas
- **FECHA DEL DATO**: 2024
- **SEÑAL DE TENDENCIA**: al alza

### STAT-21: Intentos de ciberataque a Chile
- **DATO**: 27.600 millones de intentos de ciberataque en 2024 (4x respecto a 6.000 millones en 2023)
- **INDICADOR**: # intentos detectados por sensores de seguridad nacional
- **FUENTE**: Fortinet FortiGuard Labs, 2024 (BC Tecnología)
- **VERTICAL**: Ciberseguridad
- **DOLOR ASOCIADO**: Chile = 3er país más atacado de LATAM
- **FECHA DEL DATO**: 2024
- **SEÑAL DE TENDENCIA**: al alza explosivo (+360%)

### STAT-22: Phishing bloqueado en 2025
- **DATO**: 6,3 millones de intentos de phishing bloqueados ene-oct 2025 (imitando bancos, e-commerce, sistemas de pago)
- **INDICADOR**: volumen anual de phishing detectado/bloqueado
- **FUENTE**: Análisis sectorial citando ANCI/CSIRT 2025 (Revista Seguridad y Defensa, 27-ene-2026)
- **VERTICAL**: Ciberseguridad
- **DOLOR ASOCIADO**: vector de ataque dominante en banca chilena
- **FECHA DEL DATO**: enero-octubre 2025
- **SEÑAL DE TENDENCIA**: al alza

### STAT-23: Composición delitos económicos PDI
- **DATO**: 18,5% de las denuncias PDI en O'Higgins 2024 fueron "estafas y otros fraudes" (sobre +7.000 denuncias regionales)
- **INDICADOR**: % delitos económicos en mix denuncias PDI regional
- **FUENTE**: PDI O'Higgins, jun-2025 (eltipografo.cl)
- **VERTICAL**: Ciberseguridad
- **DOLOR ASOCIADO**: fraude lidera la criminalidad económica
- **FECHA DEL DATO**: 2024
- **SEÑAL DE TENDENCIA**: al alza

### STAT-24: Estafas como % de causas judiciales
- **DATO**: 68,51% del total de causas judiciales nuevas a Q3 2025 fueron estafas y defraudaciones
- **INDICADOR**: % causas defraudación / total causas penales nuevas
- **FUENTE**: Revista Seguridad y Defensa, ene-2026
- **VERTICAL**: Ciberseguridad
- **DOLOR ASOCIADO**: el sistema judicial está saturado de fraude
- **FECHA DEL DATO**: tercer trimestre 2025
- **SEÑAL DE TENDENCIA**: al alza histórica

### STAT-25: Brecha género rechazo crédito consumo
- **DATO**: 18% menos probabilidad de aprobación de crédito consumo para mujeres con igual perfil de riesgo que hombres
- **INDICADOR**: diferencial probabilidad aprobación crédito ajustado por riesgo
- **FUENTE**: Estudio CIEDESS sobre banca chilena (ciedess.cl); CMF Informe Género 2024
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: discriminación crediticia no explicada por riesgo
- **FECHA DEL DATO**: 2023-2024
- **SEÑAL DE TENDENCIA**: estable

### STAT-26: Brecha hipotecaria de género
- **DATO**: solo 43% de los créditos hipotecarios se otorgan a mujeres; monto promedio 40% menor que hombres
- **INDICADOR**: % participación femenina y diferencial monto en mercado hipotecario
- **FUENTE**: CMF, Informe de Género en Sistema Financiero 2024
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: barrera estructural al acceso a vivienda
- **FECHA DEL DATO**: 2024
- **SEÑAL DE TENDENCIA**: estable

### STAT-27: Brecha bancarización migrantes
- **DATO**: solo 33% de los migrantes en Chile tiene algún producto financiero vs 97% chilenos
- **INDICADOR**: tasa tenencia producto financiero por origen
- **FUENTE**: Informe Inclusión Financiera CMF 2019; ratificado IDB Invest / AFI 2024
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: brecha de 64 pp entre nativos y migrantes
- **FECHA DEL DATO**: 2019 (último dato comparado público)
- **SEÑAL DE TENDENCIA**: estable / mejorando lento

### STAT-28: Microemprendedores informales
- **DATO**: 68% de los emprendimientos chilenos en etapa temprana opera informalmente; 40% del e-commerce sin documento tributario
- **INDICADOR**: tasa de informalidad en emprendimiento temprano (TEA)
- **FUENTE**: Global Entrepreneurship Monitor (GEM) Chile 2024; Cámara Nacional de Comercio
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: exclusión del sistema bancario por falta de inicio de actividades
- **FECHA DEL DATO**: 2024
- **SEÑAL DE TENDENCIA**: estable; presión regulatoria al alza con Ley 21.713

### STAT-29: Fondos cesantía no reclamados (AFC)
- **DATO**: $156.051 millones CLP esperan ser reclamados; 482.033 personas afectadas
- **INDICADOR**: $ y # con saldos AFC pendientes (jubilados + herederos de fallecidos)
- **FUENTE**: AFC Chile / RediMin 2024
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: dinero ya cotizado que el ciudadano no sabe que existe
- **FECHA DEL DATO**: 2024
- **SEÑAL DE TENDENCIA**: estable

### STAT-30: PGU monto y población objetivo
- **DATO**: PGU $231.732 mensual; entregada al 90% no más rico, mayores 65 años
- **INDICADOR**: cobertura y valor del beneficio
- **FUENTE**: Superintendencia de Pensiones / IPS / ChileAtiende, feb-2026
- **VERTICAL**: Inclusión Financiera
- **DOLOR ASOCIADO**: existen adultos mayores con derecho que no postulan por desconocimiento
- **FECHA DEL DATO**: febrero 2026
- **SEÑAL DE TENDENCIA**: al alza (reajustada anualmente)

### STAT-31: Empresas con DPO (Data Protection Officer)
- **DATO**: solo 41% empresas chilenas tiene DPO designado; 54% NO lo tiene
- **INDICADOR**: % empresas preparadas para Ley 21.719 en figura clave
- **FUENTE**: PwC Encuesta Protección de Datos Personales 2025
- **VERTICAL**: Protección de Datos
- **DOLOR ASOCIADO**: brecha de cumplimiento ante vigencia 1-dic-2026
- **FECHA DEL DATO**: 2025
- **SEÑAL DE TENDENCIA**: al alza pero insuficiente

### STAT-32: Sanciones potenciales Ley 21.719
- **DATO**: hasta 20.000 UTM (~USD 1,39 millones) por infracción + suspensión 30 días
- **INDICADOR**: techo sancionatorio nuevo régimen datos
- **FUENTE**: Ley 21.719, BCN; análisis tichile.cl, rkabogados.cl
- **VERTICAL**: Protección de Datos
- **DOLOR ASOCIADO**: riesgo regulatorio masivo para incumplidores
- **FECHA DEL DATO**: ley publicada 13-dic-2024, vigente 1-dic-2026
- **SEÑAL DE TENDENCIA**: nueva; impacto pendiente

### STAT-33: Pobreza por ingresos Chile
- **DATO**: 6,5% pobreza por ingresos = 1.292.521 personas
- **INDICADOR**: # personas bajo línea de pobreza
- **FUENTE**: CASEN 2022, Ministerio Desarrollo Social
- **VERTICAL**: Inclusión Financiera (contexto)
- **DOLOR ASOCIADO**: segmento prioritario para inclusión
- **FECHA DEL DATO**: 2022
- **SEÑAL DE TENDENCIA**: a la baja (era 10,7% en 2020 y 8,5% en 2017)

### STAT-34: Hogares con adulto mayor
- **DATO**: 35,4% de hogares chilenos tiene un adulto mayor; 14,6% AM vive solo
- **INDICADOR**: composición demográfica con incidencia financiera
- **FUENTE**: CASEN 2022
- **VERTICAL**: Inclusión / Ciberseguridad (perfil vulnerable)
- **DOLOR ASOCIADO**: AM solos = blanco de fraude y desinformación financiera
- **FECHA DEL DATO**: 2022
- **SEÑAL DE TENDENCIA**: al alza por envejecimiento poblacional

### STAT-35: Comportamiento pago mujeres vs hombres
- **DATO**: mora bancaria <90 días 0,31% mujeres vs 0,40% hombres en 2025
- **INDICADOR**: tasa morosidad bancaria por género
- **FUENTE**: CMF, Informe de Género 2024
- **VERTICAL**: Inclusión
- **DOLOR ASOCIADO**: mejor comportamiento femenino NO se traduce en mejor acceso (paradoja)
- **FECHA DEL DATO**: 2025
- **SEÑAL DE TENDENCIA**: estable

---

## RANKING DE DOLORES CHILENOS POR MAGNITUD CUANTIFICADA

| # | Dolor | # Chilenos afectados | $ CLP en juego | Vertical | Fuente |
|---|---|---|---|---|---|
| 1 | Mora / DICOM (deudores impagos) | **3.909.120** | **USD 9.416 M ≈ $9 billones CLP** | Inclusión | USS-Equifax Q1 2025 |
| 2 | Hogares con deuda activa (~51%) | **~3,5 millones de hogares** | 47% PIB en deuda hogar (~$58 billones CLP stock) | Inclusión | EFH 2024 BCCh |
| 3 | Microemprendedores informales (68% TEA) | **~1.500.000** emprendedores estimado | 40% e-commerce sin documento tributario | Inclusión | GEM Chile 2024 |
| 4 | Stock CAE — deudores universitarios | **1.110.000** | USD 4.500 M (~$4,3 billones CLP) | Inclusión | Mineduc 2022 / CIPER |
| 5 | Sobreendeudados (carga >50% ingreso) | **950.000** | n/d (refinanciación incentivada) | Inclusión | CMF jun-2024 |
| 6 | Fondos AFC no reclamados | **482.033** | $156.051 millones CLP | Inclusión | AFC 2024 |
| 7 | Fraude — reclamos SERNAC (volumen oficial) | **19.834 reclamos 2024** (~personas únicas) | $275.000 millones CLP reclamados | Ciberseguridad | SERNAC 2025 |
| 8 | Reclamos a CMF (banca + financieras) | **80.798 reclamantes 2024** | n/d (porción sobre el universo) | Inclusión / Ciber | CMF 2024 |
| 9 | Pérdidas por phishing/vishing/smishing | n/d (millones expuestos) | **>$40.000 millones CLP perdidos 2024** | Ciberseguridad | CMF + PDI 2024 |
| 10 | Suplantación de identidad reclamada | **2.396 casos 2024** | parte de los $275B | Datos / Ciber | SERNAC 2025 |
| 11 | Brecha bancarización migrantes | ~600.000-800.000 sin productos | n/d | Inclusión | CMF 2019 |
| 12 | Brecha género acceso crédito | ~5,5M mujeres adultas con peor acceso | 39 pp menos en monto crédito vigente | Inclusión | CMF Género 2024 |
| 13 | Empresas sin DPO ante Ley 21.719 | 54% del universo empresarial | hasta USD 1,39M sanción × empresa | Datos | PwC 2025 |
| 14 | Adultos con baja alfabetización financiera | **~6,3 millones (42%)** | n/d | Inclusión | OECD/INFE Chile 2023 |
| 15 | Jóvenes que no entiende CAE | **~2,5M jóvenes 18-29** (69% no sabe) | parte de los USD 4.500M deuda CAE | Inclusión | UChile/CPP UC 2023 |

**Top 3 dolores por # personas afectadas**:
1. **Morosidad / DICOM**: 3,9 millones de adultos (24,8% de los endeudados).
2. **Hogares con deuda activa**: ~3,5 millones de hogares.
3. **Adultos con baja alfabetización financiera**: ~6,3 millones (transversal, mayor magnitud absoluta si se considera población adulta total).

**Top 3 dolores por $ CLP en juego**:
1. **Stock total mora**: USD 9.416 M ≈ $9 billones CLP.
2. **Stock CAE**: USD 4.500 M ≈ $4,3 billones CLP.
3. **Reclamos por fraude SERNAC**: $275.000 millones CLP en disputa anual.

---

## FUENTES NUMERADAS (con fecha de acceso 2026-04-29)

1. Banco Central de Chile — Encuesta Financiera de Hogares (EFH) 2024, presentación 30-sep-2025. https://www.bcentral.cl/areas/encuestas-economicas/encuesta-financiera-de-hogares
2. Banco Central de Chile — EFH 2021, oct-2022.
3. Banco Central de Chile — Informe Estabilidad Financiera (IEF) 2023-2024.
4. CMF Chile — Informe de Inclusión Financiera 2019 y 2024. https://www.cmfchile.cl/portal/estadisticas/617/w3-propertyvalue-45057.html
5. CMF Chile — 2ª Encuesta Capacidades Financieras (OECD/INFE) 2023. https://www.cmfchile.cl/portal/prensa/615/w3-article-76235.html
6. CMF Chile — Informe de Género en el Sistema Financiero 2024. https://www.cmfchile.cl/portal/estadisticas/617/w3-article-82118.html
7. CMF Chile — Radiografía del endeudamiento, jun-2024. https://www.cmfchile.cl/portal/prensa/615/w3-article-89610.html
8. CMF Chile — Estadísticas reclamos 2024. https://www.cmfchile.cl/portal/principal/613/w3-article-26815.html
9. SERNAC — "Agenda Antifraudes" jul-2025. https://www.sernac.cl/portal/604/w3-article-86590.html
10. SERNAC — Especial Ley de Fraude. https://www.sernac.cl/portal/604/w3-propertyname-791.html
11. PDI BRICIB — denuncias regionales 2024 (eltipografo.cl, jun-2025).
12. CSIRT Nacional Chile — alertas / documentos. https://csirt.gob.cl/documentos/
13. Agencia Nacional de Ciberseguridad (ANCI). https://anci.gob.cl/
14. Fortinet FortiGuard Labs Chile 2024 (vía bctecnologia.com).
15. USS-Equifax — 48° Informe Deuda Morosa Q1 2025. https://assets.equifax.com/marketing/chile/assets/informe_deuda_morosa_marzo_2025.pdf
16. Mineduc — Primer Informe CAE jul-2022. https://educacionsuperior.mineduc.cl/wp-content/uploads/sites/49/2022/07/PrimerInformeCAE-1.pdf
17. CIPER Chile — Reportaje CAE 2018.
18. Centro de Políticas Públicas UC — Radiografía educación e inclusión financiera Chile, ago-2025. https://politicaspublicas.uc.cl/web/content/uploads/2025/08/EducacionInclusionFinanciera_CPP_BF.pdf
19. U. Chile — Educación financiera en Chile, repositorio. https://repositorio.uchile.cl/bitstream/handle/2250/140193/Educaci%C3%B3n%20financiera%20en%20Chile,%20evidencia%20y%20recomendaciones.pdf
20. CASEN 2022 — Ministerio de Desarrollo Social. https://observatorio.ministeriodesarrollosocial.gob.cl/encuesta-casen-2022
21. AFC Chile — Fondos no reclamados 2024 (vía redimin.cl). https://www.afc.cl/
22. Superintendencia de Pensiones — PGU y Herencia AFP. https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-10531.html
23. CPLT — Procedimiento ARCO Resolución 489 dic-2022. https://www.consejotransparencia.cl/proteccion-datos-personales/
24. Ley 21.719 — Datos personales, vigencia 1-dic-2026. https://www.bcn.cl/leychile/Navegar?idNorma=1209272
25. Ley 21.713 — Formalización tributaria, vigencia ene-2026. https://www.duemint.com/blog/ley-antievasion-2026-chile-pymes-emprendedores
26. Ley 20.009 mod. Ley 21.673 — Fraudes bancarios. https://www.cmfchile.cl/portal/principal/613/w3-article-29132.html
27. PwC — Encuesta Protección de Datos Personales Chile 2025. https://www.pwc.com/cl/es/Publicaciones/Encuesta-de-Proteccion-de-Datos-Personales.html
28. Global Entrepreneurship Monitor (GEM) Chile 2024.
29. Hacienda Chile — Balance medidas sobreendeudamiento. https://www.hacienda.cl/noticias-y-eventos/noticias/balance-de-medidas-para-reducir-sobreendeudamiento-7-300-personas-han-logrado
30. Subsecretaría Prevención del Delito — Estafas digitales 2025.
31. CIEDESS — Estudio discriminación bancaria mujeres. https://www.ciedess.cl/601/w3-article-4818.html
32. IDB Invest / AFI Global — Inclusión financiera migrantes Chile 2024. https://www.afi-global.org/wp-content/uploads/2024/06/AFI-LAC-Migrants-Special-Report_SP-v3.pdf
33. Diario Financiero, Emol, BioBíoChile, Cooperativa, El Mostrador, Diario Estrategia — síntesis de prensa de los reportes oficiales (2024-2026).
34. Revista Seguridad y Defensa — registros históricos fraudes Chile, ene-2026.
35. BCCh Recuadro I.2 — Marco regulatorio fraude pagos digitales. https://www.bcentral.cl/documents/33528/7519196/RECUADRO%20I.2%20Marco%20regulatorio%20del%20fraude%20con%20pagos%20digitales.pdf

---

## NOTAS DE LIMITACIÓN

- Los PDFs originales de CMF, SERNAC y USS-Equifax no se pudieron parsear directamente por encoding binario; las cifras provienen de las síntesis de prensa especializada chilena que las cita textualmente.
- No se encontró públicamente desagregado el dato de **# solicitudes ARCO recibidas por CPLT** ni el comparativo con población con derecho — declarado como **NO DISPONIBLE PÚBLICAMENTE**. La métrica relevante reemplazo es % empresas con DPO (STAT-31) y vigencia Ley 21.719.
- Los datos por quintil del EFH 2024 aún no se publicaron desagregados; se usaron datos EFH 2021 que sí están disponibles por estrato.

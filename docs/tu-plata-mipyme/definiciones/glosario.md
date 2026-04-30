---
title: Glosario
description: Términos fintech, regulatorios y técnicos relevantes para el proyecto.
tags:
  - definiciones
  - glosario
---

# Glosario

<!-- AUTO-BANNER -->
!!! abstract ":material-toy-brick: Plantilla / esqueleto inicial"
    Estructura generada al iniciar la wiki, sin datos del equipo. **Reemplazar el contenido antes de citarlo.** Convención: ver [Convenciones de contenido](../../convenciones-de-contenido.md).

Mantener este archivo vivo: cada vez que aparezca un acrónimo o término que costó entender, agrégalo aquí.

## Regulatorio / institucional

| Término | Definición |
|---|---|
| **CMF** | Comisión para el Mercado Financiero. Regulador de bancos, valores, seguros y Fintechs en Chile. |
| **SII** | Servicio de Impuestos Internos. Autoridad tributaria de Chile. |
| **SERNAC** | Servicio Nacional del Consumidor. Defiende derechos del consumidor; emite alertas de fraude. |
| **SERCOTEC** | Servicio de Cooperación Técnica. Agencia del Estado que apoya a microempresas con capacitación, asesoría y subsidios. |
| **CORFO** | Corporación de Fomento de la Producción. Agencia estatal que financia emprendimiento, innovación y crecimiento empresarial. |
| **FOSIS** | Fondo de Solidaridad e Inversión Social. Subsidios a personas en situación de pobreza, incluye apoyo a microemprendimiento. |
| **Ley Fintech 21.521** | Ley chilena que regula servicios financieros tecnológicos: crowdfunding, asesoría, custodia, sistemas alternativos de transacción y **Open Finance**. |
| **Ley 19.628** | Ley sobre protección de la vida privada (datos personales) vigente en Chile. |
| **Ley 21.719** | Nueva ley de protección de datos personales (vigencia escalonada). Crea la Agencia de Protección de Datos. |
| **Open Finance** | Marco que permite al usuario portar y compartir su información financiera entre instituciones autorizadas, con su consentimiento. |
| **NCG** | Norma de Carácter General — instrumento que usa la CMF para regular en detalle. |
| **DICOM / Equifax** | Buró de información comercial; mantiene registros de morosidad y comportamiento crediticio. |
| **PDI / Brigada del Cibercrimen** | Policía de Investigaciones de Chile, unidad especializada en delitos digitales. |
| **CSIRT de Gobierno** | Equipo de respuesta a incidentes de ciberseguridad del Estado chileno. |

## Tu Plata Mipyme

Términos propios del producto y del dominio mipyme. Definición canónica del producto: [tu-plata-mipyme.md](../../competencia/ideas-evaluadas/tu-plata-mipyme.md).

### Régimen y formalización tributaria

| Término | Definición |
|---|---|
| **Microempresa** | Empresa con ventas anuales hasta UF 2.400 (definición SII / Estatuto PYME). |
| **Pequeña empresa** | Ventas anuales entre UF 2.400 y UF 25.000. |
| **Mediana empresa** | Ventas anuales entre UF 25.000 y UF 100.000. |
| **Pro-Pyme General** | Régimen tributario simplificado para empresas con ventas hasta UF 75.000. Tributa sobre flujo (ingreso percibido − gasto pagado). |
| **Pro-Pyme Transparente** | Variante del Pro-Pyme donde la utilidad pasa directo al dueño (persona natural) y tributa con su Global Complementario. Habitual cuando el dueño tiene tasa marginal baja. |
| **Régimen General** | Régimen tributario por defecto, con contabilidad completa. Más oneroso para empresas pequeñas. |
| **Inicio de Actividades** | Trámite en SII donde una persona o empresa declara que comienza a desarrollar actividades comerciales. Punto de partida de la formalización. |
| **Boleta Electrónica** | Documento tributario digital obligatorio para ventas a consumidor final. Su emisión registra ingreso ante el SII. |
| **F29** | Formulario mensual de declaración de IVA y otros impuestos retenidos. |
| **F22** | Declaración anual de renta. |

### Productos de fomento y financiamiento

| Término | Definición |
|---|---|
| **FOGAPE** | Fondo de Garantía para Pequeños y Medianos Empresarios. Estado garantiza parte de un crédito a la PYME, reduciendo riesgo del banco. |
| **FSGarantía** | Fondo de Seguros y Garantías de CORFO. Cobertura de riesgo crediticio para PYMEs. |
| **Capital Semilla SERCOTEC** | Subsidio no reembolsable de SERCOTEC para iniciar o ampliar negocios. |
| **Crece SERCOTEC** | Programa SERCOTEC para fortalecer capacidades de gestión de microempresas existentes. |
| **Capital Abeja** | Subsidio SERCOTEC dirigido a mujeres emprendedoras. |
| **PAR (Programa de Apoyo a la Reactivación)** | Subsidio CORFO para empresas que necesitan capital de trabajo o inversión post-crisis. |

### Datos demográficos / mercado

| Término | Definición |
|---|---|
| **EME** | Encuesta de Microemprendimiento del INE. La 8° edición (EME8) es la fuente para el dato de **1,08 M de microemprendedores informales** en Chile. |
| **ENIF** | Encuesta Nacional de Inclusión Financiera. Mide acceso, uso y conocimiento financiero. |
| **Informalidad** | Microemprendimiento que opera sin Inicio de Actividades en SII. 54 % del universo total de microemprendedores en Chile. |
| **NSE D-E** | Niveles socioeconómicos bajo y muy bajo según clasificación AIM/ESOMAR. Foco demográfico del producto. |
| **PIAAC** | Programa Internacional de Evaluación de Competencias de Adultos (OCDE). Mide comprensión lectora y competencias matemáticas. |

### Modelo de negocio

| Término | Definición |
|---|---|
| **Freemium** | Modelo donde la versión básica es gratis indefinidamente y la monetización ocurre por funcionalidades premium. En Tu Plata Mipyme: gratis para informales, pago al formalizar y postular a subsidios. |
| **Trigger de conversión** | Momento contextual donde el sistema propone un upgrade de tier porque el valor monetario del paso es evidente para el usuario. Opuesto al upsell agresivo basado en cuotas o paywalls. |
| **Marketplace de asesores** | Mecanismo donde la plataforma deriva al usuario a un profesional certificado (contador, abogado) y cobra comisión por transacción, sin agregar margen al precio del usuario. |
| **Repositorio contable** | Versionado de los documentos contables del emprendedor (boletas, gastos, cierres mensuales) bajo su propiedad y portable a cualquier contador. |

### Arquitectura multi-agente

| Término | Definición |
|---|---|
| **Multi-agente** | Sistema donde varios agentes IA con roles especializados se coordinan vía un supervisor para resolver una tarea. En Tu Plata Mipyme: 1 supervisor + 4 subagents por etapa. |
| **Subagent** | Agente subordinado dentro del Agent SDK, con su propio system prompt, tools y memoria, invocable desde un agente supervisor. |
| **Handoff entre agentes** | Pasaje explícito de contexto entre dos agentes cuando el caso del usuario cruza una frontera (ej: de "informal" a "en formalización"). |
| **Expediente del emprendedor** | Estado persistente del usuario en la base de datos: perfil, hechos extraídos, etapa, tier. Lo leen y escriben todos los agentes. |
| **Journey del emprendimiento** | Recorrido del usuario por las 4 etapas del producto: Sueño → Informal → Formalizando → PYME. |

## Derechos del titular del dato

| Término | Definición |
|---|---|
| **Derechos ARCO** | **A**cceso, **R**ectificación, **C**ancelación y **O**posición. Derechos del titular sobre sus datos personales. |
| **Consentimiento** | Manifestación libre, específica e informada del titular para que sus datos sean tratados. |
| **Portabilidad** | Derecho a obtener y reutilizar los propios datos en distintos servicios (clave en Open Finance). |
| **Datos sensibles** | Datos que requieren protección reforzada (salud, situación económica, etc.). |

## Técnico / IA

| Término | Definición |
|---|---|
| **Claude** | Familia de modelos de IA de Anthropic (Opus, Sonnet, Haiku). |
| **Agentic thinking** | Diseño donde el modelo descompone tareas, usa herramientas, valida y se auto-corrige. |
| **Agent SDK** | Kit de Anthropic para construir agentes con loops de planificación, tool use y verificación. |
| **MCP** | **M**odel **C**ontext **P**rotocol — protocolo abierto para que un modelo se conecte con datos y herramientas externas. |
| **RAG** | **R**etrieval-**A**ugmented **G**eneration — el modelo genera respuestas apoyado en información recuperada de una base externa. |
| **Tool use** | Capacidad del modelo de invocar funciones externas (APIs, búsquedas, cálculos) durante la generación. |
| **Prompt caching** | Funcionalidad que reduce el costo y latencia al reutilizar prefijos de prompts ya enviados. |
| **Alucinación** | Respuesta del modelo que parece correcta pero no se sustenta en la realidad o las fuentes. |
| **Citación** | Referencia explícita a la fuente que sustenta cada afirmación de una respuesta. |

## Producto / negocio

| Término | Definición |
|---|---|
| **JTBD** | Jobs-to-be-done — qué "trabajo" contrata el usuario a la solución. |
| **Persona** | Perfil ficticio sintetizado a partir de datos reales que representa un segmento. |
| **MVP** | Mínimo producto viable — la versión más simple que entrega valor. |
| **Pitch** | Presentación corta y persuasiva de la solución. |

## Convención

Si tienes que **explicar un término dos veces** al equipo, súbelo aquí.

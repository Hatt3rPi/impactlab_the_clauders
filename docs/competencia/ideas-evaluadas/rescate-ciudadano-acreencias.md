---
title: "Idea: Rescate Ciudadano / Bombero Pyme — recuperar plata olvidada en bancos"
description: "Cruza RUT con base CMF de acreencias bancarias caducables y agenda alertas para que herederos y pymes cobren antes de que el dinero pase a Bomberos."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: activa
prioridad: estrella
tags:
  - idea
  - inclusion-financiera
  - acreencias
  - cmf
  - whatsapp
---

# Idea: Rescate Ciudadano / Bombero Pyme — recuperar plata olvidada en bancos :material-star:

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md) y validada con cifras del [run #04 (transferencias no activadas)](../research/usuarios/transferencias-no-activadas-chile-2026.md). **Aún no validada por el equipo.**

> *Sube tu cédula o RUT de empresa y la IA cruza tu identidad con la base CMF de acreencias bancarias en tiempo real. Si encuentra plata olvidada, te genera un evento de calendar con la fecha exacta de caducidad y las instrucciones para ir al banco a cobrarla antes de que pase a Bomberos.*

> :material-star-circle: **Top 1 según el agente Deep Research**: combina momento *wow* en la demo (recuperar plata real en 60 s frente al jurado) con métrica de impacto trivialmente cuantificable.

## Problema

- **CLP 106.845 millones (2026)** distribuidos en **94.654 acreencias bancarias** caducables ([CMF](https://acreencias.cmfchile.cl)).
- Un fondo bancario inactivo por **2 años** entra al boletín de caducidad. Si nadie lo reclama en **3 años más**, **se transfiere irrevocablemente a la Junta Nacional de Cuerpos de Bomberos de Chile**.
- **Pérdida promedio por cuenta abandonada:** CLP 806.138 ([run #04](../research/usuarios/transferencias-no-activadas-chile-2026.md)).
- Acumulado 2024-2025: **CLP 199.352 millones**.
- Fricción raíz: **revisar acreencias requiere acción proactiva** en el sitio CMF, con CAPTCHA y sin notificación push. Nadie lo hace por costumbre.
- **Sub-segmento más afectado:** mipymes que cambiaron de banco o cesaron operaciones, y herederos de cuentas inactivas de fallecidos.

## Hipótesis

Si una persona o pyme puede subir una foto de su cédula / RUT empresa y obtener en menos de 60 segundos un **diagnóstico cruzado con la base CMF + recordatorio agendado**, recuperará plata que de otra forma habría perdido.

## Propuesta

### Qué hace

- **Recibe** una foto de cédula chilena o RUT de empresa por WhatsApp.
- **Vision (OCR)** extrae nombre/RUT.
- Cruza vía **Tool Use** contra el dataset descargado de la CMF (CSV anual de acreencias).
- Si hay match: **genera diagnóstico**: monto encontrado, banco, fecha de caducidad, instrucciones específicas para ir al banco.
- **Genera archivo `.ics`** descargable para Google Calendar / Outlook con la fecha límite + recordatorio 7 días antes.

### Qué NO hace

- No retira la plata por el usuario (la CMF requiere presencia física en el banco).
- No identifica fondos inactivos antes de los 2 años (no están en el boletín CMF aún).
- No procesa cuentas de extranjeros sin RUT chileno.

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 (Vision + Tool use).
- **Patrones agénticos:** Vision (OCR de cédula), Tool use (consulta a base de datos local), Structured Outputs (generación del archivo `.ics`).
- **Datasets:** Base de datos pública anual de [Acreencias Bancarias CMF](https://acreencias.cmfchile.cl), descargada vía Transparencia (CSV) para evitar el CAPTCHA del buscador web.
- **Limitación técnica:** el sistema CMF a veces requiere validación manual CAPTCHA. Para el hackathon se descarga el volcado anual completo y se sirve localmente.

## Demo imaginada (60 segundos)

1. **Inicio:** un voluntario del público comparte su cédula por WhatsApp con el bot.
2. **Acción:** el bot la procesa.
3. **Magia:** "Hola Carlos. Encontramos **CLP 312.450** a tu nombre en BancoEstado, depositados el 14-mar-2024. **Caducan el 14-mar-2027** y pasarán a Bomberos. Te dejé el evento en tu calendar con las instrucciones de tu sucursal."
4. **Cierre:** el evento aparece descargado, con dirección de la sucursal y horarios.

> Si no aparece plata: "Carlos, no encontramos acreencias a tu nombre. Tu prima Carla, que falleció el año pasado, podría tener — sube su cédula también si eres heredero."

## Scoring (criterios oficiales)

| Criterio | Peso | Score (0-1) | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,95 | 23,75 |
| Uso responsable de datos | 20 | 0,85 | 17,00 |
| Claude & Agentic Thinking | 25 | 0,90 | 22,50 |
| Funcionalidad | 15 | 0,80 | 12,00 |
| Calidad del pitch | 15 | 0,95 | 14,25 |
| **Total** | **100** | | **89,50** |
| Bonus agentic (+5) | 5 | 0,80 | +4,00 |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** S-M (idea más simple del backlog porque no requiere RAG legal extenso).
- **Riesgos técnicos:**
    - Mantener el dataset CMF sincronizado anualmente (publican una vez al año, en marzo).
    - OCR de cédula chilena requiere modelo robusto a fotos malas.
- **Datos disponibles ya:** sí — la CMF publica el CSV vía Transparencia.
- **Demo end-to-end factible:** sí, **idealmente en vivo durante el pitch**.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| CMF bloquea consultas masivas (scraping) | Alta | Medio | Descargar el CSV anual completo, no scraping en runtime |
| Falsos positivos por nombres comunes | Media | Alto | Cruce estricto por **RUT exacto**, no por nombre |
| Manejo de PII (cédula con foto) | Alta | Alto | No persistir imagen original, anonimizar logs |
| Dataset desactualizado por 12 meses | Alta | Bajo | Documentar fecha del dataset en cada respuesta |

## Por qué gana (según la estrategia)

- **Métrica de impacto ridículamente cuantificable:** *"Logramos que X usuarios descubrieran Y millones de pesos en vivo durante la demo."*
- Demo *wow*: dinero real recuperado en pantalla en 60 segundos. Imposible de igualar por un chatbot RAG.
- **Caso análogo verificable:** [Stamford CARE (UK)](https://stamfordcare.gov.uk) — plataforma de welfare reclaim que automatiza la búsqueda de fondos no reclamados.
- **Brecha clara:** No existe en Chile un servicio "push" que cruce RUTs y genere alertas urgentes con plazos de expiración.

## Próximos pasos para validar

- [ ] Descargar el CSV de acreencias 2026 desde Transparencia CMF y verificar formato.
- [ ] Spike Vision: leer 5 cédulas chilenas reales y extraer RUT con >95 % precisión.
- [ ] Spike Tool use: cruce de RUT contra el CSV en <2 segundos.
- [ ] Generar archivo `.ics` válido para Google Calendar y Outlook.
- [ ] Conseguir 5-10 voluntarios con cédulas para demo pre-lab.

## Notas y referencias

- **Caso análogo internacional:** Stamford CARE (Reino Unido) y plataformas de welfare reclaim como [Propel Inc (USA)](https://www.joinpropel.com).
- **Como módulo de [sabidurIA ciudadana](sabiduria-ciudadana.md):** este es uno de los **3 módulos perfectos** para el demo del 7 de mayo (junto con Legado Claro y un tercer módulo a elegir).
- **Cruce con [datos del run #04](../research/usuarios/transferencias-no-activadas-chile-2026.md):** misma cifra de CLP 94.444-106.845 millones validada por dos fuentes independientes.
- Catálogo completo de origen: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

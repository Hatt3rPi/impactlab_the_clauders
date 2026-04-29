---
title: "Idea: GES-Claim — activador de seguros de salud ocultos"
description: "Foto de epicrisis + boleta médica → la IA detecta si el diagnóstico tiene cobertura GES y genera el formulario de activación retroactiva."
autor: "Síntesis del equipo a partir del run Deep Research Max 01-ideas-fuera-del-radar"
fecha: 2026-04-29
linea: inclusion-financiera
estado: activa
prioridad: alta
tags:
  - idea
  - inclusion-financiera
  - salud
  - ges
  - vision
---

# Idea: GES-Claim — activador retroactivo de cobertura de salud

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Ficha de idea construida a partir del [run Deep Research #01](../research/_runs-deep-research/2026-04-29-01-ideas-fuera-del-radar.md). **Aún no validada por el equipo.**

> *El paciente toma una foto a su epicrisis y a una boleta de clínica de alto costo. La IA identifica si el diagnóstico tiene cobertura GES (Garantías Explícitas en Salud), genera el "Formulario de Constancia de Información al Paciente GES" y le permite exigir la activación retroactiva.*

## Problema

- El **GES (AUGE)** obliga a FONASA y a las Isapres a cubrir **90 patologías** con tiempos máximos de espera y copago limitado al **20 %** (Isapres) o **0 %** (FONASA).
- **Muchos pacientes pagan privadamente** por tratamientos que el Estado garantiza, por incapacidad de cruzar su diagnóstico médico con el decreto legal vigente.
- **Sub-segmento más afectado:** familias de pacientes recién diagnosticados con enfermedades catastróficas (cáncer, insuficiencia renal) atendidos en sistema privado o público institucional.
- Fricción: los pacientes asumen que el médico activa el GES automáticamente — falso en muchos prestadores privados.

## Hipótesis

Si el usuario puede subir una **foto de su epicrisis + una boleta de alto costo**, la IA puede identificar si el diagnóstico tiene cobertura GES y generar el formulario para exigir activación retroactiva, evitando la ruina financiera familiar.

## Propuesta

### Qué hace

- Recibe foto de epicrisis (con código diagnóstico) + boleta médica.
- **Vision** identifica terminología médica + monto pagado.
- Cruza el diagnóstico con el **Decreto GES vigente** ([Sup. Salud](https://www.supersalud.gob.cl/)).
- Devuelve:
    - "**Este diagnóstico SÍ tiene cobertura GES.** Te ahorras hasta CLP X."
    - **Formulario de Constancia de Información al Paciente GES** prellenado.
    - Pasos para exigir activación retroactiva al prestador.
    - Cita exacta del decreto GES.

### Qué NO hace

- No diagnostica ni reemplaza al médico.
- No tramita la activación (la presenta el usuario al prestador).
- Disclosure permanente: "no soy un servicio de salud, solo te ayudo a leer tus derechos".

## Stack y datos

- **Modelo Claude:** Sonnet 4.6 (Vision + Citations).
- **Patrones agénticos:**
    - **Vision:** lectura de epicrisis y facturas médicas (jerga densa).
    - **Citations:** referencia al decreto exacto de Sup. Salud (Decretos GES vigentes).
    - **Structured outputs:** schema `{diagnostico, cobertura_ges, monto_ahorrable, formulario_pdf, decreto_citado}`.
- **Datasets:** Decretos GES vigentes (MinSal), formularios oficiales de notificación (Sup. Salud), [compendio Sup. Salud](https://www.supersalud.gob.cl/normativa/665/w3-propertyvalue-1962.html).

## Demo imaginada (60 segundos)

1. "**Marta** lleva 3 meses con cáncer de mama. Pagó CLP 4,8 M en clínica privada por una cirugía."
2. Sube su epicrisis y la boleta.
3. La IA: "**Tu diagnóstico está cubierto por GES** (Decreto 369/2024, art. 12). Tu copago debió ser **CLP 280.000**, no CLP 4,8 M. **Tienes derecho a exigir reembolso retroactivo.**"
4. "Aquí está tu **Formulario de Constancia GES** prellenado. Llévalo a tu Isapre y pide la activación retroactiva."

## Scoring (criterios oficiales)

| Criterio | Peso | Score (0-1) | Aporte |
|---|---|---|---|
| Impacto cívico | 25 | 0,95 | 23,75 |
| Uso responsable de datos | 20 | 0,75 | 15,00 |
| Claude & Agentic Thinking | 25 | 0,90 | 22,50 |
| Funcionalidad | 15 | 0,75 | 11,25 |
| Calidad del pitch | 15 | 0,90 | 13,50 |
| **Total** | **100** | | **86,00** |
| Bonus agentic (+5) | 5 | 0,75 | +3,75 |

> Scoring inicial heurístico — el equipo debe validar y ajustar tras spike técnico.

## Viabilidad en 48 h

- **Esfuerzo:** M (Vision sobre documentos médicos requiere cuidado).
- **Riesgos técnicos:**
    - Variabilidad de epicrisis según prestador.
    - Riesgo de responsabilidad civil/médica si la IA "alucina" cobertura GES.
- **Datos disponibles ya:** sí (decretos GES son públicos).
- **Demo end-to-end factible:** sí.

## Riesgos / mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Falsa activación de GES por error de OCR | Media | Alto | Disclosure permanente; siempre mostrar la cita textual del decreto |
| Variabilidad de epicrisis | Alta | Medio | Acotar a 10-15 patologías GES más comunes en demo |
| Datos de salud son sensibles (PII médica) | Alta | Alto | No persistir imágenes; anonimizar logs; advertencia previa al usuario |

## Por qué gana

- **Sale del nicho CMF/Bancos** y entra a salud financiera — dolor universal y emocionalmente resonante.
- **Caso análogo verificable:** [SafeMortgage / MakeMyMoney (UK)](https://www.makemymoney.uk) aplicado a la intersección de derechos de salud y finanzas personales.
- **FONASA cubre 85 %** de la población — es masivo.

## Próximos pasos para validar

- [ ] Conseguir 5 epicrisis reales (anonimizadas) para spike Vision.
- [ ] Construir base de datos de las 10 patologías GES más frecuentes (cáncer, hipertensión, diabetes, etc.).
- [ ] Validar plantilla de Formulario de Constancia GES con un médico o trabajadora social.
- [ ] Entrevistar a 3 personas que pagaron de bolsillo por algo cubierto por GES.

## Notas y referencias

- **Caso análogo internacional:** [SafeMortgage / MakeMyMoney (UK)](https://www.makemymoney.uk).
- **Posible módulo de [sabidurIA ciudadana](sabiduria-ciudadana.md)** (evento de vida: enfermedad).
- **Cruce con run #03 datasets:** [FONASA Datos Abiertos PAD/GRD](../research/tecnologia/datasets-subutilizados-y-cruces.md) está sub-utilizado y permite estimar el costo referencial.
- Catálogo completo de origen: [15 ideas fuera del radar](../research/ideas-emergentes/ideas-fuera-del-radar-2026-04-29.md).

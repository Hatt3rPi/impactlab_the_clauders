---
title: "Marco regulatorio chileno 2026 (Ley Fintech, Datos, Antifraude)"
description: "Síntesis del marco normativo financiero y de privacidad relevante para inclusión financiera, ciberseguridad y protección de datos."
autor: "Síntesis sobre research previo del equipo (Calibria + estrategia Literacy Regulatoria)"
fecha: 2026-04-29
categoria: regulatorio
linea: transversal
tags:
  - research
  - regulatorio
  - fintech
  - datos
  - antifraude
---

# Marco regulatorio chileno 2026

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Sintetizado a partir del [PDF de estrategia](../../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf) y el [Deep Research de Calibria](../../assets/research/2026-04-29-deep-research-calibria.html). **Verificar cifras antes de citarlas en el pitch.**

Síntesis de las normas que el agente IA debe **conocer y citar correctamente**. Sin esto, la solución cae en alucinación regulatoria → descalifica.

## Fuentes de esta nota

- :material-file-pdf-box: [Estrategia Literacy Regulatoria (PDF)](../../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf), 12 páginas, autor del equipo, 29-abr-2026.
- :material-file-document: [Deep Research Calibria (HTML)](../../assets/research/2026-04-29-deep-research-calibria.html), 62 fuentes, 29-abr-2026.

## Tesis central

> Chile tiene la legislación financiera y de privacidad **más alineada con OCDE/GDPR de Latinoamérica**, pero carece de **traducción operativa**. Las leyes dibujan un consumidor protegido; en la práctica no sabe ejercer sus derechos.

Las soluciones IA-nativas más valiosas son las que **convierten artículos de ley en flujos accionables conversacionales**.

---

## 1. Ley 21.521 — Ley Fintech (Inclusión)

Promulgada el **22-dic-2022**, vigente desde el **3-feb-2023**. Reformó el mercado financiero con **7 servicios regulados**:

1. Asesoría crediticia
2. Asesoría de inversión
3. Custodia de instrumentos financieros
4. Plataformas de financiamiento colectivo
5. Sistemas alternativos de transacción (SAT)
6. Enrutamiento de órdenes
7. Intermediación de instrumentos financieros

**Gobernanza:** la **CMF** opera el **Registro de Prestadores de Servicios Financieros (RPSF)** bajo modelo proporcional por bloques.

### Cronología de implementación

| Fecha | Hito |
|---|---|
| 04 ene 2023 | Publicación en Diario Oficial |
| 12 ene 2024 | **NCG 502** — Registro, autorización, gobierno corporativo y capital |
| 03 jul 2024 | **NCG 514** — Sistema de Finanzas Abiertas (4 tipos de participantes IPI/IPC/PSBI/PSIP, APIs ISO 22022, 6 categorías de datos, 5 APIs de pago) |
| 03 feb 2025 | Cierre de transitoriedad: 335 solicitudes; **solo 179 autorizadas** (178 asesores heredados + 1 intermediario nuevo: **Koywe**) |
| 12 nov 2025 | CMF pone en consulta postergación de Open Finance **+12 meses** |
| 09 feb 2026 | **NCG 559** dictada — regula entidades fiscalizadas con servicios fintech sin inscripción. Plazo declarativo: 30-abr-2026 |
| 06-07 may 2026 | Chile Fintech Forum 2026 — *por primera vez en 6 años, la CMF NO asistirá* (señal de fricción regulador-gremio) |
| **04 jul 2027** | **Open Finance operativo** (postergado desde jul-2026) |

### Brechas reconocidas

- Sesgo del registro hacia **asesoría de inversión** (no hacia inclusión).
- Demoras en el **Anexo Técnico 3** del Sistema de Finanzas Abiertas.
- Costos de cumplimiento prohibitivos para fintech pequeñas: **UF 5.000 ≈ CLP $190 M**.
- Zona gris que la NCG 559 recién cerró tres años después de la promulgación.
- **Resultado:** la promesa de "más competencia" sigue concentrada en pocos jugadores.

---

## 2. Ley 21.719 — Protección de Datos Personales

Publicada el **13-dic-2024** con vacancia de 24 meses → **vigencia plena el 1-dic-2026**. Reemplaza la Ley 19.628 (de 1999, que carecía de autoridad de control).

### Lo que introduce

- **8 principios** de tratamiento.
- **Derechos ARCOP**: Acceso, Rectificación, Cancelación, Oposición, **Portabilidad**, Bloqueo + oposición a decisiones automatizadas.
- **Aplicación extraterritorial**.
- **Régimen sancionatorio escalonado**.

### Cifras clave

| Métrica | Valor |
|---|---|
| Multa máxima por infracción gravísima | **20.000 UTM (~CLP $1.392 M / USD $1,2 M)** |
| Reincidencia (no-PYMEs) | 2-4 % de ingresos anuales en Chile |
| Empresas que creen tener tiempo de adaptarse | 59 % (PwC-FGE 2025) |
| **Empresas chilenas con DPO designado** | **41 %** (a 17 meses de la vigencia) |

### Convergencia con GDPR

≈85-90 % alineada, **sin** decisión de adecuación de la Comisión Europea. Divergencias principales:

- **Sin plazo numérico** para notificación de brechas (GDPR exige 72 hrs; Chile usa 48-72 hrs como práctica recomendada).
- Máximos sancionatorios **menores** (USD 1,2 M vs €20 M).
- Figura del **Modelo de Prevención de Infracciones (MPI)** inexistente en GDPR.
- **Período de gracia de 12 meses solo amonestaciones para PYMEs**.

### Riesgo institucional

La Comisión Asesora Ministerial denunció **insuficiencia presupuestaria estructural** de la APDP. Las remuneraciones proyectadas (Presidente $7,1 M; consejeros $6 M mensuales) están bajo el promedio de fiscalizadores (>$12 M) → riesgo de captura regulatoria. El plazo legal para reglamentos (jun-2025) se incumplió: a abril 2026 solo se aprobaron las **cláusulas modelo para transferencias internacionales** (dic-2025).

---

## 3. Otras normas clave

### Ley 21.673 — Antifraude bancario

- Tras su promulgación, los **reclamos por fraude subieron 88 % mensual**.
- La **respuesta favorable cayó del 51 % al 7 %**.
- **~30.000 juicios** entre bancos y clientes en curso (cifra Hora12, sin confirmación oficial del Poder Judicial).

### Ley 21.236 — Portabilidad financiera

- Vigente desde **sept-2020**.
- Existe pero la UX está dispersa en cada banco.

### Ley 21.563 — Régimen concursal (Renegociación y Liquidación)

- Marco legal para que personas naturales sobreendeudadas accedan a procedimiento concursal con la Superintendencia de Insolvencia.

### Ley 21.680 — Registro de Deuda Consolidada (2024)

- Antes de esta ley, **Chile era el único país sudamericano sin un registro de deuda consolidada**.

### Ley 21.320 — Límites a cobranzas

- Regula prácticas de cobranza extrajudicial (incluye llamadas, mensajes, frecuencia).

### Ley 20.555 / SERNAC Financiero

- Transparencia: hojas resumen, **CAE** (Carga Anual Equivalente).

### Ley 21.325 — Ley de Migración (2021)

- Marco para regularización; KYC con cédula extranjera.

### Estrategia Nacional de Inclusión Financiera (ENIF, ene-2025)

Grupos prioritarios:

- Mujeres
- Jóvenes
- Personas mayores
- Personas con discapacidad
- Personas de menores ingresos
- Microempresas

---

## 4. Implicancias directas para el proyecto

| Implicancia | Acción concreta |
|---|---|
| Cualquier respuesta del agente debe **citar artículo + ley**. | Diseñar tools/MCPs que retornen la fuente, no solo el texto. Usar la **Citations API** de Claude. |
| **Ley 21.521** + **NCG 514** + **Ley 21.680** + **SERNAC Financiero** son las normas que mentores CMF/SII van a evaluar. | Equipo debe dominarlas a nivel operativo el día 2 del lab. |
| **Línea roja AUP de Anthropic:** el MVP NO puede tomar decisiones finales de aprobación crediticia, recomendar inversión específica, ni operar como "asesor financiero" sin disclosure. | Disclosure permanente: *"Soy una IA, no un abogado/asesor"*. Nunca recomendar AFP, fondo, banco específico. |
| Caída de respuesta favorable a reclamos (51 % → 7 %) post Ley 21.673 | Oportunidad clara: agente que **prepara el reclamo bien fundamentado** desde el día 1. |
| **Open Finance postergado a jul-2027**. | No depender de APIs Open Finance reales para el demo del 7 may. Mockear si es necesario. |
| **APDP sin Consejo Directivo a abril 2026**, solo se aprobaron cláusulas modelo de transferencias internacionales. | El vacío institucional en datos personales es real → mayor valor de un asistente ARCOP. |

---

## 5. Preguntas abiertas

- ¿Qué circulares CMF específicas son las más usadas hoy contra repactaciones abusivas? (research deep dive pendiente).
- ¿Qué **NCGs** sancionan el ocultamiento de comisiones en contratos retail? (Letra Chica idea).
- ¿Cuándo entran en vigencia los **reglamentos de la Ley 21.719**? (estado al 29-abr-2026: incompleto).
- ¿La **mesa público-privada** del lab incluirá representantes oficiales de CMF/SII/SERNAC presentes los días 6-7? (confirmar con organizadores).

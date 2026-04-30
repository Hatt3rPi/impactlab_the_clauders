---
title: "Soluciones existentes en Chile y brechas críticas"
description: "Mapeo de fintechs, bots y portales públicos vigentes; identificación de gaps no cubiertos."
autor: "Síntesis sobre research previo del equipo (Calibria + estrategia Literacy Regulatoria)"
fecha: 2026-04-29
categoria: mercado
linea: transversal
tags:
  - research
  - mercado
  - competencia
  - brechas
---

# Soluciones existentes en Chile y brechas críticas

<!-- AUTO-BANNER -->
!!! info ":material-book-open-variant: Síntesis de fuentes externas"
    Sintetizado a partir del [PDF de estrategia](../../../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf) y el [Deep Research de Calibria](../../../assets/research/2026-04-29-deep-research-calibria.html). **Verificar cifras antes de citarlas en el pitch.**

Mapeo de **qué ya existe** para no duplicar y **dónde están los huecos** que justifican nuestra solución.

## Fuentes

- :material-file-pdf-box: [Estrategia Literacy Regulatoria (PDF)](../../../assets/research/2026-04-29-estrategia-literacy-regulatoria.pdf), p. 4.
- :material-file-document: [Deep Research Calibria (HTML)](../../../assets/research/2026-04-29-deep-research-calibria.html), sección 05.

---

## Inclusión Financiera (348 fintechs en el ecosistema)

| Solución | Cobertura | Limitación |
|---|---|---|
| **CMF Educa** | Portal estático con simuladores | Sin IA ni personalización |
| **App BancoEstado / CuentaRUT** | +13 M cuentas, base de la pirámide | Asistente virtual básico |
| **Comparaonline** | Corredora regulada, USD 60 M ventas 2023 | Sesgo comercial |
| **Comparador SERNAC** | Créditos de consumo, gratis | UX anticuada |
| **Tenpo · Mach · Mercado Pago** | Dominan billeteras digitales | No hacen literacy |
| **Fintual** | +USD 1.000 M AUM, robo-advisor | Perfila clase media-alta |
| **Destácame** | +2 M usuarios (16 % de adultos) | Lo más cercano a "asistente financiero" — ya cubre scoring alternativo |
| **Daniela (BCH) · Santi (Santander)** | Asistentes IA | Solo para clientes existentes |
| **Fondo Esperanza · Banigualdad** | Microfinanzas presenciales | Para mujeres y vulnerables, no escala digital |
| **Galgo** | Crédito a migrantes, licencia CMF, respaldo BID Lab | Cubre el segmento migrante |
| **Cumplo · Xepelin · RedCapital** | Factoring/lending PyME | Comercial, no educativo |
| **Floid · Fintoc** | Agregadores Open Finance | Infraestructura, no usuario final |

> **Conclusión:** "otra wallet" o "otro scoring" pierde por defecto. Los jurados conocen el mapa.

---

## Ciberseguridad Ciudadana (mayoría reactiva)

| Solución | Tipo | Limitación |
|---|---|---|
| **CSIRT Nacional / ANCI** | Alertas con mascota Ciberpudú | Sin app móvil ni reporte ciudadano |
| **Comisaría Virtual** | App de Carabineros desde jul-2025 | ClaveÚnica, sin foco ciberdelitos |
| **Denuncia Seguro 600** | Línea legacy | — |
| **CMF Reclamos · SERNAC** | Centralizan reclamos | Responden en ~18 días hábiles |
| **Antifraude bancario** (BancoEstado, BCH, Santander, BCI, Itaú) | ML reactivo | Sin compartir info cross-banco |
| **Movistar McAfee · Entel · NeoSecure** | Antivirus comercial | B2B principalmente |
| **Fundación País Digital · Mercado Hacker** | Incidencia y formación | No producto operativo |

### :material-alert: Brecha crítica

> **NO existe en Chile a abril 2026** una app gratuita ciudadana de detección de phishing/SMS/llamadas con IA generativa. Tampoco un bot WhatsApp/Telegram que verifique URLs en tiempo real.

---

## Protección de Datos (B2B only)

| Solución | Cobertura | Limitación |
|---|---|---|
| **Formulario ARCO CPLT** | Solo aplica al CPLT como responsable | No centraliza derechos contra empresas |
| **Portabilidad Financiera (Ley 21.236)** | Existe desde sept-2020 | UX dispersa en cada banco |
| **Conoce tu Deuda CMF** | Informes gratis | Procesos de eliminación post-pago manuales y demoran |
| **DefensaDeudores.cl y similares** | Mercado privado | Con muchas estafas |
| **Derechos Digitales · Datos Protegidos** | ONGs de incidencia | No proveedores operativos |
| **OneTrust · Trustjourney · Idónea · GlobalSuite** | SaaS B2B premium | Cumplimiento empresarial, no ciudadano |

### :material-alert: Brecha crítica

> **NO hay un asistente IA generativa** que ayude al ciudadano a entender qué información tiene una empresa sobre él, redactar y trackear solicitudes ARCO, ni descifrar políticas de privacidad. **El ciudadano está completamente huérfano.**

---

## Cuadrante de oportunidades IA-nativas (deep research)

Eje X: complejidad técnica → · Eje Y: ↑ impacto potencial.

### Quick Wins (alto impacto, baja complejidad — ideal para hackathon 24-72 h)

1. **Pillo** — Verificador antiphishing WhatsApp + voz. *Vertical: Ciberseg.*
2. **Tu Plata** — Traductor CAE/CTC con simulador. *Vertical: Inclusión.* :material-star:
3. **Mis Datos** — Copiloto ARCOP. *Vertical: Datos.*

### Big Bets (alto impacto, alta complejidad — visión 6-18 meses)

4. **Agente antifraude end-to-end Ley 21.673**. *Vertical: Transversal.*
5. **Copiloto financiero PYMES con SII + Open Finance**. *Vertical: Inclusión.*
6. **Plataforma cross-banco de cuentas-mula** (registro federado). *Vertical: Ciberseg.*

### Fill-ins / Time-sinks (no priorizar)

7. **Bot "No Molestar" SERNAC en lote** — bajo impacto estratégico.
8. **Scoring crediticio alternativo nicho** — Destácame ya cubre el espacio.

---

## Implicancias para nuestra solución

1. **No competir** con Tenpo, Destácame, Fintual, Comparaonline. Si nuestra idea suena a uno de ellos, pivotear.
2. **Brecha más clara** = literacy regulatoria conversacional (Línea 1 del lab) — el ecosistema chileno la dejó vacía.
3. **WhatsApp + voz** es vector subutilizado en este vertical (lo aprovechan asistentes bancarios, no productos cívicos).
4. **Posible diferenciador**: combinar **Citations API + Vision (PDF)** como pieza central. Ningún producto chileno hace eso aún para ciudadanos.

## Preguntas abiertas

- ¿Cuál es el rate-card de uso real de Comparaonline / Destácame por NSE? (necesario para proyección de mercado).
- ¿Cómo piensan evolucionar Fintual / Tenpo en literacy? Posible competencia post-lab.
- ¿Qué partnerships con ONGs (Hogar de Cristo financiero, Fondo Esperanza, Coopeuch con 1,2 M socios) son viables como canal de distribución?

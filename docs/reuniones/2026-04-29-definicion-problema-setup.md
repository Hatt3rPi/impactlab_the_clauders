---
title: "Definición de problema y setup del hackathon"
fecha: 2026-04-29
hora: "11:15"
duracion: "45 min"
tipo: "kickoff"
participantes:
  - Felipe Abarca
  - Jose Foncea
  - Cristian Astorga
  - Anahi Gonzalez
ausentes: []
tags:
  - reunion
  - kickoff
  - decision-linea
---

# Reunión: Definición de problema y setup del hackathon

<!-- AUTO-BANNER -->
!!! success ":material-check-bold: Producido por el equipo"
    Documento generado por el equipo The Clauders. Es fuente primaria para este tema.

## TL;DR

- Primera reunión del equipo. Cada miembro se presentó (background, disponibilidad, expectativas).
- **Línea temática elegida: Inclusión financiera.** Razón: ataca el problema raíz; ciberseguridad y protección de datos actúan *después* de que el usuario ya está dentro del sistema.
- **Plataforma: página web mobile-first (no app).** Argumento de Anahi: el 95-97 % de los chilenos accede a internet por mobile y busca información financiera/legal vía Google → necesitamos ser encontrables en Google y rastreables por IA (AI Overviews, ChatGPT, Perplexity).
- **Filosofía del equipo:** transparencia para decir desacuerdos sin miedo, no saltar a la solución antes de tener el problema claro, evitar sobre-ingeniería.
- **Hoja de ruta acordada:** cada miembro trae 10 problemas evaluados con métricas → reducir a 3 → reducir a 1 → MVP previo al lab.
- **Próxima reunión:** hoy 29/04 a las 21:00 (express, setup + lo recopilado en el día).

## Objetivo

Conocernos como equipo, alinear expectativas y definir el proceso de selección de problema antes del lab del 6-7 de mayo.

## Decisiones tomadas

| # | Decisión | Razón | Registro |
|---|---|---|---|
| 1 | Línea temática: **Inclusión financiera** | Ataca el problema raíz; las otras dos líneas actúan sobre usuarios ya dentro del sistema. Equipo sin expertise en ciberseguridad técnica. | [ADR 0002](../especificaciones/adrs/0002-linea-tematica-inclusion-financiera.md) |
| 2 | Plataforma: **web mobile-first**, no app nativa | 95-97 % de chilenos accede por mobile; búsqueda financiera/legal pasa por Google → priorizar SEO + accesibilidad por crawlers IA. | [ADR 0003](../especificaciones/adrs/0003-plataforma-web-mobile-first.md) |
| 3 | Repositorio del equipo como **fuente de la verdad** (wiki + research + ideas) | Ambiente productivo "todo por excelencia"; nos obliga a subir el estándar. | Implícita; este repo. |
| 4 | **Validación con usuarios** en paralelo a la fase de ideas, vía redes sociales personales | Cruzar data oficial (CMF, SII, SERNAC) con feedback real antes del lab. | — |
| 5 | **Llegar al lab con MVP testeado**, no construir desde cero allá | Permite usar las 48 h para refinar y estresar la solución con apoyo de mentores. | — |

## Roles asumidos

| Persona | Rol principal | Responsabilidades |
|---|---|---|
| Felipe Abarca | AI Builder + Tech lead + Owner del repo | Stack técnico, repositorio, MCPs, parte técnica fuerte |
| Jose Foncea | Project Manager + Comercial/Producto | Hoja de ruta, etapas, hitos, research inicial cruzando fuentes |
| Cristian Astorga | AI Builder de apoyo | Externalizar tareas técnicas, soporte a Felipe |
| Anahi Gonzalez | UX/UI + Vibecoder + análisis de datos | Diseño, estructura informativa, validación con datos de comportamiento |

> Detalle ampliado en [Equipo · Miembros](../equipo/miembros.md) y [Equipo · Roles](../equipo/roles.md).

## Acciones

| # | Responsable | Acción | Fecha límite | Estado |
|---|---|---|---|---|
| 1 | @Felipe | Montar el repositorio/wiki como fuente de la verdad | 2026-04-29 (hoy) | :white_check_mark: hecho |
| 2 | @Jose | Compartir el research inicial (cruce CMF + Impact Lab + otras fuentes) en el repo | 2026-04-29 | abierta |
| 3 | @Jose | Armar hoja de ruta con etapas e hitos | 2026-04-29 | abierta |
| 4 | @Todos | Levantamiento individual de **10 problemas** con métricas (volumen, severidad, frecuencia) en línea de inclusión financiera | antes de hoy 21:00 | abierta |
| 5 | @Todos | Centralizar links y fuentes que se vayan encontrando en el repo | continuo | abierta |
| 6 | @Todos | Diseñar proceso de validación con usuarios vía redes sociales | esta semana | abierta |
| 7 | @Equipo | Reducir el pool a 3 problemas y luego a 1 en próximas reuniones | antes del 5 de mayo | abierta |
| 8 | @Equipo | Tener MVP testeado antes del kickoff del lab | 2026-05-06 (mañana del lab) | abierta |

## Discusión

### 1. Presentaciones y contexto del equipo

- **Felipe (38)** — civil industrial, 6 años en Banco de Chile, 7 en Transbank, ex-jefe de evaluación de negocio en planificación estratégica. Programa de hobby desde 2019, full vibecoder con Claude Code desde Sonnet 3.5. Tiene un producto en marcha (`lacuenteria.cl`) generando cuentos físicos personalizados con flujo agéntico. Disponibilidad limitada los días 6-7 (hijos pequeños), pero entrada/salida es flexible y trabaja también de noche.
- **Jose** — sin experiencia previa en hackathons, ve el lab como "catapulta". Hizo investigación previa cruzando recursos del Impact Lab con fuentes de la CMF para mapear problemas existentes en la industria financiera chilena.
- **Cristian** — participó en hackathon de AWS. Insistencia en **leer las reglas** y en el peso del pitch ("vi gente con buenas ideas que guatearon en la presentación"). Considera Supabase para datos y Obsidian para RAG.
- **Anahi** — periodista, especializada en análisis de datos, ex-RTBN. Recién desempleada (lunes 27/04) → disponibilidad alta. Foco en UX/UI, marketing y estructura informativa. Ya colabora con Cristian en otra app.

### 2. Research inicial presentado por Jose

Cifras y temas que enmarcan la oportunidad:

- Chile **bancarizó 91 %** pero perdió la batalla por la **calidad**.
- **~700.000 reclamos** en SERNAC.
- 4 grandes áreas detectadas: **reclamos, ciberataques, morosidad, alfabetización financiera**.
- **Tesis:** "Chile tiene la legislación financiera y de privacidad más alineada (a estándares internacionales), pero carece de traducción operativa. Las leyes dibujan un consumidor protegido, pero en la práctica no sabe ejercer."
- **Ley Fintech 21.521:** brecha entre registro y asesoría de inversión, concentración en pocos jugadores.
- **Ley de Protección de Datos:** entra en vigencia nov/dic 2026, con 17 meses para que las empresas se adapten. Habilita **portabilidad de información personal** (ej: pasar historial de clínica A a clínica B).

> Jose comparte este documento al equipo después de la reunión. Cuando llegue, va a [Research · Regulatorio](../research/regulatorio/index.md).

### 3. Selección de línea temática

Posiciones expresadas:

- **Cristian** propuso inclusión financiera, reconociendo que "muchos van a hacer un RAG de inclusión financiera, es lo más sencillo de implementar y por eso también es viable".
- **Felipe** comentó que está vendiendo implementación de la Ley de Protección de Datos como freelance, pero que no se siente súper cómodo en esa línea, y le gusta "harto" inclusión financiera porque "hay un montón de carne".
- **Cristian y todos** descartaron ciberseguridad: "es muy técnico, muy sensible, hay un montón de cosas que se pueden hacer pero estamos en desventaja sin equipo full técnico de seguridad".
- **Argumento decisivo de Jose:** ciberseguridad y protección de datos actúan *una vez que el usuario ya está dentro del sistema*. Inclusión financiera ataca el problema en la raíz, antes de que se generen los problemas downstream → mayor impacto cívico potencial.

### 4. Plataforma y formato del producto

Propuesta de Anahi (con datos):

- **97 %** de chilenos usa el celular para acceder a internet vs **69 %** desde computador.
- Lo que más se hace es **buscar información en Google** — incluyendo temas financieros y legales.
- Conclusión: hacer una **página web mobile-first**, encontrable en Google y rastreable por IA, no una app.
- Sugerencia de **mascota / branding** para generar empatía y confianza.

Felipe propuso usar **Astro** como framework (justifica que ya lo usa para "Presencia Digital", su otro producto, porque permite buen renderizado para SEO + AI crawlers). No queda como decisión cerrada — pendiente capturar como ADR cuando se confirme stack.

### 5. Filosofía y proceso de trabajo

Jose levantó dos puntos que el equipo aceptó:

1. **Transparencia con respeto:** decir desacuerdos sin miedo. "Es muy normal que en los equipos de trabajo uno se quede callado por miedo a generar roces".
2. **No saltar a la solución antes de tener el problema claro.** "La mitad de los equipos del lab se va a ir directo a un RAG, Carpathi, Obsidian. La pregunta es cuántos equipos se van a plantear realmente un problema, aunque sea minúsculo, pero resolverlo con un stack eficiente".
3. **Anti-sobre-ingeniería**: como no son un equipo full técnico, no caer en lo que les pasa a los "computines": sobreingenierizarlo todo.

### 6. Hoja de ruta consensuada

```
[hoy 29/04 mañana]   Reunión kickoff (esta) — definimos línea + plataforma + roles
[hoy 29/04 día]      Cada uno hace levantamiento individual (10 problemas con métricas)
[hoy 29/04 21:00]    Reunión express — compartir levantamientos, alinear setup
[próximos días]      Reducir pool: 10 c/u → 3 globales → 1 elegido
                     Validación con usuarios vía redes sociales personales
[antes 5/05]         MVP testeado y refinado
[6-7/05]             Lab: refinar + estresar + pulir pitch (no construir desde cero)
```

### 7. Repositorio como fuente de la verdad

Felipe se compromete a montar el repositorio/wiki esa misma noche con estructura para:

- Centralizar links y fuentes que cada uno encuentre.
- Consolidar ideas de cada uno.
- Eventualmente conectar a una base de datos vía MCP para automatizar consumo de fuentes.

> Esa estructura es esta misma wiki. La acción está cerrada al momento de subir esta acta.

## Preguntas abiertas

- ¿Cuál es el sub-segmento dentro de inclusión financiera al que vamos a apuntar? (PyMEs, emprendedores, adultos mayores, jóvenes, mujeres, migrantes...).
- ¿Stack frontend definitivo (Astro vs alternativas)?
- ¿Vamos a usar Supabase + Obsidian para RAG, o algo más simple?
- ¿Cuándo y cómo lanzamos la validación con usuarios?
- ¿Cómo nos diferenciamos del resto de equipos que harán "RAG sobre regulación"?

## Próximos pasos

1. Cada miembro hace su levantamiento individual de 10 problemas hoy en el día.
2. Felipe deja repo + wiki listos para esta noche.
3. Reunión express hoy 29/04 a las 21:00.
4. Próxima reunión más profunda ya con problemas y métricas en mesa.

## Material de apoyo

- Research previo de Jose (cruce CMF + Impact Lab) — pendiente de subir al repo.
- Estadística de Anahi sobre uso mobile vs desktop en Chile — pendiente link al estudio fuente.
- [Sitio oficial del lab](https://fintech.benditaia.cl/es).

## Transcripción

<details markdown>
<summary>Click para expandir transcripción cruda</summary>

```text
Definición Problema y Setup Hackathon
mié, 29 abr 2026

0:00 - Felipe Abarca
las transcripciones más que nada. Después podremos tener un repositorio compartido para las transcripciones.

0:07 - Felipe Abarca
Bueno, bueno, bueno.

0:08 - Jose Foncea
Voy a grabar igual por si acaso, como fallback. Ya, entonces, Aya, ¿puedes comentar el tema de la definición del problema? De hecho antes de la reunión no alcanzé a leerlo, pero ahí les voy a compartir un una investigación que hice tomando los recursos de la página del Impact Lab, ahí la crucé con otras fuentes del ACMF, todo el tema, para ver cuál es el problema hoy día en la industria financiera en Chile, qué soluciones se han hecho, y un poco evaluar, ahí se los paso, algunas variables de impacto como tiempo de implementación, impacto potencial en cantidad de personas, lucas involucradas en el problema, etcétera, para ver cómo eso lo podemos incluir dentro de un proceso de levantamiento inicial, para que ahí digamos ya, cada uno de ustedes, no sé, han trabajado en una, dos, tres ideas, veamos cuál de esas ideas más a la vertical y después ya poder ir como encasillándonos en una línea de desarrollo por así decirlo. Esto era como en definitiva la presentación. Oye, Jose, aprovechando que llegas ahí, ¿Cuántos años tenís?

1:42 - Felipe Abarca
¿Estás casado?

1:43 - Felipe Abarca
¿Tenís familia?

1:44 - Felipe Abarca
Tengo que pasar con que yo tengo harto que contar ahí, así que Yo tengo 31 años, casado, sin hijos, con disponibilidad inmediata.

1:58 - Jose Foncea
La verdad es que yo no tenía expectativas del Impact Lab, como le comentaba a Cristian, no tengo experiencia tampoco en hackathons, pero sí creo que es una gran oportunidad para nosotros cuatro, de la expectativa y planes que tenga de utilizar esta este momento como una catapulta.

2:26 - Felipe Abarca
Sí, es una buena palanca.

2:28 - Jose Foncea
Sí, eso, eso. ¿Y ustedes?

2:30 - Felipe Abarca
Eh, eh, treinta y ocho años, soy civil industrial, eh, eh, estoy casado, eh, tengo gemelos de un año y una niñita de tres. Entonces, mi mi tiempo, tengo dos jornadas de trabajo, de de ocho y media a cinco, y de nueve a las nueve a dos de la mañana eh y ahí me me dejo esas tres horas como horario horario familiar comida eh quería jugar eh entonces eso igual me va a limitar por ejemplo el seis y siete eh tengo que ir a buscar los jardines son tres guaguas entonces no mi señora no puede ir solo pero como la web es eh ir y venir y todo el rato y se puede eh asumiría que no habría problema además entiendo que que son cuarenta y ocho horas fuera, porque sé que ustedes igual van a poder estar trabajando, y en la noche igual me quedo hasta las tantas trabajando. Claro, trabajé como seis años en el Banco Chile, siete años en Transam, era jefe del área de evaluación de negocio, experto en evaluación de casos de negocio, de rentabilidad, de pricing, de benchmarking de la industria, siempre pensando, bueno, dentro del área planificación estratégica, planificación estratégica, siempre estamos mirando el futuro, entonces veíamos cómo se venían las regulaciones, veíamos cómo se venían eh mmm eh la ley de protección de datos, cómo se venía la ley Marcelino, cómo se venía eh como el el open finance eh entonces eh eh siempre pensando como como con mirando hacia adelante eh evaluado desde integraciones con visa, compra de eh pero eso es mi mi vida laboral. Eh mi vida eh de hoy no tiene nada que ver con eso. De hecho eso ya lo lo he dejado atrás porque me aburre. Eh vengo como el dos mil diecinueve programando de hobby. ¿Cachaí? Entonces como que he hecho distintas páginas, ya tengo varios clientes, eh ahora tengo un producto que lancé en enero y ahora estoy en plena campaña que es la cuentería punto CLA y lo lo invito a a meterse. Eh creé con pasado, estoy básicamente generando cuentos físicos personalizados. Lo mando a una imprenta y lo entrego. Entonces ahora para lidiar nada más, estoy en una campaña súper intensa. Con esto aprendí un montón, automaticé ya mi generación de contenido para redes sociales. Tengo un...

5:02 - Felipe Abarca
¿Cachan el proyecto MiroChark?

5:04 - Jose Foncea
¿Alguno?

5:05 - Orador no identificado
¿Cuánto?

5:07 - Cristian Astorga
Sí, ese que es como uno que crea muchos personitas para simular como...

5:12 - Felipe Abarca
Ya, lo adapté a mi necesidad y generé como... Eso está pensado para Twitter y está pensado para Reddit, entonces lo adapté y me generé uno para Instagram, entonces tengo análisis de industria, perdón, así como análisis de pricing, análisis de todo lo que es growth, a ver si la gente reacciona para arriba, para abajo, le gusta el click, le gusta, no le gusta, los enfocando vaya cachay como que porque es costoso y y uno que está y uno que es founder como que tiene un montón de cosas pero le da un potencial infinito entonces hasta eso nos podría servir para para sacar idea para testear para cualquiera estresarlo entonces esto básicamente te genera mil agentes tú le podéis pasar una encuesta oye tú te serviría trayéndolo para acá te serviría un asistente que te que te explique eh clara eh o o cómo generar tu PPM, cómo generar el eh tu devolución de impuestos, echa y eso lo podemos pasar para allá eh y y tendríamos como una nota eh se se supone que no son o sea podrían ser como lo lo podríamos consumir si es que si es que se requiere eh tengo como eh a ver bueno, Presencia Digital, también tengo otra empresa que la generé con OpenCloud. OpenCloud me está trabajando 24x7 en esa empresa, entonces ya conecté Stripe, es un proveedor de medio pago. Ya estoy vendiendo a todo el mundo. No cae en muchas compras porque no la he dedicado mucho tiempo.

6:54 - Jose Foncea
No llueve pero gotea.

6:56 - Felipe Abarca
Claro, no llueve pero gotea. Una guá que hizo 100% autónomo open-close. Yo solamente le hice la integración con Stripe, hice la integración con, perdón, valgué los productos que estaba generando y de ahí en adelante lo he dejado solo, no he hecho ni una guá. Entonces como que tengo algunas experiencias que me han servido y que podríamos utilizar, 100% iCoder, al principio lo programaba, ya dejé programar así, no sé, hace dos años. Estoy en Cloud Code desde SONET 3.5, que era el mejor modelo en ese momento, y antes de eso estaba con, claro, con un asistente, haciendo copy-paste de lo que te va entregando, pero ya... Bueno, y tengo varios experimentos también con NIA.

7:49 - Orador no identificado
Eso.

7:50 - Jose Foncea
Bueno, buen bagaje. Tenía harto know-how que aportar al equipo. Felipe, gracias por eso.

7:56 - Felipe Abarca
Y los modelos también, siempre estoy al día porque como me gusta esto y tengo el hiperfoco pero activadísimo con lo que veía, a pensar un modelo y hacer lo que hace, si nos funciona o no, pero entendería que no aplicaría mucho para acá dado que estamos bajo cloud, pero si hay que generar imágenes, hay que generar no sé qué nos podría servir más adelante, pero por lo menos tengo ahí como los conocimientos del estado del arte de los modelos fronteras.

8:34 - Cristian Astorga
Buenísimo, buenísimo.

8:35 - Orador no identificado
Máquina, crack.

8:36 - Felipe Abarca
No me permiten sobrevivir, pero sí ya me estoy dando como alguna... Me están estirando mi runway, así con mi... Hasta cuántos meses puedo sobrevivir con el eh con el finiquito más el el pago del seguro social como que va extendiendo a poquito, ¿cachai? Mi idea es como que mantenerlo, ¿cachai?

8:58 - Cristian Astorga
Claro, eh mi mi pregunta sobre lo mismo, tus expectativas son eh catapultarte en el sentido de que poder como tirar tu emprendimiento y tu idea al a la vista del público general, buscar trabajo, como en una empresa.

9:12 - Felipe Abarca
No, no, estoy buscando trabajo, eh, pero como como estoy desarrollando esta patita de de curso, estoy vendiendo como cuatro cursos, o sea, como cuatro o dos sesiones por 100 lucas, básicamente en cloud esto. Enfocado a emprendedores, enfocado a desempleados, enfocado a... Ahí como que lo he estado enfocando en distintos grupos según necesidades. Si están en mi link en que participamos en esto y nos fue bien, va a caer fácil un flujo.

9:49 - Jose Foncea
El proceso es la meta.

9:52 - Jose Foncea
Bueno, oigan ahí, cuéntanos.

9:55 - Anahi Gonzalez
Hola, ahora se escucha con un eco o no?

10:01 - Jose Foncea
Usted lo escucha con eco?

10:07 - Anahi Gonzalez
¿Parece que hay alguien que tiene el altavoz prendido? ¿A ver? ¿Aló? ¿Ya? Bueno.

10:13 - Felipe Abarca
Ahí te escucho yo.

10:14 - Felipe Abarca
Sí.

10:15 - Anahi Gonzalez
Ya, súper.

10:16 - Anahi Gonzalez
Mi nombre es Anahi, soy periodista, como comenté, me especialicé en análisis de datos, pases de datos, estuve trabajando en el etcétera y en RTDN y ahora último trabajé con ¿Te muteaste? Estoy de corto.

10:33 - Orador no identificado
Terrible.

10:34 - Orador no identificado
¿Hay algún parlante?

10:37 - Orador no identificado
¿Aló?

10:39 - Felipe Abarca
Ya no, ya no.

10:43 - Anahi Gonzalez
Estoy, ¿cierto? Ya, soy práctica. No sé, ¿hasta dónde me escucharon? Y me gusta mucho el diseño, por lo tanto, a la hora de desarrollar, me gusta centrarme en el diseño UX-UI, como soy periodista, tengo la facilidad de saber un poquito más, cierto, un poquito de marketing, un poquito de, digamos, cómo estructurar la información para que sea fácilmente leíble para el ojo humano y que sea de manera intuitiva, que es lo que más me gusta. En este momento estoy ayudando a Cristian a desarrollar su aplicación, ¿cierto? Lo conocí igual en el curso de AWS y estamos funcionando ahí y ahora también estoy desempleada desde el lunes. ¡Oh, guau!

11:41 - Jose Foncea
¿Y cómo te sentís con eso?

11:44 - Felipe Abarca
La verdad estoy muy feliz porque está como preciso para venir acá y poder así que muy feliz como que no nos cachen esta wea entonces está muy desactualizado y lo que se logren sumar es una revolución los que tomen crédito en esta revolución como de forma temprana son los que mejor le va a ir después entonces yo también comparto eso es súper momento es súper buen momento para estar trabajando.

12:18 - Cristian Astorga
Exacto, y con esta compañía de Hackathon también.

12:22 - Cristian Astorga
¿Y Hackathon han participado?

12:24 - Cristian Astorga
Sí, yo por lo menos en una de AWS.

12:29 - Cristian Astorga
¿Qué tal la experiencia?

12:31 - Jose Foncea
¿Qué destacarían ustedes como, no sé, a mí se me imagina desde la ignorancia, un tema relevante, la presión, la gestión de equipos? Los procesos, la relevancia de tener o de delimitar un proceso con etapas para que cada uno vaya sabiendo cuándo y de qué manera tiene que ir aportando. ¿Qué retroalimentación o qué aprendizaje sacaron ustedes respecto a eso?

13:04 - Cristian Astorga
Fue una jaquetona en la que en realidad no eran equipos como esta y tampoco era tan serio sino que era más como darse a conocer para una empresa, resolver un problema, proponer una solución. En ese sentido, creo que lo más importante es tomarse todo el tiempo posible, o sea, desde que te enteraste hasta que se hace, para poder desarrollar lo mejor posible, ajustar las expectativas, porque a lo mejor uno sabe que no va a ganar, pero uno tiene que hacerlo para uno, para darse a conocer, para mostrar estos Linkedin, pero no creo que estemos tan lejos de la idea de que podamos ganar aquí. No sé si es la categoría más alta de Builder, pero por lo menos de Bike Coder, puede ser, no sé. Depende de lo que presentemos. Entonces, como te digo, lo más importante, creo yo, es generar, como tú dices, un flujo de cómo vamos a ir avanzando en los días, qué podemos aportar cada uno y cuándo deberíamos tener las tarifas listas para poder probarla, porque esa es la parte más importante, probarla. Vi mucha gente que iba con ideas buenas, el desarrollo no era malo, pero pareciera que no lo probaron porque en el momento de la presentación guatearon. Entonces ahí perdieron la mitad de los puntos. Aunque la idea ya ha sido muy buena, yo creo que perdieron la mitad de los puntos.

14:31 - Felipe Abarca
Y lee la regla.

14:33 - Cristian Astorga
A no ser que digas desde un principio, estamos teniendo estos problemas actualmente, pero pensamos trabajarlos de esta manera. Ahí ya es como ya, él sabe que su producto está fallando, eso es muy distinto a presentarlo como algo genial y que falle en vivo, es horrible, eso es muy importante. Bueno y lo otro también es el pitch, como la presentación también tiene que ser de alto impacto, si una idea es muy buena y no se presenta de la correcta forma, igual no lo pescan tanto.

15:02 - Felipe Abarca
Yo he participado en dos en vivo. Una fue de que es como una competencia de eh participé con la cuantería al principio cuando partí con la cuantería. Ehh no no te dan feedback de cómo quedaste vos ¿Entendí? Ehh entonces no sé cómo me fue, pero por lo menos fue entretenido. Y la segunda fue en una de Open Eye cuando salió el el eh no esa estuvo buena porque aprendí caleta como como eh tenía un servicio un tenía un servidor con un con un un PC pero potentísimo tenía ese servidor tenía tokens ilimitado entonces como que eh eh destravé un montón de trabajo también para la cuentería ¿Cachai? Porque eh si bien genero cuentos eh ahí le metí como tenía tokens ilimitados le metí con regulación emocional, con guardarrieles para que no se nos cuida con las palabras, con reforzamiento conductual, ¿caché? Como que le metí mucha psicoterapia al cuento mismo. Y eso fue producto de este flujo agente. Claro, yo obviamente, leer las reglas es una guagua que suena básico, pero de verdad hay que entender que es la guagua que necesitamos. Oye, y debo decir algo, Yo me había postulado como coach. Ya, acá. Sí, y de hecho, por eso había generado un proyecto y lo había mandado y como que responde poco y nada a los correos. Entonces, como vi que no pasó nada, me metí a cabo. Entonces, no tenía idea que había categorías para esta jacatón.

16:51 - Cristian Astorga
Estaba recién leyendo. Sí, la categoría está, pero hay premios. Premios, el tema de las categorías, no sé si es que nosotros nos tenemos que inscribir en una categoría o ellos como que, en realidad como aquí dice mención especial, así como Best iBuilder, reconocimiento Crosstrack al equipo con la mejor implementación técnica, arquitectura de agentes y uso creativo de Cloud API. Y por otro lado está como el Best Vibe Coder, que sería como reconocimiento Crosstrack al equipo que logró el mayor impacto usando herramientas no code, low como Cloud Code, Cursor o Bio.

17:26 - Felipe Abarca
Bueno, yo creo que en 8n hay que tener dentro del stack, bueno, el lenguaje yo creo que es lo mismo, hay que saber el código, un buen stack de base de datos, no sé cuál usan ustedes, pero yo por lo menos con Superbase estoy contentísimo.

17:45 - Cristian Astorga
Sí, sobre eso mismo, yo ocupo Superbase, pero no sé si sea tanto como para este proyecto, en este proyecto me imagino más ocupando Obsidian. No lo he ocupado, pero creo que tengo una idea de cómo podría servir mucho en este caso.

18:01 - Jose Foncea
Ahí te está yendo, Cristian, a la solución por el tema del RAC, ¿cierto?

18:06 - Cristian Astorga
Claro, claro, claro. Me estoy pensando en el tema financiero.

18:09 - Jose Foncea
Solo para transparentarlo y aprovecho de decir algo que para mí es lo más importante en los equipos. Si es que dentro, desde ahora, hasta el fin de la alguno de nosotros está en desacuerdo con lo que el otro plantea, que es totalmente normal, válido y productivo, no tengamos miedo en decirlo, porque es muy normal que en los equipos de trabajo uno se quede callado por miedo a generar temas, roces. Es normal, hay que saberlo llevar. Entonces, desde ya, conociéndome y lo que creo que puedo aportar, es como atajar, es como el irse al tiro a la solución sin antes tener claro el problema, porque estoy casi seguro, casi seguro, que, bueno, no sé, por lo bajo, la mitad de los equipos se va a tender a ir por algo RAC, algo Carpathi, Obsidian, esa índole. Entonces, ok, la tecnología está, hay muchísimas vías para solucionar problemas, pero ¿cuántos de los equipos se van a plantear realmente un problema, aunque sea minúscula, pero si lo resuelves con un stack eficiente, y que probablemente nosotros no somos un equipo full técnico, pero lo que les puede pasar a los computines full, es que sobreingenericen todo. Ahí lo que nos invito primero es transparencia, decir las cosas con respeto siempre, y estar abierto al cambio. Más probable es que vamos a pivotear muchísimo, pero que privilegiemos siempre un proceso, que aún no está definido, pero privilegiemos un proceso que nos oriente y nos ayude a saber que estamos yendo por el camino correcto, independientemente de la solución que el día de mañana vayamos a trabajar.

20:00 - Cristian Astorga
Sí, me parece bueno. Entonces, en línea de lo mismo, me gustaría empezar entonces a conversar un poco de los problemas. Se nos plantean tres líneas, por cierto, la inclusión financiera, ciberseguridad ciudadana y protección de datos. ¿Tienen algún problema que les gustaría...? O sea, no sé, comentenme que... Yo ya comenté que tengo la idea de hacer la inclusión financiera, pero también estoy de acuerdo que muchos van a hacer un rack de inclusión financiera y creo que es lo más sencillo de implementar, por eso también es viable, pero cuéntenme.

20:33 - Jose Foncea
Lo que... O sea, yo en realidad estoy abierto, no tengo ninguna preferencia porque no he pensado en soluciones. Les comentaba al principio de la reunión que hice un bit research, cruzando fuentes chilenas y todo el tema, para orientarnos qué existe, qué problemas hay con todo eso, y con ese contexto claro, poder decir ya, como equipo nos conviene preferencias nuestras con lo que el mercado necesita, nos conviene irnos por allá. No sé si les parece que les comparta pantalla para revisar.

21:13 - Felipe Abarca
Yo también, teniendo clara la parrilla de información que podemos disponer de ofrecer, de buscar problemas asociados. Porque me parece que también había propuesto una idea buena, pero no tenía totalmente el acceso a la información, entonces como que la idea fue guateando en el camino.

21:30 - Jose Foncea
Ya bueno, bueno. Veámoslo entonces. No me quiero detener tanto en el detalle, sino que tengamos una pincelada de esto. Hay información de aquí que probablemente ya esté en el en el enlace del Impact Lab, que lo dejé ahí en la descripción del grupo de WhatsApp. Pero vámonos a la carne. Ya, a ver. ¿Qué dice? En resumen ejecutivo, Chile bancarizó el 91 por ciento, pero perdió la batalla por la calidad Ya, ojo con ese concepto. Calidad. Tenemos grandes números acá. Casi 700.000 reclamos en CERNAC. Ya, más del 50% presidente. Ya, reclamos, tenía un tema con los reclamos.

22:12 - Orador no identificado
Ciberataque.

22:13 - Jose Foncea
Ah, importante, las soluciones van orientadas al ciudadano, al usuario a pie, a nosotros. Por lo tanto, ahí debiésemos generar el impacto. Fishing, entonces tenía un tema de reclamos. Tenía un tema de ciberataques, check of fraud, morosidad, síntomas. Esto te habla quizás de un tema del sistema y de falta de educación financiera.

22:46 - Jose Foncea
Alfabetización financiera.

22:47 - Jose Foncea
Entonces aquí a grande rasgo vemos reclamos, ciberataques, morosidad y educación. Como grandes temas. Tesis. Chile tiene la destinación financiera y privacidad más alineada. Estos estándares creo que son americanos o europeos. Ahí yo creo que tú, Felipe, tenés más clara la película. Pero carece de traducción operativa. Las leyes dibujan un consumidor protegido en la práctica, no sabe ejercer. O sea, nos blindaron demasiado, nos ofrecieron todo, pero no sabemos qué diablo hacer. Por lo tanto, debemos pensar en un perfil cliente, puede haber varios, pero que está abrumado, sabe quizás que existen muchas cosas como soluciones digitales, pero no sabe por dónde partir. Esta es la ley FinTech, sobre un intermediario nuevo autorizado. Clonología. Este después igual se los voy a mandar para que lo veamos más bien. Brecha reconocida. Cerco del registro hacia asesoría de inversión. Resultado, la promesa de más competencia sigue concentrada en pocos jugadores. Ahí tenía un tema de que está trancada la cuestión con la ley Fintech. Ahora, la ley de protección de datos que sale en vigencia en noviembre o diciembre de este año. 17 meses para que las empresas se adapten. Yo no sé a priori cuál va a ser el impacto de esto en usuarios. Lo único que tengo entendido es que uno va a poder decirle a la empresa, oye, esto nunca lo autoricé, sácame del sistema, cuando no tenga nada que ver con...

24:36 - Felipe Abarca
Para poder tener acceso a tu información. Si fuiste un cliente de la clínica, le podés decirle, quiero que mi nombre desaparezca O entregame todo lo que tenga asociado a mi perfil.

24:50 - Orador no identificado
No sé.

24:51 - Felipe Abarca
Ya, buenísimo.

24:52 - Orador no identificado
Perfecto.

24:52 - Felipe Abarca
Puedes optar a tener una especie de portabilidad de información.

24:56 - Felipe Abarca
Eso está bueno, ¿cachai?

24:57 - Felipe Abarca
Podís pasar de la clínica A a la clínica B llevándote todo tu historial.

25:03 - Jose Foncea
Ya, ahí lo tenemos como para la grabación una oportunidad para proyectos. El tema de la portabilidad de la información personal como parte de la de la vertical de protección de datos. Veamos ahora un poquito más clara la película. Tenemos estas tres verticales. Inclusión financiera, que entiendes como por la línea en que al menos tú, Cristian, estás proponiendo. El tema no es el acceso, sino la calidad. El comportamiento financiero. Yo entraría a picar acá en qué problemas hay en el comportamiento ¿Ya? ¿Tenéis algunas cifras? Y no solo pensando en empresas.

25:46 - Felipe Abarca
Las pymes yo creo que son las más afectadas hoy día. Hay un montón de pymes chicas que se los come la máquina y a nivel financiero caen en deuda, no hacen bien el pago de impuestos en el servicio impuesto interno porque o no tienen el contador para pagarles, o el contador los caga, o el tiempo ya no les dio. En infinito lo que se le puede hacer. Se le puede generar un asistente, se le puede generar un pre-analizador, o sea, un analizador tributario. Oye, ya estáis pasados en gasto, ahora te conviene invertir, como inversión para tu negocio específico, te conviene cursos, pagar cense, entonces como una especie Pime.

26:39 - Orador no identificado
Está buena, está bien buena.

26:41 - Jose Foncea
De hecho, lo que pudiéramos hacer es que dentro de todo el proceso que tengamos, por ejemplo, definimos ya la línea por la que nos vamos a tirar, generamos un pool de posibles proyectos. Claro, sí, hacemos la evaluación y todo el tema, y en vía paralela lo que podemos hacer antes de la hackathon es un proceso de validación con usuarios. ¿Cachai? Como que la cuestión no se queda acá entre cuatro paredes, sino que nos organizamos, cada uno por las vías de redes sociales que tenga disponible, echamos a correr un proceso y con data real, no solo con la de la CMF, Servicio Impuesto Interno, sino que lo cruzamos eso con las iniciativas que nosotros creemos que pueden generar impacto y vemos qué dicen los usuarios. Ya. Cyberseguridad y protección de datos. Y aquí me quiero detener antes de que pasemos a esta patita que es más de los dolores priorizados y después hay una matriz. Acá está. Aquí es como qué cosas existen, qué cosas pudieran ser buenas ideas o buenos proyectos y todo el tema. Ya. Respecto a las verticales. De Guata. ¿Cuál nos hace más sentido a nosotros? ¿Preferencia? ¿Experiencia? ¿Cómo va a tener algo ahí ya agarrado?

28:08 - Felipe Abarca
En este camino de la independencia yo estoy vendiendo protección de datos. Implementación de la ley de protección de datos. Igual, tú hay que achar que uno con cloud promete todo. Y aprende en el camino nomás. Entonces hasta el momento no he aprendido mucho porque hasta el momento no he cerrado ningún contrato. Pero claro, Si bien es como está dentro de mi día a día, no me siento muy cómodo en eso. Pero si hay que aprender, aprendo. Y yo creo que estamos los cuatro en esto. Aprenderemos más rápido. Yo en la primera, en la inclusión financiera, me gusta harto. Porque siento que hay un montón de carne.

28:50 - Orador no identificado
De ciberseguridad...

28:51 - Cristian Astorga
Yo no me siento cómodo con ciberseguridad porque es más bien fuerte, es muy sensible.

28:56 - Orador no identificado
Más técnico también.

28:57 - Jose Foncea
Es más técnico.

28:59 - Felipe Abarca
Hay un montón de cosas que se pueden hacer, pero...

29:03 - Cristian Astorga
Sí, definitivamente. Pero es más técnico.

29:06 - Felipe Abarca
Pensando en simple, para decir seguridad, hacer una especie de true caller que te analice de alguna base de datos de dónde viene el número, la probabilidad de estafa o que tenga una escucha. Eh activa y que y que te que para cualquiera sea el el usuario estoy pensando ahí como en un adulto mayor eh si si ya te están empezando con la parte de la estafa esta aplicación misma te diga epa eh déjalo hasta aquí es como un como un controlador eh sí, en el tiempo tema real es que el ciberseguridad yo creo que es algo que va a cambiar muchísimo porque así como están los Blue Team, los de defensa, tenéis los otros gallos que van a ocupar IA para atacar.

30:04 - Jose Foncea
Entonces al final con nuestra inexpertiza técnica en este sentido creo que No. Mira la relación del usuario a nivel financiero con instituciones o con hackers. Lo más lógico es atacar el problema, cualquiera que este sea, al comienzo. Problema raíz. ¿Y cuál es eso? Inclusión financiera. A través de la educación, a través de cualquier tipo de solución que le haga aprender o resguardarse, lo que sea, en esta etapa. Porque para mí estas dos son una vez que el usuario ya está dentro del sistema y puede ejercer mejor sus derechos o protegerse de estafas, lo que sea, pero siento que acá uno aborda los problemas a nivel raíz antes de que se generen. Creo que eso pudiera generar un mayor impacto a priori. Les propongo que definamos esta patita Un poco para ir ya haciendo algunas disminuciones y que nos vayamos con Anahi.

31:13 - Anahi Gonzalez
Me gustaría hablar un poquito al respecto, creo que todos los puntos se pueden ir a través de generar, por ejemplo, lo más básico sería generar un chatbot en donde tú le presentes tu problema, le das un cuestionario en donde ahí en ese momento el chatbot elige los documentos específicos a revisar para ver el caso, ¿cierto? Y ahí podemos generar una interacción en donde las personas puedan, por ejemplo, explicar su caso, saber cuál es su consulta, etcétera. Tengo aquí un link que me interesa bastante, que creo que deberíamos implementar, que es de cierta manera la estrategia de cómo vamos a nuestro producto. Este es el documento más actualizado respecto a el uso de la tecnología del usuario de promedio en Chile en donde muestra que si nosotros lo abrimos que el 97% de las personas utiliza el teléfono móvil para ingresar a internet versus el 69% que ingresa desde el computador. Y lo que más se hace es realizar búsquedas, especialmente a través de Google para encontrar información. Entonces creo que deberíamos aprovechar este tipo de datos para nosotros presentar la mejor forma de hacer nuestra plataforma, digámoslo así. Considero que ante estos datos, el mejor tipo de plataforma sería una página web, ¿cierto? Que sea encontrable, por ejemplo, a nivel Google, rastreable por la IA de Google, ¿cierto? Para que te lleve ahí inmediatamente a hacer el link y que idealmente, no sé, ahí le diseño una mascota para que ese algo que te hable esa IA pueda también tener un rostro, genera un poquito de más empatía y más confianza y genera una marca. Y ante eso, bueno eso es lo que yo les ofrezco, ante eso podemos tenemos una infinidad de estructuras y eh distintas formas de presentar este proyecto eh como eh cierto como núcleo pero yo les propongo eh de esta forma entregarlo lo que tú dices que para para la solución que que necesitemos un chat conversacional en la parte como visual, interactiva, independiente de lo que hagamos por detrás.

34:01 - Felipe Abarca
Hagamos ciberseguridad, hagamos fintech, hagamos... Lo que sea.

34:04 - Anahi Gonzalez
Y pensando en el usuario chileno, pensemos en que las personas siempre entran desde el celular y cuando se trata de un tema financiero o una duda más legal, digamoslo, lo hacen siempre a través de Google. Entonces, idealmente hacer una página web en vez de, pues, ejemplo una aplicación.

34:24 - Felipe Abarca
Mira ahí en ese sentido estoy de acuerdo y yo creo que esto ya sería más una definición independiente de la solución para que sea que tenga presencia digital yo propongo usar astro porque astro te permite que google te renderice ya sé cómo aparecer en chat gpt en cloud y en todas esas weas porque estoy vendiendo presencia digital entonces eh perdí y nombraste ah y bueno que la aplicación tenga por concepto que sea eh es como filosofía sí sí porque eh es el mercado si tú ves ahí eh mismo dice creo que un poquito más arriba de hecho dice que el noventa y siete por ciento de las más más creo que siguiente es un marco con dos son circulitos y tiene dos ahí está abajo ese ahí está entonces dice 95 por ciento de las personas utilizan mobile en naranjo cierto y el 69 por ciento utiliza el computador considerando haciendo first mobile te permite cubrir las dos vistas y hasta se puede se podría instalar en los teléfonos y que se cumplen algunos cheques.

35:50 - Anahi Gonzalez
Sí, pero idealmente, claro, intentar vender esto como algo realmente, digamos, accesible para la persona a pie, que es nuestro primer usuario. Independiente de que si queremos como que igual sirva para la pymes, si el usuario cumple con estas características o otras, que probablemente va a ser mucha pymes. Normalmente la persona que está creando una pymes que no sabe nada, es un usuario a pie, que es el que se mete al celular y empieza a buscar desde ahí, como primera búsqueda al menos.

36:29 - Jose Foncea
Buenísimo el aporte Anaís, yo creo que este análisis etnográfico nos da una definición súper concreta, independiente de la solución, de qué plataforma usar, qué arquitectura y dónde enfocarse. Yo creo que eso es súper, súper valioso.

36:48 - Orador no identificado
Así que bacán.

36:49 - Jose Foncea
Ah, yo les estaba escribiendo, no les mandé. Yo a las 12 tengo que pasarme otra reunión, así que ahí los dejo nomás y después me pongo el día.

37:01 - Felipe Abarca
Sí, no, pero esta roba era como para conocernos y ya ahora empezar a iterar ideas.

37:07 - Jose Foncea
Eco, eco. Yo ahí ya, si me quedan cuatro minutitos, me pudo comprometer a proponerles como una hoja de ruta, un proceso, donde primero, saliendo de esta reunión, lo más probable es que tengamos que cada uno hacer un breve levantamiento desde su experiencia, su óptica, cuáles son los problemas que ve. ¿Cuáles son los problemas que ve? Evaluarlos con métricas variables de todo el tema, que es como sale un poquito acá. Volumen, severidad, frecuencia, etcétera. Y de ahí debiésemos llegar en una próxima reunión a mostrar esos resultados y decir ya, como equipo, qué problema y por qué debiésemos atacar. Entonces si llegamos con lista, cada uno diez problemas, vamos a revisar eso, lo pulimos, y llegamos a tres. Ya, echamos a competir esos tres. Después vamos a llegar a uno. Ya, por ese problema nos vamos a ir. Y cuando tengamos ese problema, pero tiki-taka, ya todos lo manejemos al revés y al derecho, creo que debiésemos de aquí, al comienzo de la hackathon, llegar con un MVP relativamente testeado, y ahí aprovecho de preguntarle a ustedes cuáles son sus expectativas para que durante la jacatón, la pega no sea construir, sino que sea, con la ayuda de los expertos de antrópico, que sé yo, los mentores, refinar y botear la solución y testearla, estresarla, cosa que tampoco estemos estresados, sino que haya habido un trabajo previo, estructurado, y lo evaluamos y ya está.

39:00 - Felipe Abarca
¿No castigan eso? Si no dice, no.

39:03 - Jose Foncea
¿Castigar qué cosa?

39:04 - Cristian Astorga
¿Llegar, ir con algo listo? ¿Sí? No, no, para nada, para nada.

39:09 - Orador no identificado
Perfecto.

39:10 - Felipe Abarca
Oye, yo, yo, yo les propongo, o sea, ¿Qué, qué aplicación usan ustedes para codear?

39:17 - Jose Foncea
¿Sistema de, de, de proyectos, que estén de proyecto?

39:21 - Felipe Abarca
¿Sí? ¿Les parece que cree un, un que lo compartamos entre los cuatro y ahí empezamos a, a tener en vivo los contenidos de cada uno, cada uno repositeando en el mismo lugar.

39:36 - Jose Foncea
Vale, perfecto. Hay preguntas que yo tengo relativamente poca experiencia con Github, yo lo asocio netamente a la documentación del proyecto puro y duro a nivel más técnico, ¿cierto? Pero lo que son, por ejemplo, si nosotros vamos encontrando, oye, una fuente de información para el levantamiento, X, A, B, C, ¿se puede? ¿O es la mejor alternativa centralizarlo ahí?

40:03 - Felipe Abarca
Sí, o sea, también está bueno es decir, el ambiente productivo todo por excelencia, ¿cachái? Entonces, esto nos obliga a nosotros a subir al estándar. Si no ordenamos, podemos poner todos los links en un en un mismo lugar y todos los. Sí, y yo propongo, o sea, yo voy a armar ahí una estructura para que quede una especie de wiki, para que vayamos viendo los los de cada uno, vayamos teniendo abajo las ideas concentradas, consolidadas, y y claro, y yo yo paso ya me me estoy metiendo en la más adelante, puede pagar alguna API tipo para para hacer los racks y escala, bueno, inmediatamente, por cien pesos al día, no sé, no cuesta nada, bueno, si lo tengo. Entonces, súper bueno, perdón, bueno, y si lo conectamos a una base ATO y la base ATO ya tiene, ya está conectada por ese MSP, el modo de trabajo que se volvería es solamente pedirle cosas. En donde yo veo que vamos a tener que después hacer es como el manejo de la información ahí ya hay dos expertos entonces yo creo que va a ser fácil o sea en el manejo del dato de los flujos de la información pública como como de público lo pasamos a privado como la consumimos eh pero yo en la parte técnica tengo confianza de que yo por lo menos si no lo sé lo voy a averiguar y lo vamos a resolver he hecho peludísima eh en este en las últimas dos semanas y me han salido bien y están productivas entonces Eh, puta, enfoquémonos en desarrollar ideas, ¿cachai? Bueno, requerimientos técnicos, eh, ya con requerimientos técnicos, eh, quien tenga que construir, eh, va a ser mucho más fácil. Buenísimo, buenísimo.

41:43 - Cristian Astorga
Ahí yo reconozco que tienes más experiencia, Felipe, pero, eh, creo que yo tengo harto tiempo, entonces, si necesitas cualquier cosa, apóyame.

41:51 - Felipe Abarca
Es que son distintas, son distintas aristas las que hay que cubrir, entonces, teniendo, puta, que en el front, que en la funcionalidad, que en la que en el desarrollo de la MCP se tenía un montón de trabajo.

42:07 - Cristian Astorga
Entonces mi idea trata de externalizarlas para ir apoyándote también con mi tiempo, con mi dedicación, etcétera.

42:14 - Jose Foncea
Buenísima. Entonces, ¿les parece? Ya, ¿tú te quedás, Felipe, con esa pega en el repositorio? Yo lo que puedo hacer es armar, no sé, quedarme con un rol más de como de Project Manager, para ir trazando las etapas, los hitos, bla, bla, que estemos todos, todos sepamos qué es lo que hay que hacer, qué es lo que tiene que hacer, etcétera, etcétera.

42:41 - Felipe Abarca
Y ahí vamos usando el repositorio como fuente de la verdad. Y lo que estáis diciendo tú en el principio de las fuentes de información, yo creo que es súper útil para sacar ideas, ideas factibles, porque hay que meterle factibilidad todavía.

42:56 - Cristian Astorga
a llegar con algunas varias ideas de problemas y contabilización ahí con métricas para decir qué tanto impacto generaría.

43:05 - Orador no identificado
Buenísima.

43:05 - Jose Foncea
Entonces, disponibilidad, próxima reunión, ¿cuándo la extinca?

43:08 - Cristian Astorga
Yo creo que preferiblemente podría ser hoy día a la noche, no sé si la extinca o ya mañana, pero ojalá hoy día a la noche para ir.

43:21 - Felipe Abarca
¿Me extinco hoy día a la noche para el repositorio listo, montado y de trabajo.

43:27 - Cristian Astorga
Y ahí si alguien quiere trabajar en la noche o mañana en la mañana que lo puede hacer libre.

43:34 - Jose Foncea
Claro. Ok, ok. Entonces una reunión, yo creo que sería una reunión más express como para que todos entendamos el setup con el que vamos a partir trabajando, estemos alineados. Eso sería a las 9. ¿Tú de qué hora podés, Felipe?

43:48 - Felipe Abarca
No, si de las 9 de la noche puedo. O sea, setup más lo que logran recopilar dentro del día.

43:57 - Cristian Astorga
Claro, eso como para conversar lo que hicimos durante el día, qué encontramos.

44:02 - Felipe Abarca
Ya, perfecto. Porque tenemos que unificar los criterios de evaluación, tenemos que unificar la idea en un mismo lugar, empezar a rankear.

44:12 - Jose Foncea
Ya, buenísimo. Ya pues, chiquillos, buena primera reunión. Muchísimas gracias por la apertura.

44:20 - Felipe Abarca
Un gusto, chicos.

44:23 - Felipe Abarca
Eso.

44:24 - Jose Foncea
Cuídense, un abrazo, hablamos.

44:27 - Jose Foncea
Chau, chau.

44:28 - Orador no identificado
Chau, un gusto.
```

</details>

# Hito 5 — Informe de Gestión y Propuesta de Mejora

**Trabajo Práctico Integrador — Análisis de Datos Inicial (TUP)**
**Grupo 7:** Bontorno Pontis · Hassan Padoan Vargas · Mas Cannizzo · Mejias · Nuñez Agostinho · Vernier

Informe basado en la evidencia del análisis (Hitos 1–3) y en la exploración
interactiva del dashboard de Grafana (Hito 4). Universo: **700 alumnos** de la
TUP, cuatrimestre marzo–junio 2026, distribuidos en 9 comisiones y 3 turnos.

---

## 1. Diagnóstico Académico

El análisis de los datos revela un hallazgo central que no es evidente a simple
vista: **el principal problema de la cohorte no es el bajo rendimiento, sino el
abandono progresivo**. Tres evidencias lo sustentan.

### 1.1 El abandono es el resultado dominante, no la desaprobación

De los 700 alumnos, la distribución de estados finales es:

| Estado | Alumnos | % |
|--------|--------:|--:|
| Aprobado | 309 | 44% |
| **Ausente** | **281** | **40%** |
| Recupera | 96 | 14% |
| Desaprobado | 14 | 2% |

El dato que ordena todo el diagnóstico: **solo el 2% desaprueba el parcial, pero
el 40% directamente no se presenta**. La tasa de presentación al parcial es de
apenas **59,9%**. El sistema no está perdiendo alumnos porque les vaya mal en el
examen: los está perdiendo *antes* del examen.

### 1.2 La baja constancia anticipa el abandono

Al comparar el **Índice de Constancia** (% de entregas hechas a tiempo en TPs y
Quizzes previos) entre quienes se presentaron y quienes no:

| Grupo | Índice de Constancia promedio |
|-------|------------------------------:|
| Presentes al parcial | **72,1%** |
| Ausentes | **35,7%** |

La brecha es de **36 puntos**. Los alumnos que abandonan ya mostraban una
constancia mucho menor durante el cuatrimestre. Esto convierte al Índice de
Constancia en una **señal de alerta temprana**: no hay que esperar al parcial
para saber quién está en riesgo, el comportamiento de entregas ya lo anticipa.
Con el umbral del 43% de constancia, el dashboard identifica **253 alumnos en
zona de riesgo** sobre los que se podría intervenir.

### 1.3 La deserción es gradual y transversal

La evolución por actividad muestra que la **tasa de entrega cae de forma
sostenida** a lo largo del cuatrimestre —del **87,3%** en el primer TP al
**59,9%** en el parcial— mientras la **nota promedio de quienes sí entregan se
mantiene estable** (entre 6,5 y 7,0). Es decir: los que siguen presentes rinden
bien; el problema es la cantidad creciente de los que dejan de entregar.

Además, al filtrar por comisión y turno en el dashboard, las diferencias de
rendimiento entre comisiones son **moderadas** (notas promedio del parcial entre
6,56 y 7,64) y ninguna queda sistemáticamente por debajo del umbral de
aprobación. Esto indica que **el abandono no se concentra en una comisión o
turno específico: es un fenómeno transversal** a toda la cohorte, por lo que la
intervención debe ser general y no focalizada.

---

## 2. Propuestas de Mejora (justificadas en datos)

### Propuesta A — Sistema de alerta temprana por Índice de Constancia

**Acción:** Implementar un tablero de seguimiento (el mismo dashboard del Hito 4)
que marque automáticamente a los alumnos cuyo Índice de Constancia caiga por
debajo del **43%**, y disparar una intervención de tutoría/contacto en las
**semanas 4 a 6** del cuatrimestre —el punto de inflexión donde la tasa de
entrega empieza a caer con fuerza.

**Justificación en los datos:** Los ausentes tenían una constancia promedio de
35,7% frente al 72,1% de los presentes (sección 1.2). Como la baja constancia
*precede* al abandono, intervenir sobre los 253 alumnos que hoy están bajo el
umbral permitiría actuar **antes** de que se conviertan en parte del 40% de
ausentes, en lugar de constatar la pérdida cuando ya es irreversible.

### Propuesta B — Refuerzo de la adherencia en la segunda mitad del cuatrimestre

**Acción:** Concentrar acciones de retención (recordatorios de entregas,
instancias de recuperación de TPs, micro-evaluaciones de bajo peso) en el tramo
donde la tasa de entrega se desploma, para sostener el hábito de entrega hasta
el parcial. La acción es **general para todas las comisiones**, no focalizada.

**Justificación en los datos:** La tasa de entrega cae del 87,3% al 59,9% de
forma gradual (sección 1.3), mientras la nota se mantiene estable: el alumno que
entrega, aprueba. El objetivo entonces no es "enseñar mejor" sino **evitar que
el alumno deje de participar**. Y como las diferencias entre comisiones son
moderadas, la medida debe aplicarse a toda la cohorte por igual.

---

## 3. Conclusión Final

La cohorte 2026 de la TUP no tiene un problema de capacidad académica —quienes
participan obtienen buenas notas— sino de **adherencia**: cuatro de cada diez
alumnos abandonan antes del parcial, y ese abandono está anticipado por una
caída temprana y medible en la constancia de entregas.

Implementar las dos propuestas tendría un impacto directo sobre el indicador más
crítico: la **tasa de presentación al parcial (hoy 59,9%)**. Si la alerta
temprana lograra reincorporar aunque sea a una fracción de los 253 alumnos en
riesgo, el efecto sobre la cantidad de aprobados y sobre la retención general de
la cohorte sería significativo. La evidencia muestra que el momento de actuar no
es el examen, sino las primeras semanas: ahí es donde los datos ya avisan quién
está por quedarse en el camino.

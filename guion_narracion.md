# Guion de narración – Grupo 12 (duración total: 4:30)

Sumas inferiores y superiores: **aproximación y refinamiento**.
Ejemplo propio: $f(x) = x^2$ en $[0, 2]$, área exacta $8/3 \approx 2.67$.

> Los tiempos están sincronizados con [animacion_grupo12.py](animacion_grupo12.py)
> (cada escena usa marcas de tiempo absolutas). Ritmo de lectura sugerido: ~2 palabras por segundo,
> con pausas cortas cuando aparece una fórmula nueva.

| Voz | Tramo | Escenas |
| :-- | :-- | :-- |
| **Voz 1** | 0:00 – 0:45 | 1. Portada · 2. Problema del área |
| **Voz 2** | 0:45 – 2:00 | 3. Suma inferior · 4. Suma superior y encierro |
| **Voz 3** | 2:00 – 4:30 | 5. Refinamiento · 6. Conclusión · 7. Créditos |

---

## Voz 1 (0:00 – 0:45)

### Escena 1 – Portada (0:00 – 0:20)
**[0:00]** "Hola, somos el Grupo 12 de Cálculo Intermedio. En este video presentamos las sumas inferiores y superiores: aproximación y refinamiento."

**[0:09]** *(aparece la pregunta)* "Nuestra pregunta central es: ¿cómo podemos encerrar el valor de una región entre dos aproximaciones?"

### Escena 2 – El problema del área (0:20 – 0:45)
**[0:20]** "Para responderla, trabajaremos con un ejemplo propio: la función f de x igual a x al cuadrado en el intervalo de cero a dos."

**[0:34]** *(aparece el área sombreada)* "Es continua y no negativa, así que su área está bien definida. Vale exactamente ocho tercios, cerca de dos coma sesenta y siete."

---

## Voz 2 (0:45 – 2:00)

### Escena 3 – Suma inferior $L_4$ (0:45 – 1:20)
**[0:45]** "Dividimos el intervalo en cuatro partes iguales, de ancho cero coma cinco."

**[0:52]** "Como la función es creciente, el mínimo de cada subintervalo ocurre en el extremo izquierdo."

**[1:00]** *(aparecen los rectángulos verdes)* "Con esas alturas construimos rectángulos que quedan por debajo de la curva."

**[1:06]** *(aparece el cálculo)* "Sumamos las alturas y multiplicamos por cero coma cinco."

**[1:11]** *(aparece el resultado)* "Resulta: L cuatro igual a uno coma setenta y cinco,"

**[1:15]** *(el punto verde aparece en la recta numérica)* "una aproximación por defecto, porque queda por debajo del área."

### Escena 4 – Suma superior y encierro (1:20 – 2:00)
**[1:20]** "Ahora hacemos lo mismo con el máximo, que en una función creciente ocurre en el extremo derecho."

**[1:30]** "Estos rectángulos sobresalen de la curva, y su suma, la suma superior, es U cuatro igual a tres coma setenta y cinco: una aproximación por exceso."

**[1:42]** *(aparece la barra amarilla en la recta numérica)* "Así, el área queda encerrada: uno coma setenta y cinco, menor o igual que dos coma sesenta y siete, menor o igual que tres coma setenta y cinco."

**[1:54]** "Pero el intervalo todavía es amplio: ¿podemos achicarlo?"

---

## Voz 3 (2:00 – 4:30)

### Escena 5 – Refinamiento (2:00 – 3:35)
**[2:00]** "La respuesta es refinar la partición: usar más subintervalos y rectángulos más delgados."

**[2:10]** *(n = 8)* "Con n igual a ocho, la suma inferior sube a dos coma diecinueve y la superior baja a tres coma diecinueve."

**[2:23]** *(n = 16)* "Con n igual a dieciséis, tenemos dos coma cuarenta y dos, y dos coma noventa y dos."

**[2:36]** *(n = 40)* "Con n igual a cuarenta, dos coma cincuenta y siete, y dos coma setenta y siete."

**[2:48]** "Fíjense: las sumas inferiores siempre suben, las superiores siempre bajan, y el área real, ocho tercios, siempre queda en medio."

**[3:00]** *(aparece la fórmula del error)* "¿Cuánto se achica el intervalo? Como la función es creciente, la diferencia entre ambas sumas es f de b menos f de a, por delta x. Acá, cuatro por dos sobre n: ocho sobre n."

**[3:15]** *(n = 100)* "Con n igual a cien, el error ya es de solo cero coma cero ocho."

**[3:26]** "Cada vez que duplicamos n, el error se reduce a la mitad."

### Escena 6 – Conclusión (3:35 – 4:15)
**[3:37]** "Primero: para toda partición, la suma inferior es menor o igual que el área, y esta es menor o igual que la suma superior."

**[3:49]** "Segundo: la diferencia entre las cotas es ocho sobre n, así que podemos hacer el error tan pequeño como queramos."

**[4:00]** "Tercero: cuando n tiende a infinito, ambas sumas convergen a la integral de x al cuadrado entre cero y dos, que vale ocho tercios."

**[4:11]** *(aparece el recuadro final)* "Así, el área queda encerrada entre dos aproximaciones que se juntan al refinar."

### Escena 7 – Créditos (4:15 – 4:30)
**[4:16]** "Gracias por ver nuestro video. Las fuentes y herramientas aparecen en pantalla. Declaramos el uso de IA como apoyo en la sintaxis de Manim y en el formato de la documentación."

---

## Valores de referencia (para la defensa oral)

| n | $L_n$ | $U_n$ | $U_n - L_n = 8/n$ |
| :-: | :-: | :-: | :-: |
| 4 | 1.75 | 3.75 | 2.00 |
| 8 | 2.19 | 3.19 | 1.00 |
| 16 | 2.42 | 2.92 | 0.50 |
| 40 | 2.57 | 2.77 | 0.20 |
| 100 | 2.63 | 2.71 | 0.08 |

Fórmulas usadas (f creciente, $\Delta x = 2/n$):
$L_n = \sum_{i=1}^{n} f(x_{i-1})\,\Delta x$, $\quad U_n = \sum_{i=1}^{n} f(x_i)\,\Delta x$, $\quad U_n - L_n = (f(2) - f(0))\,\Delta x = 8/n$.

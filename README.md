# Proyecto EID - Cálculo Intermedio (Grupo 12)
## Sumas Inferiores y Superiores: Aproximación y Refinamiento

Este repositorio contiene el código fuente, el script de verificación y las animaciones desarrolladas con **Manim Community** para la Evaluación Integrada de Desempeño (EID) de Cálculo Intermedio.

---

### Información General del Equipo

* **Curso / Código:** Cálculo Intermedio MAT1188-1-2026-2
* **Grupo:** 12
* **Tema asignado:** Sumas inferiores y superiores (Aproximación y refinamiento)
* **Pregunta central:** *¿Cómo podemos encerrar el valor de una región entre dos aproximaciones?*
* **Duración del video:** 4:00 minutos

| Integrante | Usuario de GitHub | Rol Principal | Intervención en el Video |
| :--- | :--- | :--- | :--- |
| `Eduardo Escares` | `Eduardo Escares (https://github.com/eduardoscrs` | Matemática y explicación | **Voz 1** (0:00 – 0:33; luego retoma en la conclusión) |
| `Christian Ferrer` | `Christian Ferrer (https://github.com/Ozauri0)` | Visualización y código | **Voz 2** (0:34 – 1:51) |
| `Patricio Benavides` | `Patricio Benavides (https://github.com/patitojavi)` | Revisión e integración del video | **Voz 3** (1:52 – 3:10; luego retoma en el cierre) |

---

### Escenas del Video

Toda la animación está en una sola clase de Manim, `AnimacionGrupo12` (`animacion_grupo12.py`), dividida en 7 escenas consecutivas. Todas usan $f(x) = x^2$ en $[0, 2]$:

| # | Escena | Qué muestra |
| :-: | :--- | :--- |
| 1 | Portada | Título, grupo y pregunta central. |
| 2 | El problema del área | Ejes, gráfica de $f(x) = x^2$ y el área bajo la curva, con el valor exacto $\int_0^2 x^2\,dx = 8/3$. |
| 3 | Suma inferior $L_4$ | Partición regular con $n = 4$ y $\Delta x = 0.5$; rectángulos bajo la curva (alturas en el extremo izquierdo) y $L_4 = 1.75$. |
| 4 | Suma superior $U_4$ y encierro | Rectángulos sobre la curva (extremo derecho), $U_4 = 3.75$ y el encierro $1.75 \le 8/3 \le 3.75$ en una recta numérica. |
| 5 | Refinamiento | Partición con $n = 8, 16, 40$ y $100$; tabla de $n$, $L_n$, $U_n$ y $U_n - L_n$, y el error $U_n - L_n = 8/n$. |
| 6 | Conclusión | Encierro, control del error y paso al límite; respuesta a la pregunta central. |
| 7 | Créditos | Fuentes, herramientas y declaración de IA. |

---

### 1. Resumen Teórico y Matemático

Para aproximar el área bajo una función continua y no negativa $f(x)$ en un intervalo cerrado $[a, b]$, definimos una partición regular de $n$ subintervalos de ancho constante:
$$\Delta x = \frac{b - a}{n}, \quad x_i = a + i \cdot \Delta x \quad (i = 0, 1, \dots, n)$$

En nuestro proyecto utilizamos el ejemplo propio:
$$f(x) = x^2 \quad \text{en el intervalo } [0, 2]$$
Cuyo valor exacto de referencia es:
$$\int_0^2 x^2 \, dx = \frac{8}{3} \approx 2.6667$$

#### Construcción de las Cotas:
Dado que $f(x) = x^2$ es continua, no negativa y estrictamente creciente en $[0, 2]$:
1. **Suma Inferior ($L_n$):** El valor mínimo de $f$ en cada subintervalo $[x_{i-1}, x_i]$ se alcanza en el extremo izquierdo $x_{i-1}$:
   $$L_n = \sum_{i=1}^n f(x_{i-1}) \cdot \Delta x \quad (\text{Aproximación por defecto})$$
2. **Suma Superior ($U_n$):** El valor máximo de $f$ en cada subintervalo $[x_{i-1}, x_i]$ se alcanza en el extremo derecho $x_i$:
   $$U_n = \sum_{i=1}^n f(x_i) \cdot \Delta x \quad (\text{Aproximación por exceso})$$

#### Encierro y Refinamiento:
Para toda partición regular se cumple la desigualdad de encierro:
$$L_n \le \int_0^2 x^2 \, dx \le U_n$$

Al ser $f$ creciente en $[a, b]$, la diferencia entre ambas aproximaciones (cota del error) se simplifica telescópicamente a:
$$U_n - L_n = (f(b) - f(a)) \cdot \Delta x = (4 - 0) \cdot \frac{2}{n} = \frac{8}{n}$$

Al refinar la partición haciendo que $n \to \infty$ (y por tanto $\Delta x \to 0$):
$$\lim_{n \to \infty} (U_n - L_n) = \lim_{n \to \infty} \frac{8}{n} = 0 \implies \lim_{n \to \infty} L_n = \lim_{n \to \infty} U_n = \int_0^2 x^2 \, dx = \frac{8}{3}$$
Así, el área buscada queda encerrada entre dos aproximaciones que convergen al mismo límite.

---


### 2. Versiones, Dependencias y Requisitos de Instalación

* **Python:** `3.13` (compatible con Python `3.10` a `3.13`).
* **Manim Community:** `0.22.0`
* **Dependencias directas (`requirements.txt`):**
  * `manim==0.22.0`
  * `numpy>=2.0.0`
  * `matplotlib>=3.9.0`
* **Dependencia del sistema:** **FFmpeg**
  * En Windows (PowerShell):
    ```powershell
    winget install Gyan.FFmpeg
    ```
  * En Linux (Ubuntu/Debian):
    ```bash
    sudo apt update && sudo apt install ffmpeg
    ```
  * En Arch Linux / CachyOS:
    ```bash
    sudo pacman -S ffmpeg cairo pango
    ```
  * En macOS:
    ```bash
    brew install ffmpeg
    ```

---

### 3. Instrucciones de Ejecución de las Escenas

Sigue estos pasos en la terminal desde la raíz del repositorio:

```bash
# 1. Crear el entorno virtual (recomendado)
python -m venv .venv

# 2. Activar el entorno virtual:
# En Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# En Linux / macOS:
source .venv/bin/activate

# 3. Instalar las dependencias exactas
pip install -r requirements.txt

# 4. Renderizar y visualizar la escena completa:
# Versión rápida de prueba (baja resolución, 480p, 15 fps):
manim -pql animacion_grupo12.py AnimacionGrupo12

# Versión final de entrega en Alta Definición (Full HD, 1080p, 60 fps):
manim -pqh animacion_grupo12.py AnimacionGrupo12
```

*(El archivo MP4 generado se guarda localmente en `media/videos/animacion_grupo12/1080p60/AnimacionGrupo12.mp4`).*

---

### 4. Verificación de los Cálculos

El script [`verificar_calculos.py`](verificar_calculos.py) comprueba automáticamente que todos los valores numéricos y propiedades matemáticas mostradas en el video sean exactos. Importa las funciones reales de [`animacion_grupo12.py`](animacion_grupo12.py) (`suma_inferior`, `suma_superior` y `AREA_EXACTA`), verificando el mismo código que genera la animación:

* Los valores de $L_n$ y $U_n$ de la tabla del video para $n = 4, 8, 16, 40$ y $100$.
* La desigualdad de encierro $L_n \le \frac{8}{3} \le U_n$ en cada partición.
* La identidad del error $U_n - L_n = (f(2) - f(0))\cdot \Delta x = \frac{8}{n}$.
* La monotonía ($L_n$ estrictamente creciente y $U_n$ estrictamente decreciente al refinar) y que al duplicar $n$ el error se reduce exactamente a la mitad.

Para ejecutar la verificación:

```bash
python verificar_calculos.py
```

---

### 5. Fuentes y Recursos Utilizados

1. **Apunte Base del Curso:**
   * Departamento de Matemática (2026). *Introducción a la integral: Apunte base común para el proyecto de investigación y visualización*. Cálculo Intermedio, Ingeniería Civil Informática. Disponible en este repositorio en [`docs/introduccion_integral.pdf`](docs/introduccion_integral.pdf).
2. **Fuentes Matemáticas Complementarias:**
   * Stewart, J. (2012). *Cálculo de una variable: Trascendentes tempranas* (7.ª ed., Cap. 5: Integrales, pp. 360–382). Cengage Learning. Referencia editorial: [https://www.cengage.com/](https://www.cengage.com/)
   * Spivak, M. (1994). *Calculus* (3.ª ed., Cap. 13: Integrales, sumas inferiores y superiores). Publish or Perish. Referencia de catálogo: [https://openlibrary.org/works/OL4531214W/Calculus](https://openlibrary.org/works/OL4531214W/Calculus)
3. **Documentación Oficial de Manim y Recursos Adaptados:**
   * The Manim Community Developers (2026). *Manim Community Edition Documentation (v0.22.0)*. Disponible en: [https://docs.manim.community/en/stable/](https://docs.manim.community/en/stable/)
   * Métodos principales consultados y adaptados de la documentación oficial para construir las escenas:
     * `Axes.get_riemann_rectangles`: [Documentación de CoordinateSystem.get_riemann_rectangles](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.CoordinateSystem.html#manim.mobject.graphing.coordinate_systems.CoordinateSystem.get_riemann_rectangles) (usado en el método propio `rectangulos()` para generar los rectángulos con `input_sample_type="left"` y `"right"`).
     * `Axes` y `NumberLine`: [Documentación de Graphing](https://docs.manim.community/en/stable/reference/manim.mobject.graphing.html) (usados para graficar $f(x)=x^2$ y representar dinámicamente el intervalo $[L_n, U_n]$).

---

### 6. Declaración de Uso de Inteligencia Artificial 

* **Herramientas:** Claude (Anthropic; en particular Claude Code) y Gemini (Google).
* **Finalidad y partes apoyadas:**
  * Claude y Gemini, con el mismo propósito: apoyar la estructuración de la sintaxis de Manim Community y el formato de la documentación (README y ficha), y corroborar y comparar entre ambas herramientas las respuestas y los resultados obtenidos.
  * Claude Code: escritura del script de verificación `verificar_calculos.py` y sus comentarios, revisión del proyecto frente a la pauta y la rúbrica del EID, y correcciones menores de comentarios y documentación.
* **Verificación:** los cálculos del ejemplo ($L_n$, $U_n$, $8/n$ y $8/3$) fueron revisados por los integrantes y se comprueban automáticamente con `verificar_calculos.py`. Las escenas se renderizaron y revisaron en el video final. El ejemplo, las explicaciones matemáticas y la narración son del grupo, y la IA no reemplazó las fuentes ni la comprensión del trabajo.



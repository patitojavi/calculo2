# Proyecto EID - Cálculo Intermedio (Grupo 12)
## Sumas Inferiores y Superiores: Aproximación y Refinamiento

Este repositorio contiene el código fuente, la investigación matemática y las animaciones desarrolladas con **Manim Community** para la Evaluación Integrada de Desempeño (EID) de Cálculo Intermedio.

---

### Pregunta Central Asignada
> **¿Cómo podemos encerrar el valor de una región entre dos aproximaciones?**

---

### 1. Resumen Teórico y Matemático

Para aproximar el área bajo una función no negativa $f(x)$ en un intervalo cerrado $[a, b]$, definimos una partición regular de $n$ subintervalos de ancho constante:
$$\Delta x = \frac{b - a}{n}, \quad x_i = a + i \cdot \Delta x$$

En nuestro proyecto utilizamos la función propia:
$$f(x) = x^2 \quad \text{en el intervalo } [0, 2]$$
Cuyo valor analítico exacto es:
$$\int_0^2 x^2 \, dx = \left[ \frac{x^3}{3} \right]_0^2 = \frac{8}{3} \approx 2.6667$$

#### Construcción de las Cotas:
Dado que $f(x) = x^2$ es estrictamente creciente en $[0, 2]$:
1. **Suma Inferior ($L_n$):** El mínimo en cada $[x_{i-1}, x_i]$ ocurre en el extremo izquierdo $x_{i-1}$:
   $$L_n = \sum_{i=1}^n f(x_{i-1}) \cdot \Delta x \quad (\text{Aproximación por defecto})$$
2. **Suma Superior ($U_n$):** El máximo en cada $[x_{i-1}, x_i]$ ocurre en el extremo derecho $x_i$:
   $$U_n = \sum_{i=1}^n f(x_i) \cdot \Delta x \quad (\text{Aproximación por exceso})$$

#### Encierro y Refinamiento:
Para toda partición regular se cumple estrictamente:
$$L_n \le \int_0^2 x^2 \, dx \le U_n$$

La diferencia entre ambas cotas viene dada por:
$$U_n - L_n = (f(b) - f(a)) \cdot \Delta x = (4 - 0) \cdot \frac{2}{n} = \frac{8}{n}$$

Al refinar la partición haciendo que $n \to \infty$:
$$\lim_{n \to \infty} (U_n - L_n) = 0 \implies \lim_{n \to \infty} L_n = \lim_{n \to \infty} U_n = \frac{8}{3}$$
El área buscada queda exactamente "encerrada" y determinada.

---

### 2. Guion del Video (Estructura de Voces)

| Sección | Tiempo Est. | Responsable | Contenido / Narración Matemática |
| :--- | :--- | :--- | :--- |
| **1. Introducción** | 0:00 - 0:45 | **Voz 1** | Presentación del grupo, tema y formulación de la pregunta central. Planteamiento del problema del área para $f(x) = x^2$. |
| **2. Construcción** | 0:45 - 2:00 | **Voz 2** | Definición de la partición ($n = 4, \Delta x = 0.5$). Cálculo de la suma inferior $L_4 = 1.75$ y la suma superior $U_4 = 3.75$. Muestra gráfica del encierro $L_4 \le \text{Área} \le U_4$. |
| **3. Refinamiento y Cierre**| 2:00 - 4:30 | **Voz 3** | Animación dinámica del refinamiento con $n = 8, 16, 40$ y $100$. Demostración de que el error tiende a cero ($\frac{8}{n} \to 0$). Respuesta formal a la pregunta central y créditos. |

---

### 3. Requisitos de Instalación

1. **Python 3.10 o superior** (Recomendado Python 3.12 / 3.13).
2. **FFmpeg** instalado en el sistema:
   * En Windows (PowerShell):
     ```powershell
     winget install Gyan.FFmpeg
     ```
   * En Linux (Ubuntu/Debian):
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
   * En macOS:
     ```bash
     brew install ffmpeg
     ```

---

### 4. Cómo ejecutar la animación

Sigue estos sencillos pasos en la terminal:

```bash
# 1. Crear el entorno virtual (recomendado)
python -m venv .venv

# 2. Activar el entorno virtual:
# En Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# En Linux / macOS:
source .venv/bin/activate

# 3. Instalar las dependencias
pip install -r requirements.txt

# 4. Renderizar y visualizar la animación
# Versión rápida de prueba (baja resolución, 480p):
manim -pql animacion_grupo12.py AnimacionGrupo12

# Versión final en Alta Definición (Full HD, 1080p):
manim -pqh animacion_grupo12.py AnimacionGrupo12
```

*(El video generado se guardará automáticamente en tu carpeta local dentro de `media/videos/animacion_grupo12/` sin subirse al repositorio de GitHub).*

---

### 5. Fuentes y Declaración de IA

* **Apunte Base:** *Introducción a la integral*, Cálculo Intermedio, Departamento de Matemática.
* **Bibliografía Complementaria:** 
  * Stewart, J. (2012). *Cálculo de una variable: Trascendentes tempranas* (7ma ed.). Cengage Learning.
  * Spivak, M. (1994). *Calculus* (3ra ed.). Publish or Perish.
* **Software:** [Manim Community v0.22.0](https://www.manim.community/)
* **Declaración de IA:** Se utilizó asistencia de IA como apoyo en la estructuración de la sintaxis de Manim Community y formato de documentación. Todos los cálculos matemáticos, justificaciones y scripts fueron revisados y verificados por los integrantes del grupo.

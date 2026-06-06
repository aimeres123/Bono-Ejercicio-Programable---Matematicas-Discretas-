<p align="center">
  <img src="https://lh4.googleusercontent.com/proxy/WNtyuTbDjnnITJFxg1dlI63L0jfIMRf0CIKg75VavFd3ameUuokpEiXIZvafO0UbA3rGKkhjDZ2HFtRWcGiPIn7Syd37PqnCrQuXFNHguRRPYm__safRJi9Q" alt="Logo Universidad Nacional de Colombia" width="400">
</p>

<h1 align="center">Bono de Programación - Matemáticas Discretas I</h1>
<p align="center"><b>Autor:</b> Aimer Esteban García Rojas</p>

---
# Bono de Programación: Problemas Generales de Conteo
**Universidad Nacional de Colombia - Sede Bogotá** **Asignatura:** Matemáticas Discretas I  
**Docente:** Jhoan Sebastian Tenjo García  
**Estudiante:** Aimer Esteban García Rojas  

---

## 1. Descripción General de la Actividad
Este repositorio contiene la solución computacional al bono de programación correspondiente al segundo corte de Matemáticas Discretas I. El objetivo central de la actividad es conectar los conceptos de combinatoria con el diseño de algoritmos generales, parametrizables y modulares. 

A diferencia de un script estático, estos 2 programas son herramientas donde el usuario puede ingresar variables dinámicas ($n, r$) y recibir un desglose del procedimiento, acompañado de un control de excepciones para mitigar datos inválidos.

Se seleccionaron y desarrollaron los siguientes componentes:
* **Problema 1:** Calculadora general de permutaciones y k-permutaciones.
* **Problema 2:** Calculadora general de combinaciones, identidades simétricas y Triángulo de Pascal.

---

## 2. Sustentación Matemática y Algorítmica

### PROBLEMA 1: Permutaciones y k-permutaciones
1. **Explicación:** Modela los escenarios en los cuales se desea calcular el número de formas de ordenar un subconjunto de $r$ objetos tomados a partir de un conjunto total de $n$ elementos distinguibles, donde **el orden de selección sí importa**.
2. **Fórmula combinatoria:** $$P(n, r) = \frac{n!}{(n-r)!}$$
3. **Algoritmo implementado:** Se estructuró una función central iterativa para el cálculo factorial. Al recibir los parámetros, el sistema calcula de manera independiente $n!$ y $(n-r)!$ utilizando ciclos acumuladores, realizando posteriormente una división entera exacta con el operador: `//`. Cuenta además con un benchmark para comparar el coste temporal de la recursión frente al ciclo iterativo (Requiere Espera).
4. **Análisis de Eficiencia:**
   * **Complejidad Temporal:** $\mathcal{O}(n)$. La función del factorial ejecuta un ciclo finito desde $2$ hasta $n$, realizando multiplicaciones consecutivas de complejidad lineal.
   * **Complejidad Espacial:** $\mathcal{O}(1)$ para el enfoque iterativo, ya que mantiene variables escalares fijas en memoria. El enfoque recursivo posee una complejidad espacial de $\mathcal{O}(n)$ debido al apilamiento en la pila de llamadas *Call Stack*.

### PROBLEMA 2: Combinaciones Simples y Triángulo de Pascal
1. **Explicación:** Modela los casos en los cuales se escogen $r$ elementos de un total de $n$ objetos disponibles sin que interese el orden en absoluto. Adicionalmente, mapea dichos coeficientes binomiales de forma coordinada con la construcción de las componentes indexadas del Triángulo de Pascal.
2. **Fórmulas y Principios:**
   * **Combinación Simple:** $\binom{n}{r} = \frac{n!}{r!(n-r)!}$
   * **Identidad de Simetría:** $\binom{n}{r} = \binom{n}{n-r}$.
   * **Fila $n$ de Pascal:** Construida mediante una lista por comprensión que itera $r$ desde $0$ hasta $n$: $\left[ \binom{n}{0}, \binom{n}{1}, \dots, \binom{n}{n} \right]$.
3. **Análisis de Eficiencia:**
   * **Complejidad Temporal:** $\mathcal{O}(n)$ para el cálculo de una combinación individual. No obstante, para la generación de la fila $n$ del Triángulo de Pascal, al calcular $n+1$ coeficientes correlativos, la complejidad global sube a **$\mathcal{O}(n^2)$**.
   * **Complejidad Espacial:** $\mathcal{O}(n)$ al requerir una estructura de datos lineal para almacenar y retornar los $n+1$ elementos que componen la fila solicitada.

---
## 3. Explicación del Algoritmo Principal
A continuación se detallan los fragmentos de código centrales encargados de procesar la lógica de ambos problemas, explicando el funcionamiento de sus bucles y operaciones:

### Lógica del Problema 1 (Permutaciones)
Se basa en un enfoque iterativo que previene el sobrecosto en memoria y un posible Stack Overflow asociado a la recursión tradicional. Su funcionamiento se divide en dos componentes:

1. **`factorial_iterativo(n)`:** Su objetivo es calcular el producto de todos los números enteros positivos desde 1 hasta $n$. 
   * **Bucle.** Inicializa una variable llamada `resultado` en 1. Luego, ejecuta un ciclo `for` que utiliza la función `range(2, n + 1)`. Esto genera una secuencia que arranca en 2 y termina exactamente en el número $n$. En cada iteración del bucle, el valor actual del índice `i` se multiplica por el valor acumulado en `resultado` (`resultado *= i`), actualizando su valor. Al terminar el ciclo, la función retorna el producto total acumulado.
2. **`calcular_permutacion(n, r)`:** Modela los escenarios donde el orden de selección sí importa.
   * **Procedimiento** Primero invoca una función que valida que los datos no sean negativos y que $r \le n$. Tras la validación, realiza dos llamadas independientes a la función anterior, una para calcular el factorial del conjunto total (`factorial_iterativo(n)`) y otra para el factorial de la diferencia (`factorial_iterativo(n - r)`). Finalmente, toma ambos resultados y ejecuta una división entera utilizando el operador `//`. Esto garantiza que la salida sea un número entero exacto.
```python
def factorial_iterativo(n):
    n = int(n)
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def calcular_permutacion(n, r):
    validar_n_y_r(n, r)
    n, r = int(n), int(r)
    return factorial_iterativo(n) // factorial_iterativo(n - r)
```
### Lógica del Problema 2 (Combinaciones y Pascal)
Este componente calcula los coeficientes binomiales y mapea la construcción de las componentes del Triángulo de Pascal:

1. **`calcular_combinacion(n, r)`:** Evalúa cuántos subconjuntos únicos de tamaño $r$ pueden extraerse de un total de $n$ objetos.
   * **Procedimiento.** La función calcula el numerador obteniendo el factorial de $n$. Luego, calcula el denominador multiplicando el factorial de la cantidad seleccionada (`factorial_iterativo(r)`) por el factorial de los elementos restantes (`factorial_iterativo(n - r)`). Al igual que en las permutaciones, concluye aplicando el operador de división entera `//` entre el numerador y el denominador consolidado, devolviendo el coeficiente exacto.
2. **`obtener_fila_pascal(n)`:** Se encarga de generar numéricamente la fila completa del Triángulo de Pascal correspondiente al nivel $n$.
   * **Bucle por Comprensión:** Utiliza una estructura de lista por comprensión (`[... for r in range(n + 1)]`), que actúa como un ciclo optimizado. Este bucle genera un índice `r` que va desde 0 hasta $n$ de forma consecutiva, haciendo un total de $n + 1$ elementos. En cada paso del ciclo, toma el valor de `r` actual, lo envía como parámetro a la función `calcular_combinacion(n, r)` y va almacenando cada resultado ordenadamente dentro de la lista que finalmente es retornada.

```python
def calcular_combinacion(n, r):
    n, r = int(n), int(r)
    numerador = factorial_iterativo(n)
    denominador = factorial_iterativo(r) * factorial_iterativo(n - r)
    return numerador // denominador

def obtener_fila_pascal(n):
    n = int(n)
    return [calcular_combinacion(n, r) for r in range(n + 1)]
```
---

## 4. Acceso al Código Fuente
Los scripts con sus respectivos pueden ser consultados directamente en los siguientes enlaces del repositorio:

* [Ver Código del Problema 1](https://github.com/aimeres123/Bono-Ejercicio-Programable---Matematicas-Discretas-/blob/main/Main_Bono_Matematicas_Discretas_Punto1.py)
* [Ver Código del Problema 2](https://github.com/aimeres123/Bono-Ejercicio-Programable---Matematicas-Discretas-/blob/main/Main_Bono_Matematicas_Discretas_Punto2.py)

---

## 5. Evidencias de las pruebas.
Para certificar la estabilidad de ambos sistemas ante casos ordinarios, valores extremos y entradas erróneas, se detallan las matrices de control de las pruebas integradas de cada script:

### Casos de Prueba - Problema 1 (Módulo de Permutaciones)
Casos ejecutados automáticamente mediante la **Opción 3** del menú:

| Prueba | Entrada ($n, r$) | Salida del Programa ($P(n,r)$) | Justificación y Tipo de Caso |
| :---: | :--- | :--- | :--- |
| **1** | `10, 3` | `720` | **Caso 1:** Parámetros enteros positivos ordinarios. |
| **2** | `20, 5` | `1860480` | **Caso 2:** Demuestra generalidad con resultados grandes. |
| **3** | `6, 6` | `720` | **Caso 3:** Límite máximo donde $r = n$ (permutación total). |
| **4** | `8, 0` | `1` | **Caso 4:** Límite mínimo donde $r = 0$. |
| **5** | `0, 0` | `1` Por definición $0!=1$ | **Caso 5:** Conjunto vacío. |

### Casos de Prueba - Problema 2 (Módulo de Combinaciones)
Casos ejecutados automáticamente mediante la **Opción 4** del menú:

| Prueba | Entrada ($n, r$) | Salida del Programa ($\binom{n}{r}$) | Justificación y Tipo de Caso |
| :---: | :--- | :--- | :--- |
| **1** | `10, 4` | `210` | **Caso 1:** Parámetros enteros positivos ordinarios. |
| **2** | `7, 7` | `1` | **Caso 2:** Límite máximo donde $r = n$. |
| **3** | `5, 0` | `1` | **Caso 3:** Límite mínimo donde $r = 0$. |
| **4** | `6, 2` | `15` | **Caso 4:** Evaluación de simetría con $\binom{6}{2} = \binom{6}{4}$. |
| **5** | `0, 0` | `1`  | **Caso 5:** Espacio muestral vacío. |

### Casos de Control de Errores y Sanitización (Común para ambos módulos)
Estrategias probadas mediante el ingreso de datos manual en las opciones interactivas:
* **Entrada:** `n = 5`, `r = 8` ($r > n$) $\rightarrow$ X `ValueError: r no puede ser mayor que n.` Manejo de Errores.
* **Entrada:** `n = -4`, `r = 2` (Valores negativos) $\rightarrow$ X `ValueError: n no puede ser negativo.` Validación del dominio.
* **Entrada:** `n = "hola"`, `r = 2` (Cadenas de texto) $\rightarrow$ X `ValueError: n debe ser un número entero.` Validación tipo.

---

## 6. Instrucciones de Instalación y Ejecución.

### Requisitos del Sistema
El proyecto fue construido utilizando únicamente la librería estándar de **Python 3.x**. No requiere dependencias de terceros o librerías externas.

---

### Opción 1: Ejecución Directa en Editores de Código
Esta es la alternativa recomendada si se prefiere interactuar visualmente con el entorno:
1. Descargue los archivos del repositorio de forma individual o descargue el ZIP completo.
2. Descomprima la carpeta en su equipo.
3. Abra su editor de código favorito como *Visual Studio Code* o *PyCharm* y seleccione **"Abrir Carpeta o Abrir Archivo"** apuntando al directorio donde se encuentran los archivos.
4. Abra cualquiera de los dos archivos (`problema1_permutaciones.py` o `problema2_combinaciones.py`) y presione el botón de **Run / Ejecutar** del entorno.

---

### Opción 2: Ejecución en Compilador Web
Si desea testear la lógica de forma inmediata sin descargar nada ni crear cuentas, se recomienda usar **OnlineGDB**.
1. Copie el código del archivo que desea probar (`problema1_permutaciones.py` o `problema2_combinaciones.py`).
2. Ingrese al compilador interactivo a través de este enlace directo para Python: [Compilador Python](https://www.onlinegdb.com/online_python_compiler)
3. Borre el código que viene por defecto en el editor, pegue el código y presione el botón verde **"Run"** o la tecla `F9`.
4. La consola se desplegará en la parte inferior.

---
## 7. Comentarios Finales.
A nivel académico y personal, hacer este bono de programación fue una excelente herramienta que me ayudó a comprender de una mejor manera el cómo se manejan las permutaciones y combinaciones. 

Poner las fórmulas en código me sirvió para ver de forma tangible el impacto que tiene el orden de selección dentro de un conjunto de datos y cómo un cambio conceptual tan sutil altera por completo el tamaño del resultado. Además, diseñar la lógica para comprobar la identidad de simetría y armar la fila del Triángulo de Pascal fueron retos interesantes, además interpretar tanto la complejidad temporal como espacial fue importante para entender cómo las matemáticas discretas se pueden aplicar directamente en la optimización de software y se demostró que el enfoque iterativo es mucho más eficiente que el recursivo en las pruebas.

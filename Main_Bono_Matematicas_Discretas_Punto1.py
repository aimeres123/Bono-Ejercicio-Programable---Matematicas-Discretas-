"""
Universidad Nacional de Colombia - Sede Bogotá
Matemáticas Discretas I
Docente: Jhoan Sebastian Tenjo García

PROBLEMA 1: Calculadora general de permutaciones y k-permutaciones
Autor: Aimer Esteban García Rojas
"""

import time

# ==============================================================================
# 1. VALIDACIÓN DE ENTRADAS Y CASOS ESPECIALES
# ==============================================================================

def validar_entero_no_negativo(valor, nombre_variable):
    """Verifica de forma estricta que la entrada sea un entero natural (N0)."""
    try:
        valor_entero = int(valor)
    except (ValueError, TypeError):
        raise ValueError(f"{nombre_variable} debe ser un número entero.")

    if valor_entero < 0:
        raise ValueError(f"{nombre_variable} no puede ser negativo.")
    return True


def validar_n_y_r(n, r):
    """Valida las restricciones de existencia para una k-permutación."""
    validar_entero_no_negativo(n, "n")
    validar_entero_no_negativo(r, "r")
    
    if int(r) > int(n):
        raise ValueError("r no puede ser mayor que n.")
    return True


# ==============================================================================
# 2. ALGORITMOS PARA FACTORIAL ITERATIVO Y RECURSIVO
# ==============================================================================

def factorial_iterativo(n):
    """
    Calcula n! mediante un ciclo acumulador lineal.
    Eficiencia: Temporal O(n) | Espacial O(1)
    """
    validar_entero_no_negativo(n, "n")
    n = int(n)
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def factorial_recursivo(n):
    """
    Calcula n! mediante llamadas recursivas.
    Eficiencia: Temporal O(n) | Espacial O(n) por la pila de llamadas.
    """
    n = int(n)
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)


def mostrar_procedimiento_factorial(n):
    """Muestra el desarrollo de n! dentro de una caja alineada dinámicamente."""
    validar_entero_no_negativo(n, "n")
    n = int(n)

    # 1. Definir el contenido interno de la caja de manera limpia
    linea_tit = f"Desarrollo de {n}!"
    if n == 0 or n == 1:
        linea_proc = f"Procedimiento: Por definición, {n}! = 1"
    else:
        desglose = " x ".join(str(i) for i in range(n, 0, -1))
        linea_proc = f"Procedimiento: {desglose}"
    linea_res = f"Resultado Final = {factorial_iterativo(n)}"

    # 2. Calcular el ancho máximo exacto basado únicamente en el contenido de texto
    ancho_contenido = max(len(linea_tit), len(linea_proc), len(linea_res))

    # 3. Renderizar la caja con un encuadre dinámico simétrico y perfecto
    print(f"\n  ┌─ {linea_tit.ljust(ancho_contenido, '─')} ─┐")
    print(f"  │  {linea_proc.ljust(ancho_contenido)}  │")
    print(f"  │  {linea_res.ljust(ancho_contenido)}  │")
    print(f"  └─ {'─' * ancho_contenido} ─┘")


# ==============================================================================
# 3. ALGORITMO DE PERMUTACIÓN Y DESGLOSE DE PROCEDIMIENTO
# ==============================================================================

def calcular_permutacion(n, r):
    """Aplica la fórmula P(n, r) = n! / (n - r)! usando división entera."""
    validar_n_y_r(n, r)
    n, r = int(n), int(r)
    return factorial_iterativo(n) // factorial_iterativo(n - r)


def mostrar_procedimiento_permutacion(n, r):
    """Imprime el desarrollo de P(n, r) dentro de una caja alineada dinámicamente."""
    validar_n_y_r(n, r)
    n, r = int(n), int(r)
    
    # 1. Definir las líneas de texto internas de manera limpia
    linea_tit = f"Desarrollo de la Permutación P({n}, {r})"
    linea_form = f"Fórmula: P({n}, {r}) = {n}! / ({n} - {r})!"
    linea_sub = f"Sustitución de factoriales: {factorial_iterativo(n)} / {factorial_iterativo(n - r)}"
    linea_res = f"Resultado Final = {calcular_permutacion(n, r)}"

    # 2. Encontrar la línea más larga para establecer el ancho exacto del contenido
    ancho_contenido = max(len(linea_tit), len(linea_form), len(linea_sub), len(linea_res))

    # 3. Renderizar la caja garantizando el mismo ancho exacto en todas sus secciones
    print(f"\n  ┌─ {linea_tit.ljust(ancho_contenido, '─')} ─┐")
    print(f"  │  {linea_form.ljust(ancho_contenido)}  │")
    print(f"  │  {linea_sub.ljust(ancho_contenido)}  │")
    print(f"  │  {linea_res.ljust(ancho_contenido)}  │")
    print(f"  └─ {'─' * ancho_contenido} ─┘")


# ==============================================================================
# 4.PRUEBAS Y COMPARATIVA DE EFICIENCIA
# ==============================================================================

def ejecutar_pruebas_obligatorias():
    """Ejecuta los casos de prueba solicitados explícitamente en la guía."""
    print("\n" + "="*60)
    print("    CASOS DE PRUEBA - PROBLEMA 1")
    print("="*60)
    
    casos_guia = [(10, 3),(20, 5),(6, 6),(8, 0),(0, 0)]
    
    for indice, (n, r) in enumerate(casos_guia, 1):
        print(f"\n▶ PRUEBA {indice}")
        mostrar_procedimiento_permutacion(n, r)


def evaluar_eficiencia_complejidad():
    """
    Comparación del tiempo de ejecución.
    """
    print("\n" + "="*60)
    print("    COMPARATIVA ITERATIVA VS RECURSIVA")
    print("="*60)
    print("ANÁLISIS TEÓRICO:")
    print(" • Iterativo: Usa un bucle simple. Mantiene una sola variable en memoria,")
    print("   por lo que su complejidad espacial es O(1).")
    print(" • Recursivo: Cada llamada se apila en la Call Stack esperando que la")
    print("   siguiente resuelva. Su complejidad espacial es O(n), lo que podría")
    print("   causar un 'Stack Overflow' con números excesivamente grandes.")
    
    VALOR_TEST = 15
    REPETICIONES = 10000000
    print(f"\nEJECUTANDO BENCHMARK")
    print(f"\nCorriendo {REPETICIONES} veces para n = {VALOR_TEST}):")
    
    # Medición del método Iterativo
    t_inicial = time.perf_counter()
    for _ in range(REPETICIONES):
        factorial_iterativo(VALOR_TEST)
    t_iterativo = time.perf_counter() - t_inicial

    # Medición del método Recursivo
    t_inicial = time.perf_counter()
    for _ in range(REPETICIONES):
        factorial_recursivo(VALOR_TEST)
    t_recursivo = time.perf_counter() - t_inicial

    print(f"  » Tiempo total Iterativo: {t_iterativo:.5f} segundos (Más rápido, evita sobrecosto de registros)")
    print(f"  » Tiempo total Recursivo: {t_recursivo:.5f} segundos (Más lento por manipulación de marcos de pila)")
    print("-" * 60)


# ==============================================================================
# 5. MENÚ INTERACTIVO COMPONENTAL
# ==============================================================================

def menu():
    while True:
        print("\n=================================================")
        print("    SISTEMA DE PERMUTACIONES (PROBLEMA 1)")
        print("=================================================")
        print("1. Calcular Factorial de un número n.")
        print("2. Calcular una Permutación P(n, r)")
        print("3. Ejecutar los 5 casos de prueba")
        print("4. Benchmark Factorial Iterativo vs Recursivo")
        print("0. Regresar / Salir")
        print("=================================================")
        
        opcion = input("\nSeleccione una opción (0-4): ").strip()

        if opcion == "1":
            while True:
                try:
                    n = input("Ingrese el número n para su factorial: ")
                    validar_entero_no_negativo(n, "n")
                    mostrar_procedimiento_factorial(n)
                    break
                except ValueError as error:
                    print(f"\n  X Error: {error} Inténtelo de nuevo.\n")

        elif opcion == "2":
            while True:
                try:
                    n = input("Ingrese n (Total de elementos): ")
                    r = input("Ingrese r (Elementos a ordenar): ")
                    validar_n_y_r(n, r)
                    mostrar_procedimiento_permutacion(n, r)
                    break
                except ValueError as error:
                    print(f"\n  X Error: {error} Inténtelo de nuevo.\n")

        elif opcion == "3":
            ejecutar_pruebas_obligatorias()

        elif opcion == "4":
            evaluar_eficiencia_complejidad()

        elif opcion == "0":
            print("\nSaliendo del módulo de permutaciones...")
            break
        else:
            print("\nX Opción inválida. Digite un número entre 0 y 4.")


if __name__ == "__main__":
    menu()
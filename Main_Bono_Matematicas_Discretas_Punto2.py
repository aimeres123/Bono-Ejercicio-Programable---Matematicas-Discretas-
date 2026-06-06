"""
Universidad Nacional de Colombia - Sede Bogotá
Matemáticas Discretas I
Docente: Jhoan Sebastian Tenjo García

PROBLEMA 2: Calculadora general de combinaciones, identidades y Triángulo de Pascal
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
    """Valida las restricciones de existencia para una combinación simple C(n, r)."""
    validar_entero_no_negativo(n, "n")
    validar_entero_no_negativo(r, "r")
    
    if int(r) > int(n):
        raise ValueError("r no puede ser mayor que n.")
    return True


# ==============================================================================
# 2. ALGORITMOS FACTORIAL Y COMBINATORIA
# ==============================================================================

def factorial_iterativo(n):
    """Calcula n! mediante un ciclo."""
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def calcular_combinacion(n, r):
    """Aplica la fórmula matemática C(n, r) = n! / (r! * (n - r)!)."""
    validar_n_y_r(n, r)
    n, r = int(n), int(r)
    numerador = factorial_iterativo(n)
    denominador = factorial_iterativo(r) * factorial_iterativo(n - r)
    return numerador // denominador


# ==============================================================================
# 3. LÓGICA DEL TRIÁNGULO DE PASCAL
# ==============================================================================

def obtener_fila_pascal(n):
    """Genera exclusivamente la fila n del Triángulo de Pascal usando combinaciones."""
    validar_entero_no_negativo(n, "n")
    n = int(n)
    return [calcular_combinacion(n, r) for r in range(n + 1)]


def mostrar_fila_pascal(n):
    """Imprime la fila n del Triángulo de Pascal."""
    validar_entero_no_negativo(n, "n")
    n = int(n)
    
    # 1. Definir textos
    linea_tit = f"Fila n = {n} del Triángulo de Pascal"
    linea_pasc = f"Resultado: {obtener_fila_pascal(n)}"
    
    # 2. Calcular ancho
    ancho_contenido = max(len(linea_tit), len(linea_pasc))
    
    # 3. Renderizar marco
    print(f"\n  ┌─ {linea_tit.ljust(ancho_contenido, '─')} ─┐")
    print(f"  │  {linea_pasc.ljust(ancho_contenido)}  │")
    print(f"  └─ {'─' * ancho_contenido} ─┘")


def mostrar_triangulo_pascal_completo(n):
    """Imprime todo el triángulo de Pascal hasta la fila n."""
    validar_entero_no_negativo(n, "n")
    n = int(n)
    
    filas = []
    for i in range(n + 1):
        filas.append(obtener_fila_pascal(i))
    
    print(f"\n // Triángulo de Pascal completo hasta la fila n = {n} \\ ")
    ultima_fila_str = " ".join(str(x) for x in filas[-1])
    ancho_maximo = max(len(ultima_fila_str), 40)
    
    for i, fila in enumerate(filas):
        fila_str = " ".join(str(x) for x in fila)
        print(f"Fila {str(i).ljust(2)}: {fila_str.center(ancho_maximo)}")


# ==============================================================================
# 4. DESGLOSE DE PROCEDIMIENTO Y VERIFICACIÓN DE IDENTIDADES
# ==============================================================================

def mostrar_procedimiento_combinacion(n, r):
    """Muestra C(n, r) y verifica automáticamente la identidad simétrica."""
    validar_n_y_r(n, r)
    n, r = int(n), int(r)
    
    # Calcular valores para la identidad
    res_directo = calcular_combinacion(n, r)
    res_simetrico = calcular_combinacion(n, n - r)
    identidad_valida = (res_directo == res_simetrico)

    # 1. Definir las líneas de texto
    linea_tit = f"Desarrollo de la Combinación C({n}, {r})"
    linea_form = f"Fórmula: C({n}, {r}) = {n}! / ({r}! * ({n} - {r})!)"
    linea_sub = f"Sustitución: {factorial_iterativo(n)} / ({factorial_iterativo(r)} * {factorial_iterativo(n - r)})"
    linea_res = f"Resultado Final = {res_directo}"
    linea_iden = f"Verificación Identidad C({n}, {r}) == C({n}, {n-r}) ──> {res_directo} == {res_simetrico} ({'CUMPLE' if identidad_valida else 'FALLA'})"

    # 2. Encontrar la línea más larga para establecer el ancho exacto del contenido
    ancho_contenido = max(len(linea_tit), len(linea_form), len(linea_sub), len(linea_res), len(linea_iden))

    # 3. Renderizar bordes
    print(f"\n  ┌─ {linea_tit.ljust(ancho_contenido, '─')} ─┐")
    print(f"  │  {linea_form.ljust(ancho_contenido)}  │")
    print(f"  │  {linea_sub.ljust(ancho_contenido)}  │")
    print(f"  │  {linea_res.ljust(ancho_contenido)}  │")
    print(f"  │  {linea_iden.ljust(ancho_contenido)}  │")
    print(f"  └─ {'─' * ancho_contenido} ─┘")


# ==============================================================================
# 5. PRUEBAS DE COMBINACIONES
# ==============================================================================

def ejecutar_pruebas():
    """Casos de prueba."""
    print("\n" + "="*60)
    print("    CASOS DE PRUEBA - PROBLEMA 2")
    print("="*60)
    
    casos_guia = [(10, 4), (7, 7), (5, 0), (6, 2), (0, 0)]
    
    for indice, (n, r) in enumerate(casos_guia, 1):
        print(f"\n▶ PRUEBA {indice}: Parámetros n = {n}, r = {r}")
        mostrar_procedimiento_combinacion(n, r)


# ==============================================================================
# 6. MENÚ
# ==============================================================================

def menu():
    while True:
        print("\n=================================================")
        print("    SISTEMA DE COMBINACIONES (PROBLEMA 2)")
        print("=================================================")
        print("1. Calcular Combinación C(n, r)")
        print("2. Generar fila n del Triángulo de Pascal")
        print("3. Generar todo el Triángulo de Pascal hasta fila n")
        print("4. Ejecutar los casos de prueba.")
        print("0. Regresar / Salir")
        print("=================================================")
        
        opcion = input("\nSeleccione una opción (0-4): ").strip()

        if opcion == "1":
            while True:
                try:
                    n = input("Ingrese n (Total de elementos): ")
                    r = input("Ingrese r (Elementos a seleccionar): ")
                    validar_n_y_r(n, r)
                    mostrar_procedimiento_combinacion(n, r)
                    break
                except ValueError as error:
                    print(f"\n  X Error: {error} Inténtelo de nuevo.\n")

        elif opcion == "2":
            while True:
                try:
                    n = input("Ingrese el número de la fila n a generar: ")
                    validar_entero_no_negativo(n, "n")
                    mostrar_fila_pascal(n)
                    break
                except ValueError as error:
                    print(f"\n  X Error: {error} Inténtelo de nuevo.\n")

        elif opcion == "3":
            while True:
                try:
                    n = input("Ingrese la fila máxima n para el Triángulo de Pascal: ")
                    validar_entero_no_negativo(n, "n")
                    mostrar_triangulo_pascal_completo(n)
                    break
                except ValueError as error:
                    print(f"\n  X Error: {error} Inténtelo de nuevo.\n")

        elif opcion == "4":
            ejecutar_pruebas()

        elif opcion == "0":
            print("\nSaliendo del módulo de combinaciones...")
            break
        else:
            print("\nX Opción inválida. Digite un número entre 0 y 4.")


if __name__ == "__main__":
    menu()
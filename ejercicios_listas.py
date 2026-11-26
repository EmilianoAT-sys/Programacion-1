"""Ejercicios de listas: sin repeticiones y calificaciones de estudiantes."""


def leer_entero(mensaje, minimo=1):
    """Pide un entero >= minimo hasta que el usuario lo escriba bien."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"  Debe ser un entero mayor o igual a {minimo}.")
        except ValueError:
            print("  Entrada no válida, escribe un número entero.")


def leer_numero(mensaje, minimo=None, maximo=None):
    """Pide un número (entero o decimal) dentro de un rango opcional."""
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"  Debe ser mayor o igual a {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"  Debe ser menor o igual a {maximo}.")
            else:
                return valor
        except ValueError:
            print("  Entrada no válida, escribe un número.")


def ejercicio1():
    print("\n--- Ejercicio 1: lista sin repeticiones ---")
    n = leer_entero("¿Cuántos números vas a capturar? ")
    originales = []
    for i in range(n):
        originales.append(leer_numero(f"  Número {i + 1}: "))

    sin_repetidos = []
    for numero in originales:
        if numero not in sin_repetidos:
            sin_repetidos.append(numero)

    print("\nLista original:      ", originales)
    print("Lista sin repetidos: ", sin_repetidos)


def ejercicio2():
    print("\n--- Ejercicio 2: calificaciones ---")
    n = leer_entero("¿Cuántos estudiantes? ")
    calificaciones = []
    for i in range(n):
        calificaciones.append(leer_numero(f"  Calificación del estudiante {i + 1}: ", 0, 100))

    promedio = sum(calificaciones) / n
    print(f"\nPromedio grupal: {promedio:.2f}")
    print("Estudiantes con calificación superior al promedio:")
    hay = False
    for i in range(n):
        if calificaciones[i] > promedio:
            print(f"  Estudiante {i + 1}: {calificaciones[i]}")
            hay = True
    if not hay:
        print("  Ninguno.")


def ejercicio3():
    print("\n--- Ejercicio 3: calificaciones con nombres (dos listas) ---")
    n = leer_entero("¿Cuántos estudiantes? ")
    nombres = []
    calificaciones = []
    for i in range(n):
        nombres.append(input(f"  Nombre del estudiante {i + 1}: ").strip())
        calificaciones.append(leer_numero(f"  Calificación de {nombres[i]}: ", 0, 100))

    promedio = sum(calificaciones) / n
    print(f"\nPromedio grupal: {promedio:.2f}")
    print("Estudiantes con calificación superior al promedio:")
    hay = False
    for i in range(n):
        if calificaciones[i] > promedio:
            print(f"  #{i + 1} {nombres[i]}: {calificaciones[i]}")
            hay = True
    if not hay:
        print("  Ninguno.")


def ejercicio4():
    print("\n--- Ejercicio 4: lista de elementos [nombre, calificación] ---")
    n = leer_entero("¿Cuántos estudiantes? ")
    alumnos = []
    for i in range(n):
        nombre = input(f"  Nombre del estudiante {i + 1}: ").strip()
        calificacion = leer_numero(f"  Calificación de {nombre}: ", 0, 100)
        alumnos.append([nombre, calificacion])

    total = 0
    for alumno in alumnos:
        total += alumno[1]
    promedio = total / n

    print(f"\nPromedio grupal: {promedio:.2f}")
    print("Estudiantes con calificación superior al promedio:")
    hay = False
    for i in range(n):
        if alumnos[i][1] > promedio:
            print(f"  #{i + 1} {alumnos[i][0]}: {alumnos[i][1]}")
            hay = True
    if not hay:
        print("  Ninguno.")


def main():
    while True:
        print("\n===== EJERCICIOS DE LISTAS =====")
        print("1. Lista sin repeticiones")
        print("2. Calificaciones (por número de estudiante)")
        print("3. Calificaciones con nombres (dos listas)")
        print("4. Calificaciones con lista [nombre, calificación]")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

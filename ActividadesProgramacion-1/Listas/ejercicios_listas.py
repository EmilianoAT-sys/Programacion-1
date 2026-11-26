# Ejercicios de listas

def ejercicio1():
    n = int(input("¿Cuántos números vas a capturar? "))
    lista = []
    for i in range(n):
        numero = int(input("Número: "))
        lista.append(numero)

    sin_repetir = []
    for numero in lista:
        if numero not in sin_repetir:
            sin_repetir.append(numero)

    print("Lista original:", lista)
    print("Lista sin repetidos:", sin_repetir)


def ejercicio2():
    n = int(input("¿Cuántos estudiantes? "))
    calificaciones = []
    for i in range(n):
        cal = float(input("Calificación del estudiante " + str(i + 1) + ": "))
        while True:
            if cal > 100 or cal < 0:
                print("la calificacion debe estar en el rango de entre 1-100")
                cal = float(input("Calificación del estudiante " + str(i + 1) + ": "))
            else:
                break
        calificaciones.append(cal)

    promedio = sum(calificaciones) / n
    print("Promedio grupal:", promedio)
    print("Estudiantes con calificación superior al promedio:")
    for i in range(n):
        if calificaciones[i] > promedio:
            print("Estudiante", i + 1, "- calificación:", calificaciones[i])


def ejercicio3():
    n = int(input("¿Cuántos estudiantes? "))
    nombres = []
    calificaciones = []
    for i in range(n):
        nombre = input("Nombre del estudiante " + str(i + 1) + ": ")
        while True:
            cal = float(input("Calificación de " + nombre + ": "))
            if cal > 100 or cal < 0:
                print("Error, la calificacion debe estar en un rango de 0-100")
                cal = float(input("Calificación de " + nombre + ": "))
            else:
                break
            nombres.append(nombre)
            calificaciones.append(cal)

    promedio = sum(calificaciones) / n
    print("Promedio grupal:", promedio)
    print("Estudiantes con calificación superior al promedio:")
    for i in range(n):
        if calificaciones[i] > promedio:
            print("Estudiante", i + 1, "-", nombres[i], "- calificación:", calificaciones[i])


def ejercicio4():
    n = int(input("¿Cuántos estudiantes? "))
    alumnos = []
    for i in range(n):
        nombre = input("Nombre del estudiante " + str(i + 1) + ": ")
        while True:
            cal = float(input("Calificación de " + nombre + ": "))
            if cal > 100 or cal < 1000:
                print("La calificacion debe estar entre 1-100, vuelve a asignar la calificacion")
                cal = float(input("Calificación de " + nombre + ": "))
            else:
                break
        alumnos.append([nombre, cal])

    suma = 0
    for alumno in alumnos:
        suma = suma + alumno[1]
    promedio = suma / n

    print("Promedio grupal:", promedio)
    print("Estudiantes con calificación superior al promedio:")
    for i in range(n):
        if alumnos[i][1] > promedio:
            print("Estudiante", i + 1, "-", alumnos[i][0], "- calificación:", alumnos[i][1])


# Programa principal
opcion = -1
while opcion != 0:
    print()
    print("1. Lista sin repeticiones")
    print("2. Calificaciones")
    print("3. Calificaciones con nombres (dos listas)")
    print("4. Calificaciones con lista [nombre, calificación]")
    print("0. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio3()
    elif opcion == 4:
        ejercicio4()
    elif opcion != 0:
        print("Opción no válida")

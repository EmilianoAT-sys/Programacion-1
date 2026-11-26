"""
Nombre del archivo:ejercicio3.py
Descripcion del ejercicio 2:Captura la calificación de n estudiantes y las almacene en una lista, calcula el promedio grupal e indica que estudiantes sacaron mejor que la calificacion grupal
descripcion: identico que el 2, con la lista de elementos de [nombre,calificacion]
Autor:Eduardo Emiliano Aguirre Toledo
fecha:
"""



# Ejercicio 4: igual al 2, con una lista de elementos [nombre, calificación]

n = int(input("¿Cuántos estudiantes? "))

alumnos = []
for i in range(n):
    nombre = input("Nombre del estudiante " + str(i + 1) + ": ")
    while True:
        cal = float(input("Calificación de " + nombre + ": "))
        if cal > 100 or cal < 0:
            print("las calificaciones deben estar entre el rango 0-100")
            cal = float(input("Calificación de " + nombre + ": "))
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

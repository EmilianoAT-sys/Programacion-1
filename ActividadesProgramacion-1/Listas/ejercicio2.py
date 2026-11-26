"""
Nombre del archivo:ejercicio2.py
Descripcion:Captura la calificación de n estudiantes y las almacene en una lista, calcula el promedio grupal
Autor:Eduardo Emiliano Aguirre Toledo
Fecha:
"""



n = int(input("¿Cuántos estudiantes? "))

calificaciones = []
for i in range(n):
    cal = float(input("Calificación del estudiante " + str(i + 1) + ": "))
    calificaciones.append(cal)

promedio = sum(calificaciones) / n
print("Promedio grupal:", promedio)

print("Estudiantes con calificación superior al promedio:")
for i in range(n):
    if calificaciones[i] > promedio:
        print("Estudiante", i + 1, "- calificación:", calificaciones[i])

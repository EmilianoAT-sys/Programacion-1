# Ejercicio 3: igual al 2, con los nombres en otra lista

n = int(input("¿Cuántos estudiantes? "))

nombres = []
calificaciones = []
for i in range(n):
    nombre = input("Nombre del estudiante " + str(i + 1) + ": ")
    cal = float(input("Calificación de " + nombre + ": "))
    nombres.append(nombre)
    calificaciones.append(cal)

promedio = sum(calificaciones) / n
print("Promedio grupal:", promedio)

print("Estudiantes con calificación superior al promedio:")
for i in range(n):
    if calificaciones[i] > promedio:
        print("Estudiante", i + 1, "-", nombres[i], "- calificación:", calificaciones[i])

# Ejercicio 1: lista sin repeticiones

n = int(input("¿Cuántos números vas a capturar? "))

lista = []
for i in range(n):
    numero = int(input("Número " + str(i + 1) + ": "))
    lista.append(numero)

sin_repetir = []
for numero in lista:
    if numero not in sin_repetir:
        sin_repetir.append(numero)

print("Lista original:", lista)
print("Lista sin repeticiones:", sin_repetir)

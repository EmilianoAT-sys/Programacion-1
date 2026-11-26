"""
Nombre del archivo:graficas_ordanamiento.py
Descrpcion:Programa que mediante una grafica de barras organiza en diferentes metodos de ordenamiento
Autor:Eduardo Emiliano Aguirre Toledo
Fecha:26/11/26
"""

import random


def graficar(lista):
    """
    Funcion que imprime la grafica de barras, con valores 
    """
    # Imprime las barras de forma vertical, de arriba (15) hacia abajo (1)
    for nivel in range(15, 0, -1):
        linea = ""
        for valor in lista:
            if valor >= nivel:
                linea = linea + "█  "
            else:
                linea = linea + "   "
        print(linea)
    # Imprime los valores debajo de las barras
    linea = ""
    for valor in lista:
        linea = linea + str(valor).ljust(3)
    print(linea)
    print()


def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                graficar(lista)


def insercion(lista):
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j - 1] > lista[j]:
            aux = lista[j]
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            graficar(lista)
            j = j - 1


def seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            aux = lista[i]
            lista[i] = lista[menor]
            lista[menor] = aux
            graficar(lista)


def quicksort(lista, inicio, fin):
    if inicio < fin:
        pivote = lista[fin]
        i = inicio
        for j in range(inicio, fin):
            if lista[j] < pivote:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                if i != j:
                    graficar(lista)
                i = i + 1
        aux = lista[i]
        lista[i] = lista[fin]
        lista[fin] = aux
        if i != fin:
            graficar(lista)
        quicksort(lista, inicio, i - 1)
        quicksort(lista, i + 1, fin)


# Programa principal
n = int(input("Tamaño del arreglo (entre 10 y 30): "))
while n < 10 or n > 30:
    n = int(input("Debe estar entre 10 y 30, intenta de nuevo: "))

original = []
for i in range(n):
    original.append(random.randint(1, 15))

print("Arreglo original:", original)
graficar(original)

opcion = -1
while opcion != 0:
    print("1. Burbuja")
    print("2. Inserción")
    print("3. Selección")
    print("4. Quicksort")
    print("0. Salir")
    opcion = int(input("Elige un método: "))

    lista = original[:]   # copia, para no perder el arreglo original

    if opcion == 1:
        burbuja(lista)
    elif opcion == 2:
        insercion(lista)
    elif opcion == 3:
        seleccion(lista)
    elif opcion == 4:
        quicksort(lista, 0, len(lista) - 1)
    elif opcion != 0:
        print("Opción no válida")

    if opcion >= 1 and opcion <= 4:
        print("Arreglo ordenado:", lista)

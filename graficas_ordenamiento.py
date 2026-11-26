"""Gráfica de barras de un arreglo aleatorio y animación de métodos de ordenamiento."""
import os
import random
import time

SIMBOLO = "█"
MAX_VALOR = 15
PAUSA = 0.08  # segundos entre cada paso de la animación

ROJO = "\033[91m"
VERDE = "\033[92m"
RESET = "\033[0m"

os.system("")  # activa los colores ANSI en la consola de Windows


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def leer_n():
    while True:
        try:
            n = int(input("Tamaño del arreglo n (10 <= n <= 30): "))
            if 10 <= n <= 30:
                return n
            print("  n debe estar entre 10 y 30.")
        except ValueError:
            print("  Escribe un número entero.")


def dibujar(arreglo, titulo="", resaltados=(), color=ROJO, pausa=0.0):
    """Imprime el arreglo como gráfica de barras vertical.
    Las posiciones en 'resaltados' se pintan de color."""
    if pausa > 0:
        limpiar_pantalla()
    if titulo:
        print(titulo)
    for nivel in range(MAX_VALOR, 0, -1):
        linea = ""
        for i, valor in enumerate(arreglo):
            if valor >= nivel:
                if i in resaltados:
                    linea += f"{color}{SIMBOLO}{SIMBOLO}{RESET} "
                else:
                    linea += f"{SIMBOLO}{SIMBOLO} "
            else:
                linea += "   "
        print(f"{nivel:>2} {linea}")
    print("   " + "".join(f"{v:<3}" for v in arreglo))
    if pausa > 0:
        time.sleep(pausa)


# ---------------- Métodos de ordenamiento ----------------

def burbuja(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                dibujar(arr, "Burbuja", (j, j + 1), ROJO, PAUSA)


def insercion(arr):
    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > actual:
            arr[j + 1] = arr[j]
            arr[j] = actual  # el elemento se ve "viajando" hacia su lugar
            dibujar(arr, "Inserción", (j,), ROJO, PAUSA)
            j -= 1
        arr[j + 1] = actual


def seleccion(arr):
    n = len(arr)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if arr[j] < arr[minimo]:
                minimo = j
        if minimo != i:
            arr[i], arr[minimo] = arr[minimo], arr[i]
            dibujar(arr, "Selección", (i, minimo), ROJO, PAUSA)


def quicksort(arr, inicio=0, fin=None):
    if fin is None:
        fin = len(arr) - 1
    if inicio >= fin:
        return
    pivote = arr[fin]
    i = inicio
    for j in range(inicio, fin):
        if arr[j] < pivote:
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                dibujar(arr, "Quicksort", (i, j), ROJO, PAUSA)
            i += 1
    if i != fin:
        arr[i], arr[fin] = arr[fin], arr[i]
        dibujar(arr, "Quicksort (pivote colocado)", (i,), VERDE, PAUSA)
    quicksort(arr, inicio, i - 1)
    quicksort(arr, i + 1, fin)


def main():
    n = leer_n()
    original = [random.randint(1, MAX_VALOR) for _ in range(n)]

    print("\nArreglo generado:", original)
    dibujar(original, "Gráfica de barras del arreglo original")

    while True:
        print("\n===== MÉTODOS DE ORDENAMIENTO =====")
        print("1. Burbuja")
        print("2. Inserción")
        print("3. Selección")
        print("4. Quicksort")
        print("5. Generar un nuevo arreglo")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion in ("1", "2", "3", "4"):
            copia = original[:]  # siempre se ordena una copia del original
            if opcion == "1":
                burbuja(copia)
            elif opcion == "2":
                insercion(copia)
            elif opcion == "3":
                seleccion(copia)
            else:
                quicksort(copia)
            dibujar(copia, "Arreglo ordenado")
        elif opcion == "5":
            n = leer_n()
            original = [random.randint(1, MAX_VALOR) for _ in range(n)]
            print("\nArreglo generado:", original)
            dibujar(original, "Gráfica de barras del arreglo original")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

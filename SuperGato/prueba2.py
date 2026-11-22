def crear_tablero_3x3(valor=None):
    return [[valor for _ in range(3)] for _ in range(3)]


def crear_ultimate_board():
    # tablero[mr][mc][r][c]
    tablero = [
        [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
        for _ in range(3)
    ]
    meta = crear_tablero_3x3(None)
    return tablero, meta


def revisar_ganador_3x3(grid):
    # Filas y columnas
    for i in range(3):
        if grid[i][0] in ("X", "O") and grid[i][0] == grid[i][1] == grid[i][2]:
            return grid[i][0]
        if grid[0][i] in ("X", "O") and grid[0][i] == grid[1][i] == grid[2][i]:
            return grid[0][i]

    # Diagonales
    if grid[0][0] in ("X", "O") and grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]
    if grid[0][2] in ("X", "O") and grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]

    # Empate si no hay celdas None
    if all(grid[r][c] is not None for r in range(3) for c in range(3)):
        return "E"

    return None


def mostrar_tablero(tablero, meta, siguiente_sub):
    print("\n=== ULTIMATE TIC-TAC-TOE ===")
    for mr in range(3):
        for r in range(3):
            fila_str = []
            for mc in range(3):
                estado_sub = meta[mr][mc]
                sub_cells = []
                for c in range(3):
                    val = tablero[mr][mc][r][c]
                    if estado_sub in ("X", "O"):
                        # Muestra el ganador grande si el subtablero ya está decidido
                        sub_cells.append(estado_sub if (r, c) == (1, 1) else ".")
                    else:
                        sub_cells.append(val if val is not None else ".")
                marcador = "*" if siguiente_sub == (mr, mc) else " "
                fila_str.append(f"{marcador}{' '.join(sub_cells)}")
            print("  |  ".join(fila_str))
        if mr < 2:
            print("-" * 35)


def es_movimiento_valido(tablero, meta, siguiente_sub, mr, mc, r, c):
    if not (0 <= mr < 3 and 0 <= mc < 3 and 0 <= r < 3 and 0 <= c < 3):
        return False, "Coordenadas fuera de rango (0 a 2)."

    if siguiente_sub is not None and (mr, mc) != siguiente_sub:
        return False, f"Debes jugar en el subtablero {siguiente_sub}."

    if meta[mr][mc] is not None:
        return False, "Ese subtablero ya terminó."

    if tablero[mr][mc][r][c] is not None:
        return False, "Esa casilla ya está ocupada."

    return True, ""


def jugar():
    tablero, meta = crear_ultimate_board()
    turno = "X"
    siguiente_sub = None  # None significa libertad para elegir subtablero

    while True:
        mostrar_tablero(tablero, meta, siguiente_sub)
        if siguiente_sub is None:
            print(f"\nTurno de {turno}. Puedes elegir CUALQUIER subtablero activo.")
        else:
            print(f"\nTurno de {turno}. Debes jugar en el subtablero {siguiente_sub}.")

        try:
            entrada = input("Ingresa mr mc r c (ej. 1 1 0 2): ").strip().split()
            if len(entrada) != 4:
                print("Ingresa exactamente 4 números separados por espacio.")
                continue
            mr, mc, r, c = map(int, entrada)
        except ValueError:
            print("Entrada inválida. Usa números enteros del 0 al 2.")
            continue

        valido, msg = es_movimiento_valido(tablero, meta, siguiente_sub, mr, mc, r, c)
        if not valido:
            print("Movimiento no válido:", msg)
            continue

        # Colocar ficha
        tablero[mr][mc][r][c] = turno

        # Verificar si se ganó o empató el subtablero actual
        resultado_sub = revisar_ganador_3x3(tablero[mr][mc])
        if resultado_sub is not None:
            meta[mr][mc] = resultado_sub
            if resultado_sub in ("X", "O"):
                print(f"¡{resultado_sub} ganó el subtablero ({mr}, {mc})!")
            else:
                print(f"El subtablero ({mr}, {mc}) quedó en empate.")

        # Verificar victoria global
        ganador_global = revisar_ganador_3x3(meta)
        if ganador_global in ("X", "O"):
            mostrar_tablero(tablero, meta, None)
            print(f"\n¡GANADOR DEL JUEGO: {ganador_global}!")
            break
        elif ganador_global == "E":
            mostrar_tablero(tablero, meta, None)
            print("\n¡El juego terminó en empate global!")
            break

        # Actualizar siguiente subtablero
        if meta[r][c] is not None:
            siguiente_sub = None
        else:
            siguiente_sub = (r, c)

        turno = "O" if turno == "X" else "X"


if __name__ == "__main__":
    jugar()
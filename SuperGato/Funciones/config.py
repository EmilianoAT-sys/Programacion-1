"""
Nombre del archivo: config.py
Descripción: Constantes compartidas por todo el juego (colores, tamaños y valores de jugadores).
Nombre de los autores: Juan Pablo Salcido Valenzuela y Eduardo Emiliano Aguirre Toledo
Fecha: 12/11/26
"""

# --- Valores que se guardan en las matrices del juego ---
VACIO = 0
JUGADOR_X = 1
JUGADOR_O = 2
EMPATE = 3

SIMBOLOS = {JUGADOR_X: "X", JUGADOR_O: "O"}

# --- Colores ---
COLOR_VENTANA = "#1fAfa1"
COLOR_X = "#bf0000"
COLOR_O = "#0000bf"
COLORES_JUGADOR = {JUGADOR_X: COLOR_X, JUGADOR_O: COLOR_O}

COLOR_FONDO_TABLERO = "#ffffff"    # zonas donde NO se puede jugar
COLOR_RESALTADO = "#999999"          # zonas donde SÍ se puede jugar
COLOR_GATO_TERMINADO = "#ffffff"   # gato ya ganado o empatado

# --- Tamaños (en pixeles) ---
TAM_CELDA = 50
TAM_GATO = TAM_CELDA * 3
TAM_TABLERO = TAM_GATO * 3

# --- Ventana ---
TAM_VENTANA = "800x600"

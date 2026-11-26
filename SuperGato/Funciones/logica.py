"""
Nombre del archivo: logica.py
Descripción: Reglas del Ultimate Tic Tac Toe. No usa tkinter, solo maneja el estado del juego.
Nombre de los autores: Juan Pablo Salcido Valenzuela y Eduardo Emiliano Aguirre Toledo
Fecha: 12/11/26
"""

import numpy as np

from config import VACIO, JUGADOR_X, JUGADOR_O, EMPATE


def hay_linea(tablero, jugador):
    """Revisa si el jugador tiene 3 en línea (fila, columna o diagonal) en un tablero 3x3."""
    for i in range(3):
        if np.all(tablero[i, :] == jugador) or np.all(tablero[:, i] == jugador):
            return True
    return bool(
        np.all(np.diag(tablero) == jugador)
        or np.all(np.diag(np.fliplr(tablero)) == jugador)
    )


class JuegoSuperGato:
    """
    Estado del juego.

    celdas[fila_gato, col_gato, fila, col] -> contenido de cada casilla
    gatos[fila_gato, col_gato]             -> VACIO, JUGADOR_X, JUGADOR_O o EMPATE
    """

    def __init__(self):
        self.reiniciar()

    def reiniciar(self):
        self.celdas = np.zeros((3, 3, 3, 3), dtype=int)
        self.gatos = np.zeros((3, 3), dtype=int)
        self.turno = JUGADOR_X
        self.gato_obligado = None   # (fila_gato, col_gato) o None si puede elegir
        self.ganador = None         # None mientras se juega; JUGADOR_X, JUGADOR_O o EMPATE al final

    # ------------------------------------------------------------------
    def gatos_jugables(self):
        """Lista de gatos (fila, col) donde el jugador en turno puede colocar ficha."""
        if self.ganador is not None:
            return []
        if self.gato_obligado is not None:
            return [self.gato_obligado]
        return [(f, c) for f in range(3) for c in range(3) if self.gatos[f, c] == VACIO]

    def jugada_valida(self, fila_gato, col_gato, fila, col):
        return (
            (fila_gato, col_gato) in self.gatos_jugables()
            and self.celdas[fila_gato, col_gato, fila, col] == VACIO
        )

    # ------------------------------------------------------------------
    def jugar(self, fila_gato, col_gato, fila, col):
        """
        Intenta colocar la ficha del jugador en turno.
        Devuelve False si la jugada no es válida, True si se realizó.
        """
        if not self.jugada_valida(fila_gato, col_gato, fila, col):
            return False

        jugador = self.turno
        self.celdas[fila_gato, col_gato, fila, col] = jugador

        self._evaluar_gato(fila_gato, col_gato, jugador)
        self._evaluar_partida(jugador)

        # La casilla jugada decide el siguiente gato; si ese ya está cerrado, elige libre.
        if self.gatos[fila, col] != VACIO:
            self.gato_obligado = None
        else:
            self.gato_obligado = (fila, col)

        self.turno = JUGADOR_O if jugador == JUGADOR_X else JUGADOR_X
        return True

    # ------------------------------------------------------------------
    def _evaluar_gato(self, fila_gato, col_gato, jugador):
        celdas = self.celdas[fila_gato, col_gato]
        if hay_linea(celdas, jugador):
            self.gatos[fila_gato, col_gato] = jugador
        elif np.all(celdas != VACIO):
            self.gatos[fila_gato, col_gato] = EMPATE

    def _evaluar_partida(self, jugador):
        if hay_linea(self.gatos, jugador):
            self.ganador = jugador
        elif np.all(self.gatos != VACIO):
            self.ganador = EMPATE

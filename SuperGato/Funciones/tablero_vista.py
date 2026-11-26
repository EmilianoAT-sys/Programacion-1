"""
Nombre del archivo: tablero_vista.py
Descripción: Dibujo del tablero 9x9 en un Canvas de tkinter (líneas, fichas, gatos terminados y zona jugable).
Nombre de los autores: Juan Pablo Salcido Valenzuela y Eduardo Emiliano Aguirre Toledo
Fecha: 12/11/26
"""

import tkinter as tk

from config import (
    EMPATE, SIMBOLOS, COLORES_JUGADOR,
    COLOR_FONDO_TABLERO, COLOR_RESALTADO, COLOR_GATO_TERMINADO,
    TAM_CELDA, TAM_GATO, TAM_TABLERO,
)


class TableroVista(tk.Canvas):
    def __init__(self, master, al_hacer_clic):
        """
        al_hacer_clic(fila_gato, col_gato, fila, col) se llama cada vez que
        el usuario hace clic en una casilla.
        """
        super().__init__(
            master,
            width=TAM_TABLERO,
            height=TAM_TABLERO,
            highlightthickness=0,
            bg=COLOR_FONDO_TABLERO,
        )
        self.al_hacer_clic = al_hacer_clic
        self._dibujar_lineas()
        self.activar_clics()

    # --- Clics ---------------------------------------------------------
    def activar_clics(self):
        self.bind("<Button-1>", self._procesar_clic)

    def desactivar_clics(self):
        self.unbind("<Button-1>")

    def _procesar_clic(self, evento):
        columna = evento.x // TAM_CELDA
        fila = evento.y // TAM_CELDA
        self.al_hacer_clic(fila // 3, columna // 3, fila % 3, columna % 3)

    # --- Dibujo --------------------------------------------------------
    def _dibujar_lineas(self):
        for pos in range(TAM_CELDA, TAM_TABLERO, TAM_CELDA):
            grosor = 5 if pos % TAM_GATO == 0 else 2
            self.create_line(pos, 0, pos, TAM_TABLERO, width=grosor, fill="black")
            self.create_line(0, pos, TAM_TABLERO, pos, width=grosor, fill="black")

    def limpiar(self):
        """Borra todo menos las líneas del tablero."""
        self.delete("ficha", "gato_terminado", "resaltado")

    def dibujar_ficha(self, fila_gato, col_gato, fila, col, jugador):
        x = col_gato * TAM_GATO + col * TAM_CELDA + TAM_CELDA // 2
        y = fila_gato * TAM_GATO + fila * TAM_CELDA + TAM_CELDA // 2
        self.create_text(
            x, y,
            text=SIMBOLOS[jugador],
            font=("Arial", 35, "bold"),
            fill=COLORES_JUGADOR[jugador],
            tags="ficha",
        )

    def dibujar_gato_terminado(self, fila_gato, col_gato, resultado):
        """Tapa un gato ya ganado (con la letra del ganador) o empatado (con '=')."""
        x1 = col_gato * TAM_GATO
        y1 = fila_gato * TAM_GATO
        self.create_rectangle(
            x1, y1, x1 + TAM_GATO, y1 + TAM_GATO,
            fill=COLOR_GATO_TERMINADO, outline="", tags="gato_terminado",
        )
        if resultado == EMPATE:
            texto, color = "=", "white"
        else:
            texto, color = SIMBOLOS[resultado], COLORES_JUGADOR[resultado]
        self.create_text(
            x1 + TAM_GATO // 2, y1 + TAM_GATO // 2,
            text=texto, fill=color,
            font=("Arial", 150, "bold"), tags="gato_terminado",
        )

    def resaltar(self, gatos_jugables):
        """Pinta de blanco los gatos donde el jugador puede colocar su ficha."""
        self.delete("resaltado")
        for fila_gato, col_gato in gatos_jugables:
            x1 = col_gato * TAM_GATO
            y1 = fila_gato * TAM_GATO
            self.create_rectangle(
                x1, y1, x1 + TAM_GATO, y1 + TAM_GATO,
                fill=COLOR_RESALTADO, outline="", tags="resaltado",
            )
        # Que quede debajo de las líneas y de las fichas
        self.tag_lower("resaltado")

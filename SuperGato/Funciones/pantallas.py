"""
Nombre del archivo: pantallas.py
Descripción: Las tres pantallas del programa: menú, reglas y juego.
Nombre de los autores: Juan Pablo Salcido Valenzuela y Eduardo Emiliano Aguirre Toledo
Fecha: 12/11/26
"""

import tkinter as tk

from config import (
    VACIO, EMPATE, SIMBOLOS, COLORES_JUGADOR, COLOR_VENTANA,
)
from logica import JuegoSuperGato
from tablero_vista import TableroVista

TEXTO_REGLAS = (
    "REGLAS DEL ULTIMATE TIC TAC TOE\n\n"
    "1. El tablero es un cuadrado de 9x9, formado por 9 gatos convencionales.\n"
    "2. El primer jugador (X u O) puede colocar su ficha en cualquiera de los 9 gatos.\n"
    "3. La casilla donde coloques tu ficha decide en qué gato jugará el rival.\n"
    "3.1 Ej: si O coloca su ficha en la esquina inferior izquierda de cualquier gato, "
    "X debe jugar en el gato inferior izquierdo.\n"
    "4. Quien gana un gato se queda con esa área. Si te mandan a un gato ya ganado o "
    "lleno, puedes jugar en cualquiera de los gatos disponibles.\n"
    "5. Gana quien consiga 3 gatos en línea (horizontal, vertical o diagonal).\n\n"
    "Las zonas en blanco indican dónde puedes colocar tu ficha."
)


class PantallaMenu(tk.Frame):
    def __init__(self, master, ir_a_juego, ir_a_reglas, salir):
        super().__init__(master, bg=COLOR_VENTANA)
        tk.Label(
            self,
            text=" Bienvenido a Ultimate TicTacToe\n\n",
            font=("arial", 20, "bold"),
            bg=COLOR_VENTANA,
        ).pack()

        botones = [
            ("JUGAR", ir_a_juego, 20, 10),
            ("Reglas", ir_a_reglas, 20, 10),
            ("salir", salir, 16, 20),
        ]
        for texto, comando, tamano, margen in botones:
            tk.Button(
                self, text=texto, command=comando,
                bg="white", font=("arial", tamano),
            ).pack(pady=margen)


class PantallaReglas(tk.Frame):
    def __init__(self, master, ir_a_menu):
        super().__init__(master, bg=COLOR_VENTANA)
        tk.Message(
            self, text=TEXTO_REGLAS, font=("arial", 17), bg=COLOR_VENTANA,
        ).pack(fill="both", expand=True)
        tk.Button(
            self, text="Regresar al menu", command=ir_a_menu,
            bg=COLOR_VENTANA, font=("arial", 16),
        ).pack(pady=10)


class PantallaJuego(tk.Frame):
    TITULO = "Ultimate Tic Tac Toe"

    def __init__(self, master, ir_a_menu):
        super().__init__(master)
        self.juego = JuegoSuperGato()

        self.tablero = TableroVista(self, self._al_hacer_clic)
        self.tablero.pack()

        self.etiqueta = tk.Label(self, text=self.TITULO, font=("arial", 20))
        self.etiqueta.pack()

        tk.Button(
            self, text="Regresar al menu", command=ir_a_menu,
            bg="#444444", font=("arial", 16),
        ).pack()

        self.nueva_partida()

    def nueva_partida(self):
        self.juego.reiniciar()
        self.tablero.limpiar()
        self.tablero.activar_clics()
        self._actualizar_vista()

    # ------------------------------------------------------------------
    def _al_hacer_clic(self, fila_gato, col_gato, fila, col):
        if not self.juego.jugar(fila_gato, col_gato, fila, col):
            return  # jugada inválida: se ignora

        jugador = self.juego.celdas[fila_gato, col_gato, fila, col]
        self.tablero.dibujar_ficha(fila_gato, col_gato, fila, col, jugador)

        estado_gato = self.juego.gatos[fila_gato, col_gato]
        if estado_gato != VACIO:
            self.tablero.dibujar_gato_terminado(fila_gato, col_gato, estado_gato)

        self._actualizar_vista()

    def _actualizar_vista(self):
        """Actualiza zona jugable, color de fondo y texto según el estado del juego."""
        juego = self.juego
        self.tablero.resaltar(juego.gatos_jugables())

        if juego.ganador is None:
            color = COLORES_JUGADOR[juego.turno]
            texto = self.TITULO
        else:
            self.tablero.desactivar_clics()
            if juego.ganador == EMPATE:
                color, texto = COLOR_VENTANA, "Fue empate"
            else:
                color = COLORES_JUGADOR[juego.ganador]
                texto = f"Ganó {SIMBOLOS[juego.ganador]}"

        self.config(bg=color)
        self.etiqueta.config(text=texto, bg=color)

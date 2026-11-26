"""
Nombre del archivo: main.py
Descripción: Punto de entrada del Ultimate Tic Tac Toe. Crea la ventana y cambia entre pantallas.
             Ejecutar con:  python main.py
Nombre de los autores: Juan Pablo Salcido Valenzuela y Eduardo Emiliano Aguirre Toledo
Fecha: 12/11/26
"""

import tkinter as tk

from config import TAM_VENTANA
from pantallas import PantallaMenu, PantallaReglas, PantallaJuego


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ultimate Tic Tac Toe")
        self.geometry(TAM_VENTANA)
        self.resizable(False, False)

        self.pantallas = {
            "menu": PantallaMenu(self, self.ir_a_juego, self.ir_a_reglas, self.destroy),
            "reglas": PantallaReglas(self, self.ir_a_menu),
            "juego": PantallaJuego(self, self.ir_a_menu),
        }
        self.pantalla_actual = None
        self.ir_a_menu()

    def mostrar(self, nombre):
        if self.pantalla_actual is not None:
            self.pantalla_actual.pack_forget()
        self.pantalla_actual = self.pantallas[nombre]
        self.pantalla_actual.pack(fill="both", expand=True)

    def ir_a_menu(self):
        self.mostrar("menu")

    def ir_a_reglas(self):
        self.mostrar("reglas")

    def ir_a_juego(self):
        juego = self.pantallas["juego"]
        if juego.juego.ganador is not None:   # si la partida ya terminó, empieza una nueva
            juego.nueva_partida()
        self.mostrar("juego")


if __name__ == "__main__":
    App().mainloop()

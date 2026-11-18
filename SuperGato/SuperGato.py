"""
Nombre del archivo: UltimateTicTacToe.py
Descripción: Este archivo contiene la clase gato, que representa un gato pero con un tablero con tamaño 9x9 conformado por 9 gatos.
Nombre de los autores:Juan Pablo Salcido Valenzuela y Eduardo Emiliano Aguirre Toledo
Fecha:12/11/26
"""
import tkinter as tk
import numpy as np

def Reglamento():
    """
    Reglas del juego
    """
    ventanareglas =tk.Toplevel(ventana)
    ventana.title("Reglas del juego")
    texto=tk.Message(ventanareglas,text="REGLAS DEL ULTIMATE TIC TAC TOE\n\n"
                            "1. El tablero es un cuadrado de  un tamaño total de 9x9,distribuidos por 9 gatos convencionales en total\n"
                            "2.El primer jugador en colocar su ficha (sea 0, o X) puede decidir donde  colocarla cualquiera de los 9 tableros\n"
                            "3.En el lugar donde coloque el jugador su ficha es en el tablero donde se jugara la sig jugada\n"
                            "3.1 Ej:Jugador 0 coloco su ficha en el tablero del medio y coloco su ficha en la izquierda inferior, el jugador X debe colocar su ficha en el tablero de la izquierda inferior en cualquier lugar posible\n"
                            "4.El jugador en ganar un tablero,gana en esa area, ya una bez un area sea ganada o llenada, si a uno de los dos jugadores se les envia a ese tablero,puede colocar en cualquiera de los tableros disponibles\n"
                            "5.Gana el que haya ganado 3 tableros cuyas victorias trazen una linea (horizontal o vertical)",
                            bg=COLOR_VENTANA,
                            font=("arial",12))
    texto.pack()
    ventanareglas.mainloop()
#Caracteristicas de la ventana del supergato  
ventana = tk.Tk()
COLOR_VENTANA = "#1fAfa1"
ventana.config(bg=COLOR_VENTANA)
ventana.geometry("500x600")

titulo = tk.Label(text="Ultimate Tic Tac Toe",
                  bg = COLOR_VENTANA,
                  font= ("arial", 15, "bold"))
titulo.pack()
jugar =tk.Button(text="JUGAR",
                bg="white",
                font=("arial",20)
                )
jugar.pack()
Reglas=tk.Button(text="Reglas",
                bg="white",
                font=("arial",20,),
                command = Reglamento)
Reglas.pack()


ventana.mainloop()
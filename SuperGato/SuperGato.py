"""
Nombre del archivo: UltimateTicTacToe.py
Descripción: Este archivo contiene la clase gato, que representa un gato pero con un tablero con tamaño 9x9 conformado por 9 gatos.
Nombre de los autores:Juan Pablo Salcido Valenzuela y Eduardo Emiliano Aguirre Toledo
Fecha:12/11/26
"""
import tkinter as tk
import numpy as np

tablero=np.zeros((9,3,3),dtype=int)
print(tablero)
turno="X"


#a = np.array([[1, 2, 3],
#              [4, 5, 6]])
#print(a.shape)
#b=np.array([1,2,3,4,5,6,7,8,9,10])
#b[0] = 10
#print(b[:3])
#print(a)
COLOR_VENTANA = "#1fAfa1"
def Colocar_usuario(event):
    if clic_usuario

def reglas():
    frameMenu.pack_forget()
    frameReglas.pack(fill="both",expand=True)
    textoReglas.pack(fill="both",expand=True)
    
def Menu():
    frameJuego.pack_forget()
    frameReglas.pack_forget()
   
    frameMenu.pack(fill="both",expand=True)

def jugar():
    frameMenu.pack_forget()
    frameJuego.pack(fill="both",expand=True)
    

ventana = tk.Tk()
ventana.geometry("800x600")
ventana.resizable(False,False)
frameMenu=tk.Frame(ventana)
frameMenu.config(bg=COLOR_VENTANA
                )   
textomenu = tk.Label(frameMenu,
                    text=" Bienvenido a Ultimate TicTacToe\n\n",
                    font=("arial",20,"bold"),
                    bg=COLOR_VENTANA
                    )
textomenu.pack()

frameReglas=tk.Frame(ventana)
frameReglas.config(bg=COLOR_VENTANA              
                    )

textoReglas=tk.Message(frameReglas,text="REGLAS DEL ULTIMATE TIC TAC TOE\n\n"
                            "1. El tablero es un cuadrado de  un tamaño total de 9x9,distribuidos por 9 gatos convencionales en total\n"
                            "2.El primer jugador en colocar su ficha (sea 0, o X) puede decidir donde  colocarla cualquiera de los 9 tableros\n"
                            "3.En el lugar donde coloque el jugador su ficha es en el tablero donde se jugara la sig jugada\n"
                            "3.1 Ej:Jugador 0 coloco su ficha en el tablero del medio y coloco su ficha en la izquierda inferior, el jugador X debe colocar su ficha en el tablero de la izquierda inferior en cualquier lugar posible\n"
                            "4.El jugador en ganar un tablero,gana en esa area, ya una bez un area sea ganada o llenada, si a uno de los dos jugadores se les envia a ese tablero,puede colocar en cualquiera de los tableros disponibles\n"
                            "5.Gana el que haya ganado 3 tableros cuyas victorias trazen una linea (horizontal o vertical)",
                            font=("arial",17),
                            bg=COLOR_VENTANA
                            
                            )


frameJuego =tk.Frame(ventana)
frameJuego.config(bg=COLOR_VENTANA)                


if turno=="X":
    turno="O"
else:
    turno="X"


dibujo_Tic_Tac_Toe=tk.Canvas(frameJuego,
                            height=450,
                            width=450,
                            highlightthickness=0,
                            bg=COLOR_VENTANA
                            )
dibujo_Tic_Tac_Toe.pack()
for pos in range(50,450,50):
    if pos == 150 or pos == 300:
        grosor = 5
    else:
        grosor = 2
    linea_Vertical=dibujo_Tic_Tac_Toe.create_line(pos,0,pos,450,width=grosor,fill="black")
    linea_Horizontal=dibujo_Tic_Tac_Toe.create_line(0,pos,450,pos,width=grosor,fill="black")

clic_usuario = dibujo_Tic_Tac_Toe.bind("<button-1>",colocar_usuario)


textoJuego=tk.Label(frameJuego,
                    text="Ultimate Tic Tac Toe",
                    font=("arial",20),
                    bg=COLOR_VENTANA
                    )
textoJuego.pack()

botonJugar =tk.Button(frameMenu,text="JUGAR",
                bg="white",
                font=("arial",20),
                command=jugar
                )
botonJugar.pack(pady=10)

botonReglas =tk.Button(frameMenu,text="Reglas",
                bg="white",
                font=("arial",20,),
                command=reglas
                )
botonReglas.pack(pady=10)

botonRegresar_Reglas =tk.Button(frameReglas,
                        bg=COLOR_VENTANA,
                        text="Regresar al menu",
                        font=("arial",16),
                        command=Menu
                        )
botonRegresar_Reglas.pack(pady=10)

botonRegresar_juego=tk.Button(frameJuego,
                        bg=COLOR_VENTANA,
                        text="Regresar al menu",
                        font=("arial",16),
                        command=Menu
                        )
botonRegresar_juego.pack()

botonSalir=tk.Button(frameMenu,
                    bg="white",
                    text="salir",
                    command=ventana.destroy,
                    font=("arial",16)
                    )
botonSalir.pack(pady=20)

Menu()
ventana.mainloop() 
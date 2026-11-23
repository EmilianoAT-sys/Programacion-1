"""
Nombre del archivo: UltimateTicTacToe.py
Descripción: Este archivo contiene la clase gato, que representa un gato pero con un tablero con tamaño 9x9 conformado por 9 gatos.
Nombre de los autores:Juan Pablo Salcido Valenzuela y Eduardo Emiliano Aguirre Toledo
Fecha:12/11/26
"""
import tkinter as tk
import numpy as np


gato_obligado_columna =-1
gato_obligado_fila=-1
turno="X"

Color_X = "#bf0000"
Color_O= "#0000bf"
asignar_color = Color_X
####################################################################
arreglo=np.zeros((3,3,3,3),dtype=int)
tablero_grande = np.zeros((3, 3), dtype=int)
print(arreglo)

COLOR_VENTANA = "#1fAfa1"


def colocar_usuario(event):
    global turno,Color_O,Color_X,asignar_color,gato_obligado_columna,gato_obligado_fila


    columna=event.x // 50
    fila = event.y // 50

    columnaGato = event.x //150
    filaGato = event.y //150

    UlTic_fila=fila // 3
    UlTic_columna = columna // 3
    Tic_columna = columna % 3

    Tic_fila = fila % 3
    if gato_obligado_columna != -1:
        if gato_obligado_columna != UlTic_columna or gato_obligado_fila != UlTic_fila:
            return
    

    x1=columnaGato*150
    y1=filaGato*150
    x2=x1+150
    y2=y1+150
    

    centro_x = columna * 50 + 25
    centro_y = fila * 50 + 25
    
    centro_gatoX = columnaGato*150+75
    centro_gatoY = filaGato*150+75
    
    if arreglo[UlTic_columna,UlTic_fila,Tic_columna,Tic_fila] != 0 or  tablero_grande[UlTic_columna, UlTic_fila] != 0:
        return


    
    dibujo_Tic_Tac_Toe.create_text(centro_x, centro_y, 
                                text=turno,
                                font=("Arial", 35, "bold"),
                                fill=asignar_color)
    asignar_color = Color_X
    if turno=="X":
        simbolo_actual="X"
        jugador = 1
        arreglo[UlTic_columna,UlTic_fila,Tic_columna,Tic_fila] = 1
        turno="O"
        color_actual=Color_X
        asignar_color = Color_O
    else:
        simbolo_actual="O"
        jugador = 2
        arreglo[UlTic_columna,UlTic_fila,Tic_columna,Tic_fila]= 2
        turno="X"
        color_actual=Color_O



    gatos = arreglo[UlTic_columna,UlTic_fila]
    gano=""
    



####################################################################################
    for i in range(3):
        if np.all(gatos[:,i] == jugador) or np.all(gatos[i,:] == jugador) :
            gano = jugador
            tablero_grande[UlTic_columna, UlTic_fila] = jugador
            print("gano jugador")
            dibujo_Tic_Tac_Toe.create_rectangle(x1,y1,x2,y2,
                                            fill="#888888")
            dibujo_Tic_Tac_Toe.create_text(centro_gatoX,
                                        centro_gatoY,
                                        text=simbolo_actual,
                                        fill=color_actual,
                                        font=("arial",150,"bold"))
    ###############################################################################
    if np.all(np.diag(gatos) == jugador) or  np.all(np.diag(np.fliplr(gatos)) == jugador):
        gano=jugador
        tablero_grande[UlTic_columna, UlTic_fila] = jugador 
        print("gano")
        dibujo_Tic_Tac_Toe.create_rectangle(x1,y1,x2,y2,
                                            fill="#777777")
        dibujo_Tic_Tac_Toe.create_text(centro_gatoX,
                                    centro_gatoY,
                                    text=simbolo_actual,
                                    fill=color_actual,
                                    font=("arial",150,"bold"))
    if np.all(gatos != 0) and gano != jugador:
        gano = "="
        tablero_grande[UlTic_columna, UlTic_fila] = 3
        dibujo_Tic_Tac_Toe.create_rectangle(x1,y1,x2,y2,
                                            fill="#888888")
        dibujo_Tic_Tac_Toe.create_text(centro_gatoX,
                                    centro_gatoY,
                                    text=gano,
                                    fill="#ffffff",
                                    font=("arial",150,"bold"))
        print("empate")
    if tablero_grande[Tic_columna, Tic_fila] != 0:
        print()
        gato_obligado_columna=-1
        gato_obligado_fila=-1
    else:
        gato_obligado_columna=Tic_columna
        gato_obligado_fila=Tic_fila
####################################################################################    


    for i in range(3):
            if np.all(tablero_grande[:,i] == jugador) or np.all(tablero_grande[i,:] == jugador) :
                gano = jugador
                tablero_grande[UlTic_columna, UlTic_fila] = jugador
                textoJuego.config(text=f"gano {simbolo_actual}")
                dibujo_Tic_Tac_Toe.unbind("<Button-1>")
    if np.all(np.diag(tablero_grande) == jugador) or  np.all(np.diag(np.fliplr(tablero_grande)) == jugador):
        gano=jugador
        textouego.config(text=f"gano{simbolo_actual}")
        dibujo_Tic_Tac_Toe.unbind("<Button-1>")
    if np.all(tablero_grande != 0) and gano != jugador:
        gano = "="
        textoJuego.config(text=(f"Fue empate"))
        dibujo_Tic_Tac_Toe.unbind("<Button-1>")
        print("empateFinDelJuego")

    




    frameJuego.config(bg=asignar_color)  
    textoJuego.config(bg=asignar_color) 
    print(arreglo[UlTic_columna,UlTic_fila,Tic_columna,Tic_fila])


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

frameJuego.config(bg=asignar_color)             




dibujo_Tic_Tac_Toe=tk.Canvas(frameJuego,
                            height=450,
                            width=450,
                            highlightthickness=0,
                            bg="#888888"
                            )
dibujo_Tic_Tac_Toe.pack()
for pos in range(50,450,50):
    if pos == 150 or pos == 300:
        grosor = 5
    else:
        grosor = 2
    linea_Vertical=dibujo_Tic_Tac_Toe.create_line(pos,0,pos,450,width=grosor,fill="black")
    linea_Horizontal=dibujo_Tic_Tac_Toe.create_line(0,pos,450,pos,width=grosor,fill="black")

clic_usuario = dibujo_Tic_Tac_Toe.bind("<Button-1>",colocar_usuario)


textoJuego=tk.Label(frameJuego,
                    text="Ultimate Tic Tac Toe",
                    font=("arial",20)
                    )
textoJuego.config(bg=asignar_color)
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
                        bg="#444444",
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
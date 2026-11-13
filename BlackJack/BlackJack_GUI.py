# Nombre del archivo: BlackJack.py
# Grupo: 6
# Descripción: Simulación del juego de cartas BlackJack con interfaz gráfica en Tkinter.
# Autores: Eduardo Emiliano Aguirre Toledo y Juan Pablo Salcido Valenzuela.
# Fecha: 10/11/2026.
import random
import tkinter as tk

###################################################################
"""
Area donde se encuentras las variables del color del interfaz y la baraja
"""
COLOR_FONDO = "#0b6b34"        # Verde del "tapete"
COLOR_TEXTO = "white"
COLOR_BOTON = "#f4d03f"
COLOR_CARTA = "white"
COLOR_REVERSO = "#1f3a93"
ANCHO_CARTA = 100
ALTO_CARTA = 140
PALOS = ('♥', '♦', '♣', '♠')
DENOMINACIONES = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
###################################################################

###################################################################
def Barajar(palos, denominaciones) -> list:
    """
    Crea una baraja de 52 cartas (tuplas denominación, palo) y la revuelve.
    Retorna: lista de 52 tuplas.
    """
    baraja = [(d, p) for p in palos for d in denominaciones]
    random.shuffle(baraja)
    return baraja
###################################################################

###################################################################
def Puntuación(mano: list) -> int:
    """
    Calcula los puntos de una mano. Los ases valen 11, pero se reducen
    a 1 las veces que haga falta para no pasarse de 21.
    """
    puntos = 0
    ases = 0
    for denominacion, _ in mano:
        if denominacion == 'A':
            puntos += 11
            ases += 1
        elif denominacion in ('J', 'Q', 'K'):
            puntos += 10
        else:
            puntos += int(denominacion)
    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1
    return puntos
###################################################################

###################################################################
def EsBlackjack(mano: list) -> bool:
    """Un blackjack natural son exactamente 2 cartas que suman 21."""
    return len(mano) == 2 and Puntuación(mano) == 21
###################################################################


###################################################################
class BlackJackApp:
    def __init__(self, root: tk.Tk):
        """
        Función que inicializa la ventana principal del juego y configura los elementos de la interfaz gráfica

        """
        self.root = root
        self.root.title("BlackJack - Grupo 6")
        self.root.configure(bg=COLOR_FONDO)
        self.root.resizable(False, False)

        self.baraja = []
        self.jugador = []
        self.dealer = []
        self.ronda_terminada = True
        self.ganadas = 0
        self.perdidas = 0
        self.empates = 0

        self._crear_widgets()
        self.nueva_partida()

    # ---------------------------------------------------------------
    def _crear_widgets(self):
        """
        Función que crea los elementos de la interfaz gráfica del juego, incluyendo etiquetas, lienzos
        y botones para interactuar con el juego.
        """
        fuente_titulo = ("Arial", 14, "bold")

        tk.Label(self.root, text="BLACKJACK", bg=COLOR_FONDO, fg=COLOR_BOTON,
                 font=("Arial", 22, "bold")).pack(pady=(10, 0))

        self.lbl_marcador = tk.Label(self.root, text="", bg=COLOR_FONDO,
                                     fg=COLOR_TEXTO, font=("Arial", 10))
        self.lbl_marcador.pack()

        # Dealer
        self.lbl_dealer = tk.Label(self.root, text="Dealer", bg=COLOR_FONDO,
                                   fg=COLOR_TEXTO, font=fuente_titulo)
        self.lbl_dealer.pack(pady=(10, 0))
        self.canvas_dealer = tk.Canvas(self.root, width=720, height=ALTO_CARTA + 20,
                                       bg=COLOR_FONDO, highlightthickness=0)
        self.canvas_dealer.pack(padx=20)

        # Mensaje central
        self.lbl_mensaje = tk.Label(self.root, text="", bg=COLOR_FONDO,
                                    fg=COLOR_BOTON, font=("Arial", 16, "bold"))
        self.lbl_mensaje.pack(pady=8)

        # Jugador
        self.lbl_jugador = tk.Label(self.root, text="Jugador", bg=COLOR_FONDO,
                                    fg=COLOR_TEXTO, font=fuente_titulo)
        self.lbl_jugador.pack()
        self.canvas_jugador = tk.Canvas(self.root, width=720, height=ALTO_CARTA + 20,
                                        bg=COLOR_FONDO, highlightthickness=0)
        self.canvas_jugador.pack(padx=20)

        # Botones
        marco = tk.Frame(self.root, bg=COLOR_FONDO)
        marco.pack(pady=15)
        estilo = dict(font=("Arial", 12, "bold"), width=14, bg=COLOR_BOTON,
                      activebackground="#d4ac0d", relief="raised", bd=3)
        self.btn_nueva = tk.Button(marco, text="Partida nueva",
                                   command=self.nueva_partida, **estilo)
        self.btn_pedir = tk.Button(marco, text="Pedir carta",
                                   command=self.pedir_carta, **estilo)
        self.btn_plantarse = tk.Button(marco, text="Plantarse",
                                       command=self.plantarse, **estilo)
        self.btn_nueva.grid(row=0, column=0, padx=8)
        self.btn_pedir.grid(row=0, column=1, padx=8)
        self.btn_plantarse.grid(row=0, column=2, padx=8)

    # ---------------------------------------------------------------
    # Dibujo de cartas
    # ---------------------------------------------------------------
    @staticmethod
    def _rect_redondeado(canvas, x1, y1, x2, y2, r, **kw):
        """
        funcion que dibuja un rectángulo redondeado en el lienzo del canvas
        """
        puntos = [x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r,
                  x2, y2 - r, x2, y2, x2 - r, y2, x1 + r, y2,
                  x1, y2, x1, y2 - r, x1, y1 + r, x1, y1]
        return canvas.create_polygon(puntos, smooth=True, **kw)

    def _dibujar_carta(self, canvas, x, y, carta, oculta=False):
        """
        Función que dibuja una carta en el lienzo del canvas.
        """
        x2, y2 = x + ANCHO_CARTA, y + ALTO_CARTA
        if oculta:
            self._rect_redondeado(canvas, x, y, x2, y2, 12,
                                  fill=COLOR_REVERSO, outline="white", width=3)
            canvas.create_rectangle(x + 10, y + 10, x2 - 10, y2 - 10,
                                    outline="white", width=2)
            for i in range(x + 10, x2 - 10, 10):
                canvas.create_line(i, y + 10, i, y2 - 10, fill="#4a69bd")
            return

        denominacion, palo = carta
        color = "#c0392b" if palo in ('♥', '♦') else "#1c1c1c"
        self._rect_redondeado(canvas, x, y, x2, y2, 12,
                              fill=COLOR_CARTA, outline="#444444", width=2)
        # Esquina superior izquierda
        canvas.create_text(x + 16, y + 20, text=denominacion, fill=color,
                           font=("Arial", 16, "bold"))
        canvas.create_text(x + 16, y + 40, text=palo, fill=color,
                           font=("Arial", 14))
        # Esquina inferior derecha
        canvas.create_text(x2 - 16, y2 - 20, text=denominacion, fill=color,
                           font=("Arial", 16, "bold"))
        canvas.create_text(x2 - 16, y2 - 40, text=palo, fill=color,
                           font=("Arial", 14))
        # Símbolo central
        canvas.create_text(x + ANCHO_CARTA // 2, y + ALTO_CARTA // 2, text=palo,
                           fill=color, font=("Arial", 40))

    def _dibujar_mano(self, canvas, mano, ocultar_segunda=False):
        """
        funcion que dibuja la mano de cartas en el lienzo del canvas, centrando las cartas y ajustando la separación según la cantidad de cartas.
        """
        canvas.delete("all")
        n = len(mano)
        ancho_canvas = int(canvas["width"])
        # Si hay muchas cartas se encimen un poco para que quepan
        separacion = min(ANCHO_CARTA + 12, (ancho_canvas - ANCHO_CARTA - 20) // max(n - 1, 1))
        total = ANCHO_CARTA + separacion * (n - 1)
        x0 = (ancho_canvas - total) // 2
        for i, carta in enumerate(mano):
            self._dibujar_carta(canvas, x0 + i * separacion, 10, carta,
                                oculta=(ocultar_segunda and i == 1))

    # ---------------------------------------------------------------
    # Actualización de la pantalla
    # ---------------------------------------------------------------
    def _actualizar(self, mostrar_dealer: bool):
        """
        Actualiza la pantalla con el estado actual del juego.

        
        
        """
        self._dibujar_mano(self.canvas_jugador, self.jugador)
        self._dibujar_mano(self.canvas_dealer, self.dealer,
                           ocultar_segunda=not mostrar_dealer)
        self.lbl_jugador.config(text=f"Jugador: {Puntuación(self.jugador)} puntos")
        if mostrar_dealer:
            self.lbl_dealer.config(text=f"Dealer: {Puntuación(self.dealer)} puntos")
        else:
            self.lbl_dealer.config(text=f"Dealer: {Puntuación(self.dealer[:1])} + ?")
        self.lbl_marcador.config(
            text=f"Ganadas: {self.ganadas}   Perdidas: {self.perdidas}   Empates: {self.empates}")

    def _activar_botones(self, activos: bool):
        """
        función auxiliar para activar o desactivar los botones de acción del jugador
        
        """
        estado = "normal" if activos else "disabled"
        self.btn_pedir.config(state=estado)
        self.btn_plantarse.config(state=estado)

    def _terminar(self, mensaje: str, resultado: str):
        """
        Muestra el mensaje final de la ronda y actualiza el marcador según el resultado.

        """
        self.ronda_terminada = True
        if resultado == 'gano':
            self.ganadas += 1
        elif resultado == 'perdio':
            self.perdidas += 1
        else:
            self.empates += 1
        self.lbl_mensaje.config(text=mensaje)
        self._activar_botones(False)
        self.btn_nueva.config(state="normal")
        self._actualizar(mostrar_dealer=True)

    # ---------------------------------------------------------------
    # Acciones de los botones
    # ---------------------------------------------------------------
    def nueva_partida(self):
        """
        Muestra una nueva partida, baraja las cartas y reparte dos cartas al jugador y al dealer.
        También verifica si hay un blackjack natural en las primeras dos cartas.
        """
        self.baraja = Barajar(PALOS, DENOMINACIONES)
        self.jugador = [self.baraja.pop(), self.baraja.pop()]
        self.dealer = [self.baraja.pop(), self.baraja.pop()]
        self.ronda_terminada = False
        self.lbl_mensaje.config(text="")
        self._activar_botones(True)
        self._actualizar(mostrar_dealer=False)

        # Blackjack natural (solo en las primeras 2 cartas)
        nat_j, nat_d = EsBlackjack(self.jugador), EsBlackjack(self.dealer)
        if nat_j and nat_d:
            self._terminar("EMPATE, POR NATURAL.", 'empate')
        elif nat_d:
            self._terminar("PERDISTE, EL DEALER HIZO BLACKJACK.", 'perdio')
        elif nat_j:
            self._terminar("¡GANASTE, BLACKJACK NATURAL!", 'gano')

    def pedir_carta(self):
        """
        Funcion que permite pedir una carta al jugador y verifica si se pasa de 21 puntos o si llega a 21

        """
        if self.ronda_terminada:
            return
        self.jugador.append(self.baraja.pop())
        puntos = Puntuación(self.jugador)
        self._actualizar(mostrar_dealer=False)
        if puntos > 21:
            self._terminar("Perdiste, te pasaste de 21 puntos.", 'perdio')
        elif puntos == 21:
            self.plantarse()

    def plantarse(self):
        """
        Funcion que permite al jugador plantarse y terminar su turno.
        """ 
        if self.ronda_terminada:
            return
        self._activar_botones(False)
        self.btn_nueva.config(state="disabled")
        self._actualizar(mostrar_dealer=True)
        self.root.after(700, self._turno_dealer)

    def _turno_dealer(self):
        """El Dealer pide carta (con una pausa) hasta llegar a 17 o más."""
        if Puntuación(self.dealer) < 17:
            self.dealer.append(self.baraja.pop())
            self._actualizar(mostrar_dealer=True)
            self.root.after(700, self._turno_dealer)
        else:
            self._resolver()

    def _resolver(self):
        """
        Funcion que determina el resultado de la ronda comparando la puntuación del jugador y del dealer.

        """
        puntosjugador, puntosdealer = Puntuación(self.jugador), Puntuación(self.dealer)
        if puntosdealer > 21:
            self._terminar("¡Ganaste, el Dealer se pasó de 21!", 'gano')
        elif puntosdealer > puntosjugador:
            self._terminar("Perdiste, el Dealer tiene más puntos.", 'perdio')
        elif puntosdealer < puntosjugador:
            self._terminar("¡Ganaste, tienes más puntos que el Dealer!", 'gano')
        else:
            self._terminar("Empate, no hubo ganador.", 'empate')



###################################################################
if __name__ == "__main__":
    ventana = tk.Tk()
    BlackJackApp(ventana)
    ventana.mainloop()

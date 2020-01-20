from pygame import *
from pygame.locals import *
import sys

# inicializamos pygame
init()

# Ventana principal del juego
screen = display.set_mode((1024, 768))
display.set_caption('Hola Mundo')
background_color = (30, 46, 222)

# Bucle de eventos, actualizacion de objetos y refresco del programa.
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

        # ... procesar el resto de eventos
        screen.fill(background_color)
        
        display.flip() #loop

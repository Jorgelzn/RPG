import pygame
from Director import Director
from Pantalla1 import Pantalla1

pygame.init()

director = Director()
#Creamos la instancia de la escena
scene = Pantalla1(director)
#Le decimos al director la escena que ejecutará
director.change_scene(scene)
#Y ponemos en marcha el juego!
director.loop()

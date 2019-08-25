import pygame
from Director import Director
from Pantalla1 import Pantalla1
from Variables import *


pygame.init()

director = Director()
#Creamos la instancia de la escena
scene = Pantalla1(map1,"imagenes/city.jpg")
#Le decimos al director la escena que ejecutará
director.change_scene(scene)
#Y ponemos en marcha el juego!
director.loop()
#Al terminar el loop salimos de pygame:
pygame.quit()

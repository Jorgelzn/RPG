import pygame
from Director import Director
from Pantalla1 import Pantalla1
from Variables import *


pygame.init()

director = Director()
#create first scene
scene = Pantalla1(map1,"imagenes/mapas/city.jpg")
#use the first scene
director.change_scene(scene)
#start the main loop
director.loop()

pygame.quit()

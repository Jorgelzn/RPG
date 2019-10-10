import pygame
from Director import Director
from Pantalla1 import Pantalla1
from Pantalla1 import Pantalla2
from Variables import *


pygame.init()

director = Director()
#create first scene

if mapaG==1:
    scene = Pantalla1(map1,"imagenes/mapas/city.jpg")
elif mapaG==2:
    scene = Pantalla2(map2,"imagenes/mapas/forest.png")

#use the first scene
director.change_scene(scene)
#start the main loop
director.loop()

pygame.quit()

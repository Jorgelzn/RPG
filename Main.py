import pygame
from Director import Director
from Pantallas import *
from Variables import *
from Personaje import Personaje
#testing comment
pygame.init()
#testing vs code git 2
director = Director()

pj = Personaje(pjx, pjy)

#create scenes
scene1 = Pantalla1(map1,"imagenes/mapas/city.jpg",soundtrack1,pj)
scene2 = Pantalla2(map2,"imagenes/mapas/forest.png",soundtrack2,pj)
scenes=[scene1,scene2]
#doing this we create all the scenes at the beginning and just change them during program
for e in scenes:
    e.scenes=scenes

#use the first scene
if mapaG==0:
    director.change_scene(scene1)
    pygame.mixer.music.load(scene1.soundtrack)
elif mapaG==1:
    director.change_scene(scene2)
    pygame.mixer.music.load(scene2.soundtrack)

pygame.mixer.music.play()

#start the main loop
director.loop()
#testing ssh key keeps good 
pygame.quit()

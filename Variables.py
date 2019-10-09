import pygame
from pygame.locals import *
# Escenarios y ventanas:
map1 = (1600, 1290)
map2 = (2000, 2000)
ventana = (1200, 900)

# Colores:
agua = (50, 120, 240)
hierba = (50, 220, 50)

# Otros:
FPSPRITE = 10 # frames por sprite (personaje)

f=open("save.txt","r")
lines=f.readlines()
pjx=int(lines[0])
pjy=int(lines[1])

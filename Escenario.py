import pygame
from Variables import *

class Obstaculo:
    def __init__(self, x=0, y=0, w=200, h=200):
        self.rect = pygame.Rect(x, y, w, h)
        self.frame_width = w         # Anchura de la imagen
        self.frame_height = h       # Altura de la imagen


class Objeto:

    def __init__(self, imagen,size,description, x=0, y=0, w=200, h=200, xinvent=0, yinvent=0,posx=0,posy=0,taken=False):
        self.image = pygame.image.load(imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w,h))
        self.rect = self.image.get_rect()
        self.action_rect = pygame.Rect(x,y,w+50,h+50)
        self.rect.topleft = (x,y)
        self.taken = taken
        self.imageInvent=pygame.transform.scale(self.image,(size,size))
        self.rectInvent=self.imageInvent.get_rect()
        self.rectInvent.topleft=(xinvent,yinvent)
        self.description=description
        self.posx=posx
        self.posy=posy

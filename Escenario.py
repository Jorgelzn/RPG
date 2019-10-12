import pygame
from Variables import *

class Obstaculo:
    def __init__(self, x=0, y=0, w=200, h=200, portal=False, image=None):
        self.image=image
        if image!=None:
            self.image = pygame.image.load(image).convert_alpha()
            self.image = pygame.transform.scale(self.image, (w,h))
        self.rect = pygame.Rect(x, y, w, h)
        self.rect_col = pygame.Rect(x+10, y+h-20, w-20, 20)
        self.portal=portal
        self.frame_width = w         # Anchura de la imagen
        self.frame_height = h       # Altura de la imagen
        self.action_rect = pygame.Rect(x-20, y-20, w+40, h+40)


class Objeto:

    def __init__(self, imagen,size,description, x=0, y=0, w=200, h=200, xinvent=0, yinvent=0,posx=0,posy=0,taken=False):
        self.image = pygame.image.load(imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w,h))
        self.rect = self.image.get_rect()
        self.action_rect = pygame.Rect(x-20,y-20,w+40,h+40)
        self.rect.topleft = (x,y)
        self.taken = taken
        self.imageInvent=pygame.transform.scale(self.image,(size,size))
        self.rectInvent=self.imageInvent.get_rect()
        self.rectInvent.topleft=(xinvent,yinvent)
        self.description=description
        self.posx=posx
        self.posy=posy

import pygame
from pygame.locals import *

class Text:

    def __init__(self):
        self.font = pygame.font.Font("imagenes/ARCADECLASSIC.TTF",20)
        self.image = pygame.image.load("imagenes/text_box.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (800, 300))
        self.rect = self.image.get_rect()
        self.rect.center=(500,600)
        self.rectext=(self.rect.topleft[0]+60,self.rect.topleft[1]+80,self.rect.width,self.rect.height)
        self.color1= (3, 123, 239)
        self.color2= (200,50,50)
        self.display = False
        self.text =None

    def dialog1(self):
            self.text=self.font.render('MAMAHUEVO', True, self.color2)

            if not self.display:
                self.display=True
            else:
                self.display= False

    def dialog2(self):
            self.text=self.font.render('aguita', True, self.color1)

            if not self.display:
                self.display=True
            else:
                self.display= False

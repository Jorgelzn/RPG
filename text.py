import pygame
from pygame.locals import *

class Text:

    def __init__(self):
        self.font = pygame.font.Font("imagenes/ARCADECLASSIC.TTF",20)
        self.image = pygame.image.load("imagenes/box.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center=(500,600)
        self.rectext=(self.rect.topleft[0]+20,self.rect.topleft[1]+20,self.rect.width,self.rect.height)
        self.display = False
        self.text =None

    def dialog1(self):
            self.text=self.font.render('GeeksForGeeks', True, (200,50,50))

            if not self.display:
                self.display=True
            else:
                self.display= False

    def dialog2(self):
            self.text=self.font.render('aguita', True, (200,50,50))

            if not self.display:
                self.display=True
            else:
                self.display= False

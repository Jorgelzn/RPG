import pygame
from pygame.locals import *

class Text:

    def __init__(self):
        self.font = pygame.font.Font("imagenes/ARCADECLASSIC.TTF",20)
        self.image = pygame.image.load("imagenes/box.png").convert_alpha()
        self.image.get_rect().center=(500,600)
        print(self.image.get_rect().center,"hoassd")
        self.display = False
        self.text =None

    def dialog1(self):
            self.text=self.font.render('GeeksForGeeks', True, (200,50,50))
            self.text.get_rect().center=(100,100)
            print(self.text.get_rect().topleft)
            print(self.image.get_rect().topleft)

            if not self.display:
                self.display=True
            else:
                self.display= False

    def dialog2(self):
            self.text=self.font.render('aguita', True, (200,50,50))
            self.text.get_rect().topleft=(self.image.get_rect().topleft[0]+50,self.image.get_rect().topleft[1]+50)

            if not self.display:
                self.display=True
            else:
                self.display= False

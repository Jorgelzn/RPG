import pygame
from pygame.locals import *
from Variables import *

class Text:

    def __init__(self):
        self.menuImage = pygame.image.load("imagenes/Menu.png").convert_alpha()
        self.menuImage = pygame.transform.scale(self.menuImage, (ventana[0]-100, ventana[1]-100))
        self.menuRect = self.menuImage.get_rect()
        self.font = pygame.font.Font("imagenes/ARCADECLASSIC.TTF",20)
        self.image = pygame.image.load("imagenes/text_box.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (800, 300))
        self.rect = self.image.get_rect()
        self.rect.center=(500,600)
        self.rectext=(self.rect.topleft[0]+60,self.rect.topleft[1]+80,self.rect.width,self.rect.height)
        self.color1= (3, 123, 239)
        self.color2= (200,50,50)
        self.display = False
        self.displayMenu = False
        self.finishdialog = False
        self.countdialog=0;
        self.chat1=[False, False]
        self.text =None

    def dialog1(self):
        for e in self.chat1:
            if not self.chat1[0]:
                self.text=self.font.render('MAMAHUEVO', True, self.color2)
                self.chat1[0]=True
                self.countdialog+=1
                break
            if not self.chat1[1]:
                self.text=self.font.render('PAPERIPETO', True, self.color2)
                self.chat1[1]=True
                self.countdialog+=1
                break
        if not self.finishdialog:
            self.display=True
        else:
            self.display= False
            self.finishdialog= False
            for e in self.chat1:
                self.chat1[e]=False

        if self.countdialog == len(self.chat1):
            self.finishdialog = True
            self.countdialog=0

    def dialog2(self):
            self.text=self.font.render('aguita', True, self.color1)

            if not self.display:
                self.display=True
            else:
                self.display= False


    def menu(self):
        if not self.displayMenu:
            self.displayMenu=True
        else:
            self.displayMenu= False

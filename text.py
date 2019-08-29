import pygame
from pygame.locals import *
from Variables import *
from sonidos import Sonido
from Director import Director

class Text:

    def __init__(self):
        self.menuImage = pygame.image.load("imagenes/Menu.png").convert_alpha()
        self.menuImage = pygame.transform.scale(self.menuImage, (ventana[0]-100, ventana[1]-100))
        self.menuRect = self.menuImage.get_rect()
        self.selectorImageR = pygame.image.load("imagenes/Pointer_R.png").convert_alpha()
        self.selectorImageR = pygame.transform.scale(self.selectorImageR, (40,40))
        self.selectorImageL = pygame.image.load("imagenes/Pointer_L.png").convert_alpha()
        self.selectorImageL = pygame.transform.scale(self.selectorImageL, (40,40))
        self.selectorRect = self.selectorImageR.get_rect()
        self.selectorRect.center = (self.menuRect.topleft[0]+250,self.menuRect.topleft[1]+130)
        self.countSelector=0
        self.posSelector = []
        self.posSelector.append(self.selectorRect.center)
        for i in range(3):
            self.posSelector.append((self.selectorRect.center[0],self.posSelector[i][1]+120))
        self.displayMenu = False
        self.fontMenu = pygame.font.Font("imagenes/ARCADECLASSIC.TTF",50)

        self.font = pygame.font.Font("imagenes/ARCADECLASSIC.TTF",20)
        self.image = pygame.image.load("imagenes/text_box.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (750, 300))
        self.rect = self.image.get_rect()
        self.rect.center=(500,600)
        self.rectext=(self.rect.topleft[0]+60,self.rect.topleft[1]+80,self.rect.width,self.rect.height)
        self.textcolor1= (3, 123, 239)
        self.textcolor2= (200,50,50)
        self.textcolor3= (90, 90, 90)
        self.display = False
        self.finishdialog = False
        self.countdialog=0;
        self.chat1=[False, False]
        self.text =None

        self.menuText = []
        self.menuText.append(self.fontMenu.render('Objetos', True, self.textcolor3))
        self.menuText.append(self.fontMenu.render('Mapa', True, self.textcolor3))
        self.menuText.append(self.fontMenu.render('Guardar', True, self.textcolor3))
        self.menuText.append(self.fontMenu.render('Salir', True, self.textcolor3))

        self.objectsText = []

        self.menuTextRect = []
        self.menuTextRect.append((self.selectorRect.center[0]+80,self.posSelector[0][1]-20,self.menuRect.width,50))
        self.menuTextRect.append((self.selectorRect.center[0]+80,self.posSelector[1][1]-20,self.menuRect.width,50))
        self.menuTextRect.append((self.selectorRect.center[0]+80,self.posSelector[2][1]-20,self.menuRect.width,50))
        self.menuTextRect.append((self.selectorRect.center[0]+80,self.posSelector[3][1]-20,self.menuRect.width,50))

        self.mapImage=pygame.image.load("imagenes/mapita.png").convert_alpha()
        self.mapImage = pygame.transform.scale(self.mapImage, (950, 700))
        self.displayMap=False
        self.displayObjects=False

        self.sonido= Sonido()

    def dialog1(self):
        self.sonido.dialog.play()
        for e in self.chat1:
            if not self.chat1[0]:
                self.text=self.font.render('Hola, soy peto y estoy hasta el cubo de paperi', True, self.textcolor2)
                self.chat1[0]=True
                self.countdialog+=1
                break
            if not self.chat1[1]:
                self.text=self.font.render('es un Mamahuevo', True, self.textcolor2)
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
        self.sonido.dialog.play()
        self.text=self.font.render('Hola, soy Paperi', True, self.textcolor1)

        if not self.display:
            self.display=True
        else:
            self.display= False


    def menu(self,keys):
        if keys[K_t] and not self.display:
            if not self.displayMenu:
                self.displayMenu=True
            else:
                self.displayMenu= False
            self.displayMap=False
            self.displayObjects=False
        elif self.displayMenu:
            if keys[K_DOWN]:
                self.countSelector+=1
                self.sonido.pointerSound.play()
            elif keys[K_UP]:
                self.countSelector-=1
                self.sonido.pointerSound.play()
            elif keys[K_RETURN] and self.countSelector==3:
                Director.quit()
            elif keys[K_RETURN] and self.countSelector==1:
                if self.displayMap:
                    self.displayMap=False
                    self.displayMenu=False
                else:
                    self.displayMap=True
            elif keys[K_RETURN] and self.countSelector==0 and len(self.objectsText)>0:
                if self.displayObjects:
                    self.displayObjects=False
                    self.displayMenu=False
                else:
                    self.displayObjects=True


            if self.countSelector==4:
                self.countSelector=0
            elif self.countSelector==-1:
                self.countSelector=3

            self.selectorRect.center=self.posSelector[self.countSelector]

    def displays(self, screen):
        if self.display:
            screen.blit(self.image, self.rect)
            screen.blit(self.text, self.rectext)
        elif self.displayMenu:
            if self.displayMap:
                screen.blit(self.mapImage,self.mapImage.get_rect())
            else:
                if self.displayObjects and len(self.objectsText)>0:
                    text=self.objectsText
                else:
                    text=self.menuText
                screen.blit(self.menuImage, self.menuRect)
                screen.blit(self.selectorImageR,self.selectorRect)
                leftRect=(self.selectorRect.topleft[0]+350,self.selectorRect.topleft[1],self.selectorRect.width,self.selectorRect.height)
                screen.blit(self.selectorImageL,(leftRect))
                for i in range(len(text)):
                    screen.blit(text[i],self.menuTextRect[i])

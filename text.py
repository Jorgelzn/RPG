import pygame
from pygame.locals import *
from Variables import *
from sonidos import Sonido
class Text:

    def __init__(self, pj):

        self.font = pygame.font.Font("imagenes/ARCADECLASSIC.TTF",20)
        self.image = pygame.image.load("imagenes/menus/text_box.png").convert_alpha()
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

        self.menuImage = pygame.image.load("imagenes/menus/Menu.png").convert_alpha()
        self.menuImage = pygame.transform.scale(self.menuImage, (ventana[0]-20, ventana[1]-20))
        self.menuRect = self.menuImage.get_rect()
        self.selectorImageR = pygame.image.load("imagenes/menus/Pointer_R.png").convert_alpha()
        self.selectorImageR = pygame.transform.scale(self.selectorImageR, (int(ventana[0]/20),int(ventana[0]/20)))
        self.selectorImageL = pygame.image.load("imagenes/menus/Pointer_L.png").convert_alpha()
        self.selectorImageL = pygame.transform.scale(self.selectorImageL, (int(ventana[0]/20),int(ventana[0]/20)))
        self.selectorRect = self.selectorImageR.get_rect()
        self.selectorRect.center = (self.menuRect.topleft[0]+ventana[0]/2-200,self.menuRect.topleft[1]+130)
        self.countSelector=0
        self.posSelector = []
        self.posSelector.append(self.selectorRect.center)
        for i in range(3):
            self.posSelector.append((self.selectorRect.center[0],self.posSelector[i][1]+ventana[1]/4-30))
        self.displayMenu = False
        self.fontMenu = pygame.font.Font("imagenes/ARCADECLASSIC.TTF",int(ventana[0]/20))

        self.menuText = []
        self.menuText.append(self.fontMenu.render('Inventario', True, self.textcolor3))
        self.menuText.append(self.fontMenu.render('Mapa', True, self.textcolor3))
        self.menuText.append(self.fontMenu.render('Guardar', True, self.textcolor3))
        self.menuText.append(self.fontMenu.render('Salir', True, self.textcolor3))

        self.menuTextRect = []
        self.menuTextRect.append((self.selectorRect.center[0]+50,self.posSelector[0][1]-20,self.menuRect.width,50))
        self.menuTextRect.append((self.selectorRect.center[0]+140,self.posSelector[1][1]-20,self.menuRect.width,50))
        self.menuTextRect.append((self.selectorRect.center[0]+90,self.posSelector[2][1]-20,self.menuRect.width,50))
        self.menuTextRect.append((self.selectorRect.center[0]+120,self.posSelector[3][1]-20,self.menuRect.width,50))

        self.mapImage=pygame.image.load("imagenes/mapas/mapita.png").convert_alpha()
        self.mapImage = pygame.transform.scale(self.mapImage, (ventana[0]-30, ventana[1]-30))
        self.displayMap=False

        self.displayInventario=False
        self.inventarioImage=pygame.image.load("imagenes/menus/Inventario.png").convert_alpha()
        self.inventarioImage = pygame.transform.scale(self.inventarioImage, (ventana[0]+60, ventana[1]+60))
        self.inventarioRect=self.inventarioImage.get_rect()
        self.inventarioRect.topleft=(-40,-30)
        self.objetosInventario=pj.objects

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


    def menu(self,keys,pj,director):
        if keys[K_t] and not self.display:
            if not self.displayMenu:
                self.displayMenu=True
            else:
                self.displayMenu= False
            self.displayMap=False
            self.displayInventario=False
        elif self.displayMenu:
            if keys[K_DOWN]:
                self.countSelector+=1
                self.sonido.pointerSound.play()
            elif keys[K_UP]:
                self.countSelector-=1
                self.sonido.pointerSound.play()
            elif keys[K_RETURN] and self.countSelector==3:
                self.sonido.click.play()
                director.quit()
            elif keys[K_RETURN] and self.countSelector==2:
                self.sonido.click.play()
                f = open("save.txt","w")
                f.write(str(pj.rect_spr.centerx)+'\n')
                f.write(str(pj.rect_spr.centery))
                f.close()
            elif keys[K_RETURN] and self.countSelector==1:
                self.sonido.click.play()
                self.displayMenu=False
                self.displayMap=True
            elif keys[K_RETURN] and self.countSelector==0:
                self.sonido.click.play()
                self.displayMenu=False
                self.displayInventario=True
        elif self.displayMap:
            if keys[K_t]:
                self.displayMenu=True
            elif keys[K_RETURN]:
                self.displayMap=False
        elif self.displayInventario:
            if keys[K_t]:
                self.displayMenu=True
            elif keys[K_RETURN]:
                self.displayInventario=False

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
            screen.blit(self.menuImage, self.menuRect)
            screen.blit(self.selectorImageR,self.selectorRect)
            leftRect=(self.selectorRect.topleft[0]+int(ventana[0]/2.8),self.selectorRect.topleft[1],self.selectorRect.width,self.selectorRect.height)
            screen.blit(self.selectorImageL,(leftRect))
            for i in range(4):
                screen.blit(self.menuText[i],self.menuTextRect[i])

        elif self.displayMap:
            screen.blit(self.mapImage,self.mapImage.get_rect())
        elif self.displayInventario:
            screen.blit(self.inventarioImage,self.inventarioRect)
            for e in self.objetosInventario:
                if e.taken:
                    screen.blit(e.imageInvent,e.rectInvent)

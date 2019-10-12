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
        self.textcolor= (90, 90, 90)
        self.display = False                #controla que se vean o no los dialogos
        self.finishdialog = False           # controla que haya acabado el dialogo
        self.countdialog=0;                 # counter of phrases in the dialog function
        self.text =None                     #text displayed in dialogs

        self.menuImage = pygame.image.load("imagenes/menus/Menu.png").convert_alpha()  #imagen del cuadro de menu
        self.menuImage = pygame.transform.scale(self.menuImage, (ventana[0]-20, ventana[1]-20))
        self.menuRect = self.menuImage.get_rect()

        self.selectorImageR = pygame.image.load("imagenes/menus/Pointer_R.png").convert_alpha()
        self.selectorImageR = pygame.transform.scale(self.selectorImageR, (int(ventana[0]/20),int(ventana[0]/20)))
        self.selectorImageL = pygame.image.load("imagenes/menus/Pointer_L.png").convert_alpha()
        self.selectorImageL = pygame.transform.scale(self.selectorImageL, (int(ventana[0]/20),int(ventana[0]/20)))
        self.selectorRect = self.selectorImageR.get_rect()
        self.selectorRect.center = (self.menuRect.topleft[0]+ventana[0]/2-200,self.menuRect.topleft[1]+130)
        self.countSelector=0        #controla que posicion tiene el selector del menu
        self.posSelector = []       #las posibles posiciones del selector del menu
        self.posSelector.append(self.selectorRect.center)
        for i in range(3):
            self.posSelector.append((self.selectorRect.center[0],self.posSelector[i][1]+ventana[1]/4-30))

        self.displayMenu = False        #variable para controlar si se esta mostrando o no el menu
        self.fontMenu = pygame.font.Font("imagenes/ARCADECLASSIC.TTF",int(ventana[0]/20))   #tipo de letra en menu

        self.menuText = []          #los diferentes textos del menu
        self.menuText.append(self.fontMenu.render('Inventario', True, self.textcolor))
        self.menuText.append(self.fontMenu.render('Mapa', True, self.textcolor))
        self.menuText.append(self.fontMenu.render('Guardar', True, self.textcolor))
        self.menuText.append(self.fontMenu.render('Salir', True, self.textcolor))

        self.menuTextRect = []      #las posiciones de los textos del menu
        self.menuTextRect.append((self.selectorRect.center[0]+50,self.posSelector[0][1]-20,self.menuRect.width,50))
        self.menuTextRect.append((self.selectorRect.center[0]+140,self.posSelector[1][1]-20,self.menuRect.width,50))
        self.menuTextRect.append((self.selectorRect.center[0]+90,self.posSelector[2][1]-20,self.menuRect.width,50))
        self.menuTextRect.append((self.selectorRect.center[0]+120,self.posSelector[3][1]-20,self.menuRect.width,50))

        self.mapImage=pygame.image.load("imagenes/mapas/mapita.png").convert_alpha()        #imagen del mapa
        self.mapImage = pygame.transform.scale(self.mapImage, (ventana[0]-30, ventana[1]-30))
        self.displayMap=False

        self.displayInventario=False        #variable que controla que se vea el inventario
        self.inventarioImage=pygame.image.load("imagenes/menus/Inventario.png").convert_alpha() #imagen de inventario
        self.inventarioImage = pygame.transform.scale(self.inventarioImage, (ventana[0]+60, ventana[1]+60))
        self.inventarioRect=self.inventarioImage.get_rect()
        self.inventarioRect.topleft=(-40,-30)

        self.selecInventario=pygame.image.load("imagenes/menus/square.png").convert_alpha() #selector de inventario
        self.selecInventario = pygame.transform.scale(self.selecInventario, (int(self.inventarioRect.width/7),int(self.inventarioRect.height/7)))
        firstpos=(self.inventarioRect.topleft[0]+214,self.inventarioRect.topleft[1]+150)
        self.posInventario=[] #las 16 posibles posiciones del selector en el inventario, matriz 4x4
        for i in range(4):
            self.posInventario.append([])       #creamos 4 listas dentro de la lista para la matriz
        self.selecPos=[0,0]                     #variable para controlar en que posicion esta el selector
        high=0
        width=0
        layer=0
        for e in range(4):                      #la lista es una lista de 16 rects
            for i in range (4):                 #llenamos la lista de posiciones con lass 16 posiciones
                rect=self.selecInventario.get_rect()
                rect.topleft=(firstpos[0]+width,firstpos[1]+high)
                self.posInventario[layer].append(rect)
                width+=220
            layer+=1
            high+=168
            width=0
        self.objetosInventario=pj.objects           #asignamos los objetos que tiene el personaje
        self.description=False                      #variable para controlar que se vea la descripcion de objeto

        self.sonido= Sonido()


    def dialog(self,chat):                      #controla el dialogo que se le pasa por parametro como lista string
        self.sonido.dialog.play()
        if not self.finishdialog:
            self.talking=True
            for i in chat:
                if chat.index(i)>=self.countdialog:     #solo se muestra la frase que toca dentro del dialogo
                    self.text=self.font.render(i, True, self.textcolor)
                    self.countdialog+=1
                    break
            self.display=True
        else:
            self.display= False
            self.finishdialog= False

        if self.countdialog == len(chat):
            self.finishdialog = True
            self.talking= False
            self.countdialog=0


    def menu(self,keys,pj,director):            #funcion que para navegar por el menu
        if keys[K_t] and not self.display:      #entrar y salir del menu pulsando t
            self.sonido.click.play()
            if not self.displayMenu:
                self.displayMenu=True
            else:
                self.displayMenu= False
            self.displayMap=False
            self.displayInventario=False
        elif self.displayMenu:                  #si estamos en el menu
            if keys[K_DOWN]:                                      #mover selector hacia abajo
                self.countSelector = (self.countSelector + 1) % 4
                self.sonido.pointerSound.play()
            elif keys[K_UP]:                                      #mover selector hacia arriba
                self.countSelector = (self.countSelector - 1) % 4
                self.sonido.pointerSound.play()

            elif keys[K_RETURN] and self.countSelector==3:      #seleccionar opcion de salir
                self.sonido.click.play()
                director.quit()

            elif keys[K_RETURN] and self.countSelector==1:      #seleccionar opcion de mapa
                self.sonido.click.play()
                self.displayMenu=False
                self.displayMap=True

            elif keys[K_RETURN] and self.countSelector==0:       #seleccionar opcion de inventario
                self.sonido.click.play()
                self.displayMenu=False
                self.displayInventario=True

            elif keys[K_RETURN] and self.countSelector==2:       #seleccionar opcion de guardar
                self.sonido.click.play()
                f = open("save.txt","w")
                f.write(str(pj.rect_spr.centerx)+'\n')
                f.write(str(pj.rect_spr.centery)+'\n')
                f.write(str(pj.mapa)+'\n')
                for e in pj.objects:
                    f.write(str(e.taken)+'\n')
                f.close()

            self.selectorRect.center=self.posSelector[self.countSelector]   #asigna la posicion de los selectores


        elif self.displayMap:                   #estamos en el mapa
            if keys[K_t]:                       #al pulsar t vuelves al menu
                self.displayMenu=True
                self.sonido.click.play()
            elif keys[K_RETURN]:                #al pulsar enter sales al juego
                self.displayMap=False
                self.sonido.click.play()

        elif self.displayInventario:            #estamos en el inventario
            if keys[K_t]:                       #al pulsar t vuelves al menu
                self.displayMenu=True
                self.sonido.click.play()
            elif keys[K_UP]:                                  #mover selector arriba
                self.selecPos[0] = (self.selecPos[0] - 1) % 4
            elif keys[K_DOWN]:                                #mover selector abajo
                self.selecPos[0] = (self.selecPos[0] + 1) % 4
            elif keys[K_RIGHT]:                               #mover selector a la derecha
                self.selecPos[1] = (self.selecPos[1] + 1) % 4
            elif keys[K_LEFT]:                                #mover selector a la izquierda
                self.selecPos[1] = (self.selecPos[1] - 1) % 4

            pos=self.posInventario[self.selecPos[0]][self.selecPos[1]].topleft
            for e in pj.objects:               #al pulsaar enter en un objeto se muestra su descripcion
                if e.taken and pos[0]==e.posx and pos[1]==e.posy and keys[K_RETURN] and not self.description:
                    self.description=True
                    self.text=self.font.render(e.description, True, self.textcolor)
                elif self.description and keys[K_RETURN]:       #al pulsar de nuevo enter vuelves al inventario
                    self.description=False


    def displays(self, screen):     #funcion que dibuja todos los textos

        if self.display:            #mostrando cuadros de dialogos
            screen.blit(self.image, self.rect)
            screen.blit(self.text, self.rectext)

        elif self.displayMenu:      #mostrando menu
            screen.blit(self.menuImage, self.menuRect)              #imagen de menu
            screen.blit(self.selectorImageR,self.selectorRect)      #selector derecho
            leftRect=(self.selectorRect.topleft[0]+int(ventana[0]/2.8),self.selectorRect.topleft[1],self.selectorRect.width,self.selectorRect.height)
            screen.blit(self.selectorImageL,(leftRect)) #selector izquierdo
            for i in range(4):                          #4 opciones del menu
                screen.blit(self.menuText[i],self.menuTextRect[i])

        elif self.displayMap:       #mostrando mapa
            screen.blit(self.mapImage,self.mapImage.get_rect())

        elif self.displayInventario:       #mostrando inventario
            screen.blit(self.inventarioImage,self.inventarioRect)  #imagen de inventario
            for e in self.objetosInventario:                    #objetos de inventario
                if e.taken:
                    screen.blit(e.imageInvent,e.rectInvent)
            for i in self.posInventario:                    #selector de inventario
                for e in i:
                    if self.posInventario[self.selecPos[0]][self.selecPos[1]]==e:
                        screen.blit(self.selecInventario,e)
            if self.description:                            #descripcion de objeto
                    screen.blit(self.image, self.rect)
                    screen.blit(self.text, self.rectext)

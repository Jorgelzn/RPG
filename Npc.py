import pygame
from Variables import *

class Npc:
    def __init__(self, imagen,dialog=None, x=0, y=0, w=200, h=200):
        self.spriteSheet = pygame.image.load(imagen).convert_alpha()
        self.image = self.spriteSheet.subsurface(0,0,w,h)
        self.rect = pygame.Rect(x, y, w, h)
        self.frames = 4               # Número máximo de imágenes
        self.current_frame = 0        # Imagen actual
        self.frame_width = w         # Anchura de la imagen
        self.frame_height = h       # Altura de la imagen
        self.frame_counter = FPSPRITE # Nº de frames por imagen
        self.trayectoria = [True,False,False,False] #derecha,abajo,izquierda,arriba
        self.dialog=dialog
        self.x=x
        self.y=y

    def animation(self):
        if self.frame_counter == 0:
            self.current_frame = (self.current_frame + 1) % self.frames # siguiente sprite
            self.frame_counter = FPSPRITE
        else:
            self.frame_counter -= 1

        if self.trayectoria[0]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      6*self.frame_height, # fila 6,
                                                      self.frame_width, self.frame_height))
        if self.trayectoria[1]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      0*self.frame_height, # fila 0,
                                                      self.frame_width, self.frame_height))
        if self.trayectoria[2]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      2*self.frame_height, # fila 1,
                                                      self.frame_width, self.frame_height))
        if self.trayectoria[3]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      4*self.frame_height, # fila 2,
                                                      self.frame_width, self.frame_height))

    def move(self, offset, mapa, pj):
        if self.pos_valida(mapa,pj):
            self.rect = self.rect.move(offset) # avanzamos
            #ponemos velocidad baja:
            offset = list(offset)
            if offset[0] != 0: offset[0] = -abs(offset[0])/offset[0]
            if offset[1] != 0: offset[1] = -abs(offset[1])/offset[1]

        while not self.pos_valida(mapa, pj): # mientras la posición no sea válida
            self.rect = self.rect.move(offset) # retrocedemos poco a poco


    def pos_valida(self, mapa, pj):
        return not self.rect.colliderect(pj) and self.rect.top>=0 and \
            self.rect.left>=0 and self.rect.right<=mapa[0] and self.rect.bottom<=mapa[1]


    def camino1(self,mapa, pj):
        if self.trayectoria[0]:
            self.move((5, 0), mapa, pj)
        elif self.trayectoria[1]:
            self.move((0, 5), mapa, pj)
        elif self.trayectoria[2]:
            self.move((-5, 0), mapa, pj)
        elif self.trayectoria[3]:
            self.move((0, -5), mapa, pj)

        if abs(self.rect.centerx-self.x)>=200:
            self.trayectoria = [False,False,False,False]
            self.trayectoria[1]=True
        if abs(self.rect.centery-self.y)>=200 and self.trayectoria[1]:
            self.trayectoria = [False,False,False,False]
            self.trayectoria[2]=True
        if abs(self.rect.centerx-self.x)<=5 and self.trayectoria[2]:
            self.trayectoria = [False,False,False,False]
            self.trayectoria[3]=True
        if abs(self.rect.centery-self.y)<=5 and self.trayectoria[3]:
            self.trayectoria = [False,False,False,False]
            self.trayectoria[0]=True

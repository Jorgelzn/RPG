import pygame
from Variables import *

class Npc:
    def __init__(self, imagen,dialog=None, x=0, y=0, w=200, h=200):
        self.spriteSheet = pygame.image.load(imagen).convert_alpha()
        self.image = self.spriteSheet.subsurface(0,0,w,h)
        self.rect = pygame.Rect(x, y, w, h)
        self.rect_col = pygame.Rect(x+10, y+h-20, w-20, 20)
        self.rect_accion = pygame.Rect(x-20, y-20, w+40, h+40)
        self.frames = 4               # Número máximo de imágenes
        self.current_frame = 0        # Imagen actual
        self.frame_width = w         # Anchura de la imagen
        self.frame_height = h       # Altura de la imagen
        self.frame_counter = FPSPRITE # Nº de frames por imagen
        self.direccion = "derecha" # puede ser "arriba", "abajo", "derecha", "izquierda"
        self.dialog=dialog
        self.x=x
        self.y=y

        self.name = imagen

    def animation(self):
        if self.frame_counter == 0:
            self.current_frame = (self.current_frame + 1) % self.frames # siguiente sprite
            self.frame_counter = FPSPRITE
        else:
            self.frame_counter -= 1

        if self.direccion == "abajo":
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      0*self.frame_height, # fila 0,
                                                      self.frame_width, self.frame_height))
        if self.direccion == "izquierda":
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      2*self.frame_height, # fila 2,
                                                      self.frame_width, self.frame_height))
        if self.direccion == "arriba":
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      4*self.frame_height, # fila 4,
                                                      self.frame_width, self.frame_height))
        if self.direccion == "derecha":
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      6*self.frame_height, # fila 6,
                                                      self.frame_width, self.frame_height))

    def move(self, offset, mapa, pj):
        if self.pos_valida(mapa,pj):
            self.rect_col = self.rect_col.move(offset) # avanzamos
            #ponemos velocidad baja:
            offset = list(offset)
            if offset[0] != 0: offset[0] = -abs(offset[0])/offset[0]
            if offset[1] != 0: offset[1] = -abs(offset[1])/offset[1]

        while not self.pos_valida(mapa, pj): # mientras la posición no sea válida
            self.rect_col = self.rect_col.move(offset) # retrocedemos poco a poco

        self.rect.bottomleft = self.rect_col.bottomleft
        self.rect_accion.bottomleft = self.rect_col.bottomleft

    def pos_valida(self, mapa, pj):
        return not self.rect_col.colliderect(pj) and self.rect.top>=0 and \
            self.rect.left>=0 and self.rect.right<=mapa[0] and self.rect.bottom<=mapa[1]


    def camino1(self,mapa, pj):             #camino predeterminado que pueden recorrer los npcs
        if self.direccion == "derecha":
            self.move((5, 0), mapa, pj)
        elif self.direccion == "abajo":
            self.move((0, 5), mapa, pj)
        elif self.direccion == "izquierda":
            self.move((-5, 0), mapa, pj)
        elif self.direccion == "arriba":
            self.move((0, -5), mapa, pj)

        if abs(self.rect.centerx-self.x)>=200:
            self.direccion = "abajo"
        if abs(self.rect.centery-self.y)>=200 and self.direccion == "abajo":
            self.direccion = "izquierda"
        if abs(self.rect.centerx-self.x)<=5 and self.direccion == "izquierda":
            self.direccion = "arriba"
        if abs(self.rect.centery-self.y)<=5 and self.direccion == "arriba":
            self.direccion = "derecha"



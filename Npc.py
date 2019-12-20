import pygame
from Variables import *

class Npc:
    def __init__(self, imagen,talking,dialog=None, x=0, y=0, w=200, h=200):
        self.spriteSheet = pygame.image.load(imagen).convert_alpha()
        self.image = self.spriteSheet.subsurface(0,0,w,h)
        self.rect = pygame.Rect(x, y, w, h)
        self.rect_col = pygame.Rect(x+10, y+h-20, w-20, 20)
        self.rect_accion = pygame.Rect(x-40, y-40, w+60, h+60)
        self.frames = 4               # Número máximo de imágenes
        self.current_frame = 0        # Imagen actual
        self.frame_width = w         # Anchura de la imagen
        self.frame_height = h       # Altura de la imagen
        self.frame_counter = FPSPRITE # Nº de frames por imagen
        self.direccion = "derecha" # puede ser "arriba", "abajo", "derecha", "izquierda"
        self.dialog=dialog
        self.talking=talking
        self.x=x
        self.y=y

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

    def move(self, offset, mapa, pj,obs):
        self.rect_col = self.rect_col.move(offset) # avanzamos
        self.rect = self.rect.move(offset)
        self.rect_accion = self.rect_accion.move(offset)
        #ponemos velocidad baja:
        offset = list(offset)
        if offset[0] != 0: offset[0] = -abs(offset[0])/offset[0]
        if offset[1] != 0: offset[1] = -abs(offset[1])/offset[1]

        while not self.pos_valida(mapa, pj,obs): # mientras la posición no sea válida
            self.rect_col = self.rect_col.move(offset) # retrocedemos poco a poco
            self.rect = self.rect.move(offset)
            self.rect_accion = self.rect_accion.move(offset)

    def pos_valida(self, mapa, pj,obs):
        a= not self.rect_col.colliderect(pj) and self.rect.top>=0 and \
            self.rect.left>=0 and self.rect.right<=mapa[0] and self.rect.bottom<=mapa[1]
        b=True
        for e in obs:
            if self.rect_col.colliderect(e.rect_col):
                b=False
        return a and b


    def camino1(self,mapa, pj,obs):             #camino predeterminado que pueden recorrer los npcs
        if self.direccion == "derecha":
            self.move((5, 0), mapa, pj,obs)
        elif self.direccion == "abajo":
            self.move((0, 5), mapa, pj,obs)
        elif self.direccion == "izquierda":
            self.move((-5, 0), mapa, pj,obs)
        elif self.direccion == "arriba":
            self.move((0, -5), mapa, pj,obs)

        if abs(self.rect.centerx-self.x)>=200:
            self.direccion = "abajo"
        if abs(self.rect.centery-self.y)>=200 and self.direccion == "abajo":
            self.direccion = "izquierda"
        if abs(self.rect.centerx-self.x)<=5 and self.direccion == "izquierda":
            self.direccion = "arriba"
        if abs(self.rect.centery-self.y)<=5 and self.direccion == "arriba":
            self.direccion = "derecha"

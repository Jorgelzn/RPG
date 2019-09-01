import pygame
from Variables import *

class Obstaculo:
    def __init__(self, imagen, x=0, y=0, w=200, h=200):
        self.spriteSheet = pygame.image.load(imagen).convert_alpha()
        self.image = self.spriteSheet.subsurface(0,0,w,h)
        self.rect = pygame.Rect(x, y, w, h)
        self.frames = 4               # Número máximo de imágenes
        self.current_frame = 0        # Imagen actual
        self.frame_width = w         # Anchura de la imagen
        self.frame_height = h       # Altura de la imagen
        self.frame_counter = FPSPRITE # Nº de frames por imagen

    def animation(self, fila):
        if self.frame_counter == 0:
            self.current_frame = (self.current_frame + 1) % self.frames # siguiente sprite
            self.frame_counter = FPSPRITE
        else:
            self.frame_counter -= 1

        self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                  fila*self.frame_height, # fila 1,
                                                  self.frame_width, self.frame_height))

class Flecha: # se le podría cambiar el nombre a algo maś explicativo
    '''Cualquier objeto que sirva para cambiar de escena (puertas,
    escaleras, flechas laterales...).  Colocarse dentro del sprite y
    pulsar espacio para cambiar de escena

    '''
    def __init__(self, imagen,scene, x=0, y=0, w=200, h=200):
        self.image = pygame.image.load(imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w,h))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.scene = scene


class Objeto:

    def __init__(self, imagen, x=0, y=0, w=200, h=200):
        self.image = pygame.image.load(imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w,h))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

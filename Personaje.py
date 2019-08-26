from pygame import sprite
import pygame
from pygame.locals import *
from Variables import *

class Personaje(sprite.Sprite):

    def __init__(self, x=0, y=0):
        #Init de Sprite
        sprite.Sprite.__init__(self)


        # Variables para nuestro control del sprite:
        self.frames = 4               # Número máximo de imágenes
        self.current_frame = 0        # Imagen actual
        self.frame_width = 115        # Anchura de la imagen
        self.frame_height = 158        # Altura de la imagen
        self.frame_counter = FPSPRITE # Nº de frames por imagen
        # Rectángulo para el sprite:
        self.rect_spr = pygame.Rect(x,y-self.frame_height+20,self.frame_width,self.frame_height)
        # Cargamos la hoja completa de sprites del personaje.
        # Se realiza convert_alpha() para que tenga en cuenta transparencias (capa alpha)


        self.spriteSheet = pygame.image.load("imagenes/Moki.png").convert_alpha()
        # "image" se corresponde con la imagen actual a mostrar.
        self.image = self.spriteSheet.subsurface(136,0,self.frame_width,self.frame_height)
        # Collision box:
        self.rect_col = pygame.Rect(x+23,y,self.frame_width-40,20)

        # Control del movimiento:
        self.speedx = 5
        self.speedy = 5


    def update(self, dt, keys, mapa, obs):
        # animaciones:
        if self.frame_counter == 0:
            self.current_frame = (self.current_frame + 1) % self.frames # siguiente sprite
            self.frame_counter = FPSPRITE
        else:
            self.frame_counter -= 1

        # si no se está moviendo, ponemos sprite normal:
        if not (keys[K_DOWN] or keys[K_LEFT] or keys[K_RIGHT] or keys[K_UP]):
            if self.current_frame == 4 or self.current_frame == 3:
                self.image = self.spriteSheet.subsurface((136,0, self.frame_width, self.frame_height))
            else:
                self.image = self.spriteSheet.subsurface((15,0, self.frame_width, self.frame_height))

        # movimiento y animación según la dirección de movimiento:
        if keys[K_DOWN]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width+136,
                                                      0,
                                                      self.frame_width, self.frame_height))
            self.move((0, self.speedy), mapa, obs)
        if keys[K_LEFT]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width+136,
                                                      self.frame_height,
                                                      self.frame_width, self.frame_height))
            self.move((-self.speedx, 0), mapa, obs)
        if keys[K_RIGHT]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width+136,
                                                      3*self.frame_height,
                                                      self.frame_width, self.frame_height))
            self.move((self.speedx, 0), mapa, obs)
        if keys[K_UP]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width+136,
                                                      2*self.frame_height,
                                                      self.frame_width, self.frame_height))
            self.move((0,-self.speedy), mapa, obs)

    def move(self, offset, mapa, obs):
        self.rect_spr = self.rect_spr.move(offset) # avanzamos
        self.rect_col = self.rect_col.move(offset)
        #ponemos velocidad baja:
        offset = list(offset)
        if offset[0] != 0: offset[0] = -abs(offset[0])/offset[0]
        if offset[1] != 0: offset[1] = -abs(offset[1])/offset[1]

        while not self.pos_valida(mapa, obs): # mientras la posición no sea válida
            self.rect_spr = self.rect_spr.move(offset) # retrocedemos poco a poco
            self.rect_col = self.rect_col.move(offset)

    def pos_valida(self, mapa, obs):
        return self.rect_col.collidelist(obs)==-1 and self.rect_spr.top>=0 and \
            self.rect_spr.left>=0 and self.rect_spr.right<=mapa[0] and self.rect_spr.bottom<=mapa[1]

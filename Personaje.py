from pygame import sprite
import pygame
from pygame.locals import *
from Variables import *

class Personaje(sprite.Sprite):

    def __init__(self, x=0, y=0):
        #Init de Sprite
        sprite.Sprite.__init__(self)
<<<<<<< HEAD

        # Variables para nuestro control del sprite:
        self.frames = 4               # Número máximo de imágenes
        self.current_frame = 0        # Imagen actual
        self.frame_width = 64         # Anchura de la imagen
        self.frame_height = 64        # Altura de la imagen
        self.frame_counter = FPSPRITE # Nº de frames por imagen

        # Cargamos la hoja completa de sprites del personaje.
        # Se realiza convert_alpha() para que tenga en cuenta transparencias (capa alpha)
=======
        ''' Cargamos la hoja completa de sprites del personaje.
            Se realiza convert_alpha() para que tenga en cuenta transparencias (capa alpha)
        '''

>>>>>>> texto
        self.spriteSheet = pygame.image.load("imagenes/pok.png").convert_alpha()
        # "image" se corresponde con la imagen actual a mostrar.
        self.image = self.spriteSheet.subsurface(0,0,self.frame_width,self.frame_height)
        # Collision box:
        self.rect = pygame.Rect(x,y,self.frame_width,20)

        # Control del movimiento:
        self.speedx = 5
        self.speedy = 5
<<<<<<< HEAD
=======

>>>>>>> texto


    def update(self, dt, keys, mapa, obs):
        # animaciones:
        if self.frame_counter == 0:
            self.current_frame = (self.current_frame + 1) % self.frames # siguiente sprite
            self.frame_counter = FPSPRITE
        else:
            self.frame_counter -= 1

        # si no se está moviendo, ponemos sprite normal:
        if not (keys[K_DOWN] or keys[K_LEFT] or keys[K_RIGHT] or keys[K_UP]):
            self.image = self.spriteSheet.subsurface((0,0, self.frame_width, self.frame_height))

        # movimiento y animación según la dirección de movimiento:
        if keys[K_DOWN]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      0,
                                                      self.frame_width, self.frame_height))
            self.move((0, self.speedy), mapa, obs)
        if keys[K_LEFT]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      self.frame_height,
                                                      self.frame_width, self.frame_height))
            self.move((-self.speedx, 0), mapa, obs)
        if keys[K_RIGHT]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      2*self.frame_height,
                                                      self.frame_width, self.frame_height))
            self.move((self.speedx, 0), mapa, obs)
        if keys[K_UP]:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
<<<<<<< HEAD
                                                      3*self.frame_height,
                                                      self.frame_width, self.frame_height))
            self.move((0,-self.speedy), mapa, obs)

    def move(self, offset, mapa, obs):
        self.rect = self.rect.move(offset) # avanzamos
        #ponemos velocidad baja:
        offset = list(offset)
        if offset[0] != 0: offset[0] = -abs(offset[0])/offset[0]
        if offset[1] != 0: offset[1] = -abs(offset[1])/offset[1]
            
        while not self.pos_valida(mapa, obs): # mientras la posición no sea válida
            self.rect = self.rect.move(offset) # retrocedemos poco a poco
            
    def pos_valida(self, mapa, obs):
        return self.rect.collidelist(obs)==-1 and self.rect.bottom-self.frame_height>=0 and \
            self.rect.left>=0 and self.rect.right<=mapa[0] and self.rect.bottom<=mapa[1]
=======
                                                          3*self.frame_height,
                                                          self.frame_width, self.frame_height))
            self.move(0,-self.speedy)



    def move(self, x=0, y=0):
        if self.rect.centerx+x>=self.mapa.width or self.rect.centerx+x <= 0:
            return
        if self.rect.centery+y>=self.mapa.height or self.rect.centery+y <= 0:
            return
        self.rect.center = (self.rect.centerx+x, self.rect.centery+y)
>>>>>>> texto

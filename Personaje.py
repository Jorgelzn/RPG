from pygame import sprite
import pygame
from pygame.locals import *
from Variables import *

class Personaje(sprite.Sprite):

    def __init__(self,mapa,pantalla,x=0, y=0,):
        #Init de Sprite
        sprite.Sprite.__init__(self)
        ''' Cargamos la hoja completa de sprites del personaje.
            Se realiza convert_alpha() para que tenga en cuenta transparencias (capa alpha)
        '''
        self.pantalla=pantalla
        self.spriteSheet = pygame.image.load("imagenes/pok.png").convert_alpha()
        # "image" se corresponde con la imagen actual a mostrar.
        #La hacemos más pequeña para que quede mejor
        self.image = self.spriteSheet.subsurface((0,0,64,64))
        #Necesario para mostrar la imagen
        self.rect = self.image.get_rect()
        #Donde se situa la imagen.
        if(x==0 and y ==0):
            self.rect.center = (mapa[0]/2, mapa[1]/2)
        else:
            self.rect.center = (x, y)

        self.mapa = Rect(0,0,mapa[0],mapa[1])

        ''' Variables para nuestro control del sprite
        '''
        self.frames = 4             #Número máximo de imágenes
        self.current_frame = 0      #Frame actual
        self.nframes = 4 # number of sprites/direction
        self.frame_width = 64     #Anchura de la imagen
        self.frame_height = 64     #Altura dela imagen
        self.frame_counter = FPSPRITE     #number of frames per sprite
        self.speedx = 5
        self.speedy = 5

        self.saltando = False
        self.suelo()

    def update(self, dt, keys):

        if self.frame_counter == 0:
            self.current_frame = (self.current_frame + 1) % self.nframes # next sprite
            self.frame_counter = FPSPRITE
        else:
            self.frame_counter -= 1

        if keys[K_DOWN] :
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                          0,
                                                          self.frame_width, self.frame_height))
            self.move(0, self.speedy)
        if keys[K_LEFT] :
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                          self.frame_height,
                                                          self.frame_width, self.frame_height))
            self.move(-self.speedx)
        if keys[K_RIGHT] :
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                          2*self.frame_height,
                                                          self.frame_width, self.frame_height))
            self.move(self.speedx)
        if keys[K_UP] :
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                          3*self.frame_height,
                                                          self.frame_width, self.frame_height))
            self.move(0,-self.speedy)

        if keys[K_SPACE] and not self.saltando:
            self.saltando = True
            self.speedy = -10

        if self.saltando :
            self.move(0, self.speedy)
            self.speedy += 1

        if self.suelo():
            self.move(0, 2)

        #if self.rect.bottom >= 560:
            #self.saltando = False
            #self.speedy = 0

        if not (keys[K_DOWN] or keys[K_LEFT] or keys[K_RIGHT] or keys[K_UP]):
            self.image = self.spriteSheet.subsurface((0,0, self.frame_width, self.frame_height))
                # if not moving, set standing sprite

    def move(self, x=0, y=0):
        if self.rect.centerx+x>=self.mapa.width or self.rect.centerx+x <= 0:
            return
        if self.rect.centery+y>=self.mapa.height or self.rect.centery+y <= 0:
            return
        self.rect.center = (self.rect.centerx+x, self.rect.centery+y)

    def suelo(self):
        lista = []
        for e in range(self.rect.width):
            lista.append(self.pantalla.get_at((self.rect.left + e, self.rect.bottom + 1)))
            print(lista[e])

        contador = 0
        for x in lista:
            if abs(x[0] - 50) < 50 and abs(x[1] - 120) < 50 and abs(x[2] - 240) < 50:
                contador += 1

        return contador > 30

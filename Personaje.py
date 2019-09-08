from pygame import sprite
import pygame
from pygame.locals import *
from Variables import *
from sonidos import Sonido

class Personaje(sprite.Sprite):

    def __init__(self, x=0, y=0):
        #Init de Sprite
        sprite.Sprite.__init__(self)


        # Variables para nuestro control del sprite:
        self.frames = 4               # Número máximo de imágenes
        self.current_frame = 0        # Imagen actual
        self.frame_width = 82         # Anchura de la imagen
        self.frame_height = 128       # Altura de la imagen
        self.frame_counter = FPSPRITE # Nº de frames por imagen
        # Rectángulo para el sprite:
        self.rect_spr = pygame.Rect(x,y-self.frame_height+20,self.frame_width,self.frame_height)
        # Cargamos la hoja completa de sprites del personaje.
        # Se realiza convert_alpha() para que tenga en cuenta transparencias (capa alpha)
        self.lastdir=[False,False,False,False] #(arriba,abajo,derecha,izquierda)

        self.spriteSheet = pygame.image.load("imagenes/personajes/Moki_sheet.png").convert_alpha()
        # "image" se corresponde con la imagen actual a mostrar.
        self.image = self.spriteSheet.subsurface(0,0,self.frame_width,self.frame_height)
        # Collision box:
        self.rect_col = pygame.Rect(x,y,self.frame_width,20)

        # Control del movimiento:
        self.speedx = 5
        self.speedy = 5

        self.objects=[]         #objetos del personaje
        self.action=False       #controla si el pj esta haciendo algo


    def update(self, dt, keys, mapa, obs,sound):

            if keys[K_LSHIFT]:      #con la tecla pulsada aumenta la velocidad
                self.speedx=10
                self.speedy=10
                FPSPRITE=3
            else:
                self.speedx=5
                self.speedy=5
                FPSPRITE=10

            # animaciones:
            if self.frame_counter == 0:
                self.current_frame = (self.current_frame + 1) % self.frames # siguiente sprite
                self.frame_counter = FPSPRITE
            else:
                self.frame_counter -= 1

            if self.action:                 #(solo para flauta provisional) animaciones de tocar la flauta
                if self.current_frame==1:
                    self.image = pygame.image.load("imagenes/personajes/actions/flute/flute.png").convert_alpha()
                elif self.current_frame==2:
                    self.image = pygame.image.load("imagenes/personajes/actions/flute/flute2.png").convert_alpha()
                elif self.current_frame==3 or self.current_frame==0:
                    self.image = pygame.image.load("imagenes/personajes/actions/flute/flute3.png").convert_alpha()
            else:
            # si no se está moviendo, ponemos sprite normal:
                if not (keys[K_s] or keys[K_a] or keys[K_d] or keys[K_w]):
                    if self.lastdir[0]:
                        self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                                  5*self.frame_height, # fila 6,
                                                                  self.frame_width, self.frame_height))
                    elif self.lastdir[1]:
                        self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                                  self.frame_height, # fila 1,
                                                                  self.frame_width, self.frame_height))
                    elif self.lastdir[2]:
                        self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                                  7*self.frame_height, # fila 7,
                                                                  self.frame_width, self.frame_height))
                    elif self.lastdir[3]:
                        self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                                  3*self.frame_height, # fila 3,
                                                                  self.frame_width, self.frame_height))
                elif keys[K_s] and not keys[K_a] and not keys[K_d] and not keys[K_w]:
                    self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                              0, # fila 0
                                                              self.frame_width, self.frame_height))
                    for e in range(4):
                        self.lastdir[e]=False
                    self.lastdir[1]=True
                    self.move((0, self.speedy), mapa, obs,sound)
                elif keys[K_a] and not keys[K_s] and not keys[K_d] and not keys[K_w]:
                    self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                              2*self.frame_height, # fila 2
                                                              self.frame_width, self.frame_height))
                    for e in range(4):
                        self.lastdir[e]=False
                    self.lastdir[3]=True
                    self.move((-self.speedx, 0), mapa, obs,sound)
                elif keys[K_d] and not keys[K_a] and not keys[K_s] and not keys[K_w]:
                    self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                              6*self.frame_height, # fila 6
                                                              self.frame_width, self.frame_height))
                    for e in range(4):
                        self.lastdir[e]=False
                    self.lastdir[2]=True
                    self.move((self.speedx, 0), mapa, obs,sound)
                elif keys[K_w] and not keys[K_a] and not keys[K_d] and not keys[K_s]:
                    self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                              4*self.frame_height, # fila 4
                                                              self.frame_width, self.frame_height))
                    for e in range(4):
                        self.lastdir[e]=False
                    self.lastdir[0]=True
                    self.move((0,-self.speedy), mapa, obs,sound)


    def move(self, offset, mapa, obs,sound):
        if self.pos_valida(mapa,obs):
            self.rect_spr = self.rect_spr.move(offset) # avanzamos
            self.rect_col = self.rect_col.move(offset)
            sound.play()
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


    def objectAct(self,keys,soundtrack,text):     #controla lo que hace el pj con el objeto equipado
        if keys[K_c] and not self.action and not text.display and not text.displayInventario and not text.displayMap and not text.displayMenu:
            for e in self.objects:
                pos=text.posInventario[text.selecPos[0]][text.selecPos[1]].topleft
                if e.taken and pos[0]==e.posx and pos[1]==e.posy:
                    pygame.mixer_music.load(Sonido().flute)
                    pygame.mixer.music.play()
                    self.action= True
        elif self.action and keys[K_c]:             #vuelves a pulsar c y la accion se detiene
            self.action=False
            pygame.mixer_music.load(soundtrack)
            pygame.mixer.music.play()

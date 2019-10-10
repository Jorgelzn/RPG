from pygame import sprite
import pygame
from pygame.locals import *
from Variables import *
from Escenario import Objeto
from sonidos import Sonido

class Personaje(sprite.Sprite):

    def __init__(self, x=0, y=0,):
        #Init de Sprite
        sprite.Sprite.__init__(self)

        self.order=True

        # Variables para nuestro control del sprite:
        self.frames = 4               # Número máximo de imágenes
        self.current_frame = 0        # Imagen actual
        self.frame_width = 82         # Anchura de la imagen
        self.frame_height = 128       # Altura de la imagen
        self.frame_counter = FPSPRITE # Nº de frames por imagen

        # Rectángulos para el personaje:
        self.rect_spr = pygame.Rect(x,y-self.frame_height+20,self.frame_width,self.frame_height) # para el sprite
        self.rect_col = pygame.Rect(x,y,self.frame_width,20) # collision box

        # Cargamos la hoja completa de sprites del personaje.
        # Se realiza convert_alpha() para que tenga en cuenta transparencias (capa alpha)
        self.spriteSheet = pygame.image.load("imagenes/personajes/Moki_sheet.png").convert_alpha()
        # "image" se corresponde con la imagen actual a mostrar.
        self.image = self.spriteSheet.subsurface(0,0,self.frame_width,self.frame_height)

        # Control del movimiento:
        self.speedx = 5
        self.speedy = 5
        self.mapa = 0
        self.lastdir = None # puede ser "arriba", "abajo", "derecha", "izquierda", None

        self.objects=[Objeto("imagenes/objetos/Flute.png",100,"Nadie puede resistirse al poder de la musica",700,700,60,60,210,140,174,120,objects[0])]         #objetos del personaje
        self.action=False       #controla si el pj esta haciendo algo


    def update(self, dt, keys, mapa,npcs,obs,objs,sound):

        for e in npcs:
            if self.rect_spr.colliderect(e.rect_accion):
                if self.rect_col.centery<e.rect_col.centery:
                    self.order=False
                else:
                    self.order=True

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
            if self.current_frame==0 or self.current_frame==2:
                self.image = pygame.image.load("imagenes/personajes/actions/flute/flute.png").convert_alpha()
            elif self.current_frame==1:
                self.image = pygame.image.load("imagenes/personajes/actions/flute/flute2.png").convert_alpha()
            elif self.current_frame==3:
                self.image = pygame.image.load("imagenes/personajes/actions/flute/flute3.png").convert_alpha()
        else: # gestión de movimientos:
            if keys[K_s] and not keys[K_a] and not keys[K_d] and not keys[K_w]: # pulsando solo la s
                self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                          0, # fila 0
                                                          self.frame_width, self.frame_height))
                self.lastdir = "abajo"
                self.move((0, self.speedy), mapa, npcs, obs,objs, sound)
            elif keys[K_a] and not keys[K_s] and not keys[K_d] and not keys[K_w]: # pulsando solo la a
                self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                          2*self.frame_height, # fila 2
                                                          self.frame_width, self.frame_height))
                self.lastdir = "izquierda"
                self.move((-self.speedx, 0), mapa, npcs, obs,objs, sound)
            elif keys[K_w] and not keys[K_a] and not keys[K_d] and not keys[K_s]: # pulsando solo la w
                self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                          4*self.frame_height, # fila 4
                                                          self.frame_width, self.frame_height))
                self.lastdir = "arriba"
                self.move((0,-self.speedy), mapa, npcs, obs,objs, sound)
            elif keys[K_d] and not keys[K_a] and not keys[K_s] and not keys[K_w]: # pulsando solo la d
                self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                          6*self.frame_height, # fila 6
                                                          self.frame_width, self.frame_height))
                self.lastdir = "derecha"
                self.move((self.speedx, 0), mapa, npcs, obs,objs, sound)

            else: # ninguna tecla o más de una: quedarse quieto
                if self.lastdir == "abajo" or self.lastdir == None:
                    self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                            self.frame_height, # fila 1
                                                            self.frame_width, self.frame_height))
                if self.lastdir == "izquierda":
                    self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                            3*self.frame_height, # fila 3
                                                            self.frame_width, self.frame_height))
                if self.lastdir == "arriba":
                    self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                            5*self.frame_height, # fila 5
                                                            self.frame_width, self.frame_height))
                if self.lastdir == "derecha":
                    self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                            7*self.frame_height, # fila 7
                                                            self.frame_width, self.frame_height))

    def move(self, offset, mapa, npcs, obs, objs,sound):
        self.rect_col = self.rect_col.move(offset) # avanzamos
        self.rect_spr = self.rect_spr.move(offset)
        #sound.play()
        #ponemos velocidad baja:
        offset = list(offset)
        if offset[0] != 0: offset[0] = -abs(offset[0])/offset[0]
        if offset[1] != 0: offset[1] = -abs(offset[1])/offset[1]

        while not self.pos_valida(mapa, npcs, obs, objs): # mientras la posición no sea válida
            self.rect_col = self.rect_col.move(offset) # retrocedemos poco a poco
            self.rect_spr = self.rect_spr.move(offset)

    def pos_valida(self, mapa, npcs, obs, objs):
        a = self.rect_col.collidelist([npc.rect_col for npc in npcs])==-1 and self.rect_spr.top>=0 and self.rect_spr.left>=0 and self.rect_spr.right<=mapa[0] and self.rect_spr.bottom<=mapa[1]
        b=True
        c=True
        for e in obs:
            if self.rect_col.colliderect(e.rect) and e.portal==False:
                c=False
        for e in objs:
            if self.rect_col.colliderect(e.rect) and e.taken==False:
                b= False
        return a and b and c


    def objectAct(self,keys,soundtrack,text):     #controla lo que hace el pj con el objeto equipado
        if keys[K_c] and not self.action and not text.display and not text.displayInventario and not text.displayMap and not text.displayMenu:
            for e in self.objects:
                pos=text.posInventario[text.selecPos[0]][text.selecPos[1]].topleft
                if e.taken and pos[0]==e.posx and pos[1]==e.posy:
                    pygame.mixer_music.load(flute)
                    pygame.mixer.music.play()
                    self.action= True
        elif self.action and keys[K_c]:             #vuelves a pulsar c y la accion se detiene
            self.action=False
            pygame.mixer.music.load(soundtrack)
            pygame.mixer.music.play()

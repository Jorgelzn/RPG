from pygame import sprite
import pygame
class Personaje(sprite.Sprite):

    def __init__(self,ventana,x=0, y=0,):
        #Init de Sprite
        sprite.Sprite.__init__(self)
        ''' Cargamos la hoja completa de sprites del personaje.
            Se realiza convert_alpha() para que tenga en cuenta transparencias (capa alpha)
        '''
        self.spriteSheet = pygame.image.load("D:/pok.png").convert_alpha()
        # "image" se corresponde con la imagen actual a mostrar.
        #La hacemos más pequeña para que quede mejor
        self.image = self.spriteSheet.subsurface((0,0,64,64))
        #Necesario para mostrar la imagen
        self.rect = self.image.get_rect()
        #Donde se situa la imagen.
        if(x==0 and y ==0):
            self.rect.center = (ventana.get_width()/2, ventana.get_height()/2)
        else:
            self.rect.center = (x, y)

        self.ventana = ventana



        ''' Variables para nuestro control del sprite
        '''
        self.frames = 4             #Número máximo de imágenes
        self.current_frame = 0      #Frame actual
        self.frame_width = 64     #Anchura de la imagen
        self.frame_height = 64     #Altura dela imagen

        self.speed = 10

    #Método heredado de la clase Sprite
    def update(self, dt):
        ''' Aquí es donde se realizarán las actualizaciones del personaje.
            Es decir, movimiento, cambios en el sprite, cambios
            de atributos como puede ser la vida...

            En este caso, si se llega al límite de frames se reinicia.
            De esta forma estará animándo siempre en bucle.
        '''
        if self.current_frame > 3.5:
            self.current_frame = 0
        #Si no se llega, se sigue aumentando
        else:
            #Hacemos x3 por que queremos que salgan 3 imágenes por segundow
            self.current_frame += 3*dt

        ''' Una vez actualizados los frames, se actualiza la imagen actual del personaje.

            Para ello, realizamos el mismo recorte que antes, pero la diferencia
            principal ahora es que la imagen que se recorta, va a
            depender del frame (momento actual) en el que nos situemos.
        '''
        # print(int(self.current_frame)*self.frame_width)
        self.image = self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width,0,64,64))


    def mover(self, x=0, y=0):
        if self.rect.centerx+x>=self.ventana.get_width() or self.rect.centerx+x <= 0:
            return
        if self.rect.centery+y>=self.ventana.get_height()-5 or self.rect.centery+y <= 0:
            return
        self.rect.center = (self.rect.centerx+x, self.rect.centery+y)

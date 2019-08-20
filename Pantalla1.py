from Scene import Scene
from Personaje import Personaje
import pygame
from pygame.locals import *

class Pantalla1(Scene):
    ''' Esta pantalla va a tener el color azul.
        Cuando se presione la tecla "Enter" lo que
        se va a hacer es cambiar de escena a "Pantalla2"
    '''
    def __init__(self, director):
        Scene.__init__(self, director)
        self.pj = Personaje(director.screen)
        self.otherpj = Personaje(director.screen,200, 200)

    def on_update(self, time, data_events):
        self.pj.update(time/1000)
        self.otherpj.update(time/1000)
        self.pj.mover(data_events[0], data_events[1])

    def on_event(self, time, event):
        ''' El director pasa aquí los eventos que ha captado
        '''
        yspeed = 0
        xspeed = 0
        if event.type == KEYDOWN:   #Si el usuario ha presionado una tecla
            #Recuperamos las teclas presionadas
            keys = pygame.key.get_pressed()
            if keys[K_RETURN]:  #Presiona la tecla de "Enter":
                #Creamos la nueva escena y le decimos
                # al director que ahora queremos esa
                self.director.change_scene(Pantalla2(self.director))

            if keys[K_w]:
                yspeed = -5
            if keys[K_s]:
                yspeed = 5
            if keys[K_d]:
                xspeed = 5
            if keys[K_a]:
                xspeed = -5
        return (xspeed, yspeed)


    def on_draw(self, screen):
        #se pone la pantalla de color azul
        screen.fill((0,0,0))
        screen.blit(self.otherpj.image, self.otherpj.rect)
        screen.blit(self.pj.image, self.pj.rect)

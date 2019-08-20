from Scene import Scene
from Personaje import Personaje
import Camara
import pygame
from pygame.locals import *

class Pantalla1(Scene):
    ''' Esta pantalla va a tener el color azul.
        Cuando se presione la tecla "Enter" lo que
        se va a hacer es cambiar de escena a "Pantalla2"
    '''
    def __init__(self, director):
        Scene.__init__(self, director)
        self.camera = Camara.Camera(Camara.complex_camera,1000, 1000, director)
        self.pj = Personaje(self.camera.state, 300, 300)
        self.otherpj1 = Personaje(self.camera.state,1, 1)
        self.otherpj2 = Personaje(self.camera.state,999, 1)
        self.otherpj3 = Personaje(self.camera.state,999, 999)
        self.otherpj4 = Personaje(self.camera.state,1, 999)
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)
        self.ingame_elemets.add(self.otherpj1)
        self.ingame_elemets.add(self.otherpj2)
        self.ingame_elemets.add(self.otherpj3)
        self.ingame_elemets.add(self.otherpj4)

    def on_update(self, time, data_events):
        self.camera.update(self.pj)
        self.ingame_elemets.update(time/1000)
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
        screen.fill((0,100,0))

        for i in self.ingame_elemets:
            screen.blit(i.image, self.camera.apply(i))

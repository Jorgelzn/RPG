from Scene import Scene
from Personaje import Personaje
import Camara
import pygame
from pygame.locals import *
from Variables import *

class Pantalla1(Scene):

    def __init__(self, director):
        Scene.__init__(self, director)
        self.camera = Camara.Camera(Camara.complex_camera,map1)
        self.pj = Personaje(map1, 300, 300)
        self.otherpj1 = Personaje(map1,1, 1)
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)
        self.ingame_elemets.add(self.otherpj1)
        self.background = pygame.image.load("imagenes/background.png").convert_alpha()

    def on_update(self, time,keys):

        self.camera.update(self.pj)
        self.ingame_elemets.update(time/1000, keys)

    def on_draw(self, screen):
        screen.blit(self.background, self.camera.apply(self.background.get_rect()))
        for i in self.ingame_elemets:
            screen.blit(i.image, self.camera.apply(i.rect))

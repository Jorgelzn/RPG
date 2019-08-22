from Scene import Scene
from Personaje import Personaje
import Camara
import pygame
from pygame.locals import *
from Variables import *

class Pantalla1(Scene):

    def __init__(self,map,image):
        Scene.__init__(self, map,image)
        self.pj = Personaje(map, 300, 300)
        self.otherpj1 = Personaje(map)
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)
        self.ingame_elemets.add(self.otherpj1)

    def on_update(self, time,keys):
        self.camera.update(self.pj)
        self.ingame_elemets.update(time/1000, keys)

    def on_draw(self, screen):
        screen.blit(self.background, self.camera.apply(self.background.get_rect()))
        for i in self.ingame_elemets:
            screen.blit(i.image, self.camera.apply(i.rect))

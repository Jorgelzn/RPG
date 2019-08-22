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
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)

    def on_update(self, time,keys):
        self.camera.update(self.pj)
        self.ingame_elemets.update(time/1000, keys)
        if keys[K_RETURN]:
            return Pantalla2(map2,"imagenes/test.png")
        else: return None


    def on_draw(self, screen):
        screen.blit(self.background, self.camera.apply(self.background.get_rect()))
        for i in self.ingame_elemets:
            screen.blit(i.image, self.camera.apply(i.rect))


class Pantalla2(Scene):

    def __init__(self,map,image):
        Scene.__init__(self, map,image)
        self.background = pygame.transform.scale(self.background,(10000,5000))
        Scene.__init__(self, map,image)
        self.pj = Personaje(map, 300, 300)
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)

    def on_update(self, time,keys):
        self.camera.update(self.pj)
        self.ingame_elemets.update(time/1000, keys)

    def on_draw(self, screen):
        screen.blit(self.background, self.camera.apply(self.background.get_rect()))
        for i in self.ingame_elemets:
            screen.blit(i.image, self.camera.apply(i.rect))

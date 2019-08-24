from Scene import Scene
from Personaje import Personaje
from Escenarios import Plataforma
import Camara
import pygame
from pygame.locals import *
from Variables import *

class Pantalla1(Scene):

    def __init__(self, map, image):
        Scene.__init__(self, map, image)
        self.pj = Personaje(200, 200)
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)
        self.mapa = map

        self.obs = [
            Plataforma(150, 500),
            Plataforma(550, 500),
            Plataforma(0, 700, 1000, 5)
        ]

    def on_update(self, time, keys):
        self.camera.update(self.pj)
        self.ingame_elemets.update(time/1000, keys, self.mapa, self.obs)

        if keys[K_RETURN]:
            return Pantalla2(map2,"imagenes/test.png")
        else: return None


    def on_draw(self, screen):
        screen.blit(self.background, self.camera.apply(self.background.get_rect()))
        for i in self.ingame_elemets:
            screen.blit(i.image, self.camera.apply(i.rect).move(0, -44))

        for o in self.obs:
            screen.blit(o.image, o.rect)
        pygame.draw.rect(screen, (0,0,127), self.pj.rect)


class Pantalla2(Scene):

    def __init__(self,map,image):
        Scene.__init__(self, map,image)
        self.background = pygame.transform.scale(self.background,(10000,5000))
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

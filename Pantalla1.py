from Scene import Scene
from Personaje import Personaje
from Escenarios import *
import Camara
import pygame
from pygame.locals import *
from Variables import *

class Pantalla1(Scene):

    def __init__(self, map, image):
        Scene.__init__(self, map, image)
        self.pj = Personaje(500, 200)
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)
        self.mapa = map

        self.obs = [
            Obstaculo("imagenes/snorlax.png", 100, 150),
            Obstaculo("imagenes/snorlax.png", 500, 500)
        ]

    def on_update(self, time, keys):
        self.camera.update(self.pj)
        self.ingame_elemets.update(time/1000, keys, self.mapa, self.obs)

        if keys[K_RETURN]:
            return Pantalla2(map2,"imagenes/test.png")
        else: return None


    def on_draw(self, screen):
        # fondo:
        screen.blit(self.background, self.camera.apply(self.background.get_rect()))
        # obstáculos / decorado:
        for o in self.obs:
            screen.blit(o.image, o.rect)
        # personaje:
        for i in self.ingame_elemets:
            screen.blit(i.image, self.camera.apply(i.rect).move(0, -44))
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

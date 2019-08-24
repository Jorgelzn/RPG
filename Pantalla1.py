from Scene import Scene
from Personaje import Personaje
from Escenarios import Plataforma
import Camara
import pygame
from pygame.locals import *
from Variables import *
from text import Text

class Pantalla1(Scene):

    def __init__(self,map,image):
        Scene.__init__(self, map, image)
        self.pj = Personaje(map, 200, 200)
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)
        self.text=Text()
        self.soundtrack= pygame.mixer.music.load("sonidos/Moki_Town.mp3")
        pygame.mixer.music.play()
        self.plataformas = [
            Plataforma(150, 500),
            Plataforma(550, 500),
            Plataforma(0, 700, 1000, 5)
        ]

    def on_update(self, time,keys):
        if not self.text.display:
            self.camera.update(self.pj)
            self.ingame_elemets.update(time/1000, keys)

        if keys[K_RETURN]:
                return Pantalla2(map2,"imagenes/test.png")
        else: return None

    def on_event(self,keys, screen):
        if keys[K_r]:
            if self.pj.rect.centerx>=480 and self.pj.rect.centerx<=520:
                self.text.dialog2()

            else:
                self.text.dialog1()
            self.event = False




    def on_draw(self, screen):
        if self.text.display:
            screen.blit(self.text.image, self.text.rect)
            screen.blit(self.text.text, self.text.rectext)
        else:
            screen.blit(self.background, self.camera.apply(self.background.get_rect()))
            for i in self.ingame_elemets:
                screen.blit(i.image, self.camera.apply(i.rect))
        #pygame.draw.rect(screen, (0,0,127), self.pj.rect)



class Pantalla2(Scene):

    def __init__(self,map,image):
        Scene.__init__(self, map,image)
        self.background = pygame.transform.scale(self.background,(10000,5000))
        self.pj = Personaje(map, 300, 300)
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)
        self.text=Text()

    def on_update(self, time,keys):
        if not self.text.display:
            self.camera.update(self.pj)
            self.ingame_elemets.update(time/1000, keys)



    def on_event(self,keys, screen):
        if keys[K_r]:
            self.text.dialog1(keys, screen)

    def on_draw(self, screen):
        if self.text.display:
            screen.blit(self.text.image, self.text.image.get_rect())
            screen.blit(self.text.text, self.text.text.get_rect())
        else:
            screen.blit(self.background, self.camera.apply(self.background.get_rect()))
            for i in self.ingame_elemets:
                screen.blit(i.image, self.camera.apply(i.rect))

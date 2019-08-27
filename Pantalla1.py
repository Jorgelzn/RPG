from Scene import Scene
from Personaje import Personaje
from Escenarios import *
import Camara
import pygame
from pygame.locals import *
from Variables import *
from text import Text
from sonidos import Sonido


class Pantalla1(Scene):

    def __init__(self, map, image):
        Scene.__init__(self, map, image)
        self.pj = Personaje(500, 200)
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)
        self.mapa = map
        self.sonido = Sonido()
        self.obs = [
            Obstaculo("imagenes/paperi_sheet.png", 100, 100, 68, 189),
            Obstaculo("imagenes/Peto_sheet.png",500, 600, 119, 145)
        ]
        self.text=Text()

        self.soundtrack= self.sonido.soundtrack1
        pygame.mixer.music.play()


    def on_update(self, time,keys):
        if not self.text.display and not self.text.displayMenu:
            self.camera.update(self.pj)
            self.ingame_elemets.update(time/1000, keys,self.mapa,self.obs)
            self.obs[0].animation(0)
            self.obs[1].animation(1)

        if keys[K_RETURN]:
                return Pantalla2(map2,"imagenes/test.png")
        else: return None


    def on_event(self,keys):
        if keys[K_r] and not self.text.displayMenu:
            if abs(self.pj.rect_col.centerx-self.obs[0].rect.centerx)<=100 and abs(self.pj.rect_col.centery-self.obs[0].rect.centery)<=200:
                self.text.dialog2()
            elif abs(self.pj.rect_col.centerx-self.obs[1].rect.centerx)<=100 and abs(self.pj.rect_col.centery-self.obs[1].rect.centery)<=200:
                self.text.dialog1()
        self.text.menu(keys)



    def on_draw(self, screen):
        self.text.displays(screen)
        if not self.text.display and not self.text.displayMenu:
            screen.blit(self.background, self.camera.apply(self.background.get_rect()))
            for o in self.obs:
                screen.blit(o.image, self.camera.apply(o.rect))
            for i in self.ingame_elemets:
                screen.blit(i.image, self.camera.apply(i.rect_spr))
            #pygame.draw.rect(screen, (0,100,200), self.camera.apply(self.pj.rect_col))


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

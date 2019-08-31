from Scene import Scene
from Personaje import Personaje
from Npc import *
import Camara
import pygame
from pygame.locals import *
from Variables import *
from text import Text
from sonidos import Sonido


class Pantalla1(Scene):

    def __init__(self, map, image):
        Scene.__init__(self, map, image)
        self.pj = Personaje(pjx, pjy)
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)
        self.mapa = map
        self.sonido = Sonido()
        self.npcs = [
            Npc("imagenes/personajes/paperi_sheet.png", 600, 100, 68, 189),
            Npc("imagenes/personajes/Peto_sheet.png",500, 600, 114, 145),
            Npc("imagenes/personajes/Tapa_sheet.png",1200, 600, 68, 77)
        ]
        self.ob = pygame.image.load("imagenes/ob.png").convert_alpha()
        self.text=Text()

        self.soundtrack= self.sonido.soundtrack1
        #pygame.mixer.music.play()
        self.test=True


    def on_update(self, time,keys):
        if not self.text.display and not self.text.displayMenu:
            self.camera.update(self.pj)
            self.ingame_elemets.update(time/1000, keys,self.mapa,self.npcs,self.sonido.grass)
            for e in range(len(self.npcs)):
                self.npcs[e].animation()
                self.npcs[e].camino1(self.mapa, self.pj.rect_col)
            if self.pj.rect_col.colliderect(self.ob.get_rect()) and self.test:
                self.sonido.object.play()
                self.test= False
                self.pj.objets.append("object1")
                self.text.objectsText.append(self.text.fontMenu.render('object1', True, self.text.textcolor3))

        if keys[K_l]:
                return Pantalla2(map2,"imagenes/test.png")
        else: return None


    def on_event(self,keys,director):
        if keys[K_r] and not self.text.displayMenu:
            if abs(self.pj.rect_spr.centerx-self.npcs[0].rect.centerx)<=100 and abs(self.pj.rect_spr.centery-self.npcs[0].rect.centery)<=100:
                self.text.dialog2()
            elif abs(self.pj.rect_spr.centerx-self.npcs[1].rect.centerx)<=100 and abs(self.pj.rect_spr.centery-self.npcs[1].rect.centery)<=100:
                self.text.dialog1()
        self.text.menu(keys,self.pj,director)



    def on_draw(self, screen):
        self.text.displays(screen)
        if not self.text.display and not self.text.displayMenu:
            screen.blit(self.background, self.camera.apply(self.background.get_rect()))
            if self.test:
                screen.blit(self.ob,self.camera.apply(self.ob.get_rect()))
            for o in self.npcs:
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

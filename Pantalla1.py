from Scene import Scene
from Personaje import Personaje
from Npc import *
import Camara
import pygame
from pygame.locals import *
from Variables import *
from text import Text
from sonidos import Sonido
from Escenario import *

class Pantalla1(Scene):

    def __init__(self, map, image):
        Scene.__init__(self, map, image)
        self.pj = Personaje(pjx, pjy)
        self.ingame_elemets = pygame.sprite.Group()
        self.ingame_elemets.add(self.pj)
        self.mapa = map
        self.sonido = Sonido()
        self.npcs = [
            Npc("imagenes/personajes/paperi_sheet.png",["hola","soy paperi","buenos dias"], 600, 100, 68, 189),
            Npc("imagenes/personajes/Peto_sheet.png",["paperi siempre esta igual","deberiamos llamarnos peto y paperi","mamahuevo"],500, 600, 114, 145),
            Npc("imagenes/personajes/Tapa_sheet.png",["me llamo Tapa :D","vente luego a jugar"],1200, 600, 68, 77),
            Npc("imagenes/personajes/Kea_sheet.png",["me preocupan paperi y peto","no paran de pelear"],1200, 200, 84, 132)
        ]
        self.objetos=[
            Objeto("imagenes/objetos/Flute.png",100,"Nadie puede resistirse al poder de la musica",700,700,60,60,175,120)
        ]
        self.text=Text(self.pj)

        self.soundtrack= self.sonido.soundtrack1
        pygame.mixer_music.load(self.soundtrack)
        pygame.mixer.music.play()


    def on_update(self, time,keys):

        if not self.text.display and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:        #si no estamos mostrando texto
            self.camera.update(self.pj)     #update a la camara
            self.ingame_elemets.update(time/1000, keys,self.mapa,self.npcs,self.sonido.grass) #update del personaje

            for e in range(len(self.npcs)):
                self.npcs[e].animation()    #animaciones de los npcs
                self.npcs[e].camino1(self.mapa, self.pj.rect_col)   #camino que recorren los npcs (provisional)

            for e in self.objetos:                                      #si chocas al objeto lo coges (provisional)
                if self.pj.rect_col.colliderect(e.rect) and not e.taken:
                    self.pj.objects.append(e)
                    e.taken=True

        if keys[K_l]:                           #provisional:pulsando l cambiamos de escena
                return Pantalla2(map2,"imagenes/mapas/test.png")
        else: return None


    def on_event(self,keys,director):
        if keys[K_r] and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:
            if abs(self.pj.rect_spr.centerx-self.npcs[0].rect.centerx)<=100 and abs(self.pj.rect_spr.centery-self.npcs[0].rect.centery)<=100:
                self.text.dialog(self.npcs[0].dialog)
            elif abs(self.pj.rect_spr.centerx-self.npcs[1].rect.centerx)<=100 and abs(self.pj.rect_spr.centery-self.npcs[1].rect.centery)<=100:
                self.text.dialog(self.npcs[1].dialog)       #control de colision con npcs (provisional)

        self.text.menu(keys,self.pj,director)     #control del menu
        self.pj.objectAct(keys,self.soundtrack,self.text)   #accion que realiza el personaje con los objetos (actualizable)



    def on_draw(self, screen):
        screen.blit(self.background, self.camera.apply(self.background.get_rect()))
        for o in self.npcs:
            screen.blit(o.image, self.camera.apply(o.rect))
        for i in self.ingame_elemets:
            screen.blit(i.image, self.camera.apply(i.rect_spr))
        for e in self.objetos:
            if not e.taken:
                screen.blit(e.image, self.camera.apply(e.rect))
        #dibujo de fondo necesario para limpiar los menus (un poco chapuza, a si que provisional)

        self.text.displays(screen)  #funcion que controla que se dibujen los textos y menus
        if not self.text.display and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:
            screen.blit(self.background, self.camera.apply(self.background.get_rect())) #dibujado de elementos ingame
            for o in self.npcs:
                screen.blit(o.image, self.camera.apply(o.rect))
            for i in self.ingame_elemets:
                screen.blit(i.image, self.camera.apply(i.rect_spr))
            for e in self.objetos:
                if not e.taken:
                    screen.blit(e.image, self.camera.apply(e.rect))
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

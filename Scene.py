import pygame
from pygame.locals import *
import Camara
from text import Text
from Personaje import Personaje
from sonidos import Sonido
from Variables import *

class Scene:
    #abstract representation of the game scenes

    def __init__(self, map, image,soundtrack,pj):
        self.mapa = map
        self.camera = Camara.Camera(Camara.complex_camera,map)
        self.background = pygame.image.load(image).convert_alpha()
        self.background = pygame.transform.scale(self.background,self.mapa)
        self.pj=pj

        self.text=Text(self.pj)

        self.sonido = Sonido()
        self.soundtrack=soundtrack


    def on_update(self, time, keys, director):
        #executed in every game loop, used to check events that can happen at any time

        if not self.text.display and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:             #si no estamos mostrando texto
            self.camera.update(self.pj)     #update a la camara
            self.pj.update(time/1000, keys,self.mapa,self.npcs,self.obs, self.objetos,self.sonido.grass) #update del personaje

        for npc in self.npcs:
            if npc.talking==False:
                npc.animation()    #animaciones de los npcs
                npc.camino1(self.mapa, self.pj.rect_col,self.obs)   #camino que recorren los npcs (provisional)
        for ob in self.obs:
            ob.update(self.pj,self.mapa,self.obs,self.npcs);


    def on_event(self, keys, director):
        #used to check events of keyboard or other events that happen due to a given action

        if keys[K_r] and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:

            for npc in self.npcs:
                if self.pj.rect_spr.colliderect(npc.rect_accion):
                    self.text.dialog(npc)
            for ob in self.objetos:
                if self.pj.rect_spr.colliderect(ob.action_rect) and not ob.taken:
                    ob.taken=True

        self.text.menu(keys,self.pj,director)     #control del menu
        self.pj.objectAct(keys,self.soundtrack,self.text)   #accion que realiza el personaje con los objetos (actualizable)


    def on_draw(self, screen):
        #used to draw on screen

        self.dibujarElementos(screen)
        #dibujo de fondo necesario para limpiar los menus
        self.text.displays(screen)  #funcion que controla que se dibujen los textos y menus
        if not self.text.display and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:
            self.dibujarElementos(screen)



    def dibujarElementos(self,screen):
        screen.blit(self.background, self.camera.apply(self.background.get_rect())) #dibujado de mapa ingame

        if self.pj.order:  #order 1 - pj is drawn last (is at front)
            for e in self.objetos:
                if not e.taken:
                    screen.blit(e.image, self.camera.apply(e.rect))   #draw objects
            for e in self.obs:
                #pygame.draw.rect(screen, (0,100,200), self.camera.apply(e.rect)) #draw colision obstacles(not in-game)
                if e.image!=None:
                    screen.blit(e.image, self.camera.apply(e.rect)) #draw colision obstacles
            for e in self.npcs:
                screen.blit(e.image, self.camera.apply(e.rect))   #draw npcs

            screen.blit(self.pj.image, self.camera.apply(self.pj.rect_spr))

        else    :#order 2 - pj is drawn first (is at back)
            screen.blit(self.pj.image, self.camera.apply(self.pj.rect_spr))

            for e in self.objetos:
                if not e.taken:
                    screen.blit(e.image, self.camera.apply(e.rect))     #draw objects
            for e in self.obs:
                #pygame.draw.rect(screen, (0,100,200), self.camera.apply(e.rect)) #draw colision obstacles(not in-game)
                if e.image!=None:
                    screen.blit(e.image, self.camera.apply(e.rect)) #draw colision obstacles
            for e in self.npcs:
                screen.blit(e.image, self.camera.apply(e.rect))         #draw npcs


    def changeScene(self,scene,director,pos):       #cambia de escena y pasa el personaje y su posicion a la siguiente escena
        self.pj.rect_col.topleft=(pos[0],pos[1])
        self.pj.rect_spr.topleft=(pos[0],pos[1]-self.pj.frame_height+20)
        self.pj.mapa=scene
        self.scenes[scene].pj=self.pj               #pass the pj of this scene to the next one

        pygame.mixer.music.load(self.scenes[scene].soundtrack)  #load next scene music
        pygame.mixer.music.play()
        director.change_scene(self.scenes[scene])

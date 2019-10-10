import Camara
import pygame
from pygame.locals import *

class Scene:
    #abstract representation of the game scenes

    def __init__(self,map,image):
        self.mapa = map
        self.camera = Camara.Camera(Camara.complex_camera,map)
        self.background = pygame.image.load(image).convert_alpha()
        self.background = pygame.transform.scale(self.background,self.mapa)


    def on_update(self, time, keys, director):
        #executed in every game loop, used to check events that can happen at any time

        if not self.text.display and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:             #si no estamos mostrando texto
            self.camera.update(self.pj)     #update a la camara
            self.pj.update(time/1000, keys,self.mapa,self.npcs,self.obs, self.objetos,self.sonido.grass) #update del personaje

            for npc in self.npcs:
                npc.animation()    #animaciones de los npcs
                npc.camino1(self.mapa, self.pj.rect_col)   #camino que recorren los npcs (provisional)


    def on_event(self, keys, director):
        #used to check events of keyboard or other events that happen due to a given action

        if keys[K_r] and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:

            for npc in self.npcs:
                if self.pj.rect_spr.colliderect(npc.rect_accion):
                    self.text.dialog(npc.dialog)
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
            for e in self.obs:
                pygame.draw.rect(screen, (0,100,200), self.camera.apply(e.rect)) #draw colision obstacles



    def dibujarElementos(self,screen):
        screen.blit(self.background, self.camera.apply(self.background.get_rect())) #dibujado de mapa ingame
        if self.pj.order:
            for o in self.npcs:
                screen.blit(o.image, self.camera.apply(o.rect))
            for e in self.objetos:
                if not e.taken:
                    screen.blit(e.image, self.camera.apply(e.rect))

            screen.blit(self.pj.image, self.camera.apply(self.pj.rect_spr))
        else:
            screen.blit(self.pj.image, self.camera.apply(self.pj.rect_spr))

            for e in self.objetos:
                if not e.taken:
                    screen.blit(e.image, self.camera.apply(e.rect))
            for o in self.npcs:
                screen.blit(o.image, self.camera.apply(o.rect))

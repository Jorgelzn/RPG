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

    def __init__(self, map, image,pj=None,pos=None):
        Scene.__init__(self, map, image)
        if pj==None:
            self.pj = Personaje(pjx, pjy)
        else:
            self.pj=pj
            self.pj.rect_col.topleft=(pos[0],pos[1])
            self.pj.rect_spr.topleft=(pos[0],pos[1]-self.pj.frame_height+20)
        self.sonido = Sonido()
        self.npcs = [
            Npc("imagenes/personajes/paperi_sheet.png",["hola","soy paperi","buenos dias","ven a nuestra tienda","vendemos pan"], 600, 100, 68, 189),
            Npc("imagenes/personajes/Peto_sheet.png",["paperi siempre esta igual","deberiamos llamarnos peto y paperi"],500, 600, 114, 145),
            Npc("imagenes/personajes/Tapa_sheet.png",["me llamo Tapa :D","vente luego a jugar", "miau"],1200, 600, 68, 77),
            Npc("imagenes/personajes/Kea_sheet.png",["me preocupan peto y paperi","no paran de pelear","jopé"],1200, 200, 84, 131)
        ]
        self.objetos=[
            Objeto("imagenes/objetos/Flute.png",100,"Nadie puede resistirse al poder de la musica",700,700,60,60,210,140,174,120)
        ]
        self.obs=[
            Obstaculo(780,520,155,100),
            Obstaculo(1080,520,155,100),
            Obstaculo(0,400,50,130,True),
            Obstaculo(680,self.mapa[1]-50,125,50,True),
            Obstaculo(600,0,125,50,True)

        ]
        self.text=Text(self.pj)

        self.soundtrack= self.sonido.soundtrack1
        pygame.mixer.music.load(self.soundtrack)
        #pygame.mixer.music.play()


    def on_update(self, time,keys,director):

        if not self.text.display and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:        #si no estamos mostrando texto
            self.camera.update(self.pj)     #update a la camara
            self.pj.update(time/1000, keys,self.mapa,self.npcs,self.obs, self.objetos,self.sonido.grass) #update del personaje

            for npc in self.npcs:
                npc.animation()    #animaciones de los npcs
                npc.camino1(self.mapa, self.pj.rect_col)   #camino que recorren los npcs (provisiona[3].rectl)

            if self.pj.rect_col.colliderect(self.obs[2].rect) or self.pj.rect_col.colliderect(self.obs[3].rect) or  self.pj.rect_spr.colliderect(self.obs[4].rect):   #cambiamos de zona al chocar con los cuadrados de transporte
                director.change_scene(Pantalla2(map2,"imagenes/mapas/forest.png",self.pj,(self.mapa[0]-150,self.mapa[1]+100)))


    def on_event(self,keys,director):
        if keys[K_r] and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:

            for npc in self.npcs:
                if self.pj.rect_spr.colliderect(npc.rect_accion):
                    self.text.dialog(npc.dialog)
            for ob in self.objetos:
                if self.pj.rect_spr.colliderect(ob.action_rect) and not ob.taken:
                    self.pj.objects.append(ob)
                    ob.taken=True


        self.text.menu(keys,self.pj,director)     #control del menu
        self.pj.objectAct(keys,self.soundtrack,self.text)   #accion que realiza el personaje con los objetos (actualizable)

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


    def on_draw(self, screen):

        self.dibujarElementos(screen)
        #dibujo de fondo necesario para limpiar los menus
        self.text.displays(screen)  #funcion que controla que se dibujen los textos y menus
        if not self.text.display and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:
            self.dibujarElementos(screen)
            for e in self.obs:
                pygame.draw.rect(screen, (0,100,200), self.camera.apply(e.rect)) #draw colision obstacles


class Pantalla2(Scene):

    def __init__(self, map, image,pj,pos):
        Scene.__init__(self, map, image)
        self.pj = pj
        self.pj.rect_col.topleft=(pos[0],pos[1])
        self.pj.rect_spr.topleft=(pos[0],pos[1]-self.pj.frame_height+20)
        self.sonido = Sonido()
        self.npcs = []
        self.objetos=[]
        self.obs=[
            Obstaculo(780,520,155,100),
            Obstaculo(self.mapa[0]-150,self.mapa[1]-50,125,50,True)
        ]
        self.text=Text(self.pj)

        self.soundtrack= self.sonido.soundtrack2
        pygame.mixer.music.load(self.soundtrack)
        #pygame.mixer.music.play()


    def on_update(self, time,keys,director):

        if not self.text.display and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:        #si no estamos mostrando texto
            self.camera.update(self.pj)     #update a la camara
            self.pj.update(time/1000, keys,self.mapa,self.npcs,self.obs, self.objetos,self.sonido.grass) #update del personaje

            for npc in self.npcs:
                npc.animation()    #animaciones de los npcs
                npc.camino1(self.mapa, self.pj.rect_col)   #camino que recorren los npcs (provisional)

            if self.pj.rect_col.colliderect(self.obs[1].rect):   #cambiamos de zona al chocar con los cuadrados de transporte
                director.change_scene(Pantalla1(map1,"imagenes/mapas/city.jpg",self.pj,(500,500)))


    def on_event(self,keys,director):
        if keys[K_r] and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:

            for npc in self.npcs:
                if self.pj.rect_spr.colliderect(npc.rect_accion):
                    self.text.dialog(npc.dialog)
            for ob in self.objetos:
                if self.pj.rect_spr.colliderect(ob.action_rect) and not ob.taken:
                    self.pj.objects.append(ob)
                    ob.taken=True


        self.text.menu(keys,self.pj,director)     #control del menu
        self.pj.objectAct(keys,self.soundtrack,self.text)   #accion que realiza el personaje con los objetos (actualizable)

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


    def on_draw(self, screen):

        self.dibujarElementos(screen)
        #dibujo de fondo necesario para limpiar los menus
        self.text.displays(screen)  #funcion que controla que se dibujen los textos y menus
        if not self.text.display and not self.text.displayMenu and not self.text.displayMap and not self.text.displayInventario:
            self.dibujarElementos(screen)
            for e in self.obs:
                pygame.draw.rect(screen, (0,100,200), self.camera.apply(e.rect))  #draw colision obstacles

from Scene import Scene
from Npc import *
from Variables import *
from Escenario import *

class Pantalla1(Scene):

    def __init__(self, map, image,soundtrack,pj=None,pos=None):
        Scene.__init__(self, map, image,soundtrack,pj,pos)
        self.pj.mapa=1
        self.npcs = [
            Npc("imagenes/personajes/paperi_sheet.png",["hola","soy paperi","buenos dias","ven a nuestra tienda","vendemos pan"], 600, 100, 68, 189),
            Npc("imagenes/personajes/Peto_sheet.png",["paperi siempre esta igual","deberiamos llamarnos peto y paperi"],500, 600, 114, 145),
            Npc("imagenes/personajes/Tapa_sheet.png",["me llamo Tapa :D","vente luego a jugar", "miau"],1200, 600, 68, 77),
            Npc("imagenes/personajes/Kea_sheet.png",["me preocupan peto y paperi","no paran de pelear","jopé"],1200, 200, 84, 131)
        ]
        self.objetos=[self.pj.objects[0]]
        self.obs=[
            Obstaculo(780,520,155,100),
            Obstaculo(1080,520,155,100),
            Obstaculo(0,400,50,130,True),
            Obstaculo(680,self.mapa[1]-50,125,50,True),
            Obstaculo(600,0,125,50,True)
        ]


    def on_update(self, time, keys, director):
        Scene.on_update(self,time,keys,director)
        if self.pj.rect_col.colliderect(self.obs[2].rect) or self.pj.rect_col.colliderect(self.obs[3].rect) or  self.pj.rect_spr.colliderect(self.obs[4].rect):   #cambiamos de zona al chocar con los cuadrados de transporte
            director.change_scene(Pantalla2(map2,"imagenes/mapas/forest.png",soundtrack2,self.pj,(map2[0]-150,map2[1]-100)))


class Pantalla2(Scene):

    def __init__(self, map, image,soundtrack,pj=None,pos=None):
        Scene.__init__(self, map, image,soundtrack,pj,pos)
        self.pj.mapa=2
        self.npcs = []
        self.objetos=[]
        self.obs=[
            Obstaculo(780,520,155,100),
            Obstaculo(self.mapa[0]-150,self.mapa[1]-50,125,50,True)
        ]


    def on_update(self, time,keys,director):
        Scene.on_update(self,time,keys,director)
        if self.pj.rect_col.colliderect(self.obs[1].rect):   #cambiamos de zona al chocar con los cuadrados de transporte
            director.change_scene(Pantalla1(map1,"imagenes/mapas/city.jpg",soundtrack1,self.pj,(500,500)))

import Camara
import pygame

class Scene:
    #abstract representation of the game scenes

    def __init__(self,map,image):
        self.mapa = map
        self.camera = Camara.Camera(Camara.complex_camera,map)
        self.background = pygame.image.load(image).convert_alpha()
        self.background = pygame.transform.scale(self.background,self.mapa)
    def on_update(self, time):
        #executed in every game loop, used to check events that can happen at any time
        raise NotImplemented()

    def on_draw(self, screen):
        #used to draw on screen
        raise NotImplemented()

    def on_event(self):
        #used to check events of keyboard or other events that happen due to a given action
        raise NotImplemented()

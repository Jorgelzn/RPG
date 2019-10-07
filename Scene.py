import Camara
import pygame

class Scene:
    '''Representa un escena abstracta del videojuego.

    Una escena es una parte visible del juego, como una pantalla
    de presentación o menú de opciones.
    '''

    def __init__(self,map,image):
        self.mapa = map
        self.camera = Camara.Camera(Camara.complex_camera,map)
        self.background = pygame.image.load(image).convert_alpha()
        self.background = pygame.transform.scale(self.background,self.mapa)
    def on_update(self, time):
        ''' Actualización lógica que se llama automáticamente desde el director
        '''
        raise NotImplemented("Tiene que implementar el método on_update.")

    def on_draw(self, screen):
        ''' Se llama cuando se quiere dibujar la pantalla
        '''
        raise NotImplemented("Tiene que implementar el método on_draw.")

    def on_event(self):

        raise NotImplemented("Tiene que implementar el método on_event.")

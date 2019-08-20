import pygame
from pygame.locals import *

class Director:
    '''Representa el objeto principal del juego.
    El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.
    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene.'''

    def __init__(self):
        ''' En el init establecemos las características globales como
            resolución, título de la ventana, etc"
        '''
        self.screen = pygame.display.set_mode([800,600])
        pygame.display.set_caption("RPG")
        self.scene = None       #Escena actual
        self.quit_flag = False  #Control para el bucle de juego
        self.clock = pygame.time.Clock()

    def loop(self):
        ''' Bucle de juego'''
        while not self.quit_flag:
            time = self.clock.tick(60)  #PCMaster Race

            # Eventos que capturamos en cada momento
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                    break

                ''' Si el juego no se ha cancelado,
                    le tenemos que pasar a la escena actual
                    los eventos capturados para sus cosas
                '''
                data=self.scene.on_event(time, event)

            # actualiza la escena
            self.scene.on_update(time,data)

            # dibuja la pantalla
            self.scene.on_draw(self.screen)
            pygame.display.flip()

    def change_scene(self, scene):
        '''Altera la escena actual'''
        self.scene = scene

    def quit(self):
        '''Para cuando queremos salir'''
        self.quit_flag = True

    def simple_camera(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        return Rect(-l+WIDTH//2, -t+HEIGHT//2, w, h)

    def complex_camera(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t, _, _ = -l+WIDTH//2, -t+HEIGHT//2, w, h
        l = min(0, l)                           # stop scrolling at the left edge
        l = max(-(camera.width-WIDTH), l)   # stop scrolling at the right edge
        t = max(-(camera.height-HEIGHT), t) # stop scrolling at the bottom
        t = min(0, t)                           # stop scrolling at the top
        return Rect(l, t, w, h)

import pygame
from pygame.locals import *
from Variables import *

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
        self.screen = pygame.display.set_mode(ventana)
        pygame.display.set_caption("RPG")
        self.scene = None       #Escena actual
        self.quit_flag = False  #Control para el bucle de juego
        self.clock = pygame.time.Clock()

    def loop(self):
        ''' Bucle de juego'''
        while not self.quit_flag:
            time = self.clock.tick(30)  #PCMaster Race
            # Eventos que capturamos en cada momento
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    self.scene.on_event(key, self.screen)

            keys = pygame.key.get_pressed()
            # actualiza la escena
            new_scene = self.scene.on_update(time,keys)
            if new_scene is not None: self.change_scene(new_scene)
            # dibuja la pantalla
            self.scene.on_draw(self.screen)
            pygame.display.update()

    def change_scene(self, scene):
        '''Altera la escena actual'''
        self.scene = scene

    def quit(self):
        '''Para cuando queremos salir'''
        self.quit_flag = True

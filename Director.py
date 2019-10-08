import pygame
from pygame.locals import *
from Variables import *

class Director:
    #main class of the game, it is where the game is executed
    #in this class is the main loop of the game

    def __init__(self):

        self.screen = pygame.display.set_mode(ventana)
        pygame.display.set_caption("RPG")
        self.scene = None       #Escena actual
        self.quit_flag = False  #Control para el bucle de juego
        self.clock = pygame.time.Clock()

    def loop(self):     #main loop

        while not self.quit_flag:
            time = self.clock.tick(30)  #PCMaster Race
            # Eventos que capturamos en cada momento
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    if key[K_ESCAPE]:
                        self.quit()
                    self.scene.on_event(key,self)

            keys = pygame.key.get_pressed()
            # actualiza la escena
            self.scene.on_update(time,keys,self)
            # dibuja la pantalla
            self.scene.on_draw(self.screen)
            pygame.display.update()

    def change_scene(self, scene):  #used to change the scene which is currently running
        self.scene = scene

    def quit(self):    #used to get out of game
        self.quit_flag = True

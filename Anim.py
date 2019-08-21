'''Example with sprite animation based on keys pressed'''

import pygame
from pygame.locals import *
from pygame import sprite

FPSPRITE = 15 # number of frames per sprite
WIDTH, HEIGHT = 1251, 757
FRAME_RATE = 60

class Character:
    def __init__(self):
        # initialise spriteSheet:
        self.spriteSheet = pygame.image.load('imagenes/pok.png').convert_alpha()

        # initialise frame data:
        self.nframes = 4 # number of sprites/direction
        self.current_frame = 0 
        self.frame_width = 64
        self.frame_height = 64
        self.frame_counter = FPSPRITE # number of frames per sprite

        self.image = self.spriteSheet.subsurface((0,0,self.frame_width,self.frame_height))

        # initialise position:
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        
    def update(self, dt, keys):
        '''Character update:
        movement, sprite animation...'''

        self.speedx = 3*self.frame_width * dt/1000 # 3 frame_width per sec
        self.speedy = 3*self.frame_height * dt/1000 # 3 frame_height per sec

        # cycle through sprites at a rate of FPSPRITE
        if self.frame_counter == 0:
            self.current_frame = (self.current_frame + 1) % self.nframes # next sprite
            self.frame_counter = FPSPRITE
        else:
            self.frame_counter -= 1

        # key presses: change sprite based on direction and move
        if keys[K_DOWN] and self.y+self.frame_height+self.speedy <= HEIGHT:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      0,
                                                      self.frame_width, self.frame_height))
            self.y += self.speedy
        elif keys[K_LEFT] and self.x-self.speedx >= 0:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      self.frame_height,
                                                      self.frame_width, self.frame_height))
            self.x -= self.speedx
        elif keys[K_RIGHT] and self.x+self.frame_width+self.speedx <= WIDTH:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      2*self.frame_height,
                                                      self.frame_width, self.frame_height))
            self.x += self.speedx
        elif keys[K_UP] and self.y-self.speedy >= 0:
            self.image = self.spriteSheet.subsurface((self.current_frame * self.frame_width,
                                                      3*self.frame_height,
                                                      self.frame_width, self.frame_height))
            self.y -= self.speedy

        else:
            self.image = self.spriteSheet.subsurface((0,0, self.frame_width, self.frame_height))
            # if not moving, set standing sprite
            
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Director:
    '''Controls the mechanics of the game'''
    def __init__(self):
        # initialise display:
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Movement animations!")
        self.bg = pygame.image.load("imagenes/background.png")

        self.char = Character() # initialise character
        self.quit = False # quit flag
        self.clock = pygame.time.Clock() # game clock

    def loop(self):
        while not self.quit:
            time = self.clock.tick(FRAME_RATE)
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT or keys[K_ESCAPE]:
                    self.quit = True
                    break

            # re-draw scene:
            self.screen.blit(self.bg, (0, 0)) # re-draw background
            self.char.update(time, keys) # update character
            self.char.draw(self.screen) # re-draw character
            pygame.display.update() # update display with new changes

        pygame.quit()

def main():
    pygame.init()
    director = Director()
    director.loop()

main()

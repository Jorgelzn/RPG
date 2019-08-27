import pygame

class Obstaculo:
    def __init__(self, imagen, x=0, y=0, w=200, h=200):
        self.spriteSheet = pygame.image.load(imagen).convert_alpha()
        self.image = self.spriteSheet.subsurface(0,0,w,h)
        self.rect = pygame.Rect(x, y, w, h)

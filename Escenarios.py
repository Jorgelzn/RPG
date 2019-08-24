import pygame

class Obstaculo:
    def __init__(self, imagen, x=0, y=0, w=200, h=200):
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = pygame.Rect(x, y, w, h)

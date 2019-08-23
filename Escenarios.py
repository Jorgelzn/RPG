import pygame

class Plataforma:
    def __init__(self, x=0, y=0, w=350, h=70):
        self.image = pygame.image.load("imagenes/plataforma.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = pygame.Rect(x, y, w, h)

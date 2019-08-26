import pygame

class Sonido:

    def __init__(self):
        self.soundtrack1 = pygame.mixer.music.load("sonidos/ost/Moki_Town.mp3")
        self.pointerSound = pygame.mixer.Sound("sonidos/effects/test.wav")

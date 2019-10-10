import pygame

class Sonido:

    def __init__(self):
        self.pointerSound = pygame.mixer.Sound("sonidos/effects/Pointer (WAV).wav")
        self.dialog = pygame.mixer.Sound("sonidos/effects/Dialog Beep (WAV).wav")
        self.object = pygame.mixer.Sound("sonidos/effects/New object_mission (WAV).wav")
        self.grass = pygame.mixer.Sound("sonidos/effects/Walking (Grass_Dirt) (WAV).wav")
        self.click = pygame.mixer.Sound("sonidos/effects/Click (WAV).wav")
        self.click.set_volume(0.9)
        self.pointerSound.set_volume(0.9)
        self.grass.set_volume(0.1)
        self.object.set_volume(0.9)

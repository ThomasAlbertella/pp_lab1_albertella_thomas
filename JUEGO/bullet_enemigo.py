import pygame
from constantes import *

class Bullete:
    def __init__(self, x, y, direction):
        self.image = pygame.image.load("JUEGO/images/Dust Particle.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction

    def update(self):
        if self.direction == DIRECTION_R:
            self.rect.x += 5 
        else:
            self.rect.x -= 5  

    def draw(self, screen):
        screen.blit(self.image, self.rect)
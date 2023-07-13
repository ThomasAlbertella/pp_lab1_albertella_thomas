import pygame
from constantes import *


class Bullet:
    def __init__(self):
        self.image = pygame.image.load("JUEGO/images/Dust Particle.png").convert()
        self.rect = self.image.get_rect()
        self.direction = DIRECTION_R

    def update(self):
        if self.direction == DIRECTION_R:
            self.rect.x += 5  
        else:
            self.rect.x -= 5  

    def draw(self, screen):
        screen.blit(self.image, self.rect)
import pygame
from constantes import *


class Corazon:
    def __init__(self):
        self.image = pygame.image.load("JUEGO/images/corazon.png").convert()
        self.image = pygame.transform.scale(self.image, (40, 40)) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0) 
        self.vidas = 3 

        self.font = pygame.font.Font(None, 40)  #

    def draw(self, screen, vidas):
        screen.blit(self.image, self.rect)

        text_surface = self.font.render('= ' + str(vidas), True, (255, 255, 255)) 
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.right + 10, self.rect.y)  
        screen.blit(text_surface, text_rect)
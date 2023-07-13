import pygame
from constantes import *
from auxiliar import Auxiliar
from player import Player

class Platform():
    def __init__(self,x,y,w,h,type=0):
        self.image= Auxiliar.getSurfaceFromSeparateFiles("JUEGO/images/tileset/forest/Tiles/{0}.png",1,18,)[type]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.colision_tierra_rect = pygame.Rect(self.rect.x,self.rect.y, self.rect.w, GROUND_RECT_H)#crear rectangulo


    

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,ROJO,self.rect)

        screen.blit(self.image,self.rect)
        
        if(DEBUG):
            pygame.draw.rect(screen,VERDE,self.colision_tierra_rect)
        
        
import pygame
from constantes import *
from auxiliar import Auxiliar

class Manzana():
    def __init__(self,x,y,frame_rate_ms):
        self.manzanas = Auxiliar.recorrer_fotos("JUEGO\images\Fruits\Apple.png", 17, 1)
        self.animation = self.manzanas
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation)-1):
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.animation[self.frame]

    def update(self,delta_ms):
        self.do_animation(delta_ms)
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
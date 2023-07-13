import pygame
from constantes import *
from auxiliar import Auxiliar

class Trampas():
    def __init__(self, x, y, frame_rate_ms, trampa_2_flag):
        self.trampa_1 = Auxiliar.recorrer_fotos("JUEGO/images/trampa 1.png", 8, 1)
        self.trampa_2 = Auxiliar.recorrer_fotos("JUEGO/images/trampa 2.png", 4, 1)
        self.animation = self.trampa_1
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.trampa_2_flag = trampa_2_flag

    def trampas(self):
        if self.trampa_2_flag:
            self.animation = self.trampa_2
        else:
            self.animation = self.trampa_1

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.animation[self.frame]
        self.trampas()

        
    def update(self, delta_ms):
        self.do_animation(delta_ms)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
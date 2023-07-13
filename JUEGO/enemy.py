from player import *
from constantes import *
from auxiliar import Auxiliar
from bullet_enemigo import Bullete




class Enemy():
    def __init__(self, x, y, frame_rate_ms, flipped,lista_balas_enemigos,vidas, one_or_two_flag):
        self.stay_r = Auxiliar.recorrer_fotos(PATH_IMAGE + "Idle Malo(32x32).png", 11, 1, True)
        self.stay_l = Auxiliar.recorrer_fotos(PATH_IMAGE + "Idle Malo(32x32).png", 11, 1, False)
        self.death = Auxiliar.recorrer_fotos(PATH_IMAGE + "Hit (32x32).png", 7, 1)
        self.enemigo_final = Auxiliar.recorrer_fotos("JUEGO\images\FINAL (32x32).png", 11, 1,flip=True)
        self.enemigo_final_scale = [pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2)) for image in self.enemigo_final]        
        
        self.frame = 0
        self.frame_rate_ms = frame_rate_ms
       
        self.vidas = vidas
        self.one_or_two_flag = one_or_two_flag


        self.tiempo_transcurrido = 0
        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido_disparo = 0
        self.lista_balas_enemigos = lista_balas_enemigos


        
        self.animation = self.stay_l
        self.image = self.animation[self.frame] if self.animation else None
        self.rect = self.image.get_rect() if self.image else pygame.Rect(0, 0, 0, 0)
        self.rect.x = x
        self.rect.y = y
        self.flipped = flipped
        self.animacion_muerta = False

        self.direction = DIRECTION_R if flipped else DIRECTION_L

        

    def animacion_muerte(self,lista_enemigos):
        self.animation = self.death
        self.animacion_muerta = True
        if self.animacion_muerta:
            if self.frame == len(self.animation) - 1:
               
                lista_enemigos.remove(self)
            return  
        
    
            
    def one_or_two(self):
        if self.one_or_two_flag:
            self.animation = self.stay_r
        else:
            self.animation = self.enemigo_final_scale


    def disparar(self):
        bala = Bullete(self.rect.x, self.rect.y, self.direction) 
        self.lista_balas_enemigos.append(bala)

    def update(self, delta_ms, lista_enemigos):
        self.tiempo_transcurrido += delta_ms

        if self.animacion_muerta:
            if self.frame >= len(self.animation) - 1:
               
                if self.vidas <= 0:
                    pass  
                else:
                    self.animacion_muerta = False  
            else:
                self.frame += 1
            return

        self.tiempo_transcurrido_disparo += delta_ms

        if self.tiempo_transcurrido_disparo >= TIEMPO_ENTRE_DISPAROS:
            self.tiempo_transcurrido_disparo = 0
            self.disparar()

        if self.tiempo_transcurrido >= self.frame_rate_ms:
            self.tiempo_transcurrido = 0
            self.frame += 1
            if self.frame >= len(self.animation):
                self.frame = 0

        self.one_or_two()



    def draw(self, screen):
        if self.animation and self.frame < len(self.animation):
            self.image = self.animation[self.frame]
            if self.flipped:
                self.image = pygame.transform.flip(self.image, True, False)
            screen.blit(self.image, self.rect)

    
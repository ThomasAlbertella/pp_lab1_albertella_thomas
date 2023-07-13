import pygame
from constantes import *
from auxiliar import Auxiliar
from bullet import Bullet



class Player:
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,vidas):
        self.walk_r = Auxiliar.recorrer_fotos(PATH_IMAGE + "Mask Dude\Run (32x32).png",12,1)
        self.walk_l = Auxiliar.recorrer_fotos(PATH_IMAGE + "Mask Dude\Run (32x32).png",12,1,True)
        self.stay_r = Auxiliar.recorrer_fotos(PATH_IMAGE + "Mask Dude\Idle (32x32).png",11,1)
        self.stay_l = Auxiliar.recorrer_fotos(PATH_IMAGE + "Mask Dude\Idle (32x32).png",11,1,True)
        self.jump_r = Auxiliar.recorrer_fotos(PATH_IMAGE + "Mask Dude\Jump (32x32).png",1,1)
        self.jump_l = Auxiliar.recorrer_fotos(PATH_IMAGE + "Mask Dude\Jump (32x32).png",1,1,True)
        self.shoot_r = Auxiliar.recorrer_fotos(PATH_IMAGE + "Mask Dude\Double Jump (32x32).png",6,1)
        self.shoot_l = Auxiliar.recorrer_fotos(PATH_IMAGE + "Mask Dude\Double Jump (32x32).png",6,1,True)
        self.hit_r = Auxiliar.recorrer_fotos("JUEGO\images\Hit Bueno(32x32).png",7,1)
        self.hit_l = Auxiliar.recorrer_fotos("JUEGO\images\Hit Bueno(32x32).png",7,1,True)

        self.frame = 0
        self.vidas = vidas
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_jump = False
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height
        
        self.is_fall = False
        self.is_hit = False
        
       
        

        self.bullets = []
        self.is_shoot = False
        self.last_shot_time = 0  # Momento del último disparo
        self.is_shooting = False
        self.shoot_delay = 200  # Retraso entre disparos en milisegundos
        
        
        

        self.colision_tierra_rect = pygame.Rect(self.rect.x + self.rect.w / 4,self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 2, GROUND_RECT_H)#crear rectangulo


    def animate_shoot(self):
        if self.is_shoot:
            if self.direction == DIRECTION_R:
                self.animation = self.shoot_r
            else:
                self.animation = self.shoot_l
            self.frame = 0
            self.tiempo_transcurrido_animation = 0
    
    

    


    def fire_bullet(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > self.shoot_delay:
            bullet = Bullet()
            bullet.rect.center = self.rect.center
            bullet.direction = self.direction  # Almacena la dirección del jugador en la bala
            self.bullets.append(bullet)
            self.last_shot_time = current_time

    def walk(self,direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.frame = 0

        self.direction = direction
        if direction == DIRECTION_R:
            self.move_x = self.speed_walk
            self.animation = self.walk_r
        else:
            self.move_x = -self.speed_walk
            self.animation = self.walk_l
    

        
        



    def jump(self,on_off = True):
        if(on_off and self.is_jump == False):
            self.y_start_jump = self.rect.y
            if (self.direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = -self.speed_walk
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        elif(on_off == False):
            self.is_jump = False
            self.stay()


    def shoot(self, on_off=True):
        if on_off != self.is_shooting:
            self.is_shooting = on_off
            if on_off:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_shot_time > self.shoot_delay:
                    self.last_shot_time = current_time
                    self.animate_shoot()
                    self.fire_bullet()



    def stay(self):
        if self.animation != self.stay_r and self.animation != self.stay_l:
            if self.direction == DIRECTION_R:
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l

            self.move_x = 0
            self.move_y = 0
            self.frame = 0
    
    
            
            


    def do_movement(self,delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0

            self.tiempo_transcurrido_move = 0
            self.add_x(self.move_x)
            self.add_y(self.move_y)


            if (self.is_on_plataform(lista_plataformas) == False):
                self.add_y(self.gravity)
            elif(self.is_jump): 
                self.jump(False)


    def is_on_plataform(self,lista_plataformas):
        retorno = False
        if(self.rect.y >= TIERRA_NIVEL):
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.colision_tierra_rect.colliderect(plataforma.colision_tierra_rect)):#colision
                    retorno = True
                    break
        return retorno
    

            
    def add_x(self,delta_x):
        self.rect.x += delta_x
        self.colision_tierra_rect.x += delta_x

    
    def add_y(self,delta_y):
        self.rect.y += delta_y
        self.colision_tierra_rect.y += delta_y



    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation)-1):
                self.frame += 1
            else:
                self.frame = 0
          

    def puntos(self,score=0):
        score += score


    def update(self,delta_ms,lista_plataformas):
        self.do_movement(delta_ms,lista_plataformas)
        self.do_animation(delta_ms)


    def draw(self,screen,puntaje,tiempo_restante_segundos):
        if DEBUG:
            pygame.draw.rect(screen, ROJO, self.rect)
            pygame.draw.rect(screen, VERDE, self.colision_tierra_rect)

        if self.animation and self.frame < len(self.animation) and self.image:
            self.image = self.animation[self.frame]
            screen.blit(self.image, self.rect)
        else:
            if self.direction == DIRECTION_R:
                self.image = self.stay_r[self.frame] if self.stay_r and self.frame < len(self.stay_r) else pygame.Surface((0, 0))
            else:
                self.image = self.stay_l[self.frame] if self.stay_l and self.frame < len(self.stay_l) else pygame.Surface((0, 0))
            screen.blit(self.image, self.rect)

        font = pygame.font.Font(None, 40)  
        text_surface = font.render("Puntos: " + str(puntaje), True, (255, 255, 255)) 
        text_rect = text_surface.get_rect()
        text_rect.topleft = (100, 0)  
        screen.blit(text_surface, text_rect)  

        font = pygame.font.Font(None, 40)  
        text_surface = font.render("Tiempo: " + str(tiempo_restante_segundos), True, (255, 255, 255))  
        text_rect = text_surface.get_rect()
        text_rect.topright = (ANCHO - 10, 0)  
        screen.blit(text_surface, text_rect)  


        

    
        
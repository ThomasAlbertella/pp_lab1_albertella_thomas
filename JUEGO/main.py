import pygame
import sys
from constantes import *
from player import Player
from funciones import *
from records import *
from corazon import Corazon
from form_level_1 import Level1
from form_level_2 import Level2
from form_level_3 import Level3



pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))

clock = pygame.time.Clock()
conexion = sqlite3.connect("records.db")
crear_tabla()


imagen_fondo = pygame.image.load(PATH_IMAGE + "fondo/all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO, ALTO))



player_1 = Player(x=0,y=500,speed_walk=4,gravity=8,jump_power=25,frame_rate_ms=40,move_rate_ms=20,jump_height=150,vidas=3)

lista_balas_enemigos = []



level1 = Level1(lista_balas_enemigos=lista_balas_enemigos)
level2 = Level2(lista_balas_enemigos=lista_balas_enemigos)
level3 = Level3(lista_balas_enemigos=lista_balas_enemigos)




puntaje = 0
juego_terminado = True
nombre_usuario = ""
jugando = True
nivel_actual = 1




tiempo_restante1 = 64
tiempo_restante2 = 60
tiempo_restante3 = 60


corazon = Corazon()

disparo = pygame.mixer.Sound("JUEGO\sounds\sounds_shoot.wav")
disparo.set_volume(0.2)
pygame.mixer.music.load("JUEGO/sounds/X2Download.app - trompetas de la 12 (128 kbps).mp3")
pygame.mixer.music.set_volume(0.1)
tomaaa = pygame.mixer.Sound("JUEGO/sounds/x2downloadapp-toma-don-ramon-128-kbps_1Pf0z1s9.mp3")
uh = pygame.mixer.Sound("JUEGO\sounds\sonido-uh-de-roblox_kMJRBU0D.mp3")
uh.set_volume(0.5)
salto = pygame.mixer.Sound("JUEGO\sounds\X2Download.app - Salto sonido sin copyright (128 kbps).mp3")
salto.set_volume(0.1)

comer = pygame.mixer.Sound("JUEGO\sounds\comer.mp3")
comer.set_volume(0.5)

pygame.mixer.music.play()


trampa_collision = False
vida_collision = False



while True:

    if juego_terminado:    

        if nivel_actual == 1:
            mostrar_pantalla_go()
            nombre_usuario = ingresar_nombre()
            juego_terminado = False
            

        elif nivel_actual == 2:
            mostrar_pantalla_nivel_2()
            juego_terminado = False

        elif nivel_actual == 3:
            mostrar_pantalla_nivel_3()
            juego_terminado = False
             

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mostrar_pantalla_pausa()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                x, y = pygame.mouse.get_pos()
                print("Coordenadas - X:", x, ", Y:", y)
            
            

                

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        player_1.walk(DIRECTION_L)
    if not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        player_1.walk(DIRECTION_R)
    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_s]:
        player_1.stay()
    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
        player_1.stay()
    if keys[pygame.K_SPACE]:
        player_1.jump(True)
        salto.play()
    if keys[pygame.K_s]:
        player_1.fire_bullet()
        player_1.shoot(True)  
        disparo.play()

          
    

    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo, imagen_fondo.get_rect())
 
    

    if nivel_actual == 1:

        tiempo_restante1 -= delta_ms / 1000
        tiempo_restante_segundos = int(tiempo_restante1)


        for plataforma in level1.lista_plataformas_nivel_1:
            plataforma.draw(screen)
        

        for enemigo in level1.lista_enemigos_nivel_1:
            enemigo.update(delta_ms,level1.lista_enemigos_nivel_1)
            enemigo.draw(screen)
        

        

        for fruta in level1.lista_objetos_nivel_1:
            fruta.update(delta_ms)
            fruta.draw(screen)
            if player_1.rect.colliderect(fruta.rect) and not vida_collision:
                if player_1.vidas < 3:  
                    player_1.vidas += 1
                    corazon.vidas += 1
                    vida_collision = True
                    comer.play()
                    level1.lista_objetos_nivel_1.remove(fruta)
                if corazon.vidas > 3:  
                    corazon.vidas = 3  
        

        for trampa in level1.lista_trampas_nivel_1:
            trampa.update(delta_ms)
            trampa.draw(screen)
            if player_1.rect.colliderect(trampa.rect) and not trampa_collision:
                player_1.vidas -= 1
                corazon.vidas -= 1
                uh.play()
                trampa_collision = True
                player_1.animation = player_1.hit_r if player_1.direction == DIRECTION_R else player_1.hit_l
                
        
        if trampa_collision and not any(player_1.rect.colliderect(trampa.rect) for trampa in level1.lista_trampas_nivel_1):
            trampa_collision = False  
                    
        if vida_collision and not any(player_1.rect.colliderect(fruta.rect) for fruta in level1.lista_objetos_nivel_1):
            vida_collision = False         


        enemies_to_remove_1 = []
        for bullet in player_1.bullets:
            bullet.update()
            bullet.draw(screen)
            for enemy in level1.lista_enemigos_nivel_1:
                if bullet.rect.colliderect(enemy.rect):
                    player_1.bullets.remove(bullet)
                    puntaje += 10
                    tomaaa.play()
                    enemy.vidas -= 1
                    enemy.animacion_muerte(level1.lista_enemigos_nivel_1)
                    if enemy.vidas <= 0:
                        enemies_to_remove_1.append(enemy)  

        
        for enemy in enemies_to_remove_1:
            if enemy in level1.lista_enemigos_nivel_1:  
                level1.lista_enemigos_nivel_1.remove(enemy)

        
        if len(level1.lista_enemigos_nivel_1) == 0:
            juego_terminado = True
            guardar_puntaje(nombre_usuario, puntaje)
            puntaje_final = puntaje
            mostrar_pantalla_final_1(puntaje_final)
            nivel_actual += 1

        for bala in lista_balas_enemigos:
            bala.update()
            bala.draw(screen)
            if bala.rect.colliderect(player_1.rect):
                player_1.vidas -= 1
                corazon.vidas -= 1
                uh.play()
                lista_balas_enemigos.remove(bala)
                player_1.animation = player_1.hit_r if player_1.direction == DIRECTION_R else player_1.hit_l
        

    elif nivel_actual == 2:

        tiempo_restante2 -= delta_ms / 1000
        tiempo_restante_segundos = int(tiempo_restante2)


        for plataforma in level2.lista_plataformas_nivel_2:
            plataforma.draw(screen)


        for enemigo in level2.lista_enemigos_nivel_2:
            enemigo.update(delta_ms,level2.lista_enemigos_nivel_2)
            enemigo.draw(screen)


        for fruta in level2.lista_objetos_nivel_2:
            fruta.update(delta_ms)
            fruta.draw(screen)
            if player_1.rect.colliderect(fruta.rect) and not vida_collision:
                if player_1.vidas < 3:  
                    player_1.vidas += 1
                    corazon.vidas += 1
                    vida_collision = True
                    level2.lista_objetos_nivel_2.remove(fruta)
                    comer.play()
                if corazon.vidas > 3:  
                    corazon.vidas = 3  


        for trampa in level2.lista_trampas_nivel_2:
            trampa.update(delta_ms)
            trampa.draw(screen)
            if player_1.rect.colliderect(trampa.rect) and not trampa_collision:
                player_1.vidas -= 1
                corazon.vidas -= 1
                uh.play()
                trampa_collision = True
                player_1.animation = player_1.hit_r if player_1.direction == DIRECTION_R else player_1.hit_l


        if trampa_collision and not any(player_1.rect.colliderect(trampa.rect) for trampa in level2.lista_trampas_nivel_2):
            trampa_collision = False  

        if vida_collision and not any(player_1.rect.colliderect(fruta.rect) for fruta in level2.lista_objetos_nivel_2):
            vida_collision = False        


        enemies_to_remove_2 = []  

        for bullet in player_1.bullets:
            bullet.update()
            bullet.draw(screen)
            for enemy in level2.lista_enemigos_nivel_2:
                if bullet.rect.colliderect(enemy.rect):
                    player_1.bullets.remove(bullet)
                    puntaje += 10
                    tomaaa.play()
                    enemy.vidas -= 1
                    enemy.animacion_muerte(level2.lista_enemigos_nivel_2)
                    if enemy.vidas <= 0:
                        tomaaa.play()
                        enemies_to_remove_2.append(enemy)  


        
        for enemy in enemies_to_remove_2:
            if enemy in level2.lista_enemigos_nivel_2:  
                level2.lista_enemigos_nivel_2.remove(enemy)

        if len(level2.lista_enemigos_nivel_2) == 0:
            juego_terminado = True
            guardar_puntaje(nombre_usuario, puntaje)
            puntaje_final = puntaje
            mostrar_pantalla_final_2(puntaje_final)
            nivel_actual += 1

                        
        for bala in lista_balas_enemigos:
            bala.update()
            bala.draw(screen)

            if bala.rect.colliderect(player_1.rect):
                player_1.vidas -= 1
                corazon.vidas -= 1
                lista_balas_enemigos.remove(bala)


    elif nivel_actual == 3:
        tiempo_restante3 -= delta_ms / 1000
        tiempo_restante_segundos = int(tiempo_restante3)


        for plataforma in level3.lista_plataformas_nivel_3:
            plataforma.draw(screen)


        for enemigo in level3.lista_enemigos_nivel_3:
            enemigo.update(delta_ms,level3.lista_enemigos_nivel_3)
            enemigo.draw(screen)
        


        for fruta in level3.lista_objetos_nivel_3:
            fruta.update(delta_ms)
            fruta.draw(screen)
            if player_1.rect.colliderect(fruta.rect) and not vida_collision:
                if player_1.vidas < 3:  
                    player_1.vidas += 1
                    corazon.vidas += 1
                    vida_collision = True
                    level3.lista_objetos_nivel_3.remove(fruta)
                    comer.play()
                if corazon.vidas > 3:  
                    corazon.vidas = 3  
        
        
        for trampa in level3.lista_trampas_nivel_3:
            trampa.update(delta_ms)
            trampa.draw(screen)
            if player_1.rect.colliderect(trampa.rect) and not trampa_collision:
                player_1.vidas -= 1
                corazon.vidas -= 1
                uh.play()
                trampa_collision = True
                player_1.animation = player_1.hit_r if player_1.direction == DIRECTION_R else player_1.hit_l


        if trampa_collision and not any(player_1.rect.colliderect(trampa.rect) for trampa in level3.lista_trampas_nivel_3):
            trampa_collision = False  
                
        if vida_collision and not any(player_1.rect.colliderect(fruta.rect) for fruta in level3.lista_objetos_nivel_3):
            vida_collision = False  
    

        enemies_to_remove_3 = []  

        for bullet in player_1.bullets:
            bullet.update()
            bullet.draw(screen)
            for enemy in level3.lista_enemigos_nivel_3:
                if bullet.rect.colliderect(enemy.rect):
                    player_1.bullets.remove(bullet)
                    puntaje += 10
                    tomaaa.play()
                    enemy.vidas -= 1
                    enemy.animacion_muerte(level3.lista_enemigos_nivel_3)
                    if enemy.vidas <= 0:
                        tomaaa.play()
                        enemies_to_remove_3.append(enemy)  


        
        for enemy in enemies_to_remove_3:
            if enemy in level3.lista_enemigos_nivel_3:  
                level3.lista_enemigos_nivel_3.remove(enemy)

        if len(level3.lista_enemigos_nivel_3) == 0:
            juego_terminado = True
            guardar_puntaje(nombre_usuario, puntaje)
            puntaje_final = puntaje
            mostrar_pantalla_final_3(puntaje_final)
            nivel_actual += 1


        for bala in lista_balas_enemigos:
            bala.update()
            bala.draw(screen)
            if bala.rect.colliderect(player_1.rect):
                player_1.vidas -= 1
                corazon.vidas -= 1
                lista_balas_enemigos.remove(bala)



    player_1.update(delta_ms, level1.lista_plataformas_nivel_1 if nivel_actual == 1 else level2.lista_plataformas_nivel_2 if nivel_actual == 2 else level3.lista_plataformas_nivel_3)
    player_1.do_animation(delta_ms)
    player_1.draw(screen,puntaje,tiempo_restante_segundos)
    


    if player_1.vidas <= 0:
        juego_terminado = True
        puntaje_final = puntaje
        mostrar_pantalla_final_perdiste(puntaje_final)
        
    corazon.draw(screen,corazon.vidas)

    if tiempo_restante_segundos <= 0:
        juego_terminado = True
        puntaje_final = puntaje
        mostrar_pantalla_final_perdiste(puntaje_final)

    pygame.display.flip()

    


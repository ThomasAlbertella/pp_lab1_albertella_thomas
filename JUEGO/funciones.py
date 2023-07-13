import pygame
from constantes import *
import re
from plataform import Platform
from records import *
import sys



pygame.init()


ventana = pygame.display.set_mode((ANCHO, ALTO))
fondo_inicio = pygame.image.load("JUEGO\images\Blue.png").convert()
fondo_inicio = pygame.transform.scale(fondo_inicio, [800,600])
reloj = pygame.time.Clock()
puntaje = 0

def mostrar_pantalla_pausa():
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                
                if event.key == pygame.K_UP:
                    pygame.mixer.music.set_volume(min(1.0, pygame.mixer.music.get_volume() + 0.1))
                elif event.key == pygame.K_DOWN:
                    pygame.mixer.music.set_volume(max(0.0, pygame.mixer.music.get_volume() - 0.1))

        ventana.fill((0, 0, 0))  
        dibujar_texto(ventana, "PAUSA", 32, ANCHO // 2, ALTO // 2 - 50)  
        dibujar_texto(ventana, "Presiona P para continuar", 20, ANCHO // 2, ALTO // 2 - 20)  
        dibujar_texto(ventana, f"Volumen: {int(pygame.mixer.music.get_volume() * 100)}%", 20, ANCHO // 2, ALTO // 2 + 40)  
        
        top_puntajes = obtener_mejores_puntajes(3)

        
        x = ANCHO // 2
        y = ALTO // 2 + 100  
        for i, puntaje in enumerate(top_puntajes):
            nombre, valor = puntaje
            linea = f"{i+1}. {nombre}: {valor}"
            dibujar_texto(ventana, linea, 20, x, y + i*20)
        pygame.display.flip()








def dibujar_texto(surface, text, size, x, y):
	fuente = pygame.font.SysFont("verdana", size) 
	text_surface = fuente.render(text, True, BLANCO)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x,y)
	surface.blit(text_surface, text_rect)


	
def mostrar_pantalla_go():
	ventana.blit(fondo_inicio, [0,0])
	dibujar_texto(ventana, "JUMP AND FIRE", 65, ANCHO // 2, ALTO // 8)
	dibujar_texto(ventana, "TENES 60 SEGUNDOS PARA MATAR", 24, ANCHO // 2, ALTO // 3)
	dibujar_texto(ventana,f"NIVEL 1", 50, ANCHO // 2, ALTO * 2/4)
	dibujar_texto(ventana, "Presiona cualquier tecla para continuar", 20, ANCHO // 2, ALTO * 3/4)
	pygame.display.flip()
	esperando = True
	while esperando:
		reloj.tick(60)
		for evento in pygame.event.get():
			if(evento.type == pygame.QUIT):
				pygame.quit()
			if(evento.type == pygame.KEYUP):
				esperando = False

def ingresar_nombre():
	
    ventana.fill(VERDE)
    dibujar_texto(ventana, "Ingresa tu nombre", 32, ANCHO // 2, ALTO // 15)
    pygame.draw.rect(ventana, BLANCO, (ANCHO // 4, ALTO // 2, ANCHO // 2, 32))
    pygame.display.flip()

    nombre = ""
    ingresando = True
    while ingresando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if re.match("^[A-Za-z]+$", nombre):
                        ingresando = False
                    else:
                        nombre = ""
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode

        ventana.fill(NEGRO)
        dibujar_texto(ventana, "Ingresa tu nombre", 32, ANCHO // 2, ALTO // 4)
        pygame.draw.rect(ventana, BLANCO, (ANCHO // 4, ALTO // 2, ANCHO // 2, 32))

        nombre_texto = pygame.font.SysFont("verdana", 32).render(nombre, True, NEGRO)
        ventana.blit(nombre_texto, (ANCHO // 2 - nombre_texto.get_width() // 2, ALTO // 2 - nombre_texto.get_height() // 4))

        pygame.display.flip()

    return nombre
   

def mostrar_pantalla_nivel_2():
	ventana.blit(fondo_inicio, [0,0])
	dibujar_texto(ventana, "JUMP AND FIRE", 65, ANCHO // 2, ALTO // 8)
	dibujar_texto(ventana, "NIVEL 2", 24, ANCHO // 2, ALTO // 3)
	
	dibujar_texto(ventana, "Presiona cualquier tecla para continuar", 20, ANCHO // 2, ALTO * 3/4)
	pygame.display.flip()
	esperando = True
	while esperando:
		reloj.tick(60)
		for evento in pygame.event.get():
			if(evento.type == pygame.QUIT):
				pygame.quit()
			if(evento.type == pygame.KEYUP):
				esperando = False

def mostrar_pantalla_nivel_3():
	ventana.blit(fondo_inicio, [0,0])
	dibujar_texto(ventana, "JUMP AND FIRE", 65, ANCHO // 2, ALTO // 8)
	dibujar_texto(ventana, "NIVEL 3", 24, ANCHO // 2, ALTO // 3)
	
	dibujar_texto(ventana, "Presiona cualquier tecla para continuar", 20, ANCHO // 2, ALTO * 3/4)
	pygame.display.flip()
	esperando = True
	while esperando:
		reloj.tick(60)
		for evento in pygame.event.get():
			if(evento.type == pygame.QUIT):
				pygame.quit()
			if(evento.type == pygame.KEYUP):
				esperando = False

def mostrar_pantalla_final_1(puntaje_final):
        ventana.blit(fondo_inicio, [0,0])
        dibujar_texto(ventana, "FIN DE PARTIDA", 32, ANCHO // 2, ALTO // 3)
        dibujar_texto(ventana, "Puntaje obtenido: " + str(puntaje_final), 20, ANCHO // 2, ALTO // 2 - 30)
        dibujar_texto(ventana, "Presiona Y para ir al NIVEL 2", 20, ANCHO // 2, ALTO // 2 + 30)
        pygame.display.flip()

        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_y:
                        esperando = False  
                        nivel_actual = 2  
                        mostrar_pantalla_nivel_2()  
                

def mostrar_pantalla_final_2(puntaje_final):
    ventana.blit(fondo_inicio, [0,0])
    dibujar_texto(ventana, "FIN DE PARTIDA", 32, ANCHO // 2, ALTO // 3)
    dibujar_texto(ventana, "Puntaje obtenido: " + str(puntaje_final), 20, ANCHO // 2, ALTO // 2 - 30)
    dibujar_texto(ventana, "Presiona Y para ir al NIVEL 3", 20, ANCHO // 2, ALTO // 2 + 30)
    
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_y:
                    esperando = False 
                    nivel_actual = 2  
                    mostrar_pantalla_nivel_2()  
                


def mostrar_pantalla_final_3(puntaje_final):
    ventana.blit(fondo_inicio, [0,0])
    dibujar_texto(ventana, "GANASTE", 32, ANCHO // 2, ALTO // 3)
    dibujar_texto(ventana, "Puntaje obtenido: " + str(puntaje_final), 20, ANCHO // 2, ALTO // 2 - 30)
    
    
    
    top_puntajes = obtener_mejores_puntajes(3)

    
    x = ANCHO // 2
    y = ALTO // 2 + 30
    for i, puntaje in enumerate(top_puntajes):
        nombre, valor = puntaje
        linea = f"{i+1}. {nombre}: {valor}"
        dibujar_texto(ventana, linea, 20, x, y + i*20)
    ganaste = pygame.mixer.Sound("JUEGO\sounds\X2Download.app - Sonido de ganador _ Efecto de sonido (128 kbps).mp3")
    ganaste.play()
    pygame.mixer.music.stop()
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_y:
                    esperando = False  
                    nivel_actual = 2  
                    mostrar_pantalla_nivel_2()  
                


    
def mostrar_pantalla_final_perdiste(puntaje_final):
    ventana.blit(fondo_inicio, [0,0])
    dibujar_texto(ventana, "PERDISTE", 32, ANCHO // 2, ALTO // 3)
    dibujar_texto(ventana, "Puntaje obtenido: " + str(puntaje_final), 20, ANCHO // 2, ALTO // 2 - 30)
    

    
    top_puntajes = obtener_mejores_puntajes(3)

    
    x = ANCHO // 2
    y = ALTO // 2 + 30
    for i, puntaje in enumerate(top_puntajes):
        nombre, valor = puntaje
        linea = f"{i+1}. {nombre}: {valor}"
        dibujar_texto(ventana, linea, 20, x, y + i*20)
    perdiste = pygame.mixer.Sound("JUEGO\sounds\X2Download.app - Perdiste, perdiste no hay nadie peor que vos - Jose Maria (128 kbps).mp3")
    perdiste.play()
    pygame.mixer.music.stop()
    pygame.display.flip()

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
                     
                    
            
    
            
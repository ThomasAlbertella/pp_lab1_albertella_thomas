import pygame
from constantes import *
from player import Player
from plataform import Platform
from bullet import Bullet
from enemy import Enemy
from funciones import *
from records import *
from corazon import Corazon
from banana import Banana
from manzana import Manzana
from kiwi import Kiwi
from trampa_1 import Trampas

class Level3():
    def __init__(self, lista_balas_enemigos):
        self.lista_balas_enemigos = lista_balas_enemigos

        self.lista_enemigos_nivel_3 = []
        self.lista_enemigos_nivel_3.append(Enemy(x=0, y=420, frame_rate_ms=40, flipped=True, lista_balas_enemigos=lista_balas_enemigos, vidas=1,one_or_two_flag=True))
        self.lista_enemigos_nivel_3.append(Enemy(x=763, y=311, frame_rate_ms=40, flipped=False, lista_balas_enemigos=lista_balas_enemigos, vidas=1,one_or_two_flag=True))
        self.lista_enemigos_nivel_3.append(Enemy(x=0, y=200, frame_rate_ms=40, flipped=True, lista_balas_enemigos=lista_balas_enemigos, vidas=1,one_or_two_flag=True))
        self.lista_enemigos_nivel_3.append(Enemy(x=735, y=75, frame_rate_ms=40, flipped=False, lista_balas_enemigos=lista_balas_enemigos, vidas=1,one_or_two_flag=False))
        
        self.lista_plataformas_nivel_3 = []
        self.lista_plataformas_nivel_3.append(Platform(0, 450, 400, 40, 1))
        self.lista_plataformas_nivel_3.append(Platform(0, 230, 400, 40, 2))
        self.lista_plataformas_nivel_3.append(Platform(300, 340, 600, 40, 1))
        self.lista_plataformas_nivel_3.append(Platform(300, 124, 600, 40, 2))

        self.lista_objetos_nivel_3 = []
        
        self.lista_objetos_nivel_3.append(Manzana(300, 200, frame_rate_ms=40))
        

        self.lista_trampas_nivel_3 = []
        self.lista_trampas_nivel_3.append(Trampas(x=140, y=200, frame_rate_ms=40, trampa_2_flag=False))
        self.lista_trampas_nivel_3.append(Trampas(500, 500, frame_rate_ms=80, trampa_2_flag=True))
        self.lista_trampas_nivel_3.append(Trampas(480, 90, frame_rate_ms=80, trampa_2_flag=True))
        self.lista_trampas_nivel_3.append(Trampas(600, 300, frame_rate_ms=60, trampa_2_flag=False))



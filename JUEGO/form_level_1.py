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





class Level1():
    def __init__(self, lista_balas_enemigos):
        self.lista_balas_enemigos = lista_balas_enemigos
        
        self.lista_enemigos_nivel_1 = []
        self.lista_enemigos_nivel_1.append(Enemy(x=0, y=120, frame_rate_ms=40, flipped=True, lista_balas_enemigos=lista_balas_enemigos,vidas=1,one_or_two_flag=True))
        self.lista_enemigos_nivel_1.append(Enemy(x=0, y=280, frame_rate_ms=40, flipped=True, lista_balas_enemigos=lista_balas_enemigos,vidas=1,one_or_two_flag=True))
        self.lista_enemigos_nivel_1.append(Enemy(x=760, y=420, frame_rate_ms=40, flipped=False, lista_balas_enemigos=lista_balas_enemigos,vidas=1,one_or_two_flag=True))

        
        self.lista_plataformas_nivel_1 = []
        self.lista_plataformas_nivel_1.append(Platform(200, 450, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(240, 450, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(280, 450, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(0, 150, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(40, 150, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(80, 150, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(80, 190, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(120, 190, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(160, 190, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(300, 350, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(340, 350, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(260, 350, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(260, 310, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(220, 310, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(180, 310, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(140, 310, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(100, 310, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(80, 310, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(40, 310, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(0, 310, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(760, 450, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(720, 450, 40, 40, 1))
        self.lista_plataformas_nivel_1.append(Platform(680, 450, 40, 40, 1))

        self.lista_objetos_nivel_1 = []
        self.lista_objetos_nivel_1.append(Banana(200, 400, frame_rate_ms=40))
        self.lista_objetos_nivel_1.append(Manzana(300, 300, frame_rate_ms=40))
        self.lista_objetos_nivel_1.append(Kiwi(400, 200, frame_rate_ms=40))

        self.lista_trampas_nivel_1 = []
        self.lista_trampas_nivel_1.append(Trampas(x=400, y=400, frame_rate_ms=40, trampa_2_flag=False))
        self.lista_trampas_nivel_1.append(Trampas(500, 300, frame_rate_ms=80, trampa_2_flag=True))
        self.lista_trampas_nivel_1.append(Trampas(100, 150, frame_rate_ms=80, trampa_2_flag=True))
import pygame as pg
from pygame.locals import *
import sys,random
from entities import *

WHITE = (255,255,255)
YELLOW = (255,255,0)


class Virus (pg.sprite.Sprite):
    vx = 0
    vy = 0
    __color = WHITE
    num_sprites = 12

    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20,20),pg.SRCALPHA,32)
        self.rect = self.image.get_rect()
        self.image.blit(self.image,(0,0))
        self.reset()

    def reset(self):
        self.vx = random.choice([-7,-5,5,7])
        self.vy = random.choice([-7,-5,5,7])
        self.rect.centerx = 400
        self.rect.centery = 400

    def comprobarChoque (self,something): #desde la bola voy a comprobar que choco con algo, y si choco, modifico mi velovidad
        dx = abs(self.rect.centerx - something.rect.centerx)#valor absoluto
        dy = abs(self.rect.centery - something.rect.centery)

        if dx < (self.rect.w + something.rect.w) //2 and dy < (self.rect.w + something.rect.h) //2:
            self.vx*= -random.uniform(0.8,1.3) #entre el 90 y 100 de la velocidad(ralentiza o le da mas velocidad a la pelota)
            self.vy*= -random.uniform(0.8,1.3)

            self.rect.centerx += self.vx
            self.rect.centery += self.vy #forzamos un paso para que no rebote hacia el otro lado(me coloca la bola un paso mas adelante sin pintarla, asi no se me va hacia la pared)
    
       
            

    def update(self,limSupX,limSupY):
        if self.rect.centerx >= limSupX or self.rect.centerx <=0:
            self.vx = 0
            self.vy = 0
            

        if self.rect.centery >= limSupY or self.rect.centery <=0:
            self.vy *= -1

        self.rect.centerx += self.vx
        self.rect.centery += self.vy
            





class Ship (pg.sprite.Sprite):
    vx = 0
    vy = 0
    __color = WHITE

    def __init__(self, centerx):
        super().__init__()
        self.image = pg.Surface((25,100))
        self.image.fill(self.__color)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = 400

    @property
    def color (self):
        return self.__color

    @color.setter
    def color(self,tupla_color):
        self.__color = tupla_color
        self.image.fill(self.__color)

    def update(self,limSupX,limSupY):
        self.rect.centerx += self.vx
        self.rect.centery += self.vy

        if self.rect.centery < self.rect.h // 2:
            self.rect.centery = self.rect.h //2

        if self.rect.centery > limSupY - self.rect.h // 2:
            self.rect.centery = limSupY - self.rect.h //2

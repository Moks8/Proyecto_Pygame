import pygame as pg
from pygame.locals import *
import sys,random
from sprites import *

BACKGROUND = (255,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

WIN_GAME_SCORE = 3

class Game:
    def __init__(self):
        #inicializar
        self.pantalla = pg.display.set_mode((800,600))
        self.pantalla.fill(BACKGROUND) #colorear el fondo
        self.pantalla.blit(self.pantalla,(0,0))
        self.virus = Virus()
        
        self.ship = Ship(30)

        self.status = "Partida"

        self.font = pg.font.Font("fonts/font.ttf",40)
        self.fontGrande = pg.font.Font("fonts/font.ttf",60)

        self.marcadorOne= self.font.render("0",True,WHITE)
        self.marcadorTwo= self.font.render("0",True,WHITE)
        
        self.text_game_over = self.fontGrande.render("GAME OVER",True,YELLOW)
        self.text_insert_coin = self.font.render("<SPACE> - Inicio partida",True,WHITE)

        self.scoreOne = 0
        self.scoreTwo = 0

        pg.display.set_caption("Covid")
        
        

    def bucle_partida(self):
      
        game_over = False
        self.scoreOne = 0
        self.scoreTwo= 0 
        self.marcadorOne = self.font.render(str(self.scoreOne),True,WHITE)
        self.marcadorTwo = self.font.render(str(self.scoreTwo),True,WHITE)
        
        while not game_over:
            game_over = self.handlenEvent()
            
            self.virus.update(800, 600)
            self.ship.update(800,600)

            self.virus.comprobarChoque(self.ship)

            if self.virus.vx == 0 and self.virus.vy == 0 :
                if self.virus.rect.centerx >=800:
                    self.scoreOne += 1
                    self.marcadorOne = self.font.render(str(self.scoreOne),True,WHITE)
                if self.virus.rect.centerx <= 0:
                    self.scoreTwo += 1
                    self.marcadorTwo = self.font.render(str(self.scoreTwo),True,WHITE)

                if self.scoreOne == WIN_GAME_SCORE or self.scoreTwo == WIN_GAME_SCORE:
                    game_over = True

                self.virus.reset()

            self.pantalla.blit(self.pantalla,(0,0))
            self.pantalla.blit(self.ship.image,(self.ship.rect.x,self.ship.rect.y))
            self.pantalla.blit(self.virus.image,(self.virus.rect.x,self.virus.rect.y))

            pg.display.flip()#actualizar la pantalla
        self.status = "Inicio"
        
   



    def bucle_inicio(self):
       
        inicio_partida = False
        while not inicio_partida:
            for event in pg.event.get():
                if event.type == QUIT:
                 self.quit()
                 
                if event.type == KEYDOWN:    #se hunde, KEYUP, se libera
                    if event.key == K_SPACE:
                        inicio_partida = True

            self.pantalla.fill((0,0,255))
            self.pantalla.blit(self.text_game_over,(100,100))
            self.pantalla.blit(self.text_insert_coin,(100,200))
            

            pg.display.flip()
        
        self.status = "Partida"
    

    def handlenEvent(self):
        for event in pg.event.get():
            if event.type == QUIT:
                 self.quit()
            
            if event.type == KEYDOWN:    #se hunde, KEYUP, se libera
                if event.key == K_w:
                    self.ship.vy = -5 #la velocidad refleja el estado de movimiento
                if event.key == K_z:
                    self.ship.vy = 5
               
                            
            key_pressed = pg.key.get_pressed() #lista donde te deja almacenada las teclas que han sido pulsadas

            if key_pressed[K_w]:
                self.ship.vy -= 1
            elif key_pressed[K_z]:
                self.ship.vy += 1
            else:
                self.ship.vy = 0

        return False
    
    def main_loop(self):
        while True:
            if self.status =="Partida":
                self.bucle_partida()
            else:
                self.bucle_inicio() 
    
    def quit(self):
        pg.quit()
        sys.exit()
    
            

if __name__ == "__main__":
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()
    
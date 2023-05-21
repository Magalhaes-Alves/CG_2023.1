import pygame
from classes.nave import Nave
from classes.Window import Window
from classes.viewport import mapWindow
from classes.clipping import clip
import numpy as np
from classes.Polygon import Polygon


p = Nave(250,250,10)


def game():
    window = Window(800,600)
    janela = Window(600,600)

    janela_teorica = [100,100,300,300]

    asteroids=[]
    bullets=[]
    naves =[]
    
    while(True):
        #janela.screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("Comando: Cima")
                elif event.key == pygame.K_DOWN:
                    print("Comando: Baixo")
                elif event.key == pygame.K_LEFT:
                    print("Comando: Esquerda")
                elif event.key == pygame.K_RIGHT:
                    p.rotacionar(True,800,600)
                elif event.key == pygame.K_SPACE:
                    print("Comando: Espaço")  

        subject_polygon =p.points
        clipping_polygon = [(100,100),(300,100),(300,300),(100,300)]

        #subject_polygon = np.array(subject_polygon)
        clipping_polygon = np.array(clipping_polygon)
        clipped_polygon = clip(subject_polygon, clipping_polygon)

        p2 = Polygon(clipped_polygon)
        mapWindow(p2,janela_teorica,janela)
        p2.desenha(janela)
        pygame.display.update()


if __name__=="__main__":
    game()
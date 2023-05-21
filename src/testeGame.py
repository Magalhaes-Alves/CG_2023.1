import pygame
from classes.nave import Nave
from classes.Window import Window
from classes.viewport import mapWindow
from classes.clipping import clip
import numpy as np
from classes.Polygon import Polygon


def game():
    window = Window(800,600)
    janela = Window(600,600)

    janela_teorica = [300,300,500,500]

    nave_real = Nave(window.width//2,window.height//2,10)

    asteroids_real = []
    asteroids_janela = []
    bullets_real = []
    bullets_janela = []
    naves =[]
    
    while(True):
        janela.screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    nave_real.rotacionar(False,window.width,window.height)
                elif event.key == pygame.K_RIGHT:
                    nave_real.rotacionar(True,window.width,window.height)
                elif event.key == pygame.K_SPACE:
                    print("Comando: Espaço")  

        subject_polygon = nave_real.points
        clipping_polygon = [(janela_teorica[0],janela_teorica[1]),(janela_teorica[2],janela_teorica[1]),
                            (janela_teorica[2],janela_teorica[3]),(janela_teorica[0],janela_teorica[3])]

        #subject_polygon = np.array(subject_polygon)
        clipping_polygon = np.array(clipping_polygon)
        clipped_polygon = clip(subject_polygon, clipping_polygon)
        clipped_polygon = [(int(x[0]), int(x[1])) for x in clipped_polygon]
        nave_jogo = Polygon(clipped_polygon)
        mapWindow(nave_jogo,janela_teorica,janela)
        nave_jogo.scanline(janela,(255,0,0,255))
        pygame.display.update()


if __name__=="__main__":
    game()
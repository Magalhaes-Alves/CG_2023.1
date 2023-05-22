import pygame
from classes.nave import Nave
from classes.Window import Window
from classes.viewport import mapWindow
from classes.clipping import clip
import numpy as np
from classes.Polygon import Polygon
import time

def clipp_polygon(subject_polygon, clipping_polygon):
    clipping_polygon = np.array(clipping_polygon)
    clipped_polygon = clip(subject_polygon, clipping_polygon)
    clipped_polygon = [(int(x[0]), int(x[1])) for x in clipped_polygon]

    return clipped_polygon

def game():
    window = Window(1000,600)
    janela = Window(1000,600)

    janela_teorica = [300,300,700,500]

    nave_real = Nave((janela_teorica[0]+janela_teorica[2])//2, (janela_teorica[1]+janela_teorica[3])//2,10)

    asteroids_real = []
    asteroids_janela = []
    bullets_real = []
    bullets_janela = []
    naves =[]
    
    intervalo_tempo = 15  # Intervalo de tempo em segundos
    tempo_anterior = (time.time() - 15) # Fazendo isso para gerar asteroids na primeira iteração
    
    while(True):
        tempo_atual = time.time()
    
        if tempo_atual - tempo_anterior >= intervalo_tempo:
            # Gera asteroids
            print("Comando executado após o intervalo de tempo")
        
            tempo_anterior = tempo_atual
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
                    nave_real.atirar(bullets_real, bullets_janela) 

        """
        Seção de clipping de todos os elementos da tela
        """
        clipping_polygon = [(janela_teorica[0],janela_teorica[1]),(janela_teorica[2],janela_teorica[1]),
                            (janela_teorica[2],janela_teorica[3]),(janela_teorica[0],janela_teorica[3])]
        # Clipping da nave
        subject_polygon = nave_real.points

        nave_jogo = Polygon(clipp_polygon(subject_polygon, clipping_polygon))
        mapWindow(nave_jogo,janela_teorica,janela)
        nave_jogo.scanline(janela,(255,0,0,255))

        # Clipping balas
        for i, bala in enumerate(bullets_real):
            subject_polygon = bala.points

            bullets_janela[i] = Polygon(clipp_polygon(subject_polygon, clipping_polygon))
            mapWindow(bullets_janela[i], janela_teorica, janela)
            bullets_janela[i].scanline(janela,(255,0,0,255))

            bala.movimentar()
            
            if bala.dentro_janela(janela_teorica) == False:
                bullets_real.pop(i)
                bullets_janela.pop(i)

        # Clipping asteroids
        for i, asteroid in enumerate(asteroids_real):
            subject_polygon = asteroid.points

            asteroids_janela[i] = Polygon(clipp_polygon(subject_polygon, clipping_polygon))
            mapWindow(asteroids_janela[i], janela_teorica, janela)
            asteroids_janela[i].scanline(janela,(255,0,0,255))

            asteroid.movimentar()
            
            """if asteroid.dentro_janela(janela_teorica) == False:
                asteroids_real.pop(i)
                asteroids_janela.pop(i)"""

        pygame.display.update()


if __name__=="__main__":
    game()
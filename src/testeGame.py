import pygame
from classes.nave import Nave
from classes.Window import Window
from classes.viewport import mapWindow
from classes.clipping import clip
import numpy as np
from classes.Polygon import Polygon
from classes.asteroids import Asteroids
from classes.Tranformations import escala, translacao
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
    
    intervalo_tempo = 3  # Intervalo de tempo em segundos
    tempo_anterior = (time.time() - 10) # Fazendo isso para gerar asteroids na primeira iteração
    direcao = 2
    Rodando = True
    while(Rodando):
        tempo_atual = time.time()
    
        if tempo_atual - tempo_anterior >= intervalo_tempo:
            # Gera asteroids            
            tempo_anterior = tempo_atual
            asteroid = Asteroids((janela_teorica[0]+janela_teorica[2])//2, (janela_teorica[1]+janela_teorica[3])//2, direcao, janela_teorica)
            asteroids_real.append(asteroid)
            asteroids_janela.append(asteroid)
            direcao +=1
            if direcao > 3:
                direcao = 0
        
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
        nave_jogo.scanlineInterpolacao(janela, [[0,0,255],
                                                [255,255,255],
                                                [255,255,255],
                                                [255,255,255]])

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
            
            asteroids_janela[i] = Polygon(clipp_polygon(subject_polygon, clipping_polygon),"classes/lua.jpg",[[0,0],[1,0],[1,1],[0,1]])
            
            #Verifica se o asteroid está dentro da janela
            if len(asteroids_janela[i].points)>0:
                mapWindow(asteroids_janela[i], janela_teorica, janela)
                
                if len(asteroids_janela[i].points)==5:
                    asteroids_janela[i].textureCoordenates = [[0,0],[1,0],[1,1],[0,1],[0,0]]

                asteroids_janela[i].scanlineT(janela)

            colision = clipp_polygon(subject_polygon, nave_real.points)
            if len(colision)>0:
                janela_teorica_polygon = Polygon(clipping_polygon)
                sx = 0.4
                sy = 0.4
                
                escala(janela_teorica_polygon, sx, sy)
                centro_x = (janela_teorica[2] + janela_teorica[0])//2
                centro_y = (janela_teorica[3] + janela_teorica[1])//2
                centro_x_novo = (janela_teorica_polygon.points[0,0] + janela_teorica_polygon.points[2,0])//2
                centro_y_novo = (janela_teorica_polygon.points[0,1] + janela_teorica_polygon.points[2,1])//2
                translacao(janela_teorica_polygon, (centro_x - centro_x_novo), (centro_y - centro_y_novo))


                
                janela_teorica = [janela_teorica_polygon.points[0,0], janela_teorica_polygon.points[0,1],
                                  janela_teorica_polygon.points[2,0], janela_teorica_polygon.points[2,1]]
                
                clipping_polygon = [(janela_teorica[0],janela_teorica[1]),(janela_teorica[2],janela_teorica[1]),
                            (janela_teorica[2],janela_teorica[3]),(janela_teorica[0],janela_teorica[3])]
                subject_polygon = nave_real.points
                nave_jogo = Polygon(clipp_polygon(subject_polygon, clipping_polygon))
                

                """ game_over = Polygon([[430,365],
                                     [570,365],
                                     [550,380],
                                     [430,380]
                                     ],"classes/game-over.png",[[0,0],[1,0],[1,1],[0,1]])
                
                mapWindow(game_over,janela_teorica,janela)
                game_over.scanlineT(janela) """
                janela.screen.fill((0,0,0))

                mapWindow(nave_jogo,janela_teorica,janela)
                nave_jogo.scanlineInterpolacao(janela, [[0,0,255],
                                                [255,255,255],
                                                [255,255,255],
                                                [255,255,255]])                
                Rodando = False
                

            asteroid.movimentar()            

        """
        Seção para verificar se há colisão entre algum asteroid e as balas e/ou nave
        """
        # Entre asteroids e balas
        for i, asteroid in enumerate(asteroids_real):
            for j, bala in enumerate(bullets_real):
                colision = clipp_polygon(bala.points, asteroid.points)
                if len(colision)>0:
                    bullets_real.pop(j)
                    bullets_janela.pop(j)
                    asteroids_real.pop(i)
                    asteroids_janela.pop(i)

        pygame.display.update()

    while(True):
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


if __name__=="__main__":
    game()
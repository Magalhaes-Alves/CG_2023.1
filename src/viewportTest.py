from classes.Polygon import Polygon
from classes.viewport import *
from classes.Tranformations import *
from classes.clipping import *
from classes.Window import Window
from time import sleep
import pygame

def animacao():
  
    v = [300,200]
    j = [-2, -2, 3, 2]

    i =5
    p = Polygon([[-1,-1],
                 [1,-1],
                 [1,1],
                 [-1,1]]
    )
    print(p.points)
    p.texture='./img/gato.jpg'
    p.textureCoordenates=[[0,0],
                          [1,0],
                          [1,1],
                          [0,1]]
    
    

    window = Window(v[0],v[1])
    mapWindow(p,j, window)
    rotacao(p, 2,200,300)
    print(p.points)

    while(True):
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
                    print("Comando: Direita")
                elif event.key == pygame.K_SPACE:
                    print("Comando: Espaço")  
    
        window.screen.fill((0,0,0))
        p.scanlineT(window)
        
        rotacao(p,30,200,300)
        
        pygame.display.update()

def teste_clipping():
    window = Window(400,400)
    viewport = [(200,200), (300,300)]

    reta = [(1,1), (399,399)]
    reta_desenhada = cohen_sutherland(200,200,300,300,1,1,399,399)
    window.bresenham(reta_desenhada[0][0], reta_desenhada[0][1], reta_desenhada[1][0], reta_desenhada[1][1], (255, 255, 255))
    while(True):
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
                    print("Comando: Direita")
                elif event.key == pygame.K_SPACE:
                    print("Comando: Espaço")  
        
        pygame.display.update()

def teste_clipping2():
    window = Window(400,400)
    viewport = [(200,200), (300,300)]
    subject_polygon = [(250,250), (320,300), (280,300)]
    clipping_polygon = [(200,200),(300,200),(300,300),(200,300)]
    #reta = [(1,1), (399,399)]
    subject_polygon = np.array(subject_polygon)
    clipping_polygon = np.array(clipping_polygon)
    clipped_polygon = clip(subject_polygon, clipping_polygon)
    print(clipped_polygon)
    clipped_polygon = [(int(x[0]), int(x[1])) for x in clipped_polygon]
    p = Polygon(clipped_polygon)
    p.texture = "./img/gato.jpg"
    p.textureCoordenates=[[0,0],
                          [1,0],
                          [1,1],
                          [0,1]]
    #window.bresenham(reta_desenhada[0][0], reta_desenhada[0][1], reta_desenhada[1][0], reta_desenhada[1][1], (255, 255, 255))
    while(True):
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
                    print("Comando: Direita")
                elif event.key == pygame.K_SPACE:
                    print("Comando: Espaço")  
        p.scanlineT(window)
        pygame.display.update()

if __name__=="__main__":
    #animacao()
    teste_clipping2()
        
        
    
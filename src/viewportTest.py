from classes.Polygon import Polygon
from classes.viewport import *
from classes.Tranformations import *
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
            
    
        window.screen.fill((0,0,0))
        p.scanlineT(window)
        
        rotacao(p,2,200,300)
        
        pygame.display.update()

if __name__=="__main__":
    animacao()
        
        
        
    
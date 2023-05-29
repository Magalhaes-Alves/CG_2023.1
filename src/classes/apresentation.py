from classes.Polygon import Polygon
from classes.Window import Window
import pygame
from random import randint
from classes.estrela import estrela
from classes.Tranformations import translacao
from copy import deepcopy

def apresentation():

    estrelas =[]
    planetas =[]

    janela = Window(800,600)
    time_estrela=0
    time_planeta =0

    M = Polygon([[140,80], #0
                [160,80], #1
                [170,110], #2
                [180,80], #3
                [200,80], #4
                [200,140], #5
                [180,140], #6
                [180,100], #7
                [170,130], #8
                [160,100], #9
                [160,140], #10
                [140,140] #11
                ])
        
    E = Polygon([[210,80],
                [250,80],
                [250,90],
                [220,90],
                [220,100],
                [250,100],
                [250,110],
                [220,110],
                [220,120],
                [250,120],
                [250,130],
                [250,140],
                [210,140]
                ])
    E2 = deepcopy(E)

    translacao(E2,120,0)

    T= Polygon([[260,80],
                [320,80],
                [320,100],
                [300,100],
                [300,140],
                [280,140],
                [280,100],
                [260,100]
                ])
        
        
    R = Polygon([[450,80],
                    [490,80],
                    [490,140],
                    [450,140]
                    ])
    
    R.texture = "classes/R.png"

    R.textureCoordenates = [[0,0],
                            [1,0],
                            [1,1],
                            [0,1]]

    S = Polygon([[580,80], #0
                 [650,80],#1
                 [650,100],#2
                 [610,100],#3
                 [610,110],#4
                 [650,110],#5
                 [650,140],#6
                 [580,140],#7
                 [580,130],#8
                 [630,130],
                 [630,120],
                 [580,120]
                 ])

    while(True):
        time_estrela+=1
        time_estrela = 0 if time_estrela>10 else time_estrela

        time_planeta+=1
        time_planeta = 0 if time_planeta>40 else time_planeta
        janela.screen.fill((0,0,0))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.display.quit()
                    return
            
        for i in estrelas:
            i.centro=[i.centro[0],i.centro[1]-10]
        
        fora_tela =[]
        for k,v in enumerate(estrelas):
            
            if v.centro[1]+v.distancias[0]<0:
                 fora_tela.append(k)

        for i in reversed(fora_tela):
             estrelas.pop(i)

        if len(estrelas)<60 and time_estrela==10:
            xc = randint(21,janela.width-10)

            yc= janela.height-21
            
            estrelas.append(estrela(xc,yc,20,5))

        for i in estrelas:
             i.scanline(janela,(255,255,255))

        
        for i in planetas:
            i[1]-=5
        
        fora_tela =[]
        for k,v in enumerate(planetas):
            
            if v[1]+v[2]<0:
                 fora_tela.append(k)

        for i in reversed(fora_tela):
             planetas.pop(i)
        
        if len(planetas)<10 and len(estrelas)<60 and time_planeta ==40:
            xc = randint(21,janela.width-10)

            yc= janela.height-21
            r = randint(5,15)
            planetas.append([xc,yc,r])
            planeta(janela,xc,yc,r)

        for i in planetas:
             planeta(janela,i[0],i[1],i[2])


        start = Polygon([[300,500],
                         [500,500],
                         [500,550],
                         [300,550]
                         ])
        
        start.texture = "classes/enter-crop.jpg"
        start.textureCoordenates= [[0,0],
                                   [1,0],
                                   [1,1],
                                   [0,1]]
        start.scanlineT(janela)

        fundo_titulo = Polygon([[100,60],
                                [700,60],
                                [700,160],
                                [100,160]])
        
        fundo_titulo.scanline(janela,(0,0,0))
        
        
        R.scanlineT(janela)

        E.scanline(janela,(255,255,255))
        
        T.scanline(janela,(255,255,255))

        E2.scanline(janela,(255,255,255))

        janela.drawEllipse(410,110,25,30,(255,255,255))
        janela.floodFill(410,110,(255,255,255),(0,0,0))

        janela.drawEllipse(410,110,10,15,(0,0,0))
        janela.floodFill(410,110,(0,0,0),(255,255,255))

        M.scanline(janela,(255,255,255))

        janela.drawEllipse(410+120,110,25,30,(255,255,255))
        janela.floodFill(410+120,110,(255,255,255),(0,0,0))

        janela.drawEllipse(410+120,110,10,15,(0,0,0))
        janela.floodFill(410+120,110,(0,0,0),(255,255,255))

        S.scanline(janela ,(255,255,255))
        

        pygame.display.update()
    


def planeta(window,xc,yc,r):
     
     window.drawCircle(xc,yc,r,(0,0,255))
     window.floodFill(xc,yc,(255,0,0),(0,0,0))

     window.drawCircle(xc,yc-r>>1,r>>1,(0,0,255))
     window.floodFill(xc+(r>>1),yc-(r>>1),(0,0,255),(255,0,0))

     window.bresenham(xc-r,yc,xc+r,yc,(0,120,250))
     window.bresenham(xc-r,yc-2,xc+r,yc-2,(0,120,250))
     
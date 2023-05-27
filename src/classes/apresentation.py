from Polygon import Polygon
from Window import Window
import pygame
from random import randint
from nave import Nave
from estrela import estrela

def apresentation():

    estrelas =[]
    planetas =[]

    janela = Window(800,600)
    time_estrela=0
    time_planeta =0
    while(True):
        time_estrela+=1
        time_estrela = 0 if time_estrela>10 else time_estrela

        time_planeta+=1
        time_planeta = 0 if time_planeta>40 else time_planeta
        janela.screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.K_SPACE:
                break
        
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


        """ r = randint(40,80)
        xc = randint(0,janela.width)
        yc = randint(0,janela.height)

        xc = xc-(xc +r-janela.width-1) if xc +r>= janela.width else xc
        xc = xc+abs(xc-r) if xc -r< 0 else xc

        yc = yc -(yc+r- janela.height-1)if yc +r>= janela.height else yc
        yc = yc + abs(yc-r)if yc -r<0 else yc

        circles.append([xc,yc,r])
        janela.drawCircle(xc,yc,r,(255,255,255))
        print(circles)
        pygame.display.update()
        pygame.time.delay(3000)
        janela.floodFill(xc,yc,(255,255,255),(0,0,0))
        pygame.display.update()

        if len(circles) >0 and randint(0,3)==1:
            c = circles.pop(0)
            janela.floodFill(c[0],c[1],(0,0,0),(255,255,255))  """
        
        """ xc =randint(0,janela.width)
        yc = randint(0,janela.height)

             
        p = Polygon(estrela(xc,yc,20,5))
        p.scanline(janela,(255,255,255)) """



        # Letra O
        """ xc,yc = 200,100

        janela.drawEllipse(xc,yc,30,40,(255,255,255))
        janela.floodFill(xc,yc,(255,255,255),(0,0,0))
        janela.drawEllipse(xc,yc,20,30,(0,0,0))
        janela.floodFill(xc,yc,(0,0,0),(255,255,255))

        # Letra R

        p = Polygon([[250,100],
                     [300,100],
                     [300,110],
                     [260,110],
                     [260,140],
                     [250,140]
                     ])
        p.scanline(janela,(255,255,255))

        # Letra b

        p = Polygon([[320,70],
                     [330,70],
                     [330,105],
                     [360,105],
                     [360,140],
                     [320,140]
                     ])
        
        p.scanline(janela,(255,255,255))
        
        p= Nave(390,120,3)
        p.scanline(janela,(255,255,255)) """
        

        pygame.display.update()
    


def planeta(window,xc,yc,r):
     
     window.drawCircle(xc,yc,r,(0,0,255))
     window.floodFill(xc,yc,(255,0,0),(0,0,0))

     window.drawCircle(xc,yc-r>>1,r>>1,(0,0,255))
     window.floodFill(xc+(r>>1),yc-(r>>1),(0,0,255),(255,0,0))

     window.bresenham(xc-r,yc,xc+r,yc,(0,120,250))
     window.bresenham(xc-r,yc-2,xc+r,yc-2,(0,120,250))
     




     
     

def starCreator(xc,yc,dmaior,dmenor):
       
    return p



if __name__=="__main__":
        apresentation()



        

    #game()
from Polygon import Polygon
from Window import Window
import pygame
from random import randint
from nave import Nave

def apresentation():

    estrelas =[]

    janela = Window(800,600)
    time=0
    while(True):
        time+=1
        time = 0 if time>10 else time
        janela.screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.K_SPACE:
                break
        
        for i in estrelas:
            
            i[1]-=10

        fora_tela =[]
        for k,v in enumerate(estrelas):
            
            if v[1]+v[2]<0:
                 fora_tela.append(k)

        for i in reversed(fora_tela):
             estrelas.pop(i)

        if len(estrelas)<60 and time==10:
            xc = randint(21,janela.width-10)

            yc= janela.height-21
            
            estrelas.append([xc,yc,20,5])
        #print(estrelas)
        for i in estrelas:
             p = Polygon(starCreator(i[0],i[1],20,5))
             p.scanline(janela,(255,255,255))

                  


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
     
     window.drawCircle(xc,yc,r,(255,0,0))
     window.floodFill(xc,yc,(255,0,0),(0,0,0))


     
     

def starCreator(xc,yc,dmaior,dmenor):
    p = [[xc,yc-dmaior],
         [xc+int(dmenor),yc-int(dmenor)],
        [xc+dmaior,yc],
        [xc+int(dmenor),yc+int(dmenor)],
        [xc,yc+dmaior],
        [xc-int(dmenor),yc+int(dmenor)],
        [xc-dmaior,yc],
        [xc-int(dmenor),yc-int(dmenor)],]   
    return p



if __name__=="__main__":
        apresentation()



        

    #game()
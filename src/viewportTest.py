from classes.Polygon import Polygon
from classes.Tranformations import *
from classes.Window import Window
from time import sleep

def animacao():
  
    v = [500,500]
    j = [0,0,99,99]

    i =5
    p = Polygon([[40*i,40*i],
                 [60*i,40*i],
                 [60*i,60*i],
                 [40*i,60*i]]
    )

    p.texture='./img/gato.jpg'
    p.textureCoordenates=[[0,0],
                          [1,0],
                          [1,1],
                          [0,1]]
    
    
    #cria matriz de rotacao de 2 graus
    
    rotacao(p,3)

    window = Window(v[0],v[1])
    
    while (True):
    
        window

        p.scanlineT(window)
        

        aplicaTransformacao(p,m)
        window.show()

if __name__=="__main__":
    animacao()
        
        
        
    
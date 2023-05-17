from classes.Window import Window
from classes.Polygon import Polygon
from classes.Tranformations import *


janela = Window(500,500,"Teste")
#janela.drawEllipse(250, 250, 50, 100, (255, 255, 255))

#janela.drawCircle(250,250,70,(255,255,255))

""" janela.bresenham(10, 10, 200, 200, (255, 255, 255))
janela.bresenham(10, 10, 200, 10, (255, 255, 255))
janela.bresenham(10, 10, 10, 200, (255, 255, 255))
janela.bresenham(10, 10, 200, 90, (255, 255, 255))
janela.bresenham(10, 10, 90, 200, (255, 255, 255))
 """

""" janela.ddaLine(10, 10, 200, 200, (255, 255, 255))
janela.ddaLine(10, 10, 200, 10, (255, 255, 255))
janela.ddaLine(10, 10, 10, 200, (255, 255, 255))
janela.ddaLine(10, 10, 200, 90, (255, 255, 255))
janela.ddaLine(10, 10, 90, 200, (255, 255, 255))
 """

#janela.floodFill(250,250, (0,0,255), (0,0,0))


#janela.ddaaaLine(100,100,150,150,(255,255,255,255))

""" Teste Polygon """

#poligono1 = Polygon([[250,250],[450,250],[450,350],[250,350]])
#poligono2 = Polygon([[20,20],[20,220],[110,180],[200,220],[110,120],[200,20]])
#poligono2 = Polygon([[20,20],[200,20],[110,120],[200,220],[110,180],[20,200]])


#poligono1.desenhaPoligono(janela, (255,255,255,255))
#poligono1.scanline(janela,(255,120,0))

#poligono2.desenhaPoligono(janela, (255,255,255,255))
#poligono2.scanline(janela,(255,120,0,255))

""" Teste scanline Interpolação """

#pol1 = Polygon([[150,290],[250,200],[350,290]])

#pol1.desenhaPoligono(janela,(255,255,255,255))

#colors = [(255,0,0),
#          (255,0,0),
#          (0,0,255)
#          ]

#pol1.scanlineInterpolacao(janela,colors)

pol2 = Polygon([
        [250,250],
        [300,300],
        [350,250],
        [350,350],
        [250,350]
        ])

colors = [(255,0,0),
          (0,255,0),
          (0,0,255),
          (255,255,255),
          (255,0,100)
          ]

pol2.scanlineInterpolacao(janela,colors)

"""print(pol2.points)
m = criaTransformacao()
m = compoeRotacao(m,2)
aplicaTransformacao(pol2, m)
print(pol2.points)

pol2.desenhaPoligono(janela,(255,255,255,255))
pol2.scanlineInterpolacao(janela,colors) """




#Teste texture

""" i=10
pol_texture = Polygon([[10*i,10*i],
                       [30*i,10*i],
                       [30*i,30*i],
                       [10*i,30*i]
                       ])
pol_texture.desenhaPoligono(janela,(255,0,0,255))

pol_texture.addTexture("img/gato.jpg") """
janela.show()
from classes.Window import Window
from classes.Polygon import Polygon

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

poligono1 = Polygon([[250,250],[450,250],[450,350],[250,350]])
poligono2 = Polygon([[20,20],[30,30],[10,30]])



poligono1.desenhaPoligono(janela, (255,255,255,255))
poligono1.scanline(janela,(255,120,0))

poligono2.desenhaPoligono(janela, (255,255,255,255))
poligono2.scanline(janela,(255,120,0))


janela.show()
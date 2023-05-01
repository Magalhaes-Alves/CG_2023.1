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

poligono = Polygon()

poligono.addPoint(10,10)

poligono.addPoint(20,70)

poligono.addPoint(30,80)

pontos = [[30,20],[70,80],[25,125]]

pontos2 =[[56,45],[21,43],[13,133]]

poligono.points= pontos

poligono.addPoints(pontos2)

poligono.desenhaPoligono(janela, (255,255,255,255))

janela.show()
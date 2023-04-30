from classes.Window import Window

janela = Window(500,500,"Teste")

janela.drawEllipse(250, 250, 100, 100, (255, 255, 255))

"""janela.bresenham(10, 10, 200, 200, (255, 255, 255))
janela.bresenham(10, 10, 200, 10, (255, 255, 255))
janela.bresenham(10, 10, 10, 200, (255, 255, 255))
janela.bresenham(10, 10, 200, 90, (255, 255, 255))
janela.bresenham(10, 10, 90, 200, (255, 255, 255))"""

janela.show()


from classes.Polygon import Polygon
from classes.Tranformations import rotacao


CIMA =0
BAIXO =1
ESQUERDA=2
DIREITA =3

class Nave (Polygon):

    def __init__(self,cx, cy,i):

        p1 = (cx,cy-15)
        p2 = (cx+10,cy+15)
        p3 = (cx,cy+5)
        p4 = (cx-10,cy+15)

        super().__init__([p1,p2,p3,p4])

        self._direcao = CIMA

    def atirar(self):
        pass
    
    
    def rotacionar(self,tecla,height,width):

        rot = 90 if tecla else -90

        rotacao(self,rot,height,width)

        

    def VerificarVida(self):
        pass

    def desenha(self,janela):

        super().scanline(janela,(255,0,0,255))
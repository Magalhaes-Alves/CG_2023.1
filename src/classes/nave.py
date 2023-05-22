from classes.Polygon import Polygon
from classes.Tranformations import rotacao
from classes.bullet import Bullet

CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

class Nave (Polygon):

    def __init__(self,cx, cy,i):
        self._cx = cx
        self._cy = cy

        p1 = (cx,cy-13)
        p2 = (cx+8,cy+13)
        p3 = (cx,cy+3)
        p4 = (cx-8,cy+13)

        super().__init__([p1,p2,p3,p4])

        self._direcao = CIMA

    def atirar(self):
        pass
    
    
    def rotacionar(self,tecla,height,width):

        rot = 90 if tecla else -90
         
        if tecla:
            self._direcao+=1    
        else:
            self._direcao-=1

        if self._direcao>3:
            self._direcao = 0
        elif self._direcao<0:
            self._direcao = 3
        
        rotacao(self,rot,height,width)

    def atirar(self, bullets_real, bullets_janela):
        bullet = Bullet(self._cx, self._cy, self._direcao)
        bullets_real.append(bullet)
        bullets_janela.append(bullet.points)
        
    def VerificarVida(self):
        pass

    def desenha(self,janela):

        super().scanline(janela,(255,0,0,255))
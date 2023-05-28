from classes.Polygon import Polygon
from classes.Tranformations import translacao
import numpy as np

CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

class Bullet (Polygon):

    def __init__(self,cx, cy,direcao):

        if direcao == BAIXO:
            p1 = (cx - 1,cy+23)
            p2 = (cx + 1,cy+23)
            p3 = (cx + 1,cy+27)
            p4 = (cx - 1,cy+27)
            velocidade = (0,1)
        if direcao == DIREITA:
            p1 = (cx + 12,cy+3)
            p2 = (cx + 16,cy+3)
            p3 = (cx + 16,cy+5)
            p4 = (cx + 12,cy+5)
            velocidade = (1,0)
        if direcao == ESQUERDA:
            p1 = (cx - 12,cy+3)
            p2 = (cx - 16,cy+3)
            p3 = (cx - 16,cy+5)
            p4 = (cx - 12,cy+5)
            velocidade = (-1,0)
        if direcao == CIMA:
            p1 = (cx - 1,cy-23)
            p2 = (cx + 1,cy-23)
            p3 = (cx + 1,cy-27)
            p4 = (cx - 1,cy-27)
            velocidade = (0,-1)

        self._velocidade = velocidade
        super().__init__([p1,p2,p3,p4])
        self._direcao = direcao
    
    @property
    def velocidade(self):
        return self._velocidade

    def movimentar(self):
        translacao(self, self.velocidade[0], self.velocidade[1])

    def dentro_janela(self, janela_teorica):
        condicao_1 = self.points[:, 0] >= janela_teorica[0]
        condicao_2 = self.points[:, 0] <= janela_teorica[2] 
        condicao_3 = self.points[:, 1] >= janela_teorica[1]
        condicao_4 = self.points[:, 1] <= janela_teorica[3]
        
        condicao_coluna1 = np.logical_and(condicao_1, condicao_2)
        condicao_coluna2 = np.logical_and(condicao_3, condicao_4)
        condicao_final = np.logical_and(condicao_coluna1, condicao_coluna2)

        # Usando np.where() para retornar valores com base na condição final
        if condicao_final[0] == False:
            return False

        return True
        

    def desenha(self,janela):
        super().scanline(janela,(255,0,0,255))
        
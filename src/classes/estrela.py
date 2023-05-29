from classes.Polygon import Polygon

class estrela (Polygon):

    def __init__(self,xc,yc,dmaior,dmenor,texture=None,texture_coordenates=None):
        
        p = [[xc,yc-dmaior],
        [xc+int(dmenor),yc-int(dmenor)],
        [xc+dmaior,yc],
        [xc+int(dmenor),yc+int(dmenor)],
        [xc,yc+dmaior],
        [xc-int(dmenor),yc+int(dmenor)],
        [xc-dmaior,yc],
        [xc-int(dmenor),yc-int(dmenor)]]
        
        super().__init__(p, texture, texture_coordenates)

        self._centro=[xc,yc]
        self._distancias = [dmaior,dmenor]
    
    @property
    def centro(self):
        return self._centro
    
    @centro.setter
    def centro(self,lista_centro):

        p = [[lista_centro[0],lista_centro[1]-self.distancias[0]],
        [lista_centro[0]+int(self.distancias[1]),lista_centro[1]-int(self.distancias[1])],
        [lista_centro[0]+self.distancias[0],lista_centro[1]],
        [lista_centro[0]+int(self.distancias[1]),lista_centro[1]+int(self.distancias[1])],
        [lista_centro[0],lista_centro[1]+self.distancias[0]],
        [lista_centro[0]-int(self.distancias[1]),lista_centro[1]+int(self.distancias[1])],
        [lista_centro[0]-self.distancias[0],lista_centro[1]],
        [lista_centro[0]-int(self.distancias[1]),lista_centro[1]-int(self.distancias[1])]]        
        self._centro=lista_centro
        self.points=p
    @property
    def distancias(self):
        return self._distancias
    

    @distancias.setter
    def distancias(self,lista_distancias):
        self._distancias= lista_distancias
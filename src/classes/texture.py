from PIL import Image
import os
import numpy as np

class Texture:

    def __init__(self,path_to_texture=None):
        if path_to_texture is None:
            self._texture =None
            self._width =None
            self._height = None
            return
        
        path_to_texture= os.path.join(os.path.dirname(__file__),"..",path_to_texture)

        path_to_texture = os.path.realpath(path_to_texture)

        self._texture= np.array(Image.open(path_to_texture)) 

        self._height = self._texture.shape[0]
        self._width= self._texture.shape[1]

    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width
    
    def addTexture(self,path_to_texture):
        path_to_texture= os.path.join(os.path.dirname(__file__),"..",path_to_texture)

        path_to_texture = os.path.realpath(path_to_texture)
        print(path_to_texture)

        self._texture= np.array(Image.open(path_to_texture)) 

        self._height = self._texture.shape[0]
        self._width= self._texture.shape[1]
    

    def getPixel(self, x,y):

        if self._texture is None:
            print("Não foi carregado uma textura")
            return
        
        x = 1 if x > 1 else x
        x = 0 if x<0 else x
        
        y = 1 if y > 1 else y
        y = 0 if y<0 else y
        
        x = round(x*(self._width-1))
        y = round(y*(self._height-1))

        return self._texture[y][x]
        
        

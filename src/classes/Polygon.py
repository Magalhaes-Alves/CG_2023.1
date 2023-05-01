import numpy as np

class Polygon:
    
    def __init__(self, matrix=None):
        if matrix is None:
            self._points = np.empty((0,2), int)
        else:
            self._points = np.array(matrix)

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, matrix):
        self._points = np.array(matrix)

    def addPoint(self, x, y):
        point = np.array([[x,y]])
        self._points =  np.concatenate([self._points, point], axis=0)

    def addPoints(self, matrix):
        self._points = np.concatenate([self._points, matrix], axis=0)

    def desenhaPoligono(self, janela, color):
        rows = self.points.shape[0]

        x = self.points[0][0]
        y = self.points[0][1]
        
        for i in range(1,rows):
            janela.ddaaaLine(x, y, self.points[i][0], self.points[i][1], color)
            x = self.points[i][0]
            y = self.points[i][1]
        
        janela.ddaaaLine(x, y, self.points[0][0], self.points[0][1], color)
            

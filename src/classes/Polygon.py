import numpy as np

class Polygon:
    
    def __init__(self, matrix=None):
        if matrix is None:
            self.points = np.empty((0,2), int)
        else:
            self.points = np.array(matrix)

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
class Polygon:
    
    def __init__(self,matrix=None):
        if matrix is None:
            self.points =[]
        else:
            self.points = matrix

    @property
    def points(self):
        return self._points
    
    @points.setter
    def points(self,matrix):
        
        self._points=matrix

    def addPoint(self, x,y):

        self._points= [*self.points,[x,y]]

    def addPoints(self,matrix):

        self._points = [*self.points, *matrix]
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
            
    def intersection(self,scan,edge):

        xi = edge[0][0]
        yi = edge[0][1]

        xf = edge[1][0]
        yf= edge[1][1]

        if yi ==yf:
            return -1
        
        #Seta orientação de cima para baixo
        if yi>yf:
            xi,xf = xf,xi
            yi,yf = yf,yi

        t = (scan-yi)/(yf-yi)

        if t>0 and t<=1:
            return int(xi+t*(xf-xi))
        
        return -1

    def scanline(self,window,r,g=None,b=None,alpha=None):
        if g is None and b is None and alpha is None:
            color = list(r)
        else:
            color = list(r, g, b,alpha)

        ymin = min(self.points[:,1])

        ymax = max(self.points[:,1])

        
        
        for y in range(ymin,ymax):
            i=[]
            pi = self.points[0]
            for index in range(1,self.points.shape[0]):
                pf = self.points[index]
                xi= self.intersection(y,[pi,pf])

                if xi>= 0:
                    i+=[xi]

                pi=pf
            
            pf = self.points[0]

            xi = self.intersection(y,[pi,pf])
            if xi >=0:
                i +=[xi]

            print(y,i,ymin,ymax)
            for pi in range(0,len(i),2):
                window.bresenham(i[pi]-1,y,i[pi+1],y,color)

            
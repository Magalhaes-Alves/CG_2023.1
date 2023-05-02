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
            return [-1,-1]
        
        #Seta orientação de cima para baixo
        if yi>yf:
            xi,xf = xf,xi
            yi,yf = yf,yi

        t = (scan-yi)/(yf-yi)

        if t>0 and t<=1:
            return [t,int(xi+t*(xf-xi))]
        
        return [-1,-1]

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
                _,xi= self.intersection(y,[pi,pf])

                if xi>= 0:
                    i+=[xi]

                pi=pf
            
            pf = self.points[0]

            _,xi = self.intersection(y,[pi,pf])
            if xi >=0:
                i +=[xi]

            print(y,i,ymin,ymax)
            for pi in range(0,len(i),2):
                window.bresenham(i[pi],y,i[pi+1],y,color)
        
        self.desenhaPoligono(window, (255,255,255,255))

    @classmethod
    def colorInterpolation(cls,icolor,fcolor,p):
        
        r = round(abs(fcolor[0]- icolor[0])*p)
        g =round(abs(fcolor[1]- icolor[1])*p)
        b =round(abs(fcolor[2]- icolor[2])*p)

        r=  r if icolor[0]<=fcolor[0] else -r
        g=  g if icolor[1]<=fcolor[1] else -g
        b=  b if icolor[2]<=fcolor[2] else -b
        

        r+=icolor[0]
        g+=icolor[1]
        b+=icolor[2]

        return (r,g,b)
    

    def scanlineInterpolacao(self,window,colors):
        
        if colors is not None and len(colors)!= self.points.shape[0]:
            print("O numéro de cores não é o mesmo que de pontos.")
            return


        ymin = min(self.points[:,1])
        ymax = max(self.points[:,1])

        for y in range(ymin,ymax):
            i=[]
            pi = self.points[0] #Primeiro ponto do poligono
            for index in range(1,self.points.shape[0]): #Para cada aresta
                pf = self.points[index]
                t,xi= self.intersection(y,[pi,pf])

                if xi >=0 and pi[1]<=pf[1]:
                    color = self.colorInterpolation(colors[index-1],colors[index],t) # Inverti os indices
                    i+=[[xi,color]]
                elif xi >=0 and pi[1]>pf[1]:
                    color = self.colorInterpolation(colors[index],colors[index-1],t) # Inverti os indices
                    i+=[[xi,color]]

                pi=pf
            pf = self.points[0]
            t,xi = self.intersection(y,[pi,pf])

            if xi >=0 and pi[1]<=pf[1]:
                color = self.colorInterpolation(colors[-1],colors[0],t) # Inverti os indices
                i+=[[xi,color]]
            elif xi >=0 and pi[1]>pf[1]:
                color = self.colorInterpolation(colors[0],colors[-1],t) # Inverti os indices
                i+=[[xi,color]]
            
            for pi in range(0,len(i),2):
                xi,icolor=i[pi]
                xf,fcolor=i[pi+1]

                inc =1 if xi<xf else -1
                cont=0
                while (xi+ cont) != xf:
                    t = abs(cont)/(abs(xf-xi))
                    
                    color = self.colorInterpolation(icolor,fcolor,t)

                    window.setPixel(xi+cont,y,color)
                    cont+=inc
        
        self.desenhaPoligono(window, (255,255,255,255))
            

if __name__=="__main__":

    print(Polygon.colorInterpolation((120,75,200),(150,93,78),0.9))
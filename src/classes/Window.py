import pygame

class Window:

    def __init__(self,width,height,title):
        pygame.init()
        pygame.display.set_caption("Set Pixel")
        self._screen = pygame.display.set_mode((width,height))
        self._width = width
        self._height = height

    # Setters e Getters

    @property
    def screen(self):
        return self._screen
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    # color é uma tupla com rgba
    def setPixel(self,x,y,color):

        x= 0 if x<0 else x
        y = 0 if y<0 else y
        x= self.width-1 if x>=self.width else x
        y = self.height-1 if y>=self.height else y

        pygame.gfxdraw.pixel(self.screen,x,y,color)

    def ddaLine(self,xi,yi,xf,yf,color):

        dx = xf-xi
        dy= yf-yi
        
        steps = abs(dx)

        if steps==0:
            self.setPixel(xi,xf,color)
            return
        
        if abs(dy)> abs(dx):
            steps = abs(dy)

        steps_x =dx/steps
        steps_y = dy/steps

        for i in range(steps):
            x= round(xi+i*steps_x)
            y = round(yi+i*steps_y)
            self.setPixel(x,y,color)

    def drawLine(self,xi,yi,xf,yf,color,alg=True):

        if not alg:
            pass
        else:
            self.ddaLine(xi,yi,xf,yf,color)


    def drawCircle(self,xc,yc,r,color):
        
        x=0
        y=r

        p = 5/4 -r

        while(x<y):

            self.setPixel(x+xc,y+yc,color)
            self.setPixel(y+xc,x+yc,color)
            self.setPixel(y+xc,-x+yc,color)
            self.setPixel(x+xc,-y+yc,color)
            self.setPixel(-x+xc,-y+yc,color)
            self.setPixel(-y+xc,-x+yc,color)
            self.setPixel(-y+xc,x+yc,color)
            self.setPixel(-x+xc,y+yc,color)

            x+=1
            if p<0:
                p=p+2*x+1
            else:
                y-=1
                p =p+2*x+1-2*y


    def show(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            pygame.display.update()



    


    
import pygame
from pygame import gfxdraw
from math import floor

class Window:

    def __init__(self,width,height,title=None):
        
        if title is None:
            title = "Trabalho 1 CG"
        
        pygame.init()
        pygame.display.set_caption(title)
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


    def setPixel(self,x,y, r, g=None, b=None):
        if g is None and b is None:
            color = r
        else:
            color = (r, g, b)

        x= 0 if x<0 else x
        y = 0 if y<0 else y
        x= self.width-1 if x>=self.width else x
        y = self.height-1 if y>=self.height else y
        pygame.gfxdraw.pixel(self.screen,x,y,color)

    def getPixel(self, x, y):
        pixel_color = self._screen.get_at((x, y))
        rgb_tuple = pixel_color[:3]  # extrai os primeiros 3 valores (R, G, B) da cor
        rgb_integers = tuple(rgb_tuple)  # converte para uma tupla de inteiros

        return rgb_integers
    
    def floodFill(self, x, y, corn, cori):
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            # Checando se x e y estão dentro dos limites
            if (x >= 0 and x < self._width) and (y > 0 and y < self._height):
                # Checando se a cor de (x, y) é igual a cori 
                if self.getPixel(x, y) == cori:
                    self.setPixel(x, y, corn)
                    stack.append((x+1, y))
                    stack.append((x-1, y))
                    stack.append((x, y+1))
                    stack.append((x, y-1))

    def boundaryFill(self, x, y, corn, corb):
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            # Checando se x e y estão dentro dos limites
            if (x >= 0 and x < self._width) and (y > 0 and y < self._height):
                # Checando se a cor de (x, y) é igual a cori 
                if self.getPixel(x, y) != corn and self.getPixel(x, y) != corb:
                    self.setPixel(x, y, corn)
                    stack.append((x+1, y))
                    stack.append((x-1, y))
                    stack.append((x, y+1))
                    stack.append((x, y-1))
    
    def ddaLine(self,xi,yi,xf,yf,r,g=None,b=None):
        if g is None and b is None:
            color = r
        else:
            color = (r, g, b)


        dx = xf -xi;
        dy = yf-yi;

        steps = abs(dx);

        if (abs(dy)> abs(dx)):
            steps=abs(dy)
            
        if (steps ==0):
            self.setPixel(xi,yi,color);
            return

        steps_x = dx/steps;
        steps_y = dy/steps;

        for s in range(steps):
            x = round(xi +s*steps_x)
            y = round(yi +s*steps_y)
            
            self.setPixel(x,y,color)

    def ddaaaLine(self,xi,yi,xf,yf,r,g=None,b=None,alpha=None):
        if g is None and b is None and alpha is None:
            color = list(r)
        else:
            color = list(r, g, b,alpha)

        new_alpha =color[3]
        dx = xf -xi
        dy = yf-yi

        steps = abs(dx);

        if (abs(dy)> abs(dx)):
            steps=abs(dy)
            
        if (steps ==0):
            self.setPixel(xi,yi,color);
            return

        steps_x = dx/steps;
        steps_y = dy/steps;

        for s in range(steps):
            x = xi +s*steps_x
            y = yi +s*steps_y
        
            if steps_x ==1:
                yd = y -floor(y)
                color[3] =round((1-yd)*new_alpha)
                self.setPixel(round(x),floor(y),tuple(color))
                color[3] =round(yd*new_alpha)
                self.setPixel(round(x),floor(y+1),tuple(color))
            else:
                xd = x -floor(x)
                color[3] =round((1-xd)*new_alpha)
                self.setPixel(floor(x),floor(y),tuple(color))
                color[3] =round(xd*new_alpha)
                self.setPixel(floor(x+1),floor(y),tuple(color))


    def bresenham(self, xi, yi, xf, yf, r, g=None, b=None):
        if g is None and b is None:
            color = r
        else:
            color = (r, g, b)
        
        swap = False
        
        dx = xf - xi
        dy = yf - yi
        x_inc = -1 if dx < 0 else 1
        y_inc = -1 if dy < 0 else 1

        dx = abs(dx)
        dy = abs(dy)

        if dy > dx:
            aux = dx
            dx = dy
            dy = aux
            swap = True
            
        dx2 = 2 * dx
        dy2 = 2 * dy
            
        p = -dx + dy2

        x = xi
        y = yi

        for s in range(abs(dx)):
            self.setPixel(x, y, color)
            
            if swap and p >= 0:
                x += x_inc
                y += y_inc
                p -= dx2 - dy2
            elif swap and p < 0:
                y += y_inc
                p += dy2
            elif not swap and p >= 0:
                x += x_inc
                y += y_inc
                p -= dx2 - dy2
            elif not swap and p < 0:
                x += x_inc
                p += dy2

    def drawCircle(self,xc,yc,ray, r, g=None, b=None):

        if g is None and b is None:
            color = r
        else:
            color = (r, g, b)

        x=0
        y=ray

        p=5/4-ray

        while(x<=y):
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
                p = p+2*x+1
            else:
                y-=1
                p=p+2*x+1-2*y

    def drawEllipse(self, xc, yc, rx, ry, r, g=None, b=None):
        if g is None and b is None:
            color = r
        else:
            color = (r, g, b)
        
        x = 0
        y = ry
        rx2 = rx*rx
        ry2 = ry*ry
        twoRx2 = 2*rx2
        twoRy2 = 2*ry2
        px = 0
        py = twoRx2*y

        p = round(ry2 - (rx2*ry) + (0.25*rx2))

        while px<py:
            self.setPixel(x+xc, y+yc, color)
            self.setPixel(-x+xc, y+yc, color)
            self.setPixel(x+xc, -y+yc, color)
            self.setPixel(-x+xc, -y+yc, color)

            x += 1
            px = px + twoRy2
            if p<0:
                p = p + ry2 + px
            else:
                y -= 1
                py = py - twoRx2
                p = p + ry2 + px - py
        
        p = round(ry2*(x+0.5)*(x+0.5)+rx2*(y-1)*(y-1)-rx2*ry2)

        while y>=0:
            self.setPixel(x+xc, y+yc, color)
            self.setPixel(-x+xc, y+yc, color)
            self.setPixel(x+xc, -y+yc, color)
            self.setPixel(-x+xc, -y+yc, color)

            y -= 1
            py = py - twoRx2
            if p>0:
                p=p+rx2-py
            else:
                x += 1
                px = px + twoRy2
                p = p + rx2 - py + px

    def show(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            pygame.display.update()
        

    


    
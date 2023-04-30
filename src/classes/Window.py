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



    def setPixel(self,x,y,r,g,b):

        x= 0 if x<0 else x
        y = 0 if y<0 else y
        x= self.width-1 if x>self.width else x
        y = self.height if y>self.height else y

        pygame.gfxdraw.pixel(self.screen,x,y,(r,g,b))
    
    def setPixel(self,x,y,color):

        x= 0 if x<0 else x
        y = 0 if y<0 else y
        x= self.width-1 if x>=self.width else x
        y = self.height-1 if y>=self.height else y
        print(x,y)

        pygame.gfxdraw.pixel(self.screen,x,y,color)

    def show(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            pygame.display.update()



    


    
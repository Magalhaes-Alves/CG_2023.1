import pygame

class Window:

    def __init__(self,width,height,title):
        pygame.init();
        pygame.display.set_caption("Set Pixel")
        self._screen = pygame.display.set_mode((width,height))

    def __init__(self):
        pygame.init();
        pygame.display.set_caption("Set Pixel")
        self._screen = pygame.display.set_mode((1000,1000))

    # Setters e Getters

    @property
    def screen(self):
        return self._screen;

    


    def setPixel(self,x,y,r,g,b):
        pygame.gfxdraw()

    
    setPixel(screen,50,50,WHITE)



    
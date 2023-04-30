import pygame
from pygame import gfxdraw;

def setPixel(img, x,y,color):
    pygame.gfxdraw.pixel(img,x,y,color)

def main():
    pygame.init();
    pygame.display.set_caption("Set Pixel")
    screen = pygame.display.set_mode((100,100))
    WHITE =(255,255,255)
    setPixel(screen,50,50,WHITE)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

if __name__=="__main__":
    main()


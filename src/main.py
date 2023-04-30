import pygame
from pygame import gfxdraw;

def setPixel(img, x,y,color):
    pygame.gfxdraw.pixel(img,x,y,color)
from classes.Window import Window

janela = Window(500,500,"Teste")

janela.setPixel(250,250,(255,255,255))
janela.setPixel(-1,-1,(255,255,255))
janela.setPixel(500,500,(255,255,255))

janela.drawCircle(0,0,100,(255,255,255))
janela.drawCircle(0,500,100,(255,255,255))
janela.drawCircle(500,0,100,(255,255,255))
janela.drawCircle(250,250,100,(255,255,255))
janela.drawCircle(500,500,100,(255,255,255))



janela.show()


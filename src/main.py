import pygame
from pygame import gfxdraw;

def setPixel(img, x,y,color):
    pygame.gfxdraw.pixel(img,x,y,color)
from classes.Window import Window

janela = Window(500,500,"Teste")

WHITE = (255,255,255)

janela.setPixel(250,250,WHITE)
janela.setPixel(-1,-1,WHITE)
janela.setPixel(500,500,WHITE)

janela.drawCircle(0,0,100,WHITE)
janela.drawCircle(0,500,100,WHITE)
janela.drawCircle(500,0,100,WHITE)
janela.drawCircle(250,250,100,WHITE)
janela.drawCircle(500,500,100,WHITE)

janela.drawLine(0,0,250,250,WHITE)
janela.drawLine(0,500,250,250,WHITE)
janela.drawLine(500,0,250,250,WHITE)
janela.drawLine(500,500,250,250,WHITE)

janela.show()


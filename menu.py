import pygame, sys
from pygame.locals import *

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Lab 3 UI')
screen = pygame.display.set_mode((1000,500),0,32)

font = pygame.font.SysFont("Arial", 30)

def main_menu():
    while True:

        screen.fill(pygame.Color("dimgray")) #color de fondo
        textobj = font.render('LAB3RINTO', 1, (255, 255, 255))  #titulo del juego
        textrect = textobj.get_rect() 
        textrect.topleft = (20, 20) #posicion x,y del juego
        screen.blit(textobj, textrect) 

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50) 
        button_2 = pygame.Rect(350, 100, 200, 50)
        if button_1.collidepoint((mx, my)):
          if click:
            gotogame()
        if button_2.collidepoint((mx, my)):
          if click:
            exit()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        textobj = font.render('Iniciar', 1, (255, 255, 255))  #titulo del juego
        textrect = textobj.get_rect() 
        textrect.topleft = (115, 105) #posicion x,y del juego
        screen.blit(textobj, textrect)

        textobj = font.render('Salir', 1, (255, 255, 255))  #titulo del juego
        textrect = textobj.get_rect() 
        textrect.topleft = (425, 105) #posicion x,y del juego
        screen.blit(textobj, textrect) 

        click = False
        for event in pygame.event.get():
          if event.type == QUIT:
            pygame.quit()
            sys.exit()
          if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
              pygame.quit()
              sys.exit()
          if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
              click = True

        pygame.display.update()
        mainClock.tick(60)

def gotogame():
    running = True
    while running:
        screen.fill(pygame.Color("dimgray"))
        
        textobj = font.render('Aqui se abre el juego, pero todavia no xD, presione ESC para regresar al menu', 1, (255, 255, 255))  #titulo del juego
        textrect = textobj.get_rect() 
        textrect.topleft = (20, 20) #posicion x,y del juego
        screen.blit(textobj, textrect) 

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def exit():
  pygame.quit()


main_menu()        
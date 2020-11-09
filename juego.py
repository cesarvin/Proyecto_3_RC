import pygame, sys
from pygame.locals import *
from gl import *

from math import cos, sin, pi

mainClock = pygame.time.Clock()

clock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Proyecto 3')
screen = pygame.display.set_mode((1000,500),0,32)

font = pygame.font.SysFont("Arial", 30)

r = Raycaster(screen)

#r.setColor( (128,0,0) )
r.load_map('mapa.txt')

def updateFPS():
    fps = str(int(clock.get_fps()))
    fps = font.render(fps, 1, pygame.Color("white"))
    return fps

def main_menu():
    while True:

        screen.fill(pygame.Color("dimgray")) #color de fondo
        textobj = font.render('WOLFDOOM', 1, (255, 255, 255))  #titulo del juego
        textrect = textobj.get_rect() 
        textrect.topleft = (425, 50) #posicion x,y del juego
        screen.blit(textobj, textrect) 

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(250, 150, 200, 50) 
        button_2 = pygame.Rect(550, 150, 200, 50)
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
        textrect.topleft = (285, 155) #posicion x,y del juego
        screen.blit(textobj, textrect)

        textobj = font.render('Salir', 1, (255, 255, 255))  #titulo del juego
        textrect = textobj.get_rect() 
        textrect.topleft = (635, 155) #posicion x,y del juego
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
        screen.fill(pygame.Color("dimgray"))
        game()

        # pygame.display.update()
        # mainClock.tick(60)

def exit():
  pygame.quit()


def game():
  c = 0
  isRunning = True

  while isRunning:

    screen.fill((113, 113, 113))
    r.render()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
        
        newX = r.player['x']
        newY = r.player['y']
        
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False
            elif ev.key == pygame.K_w:
                    newX = r.player['x'] + cos(r.player['angle'] * pi / 180) * r.stepSize
                    newY = r.player['y'] + sin(r.player['angle'] * pi / 180) * r.stepSize

                    i = int(newX/r.blocksize)
                    j = int(newY/r.blocksize)

                    if r.map[j][i] ==' ':
                        r.player['x'] = newX
                        r.player['y'] = newY
                    
            elif ev.key == pygame.K_s:
                    newX = r.player['x'] - cos(r.player['angle'] * pi / 180) * r.stepSize
                    newY = r.player['y'] - sin(r.player['angle'] * pi / 180) * r.stepSize

                    i = int(newX/r.blocksize)
                    j = int(newY/r.blocksize)

                    if r.map[j][i] ==' ':
                        r.player['x'] = newX
                        r.player['y'] = newY

            elif ev.key == pygame.K_a:
                    newX = r.player['x'] - cos((r.player['angle'] + 90) * pi / 180) * r.stepSize
                    newY = r.player['y'] - sin((r.player['angle'] + 90) * pi / 180) * r.stepSize

                    i = int(newX/r.blocksize)
                    j = int(newY/r.blocksize)

                    if r.map[j][i] ==' ':
                        r.player['x'] = newX
                        r.player['y'] = newY

            elif ev.key == pygame.K_d:
                    newX = r.player['x'] + cos((r.player['angle'] + 90) * pi / 180) * r.stepSize
                    newY = r.player['y'] + sin((r.player['angle'] + 90) * pi / 180) * r.stepSize

                    i = int(newX/r.blocksize)
                    j = int(newY/r.blocksize)

                    if r.map[j][i] ==' ':
                        r.player['x'] = newX
                        r.player['y'] = newY

            elif ev.key == pygame.K_q:
                    r.player['angle'] -= 5
            elif ev.key == pygame.K_e:
                    r.player['angle'] += 5

            elif ev.key == QUIT:
                pygame.quit()
                sys.exit()
            elif ev.key == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            i = int(newX / r.blocksize)
            j = int(newY / r.blocksize)

            if r.map[j][i] == ' ':
                r.player['x'] = newX
                r.player['y'] = newY

    screen.fill(pygame.Color("black"), (0,0,30,30))
    screen.blit(updateFPS(), (0,0))
    clock.tick(30) 

    pygame.display.flip()

main_menu()        
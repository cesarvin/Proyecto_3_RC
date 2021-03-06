import pygame
from gl import *

from math import cos, sin, pi

pygame.init()
screen = pygame.display.set_mode((1000,500), pygame.DOUBLEBUF | pygame.HWACCEL) 
screen.set_alpha(None)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

def updateFPS():
    fps = str(int(clock.get_fps()))
    fps = font.render(fps, 1, pygame.Color("white"))
    return fps

r = Raycaster(screen)

#r.setColor( (128,0,0) )
r.load_map('mapa.txt')

isRunning = True

while isRunning:

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


            i = int(newX / r.blocksize)
            j = int(newY / r.blocksize)

            if r.map[j][i] == ' ':
                r.player['x'] = newX
                r.player['y'] = newY

    screen.fill(pygame.Color("gray")) #Fondo

    #Techo
    screen.fill(pygame.Color("dimgray"), (int(r.width / 2), 0, int(r.width / 2),int(r.height / 2)))
    
    #Piso
    screen.fill(pygame.Color("dimgray"), (int(r.width / 2), int(r.height / 2), int(r.width / 2),int(r.height / 2)))

    r.render()
    
    # FPS
    screen.fill(pygame.Color("black"), (0,0,30,30))
    screen.blit(updateFPS(), (0,0))
    clock.tick(30)  
    
    pygame.display.update()

pygame.quit()

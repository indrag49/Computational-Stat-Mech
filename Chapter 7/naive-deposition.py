import random
import math 
import pygame, random, sys
from pygame.locals import *

pygame.font.init()

white=(255, 255, 255)
red=(255, 0, 0)
black=(0, 0, 0)

xmin, xmax, ymin, ymax=0, 1, 0, 1
radius=0.04

pos=[[random.uniform(radius, 1.-radius), random.uniform(radius, 1.-radius)]]
N=len(pos)
t=1
                
DISPLAYSURF=pygame.display.set_mode((500, 500))
pygame.display.set_caption('naive-deposition')

DISPLAYSURF.fill(white)
clock=pygame.time.Clock()
myfont=pygame.font.SysFont('Comic Sans MS', 30)

while True:
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.image.save(DISPLAYSURF, 'naive-deposition.png')
                pygame.quit()
                sys.exit()

    DISPLAYSURF.fill(white)
    textsurface=myfont.render('Steps = '+str(t), False, black)
    DISPLAYSURF.blit(textsurface, (120, 10))

    flag=0
    while True:
        p=[random.uniform(radius, 1.-radius), random.uniform(radius, 1.-radius)]
        for l in range(N):
            if min([math.sqrt((p[0]-P[0])**2+(p[1]-P[1])**2) for P in pos])>=2*radius:
                pos+=[p, ]
                for i in pos: pygame.draw.circle(DISPLAYSURF, (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)), (int(i[0]*500), int(i[1]*500)), int(radius*500), 0)
                print(p, t)
                flag=1
                break

        t+=1
        if flag==1:break
    N+=1

    clock.tick(10)
    pygame.display.update()
    

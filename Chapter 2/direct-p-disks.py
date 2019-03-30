import random
import math 
import pygame, random, sys
from pygame.locals import *

pygame.font.init()

white=(255, 255, 255)
green=(51, 255, 51)
red=(255, 0, 0)
yellow=(255, 255, 51)
blue=(0, 0, 255)
black=(0, 0, 0)
pink=(255, 0, 255)

xmin=0
xmax=1
ymin=0
ymax=1
radius=0.1
t=0
N=4 # No of hard disks inside the container
T=323
Pr=20.5
Kb=1.3807*10**(-23)
Beta=1
Upsilon=random.uniform(radius, 1.-radius)

DISPLAYSURF=pygame.display.set_mode((500, 500))
pygame.display.set_caption('direct-p-disks')

DISPLAYSURF.fill(white)
clock=pygame.time.Clock()
myfont=pygame.font.SysFont('Comic Sans MS', 30)

def prepare(Upsilon):
        #Upsilon=random.uniform(radius, 1.-radius)
        for k in range(1,N): Upsilon*=random.uniform(radius, 1.-radius)
        L=math.sqrt(-math.log(Upsilon)/(Beta*Pr))
        pos=[[L*random.uniform(radius, 1.-radius), L*random.uniform(radius, 1.-radius)]]
        for l in range(1, N):
                p=[L*random.uniform(radius, 1.-radius), L*random.uniform(radius, 1.-radius)]
                if min([math.sqrt((p[0]-P[0])**2+(p[1]-P[1])**2) for P in pos])>=2*radius: pos+=[p, ]
        if len(pos)==N: return pos
        else: return prepare(random.uniform(radius, 1.-radius))
        
prev=prepare(Upsilon) #Prepare the initial state, by using the same algorithm

while True:
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.image.save(DISPLAYSURF, 'direct-p-disks.png')
                        pygame.quit()
                        sys.exit()

        DISPLAYSURF.fill(white)
        textsurface=myfont.render('Steps = '+str(t), False, black)
        DISPLAYSURF.blit(textsurface, (120, 10))

        for k in range(1,N): Upsilon*=random.uniform(radius, 1.-radius)
        L=math.sqrt(-math.log(Upsilon)/(Beta*Pr))
        pos=[[L*random.uniform(radius, 1.-radius), L*random.uniform(radius, 1.-radius)]]
        
        for l in range(1, N):
                p=[L*random.uniform(radius, 1.-radius), L*random.uniform(radius, 1.-radius)]
                if min([math.sqrt((p[0]-P[0])**2+(p[1]-P[1])**2) for P in pos])>=2*radius: pos+=[p, ]
            
        print (pos)
        if len(pos)==N:
                pygame.draw.circle(DISPLAYSURF, red, (int(pos[0][0]*500), int(pos[0][1]*500)), int(radius*500), 0)
                pygame.draw.circle(DISPLAYSURF, blue, (int(pos[1][0]*500), int(pos[1][1]*500)), int(radius*500), 0)
                pygame.draw.circle(DISPLAYSURF, yellow, (int(pos[2][0]*500), int(pos[2][1]*500)), int(radius*500), 0)
                pygame.draw.circle(DISPLAYSURF, green, (int(pos[3][0]*500), int(pos[3][1]*500)), int(radius*500), 0)
                prev=pos[:]
                t+=1
        else:
                pygame.draw.circle(DISPLAYSURF, red, (int(prev[0][0]*500), int(prev[0][1]*500)), int(radius*500), 0)
                pygame.draw.circle(DISPLAYSURF, blue, (int(prev[1][0]*500), int(prev[1][1]*500)), int(radius*500), 0)
                pygame.draw.circle(DISPLAYSURF, yellow, (int(prev[2][0]*500), int(prev[2][1]*500)), int(radius*500), 0)
                pygame.draw.circle(DISPLAYSURF, green, (int(prev[3][0]*500), int(prev[3][1]*500)), int(radius*500), 0)
        
        clock.tick(40)
        
        pygame.display.update()



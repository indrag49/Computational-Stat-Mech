import random
import math 
import pygame, random, sys
from pygame.locals import *

pygame.font.init()

def check_covers(i, j, r1, r2):
    x1, x2=i[0], i[1]
    y1, y2=j[0], j[1]
    d=math.sqrt((x2-x1)**2+(y2-y1)**2)
    if r1>d+r2: return True
    else: return False

def check_overlaps(i, j, r1, r2):
    x1, x2=i[0], i[1]
    y1, y2=j[0], j[1]
    d_sq=(x2-x1)**2+(y2-y1)**2
    R=(r1+r2)**2
    if d_sq<=R: return True
    else: return False

def T(X, L):
    x1, x2=X[0], X[1]
    return [L-x1, L-x2]

white=(255, 255, 255)
green=(51, 255, 51)
red=(255, 0, 0)
yellow=(255, 255, 51)
blue=(0, 0, 255)
black=(0, 0, 0)
pink=(255, 0, 255)

N=5 # No. of particles
Rad=[random.uniform(0.04, 0.12) for i in range(N)]
L=1.
t=0

DISPLAYSURF=pygame.display.set_mode((500, 500))
pygame.display.set_caption('pocket-binary')

DISPLAYSURF.fill(white)
clock=pygame.time.Clock()
myfont=pygame.font.SysFont('Comic Sans MS', 30)

def prepare():
    pos=[[random.uniform(Rad[0], L-Rad[0]), random.uniform(Rad[0], L-Rad[0])]]
    for l in range(1, N):
        p=[random.uniform(Rad[l], L-Rad[l]), random.uniform(Rad[l], L-Rad[l])]
        if min([math.sqrt((p[0]-P[0])**2+(p[1]-P[1])**2) for P in pos])>=2*Rad[l]: pos+=[p, ]
    if len(pos)==N: return pos
    else: return prepare()

Pos=prepare()
#print("Pos=",Pos)

while True:
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.image.save(DISPLAYSURF, 'direct-disks.png')
                pygame.quit()
                sys.exit()

    DISPLAYSURF.fill(white)
    textsurface=myfont.render('Steps = '+str(t), False, black)
    DISPLAYSURF.blit(textsurface, (120, 10))

    print(Pos)
    pos=Pos[:]
    k=random.choice(range(N))
    P=[pos[k]]
    pos.remove(pos[k])
    A=pos

    while P!=[]:
        i=random.choice(P)
        ind=Pos.index(i)
        [x, y]=T(i, L)
        Pos[ind]=[x, y]
        for j in A:
            if check_covers(i, j, Rad[ind], Rad[Pos.index(j)])==True:
                A.remove(j)
                ind1=Pos.index(j)
                [x, y]=T(j, L)
                Pos[ind1]=[x, y]
            elif check_overlaps(i, j, Rad[ind], Rad[Pos.index(j)])==True:
                A.remove(j)
                P+=[j, ]
        P.remove(i)

    pygame.draw.circle(DISPLAYSURF, red, (int(Pos[0][0]*500), int(Pos[0][1]*500)), int(Rad[0]*500), 0)
    pygame.draw.circle(DISPLAYSURF, blue, (int(Pos[1][0]*500), int(Pos[1][1]*500)), int(Rad[1]*500), 0)
    pygame.draw.circle(DISPLAYSURF, yellow, (int(Pos[2][0]*500), int(Pos[2][1]*500)), int(Rad[2]*500), 0)
    pygame.draw.circle(DISPLAYSURF, green, (int(Pos[3][0]*500), int(Pos[3][1]*500)), int(Rad[3]*500), 0)
    pygame.draw.circle(DISPLAYSURF, pink, (int(Pos[4][0]*500), int(Pos[4][1]*500)), int(Rad[4]*500), 0)
    t+=1

    clock.tick(10)
    pygame.display.update()

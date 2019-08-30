import random
import math 
import pygame, random, sys, pylab
from pygame.locals import *

pygame.font.init()

white=(255, 255, 255)
black=(0, 0, 0)
R=[0.04, 0.06, 0.08]

for radius in R:
    xmin, xmax, ymin, ymax=0, 1, 0, 1
    pos=[[random.uniform(radius, 1.-radius), random.uniform(radius, 1.-radius)]]
    col=[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))]
    N=len(pos)
    t=1
    Particles=[N]
    Time=[t]
                    
    DISPLAYSURF=pygame.display.set_mode((500, 500))
    pygame.display.set_caption('naive-deposition')

    DISPLAYSURF.fill(white)
    clock=pygame.time.Clock()
    myfont=pygame.font.SysFont('Comic Sans MS', 30)

    while N<=23:
        for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.image.save(DISPLAYSURF, 'naive-deposition.png')
                    pygame.quit()
                    sys.exit()

        DISPLAYSURF.fill(white)
        textsurface=myfont.render('No. of particles = '+str(N), False, black)
        DISPLAYSURF.blit(textsurface, (120, 10))

        flag=0
        while True:
            p=[random.uniform(radius, 1.-radius), random.uniform(radius, 1.-radius)]
            for l in range(N):
                if min([math.sqrt((p[0]-P[0])**2+(p[1]-P[1])**2) for P in pos])>=2*radius:
                    pos+=[p, ]
                    col+=[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), ]
                    for i in range(len(pos)): pygame.draw.circle(DISPLAYSURF, col[i], (int(pos[i][0]*500), int(pos[i][1]*500)), int(radius*500), 0)
                    print(p, t)
                    Particles+=[N, ]
                    Time+=[t, ]
                    flag=1
                    break

            t+=1
            if flag==1:break
        N+=1

        clock.tick(10)
        pygame.display.update()

    pylab.plot(Particles, Time, label=radius)
    pylab.ylim(0, 500)

pylab.legend(loc='upper left')
pylab.xlabel('No. of Particles')
pylab.ylabel('Stopping time for each deposition')
pylab.title('Plots for stopping times for discs with varying radius')
pylab.show()

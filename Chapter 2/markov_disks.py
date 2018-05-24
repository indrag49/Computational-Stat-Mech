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

radius=0.15
t=0

DISPLAYSURF=pygame.display.set_mode((400, 400))
pygame.display.set_caption('Markov-disks-box')

DISPLAYSURF.fill(white)
clock=pygame.time.Clock()
myfont=pygame.font.SysFont('Comic Sans MS', 30)

R=random.uniform
pos=[[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
delta=0.1

while True:
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.image.save(DISPLAYSURF, 'Random Permutation.png')
                        pygame.quit()
                        sys.exit()

        DISPLAYSURF.fill(white)
        textsurface=myfont.render('Step = '+str(t), False, black)
        DISPLAYSURF.blit(textsurface, (120, 10))

        a=random.choice(pos)
        b=[a[0]+R(-delta, delta), a[1]+R(-delta, delta)]
        min_=min((b[0]-c[0])**2+(b[1]-c[1])**2 for c in pos if c!=a)
        cond=min(b[0], b[1])<radius or max(b[0], b[1])>1.-radius
        if not(cond or min_<4*radius**2): a[:]=b
        
        pygame.draw.circle(DISPLAYSURF, red, (int(pos[0][0]*400), int(pos[0][1]*400)), int(radius*400), 0)
        pygame.draw.circle(DISPLAYSURF, blue, (int(pos[1][0]*400), int(pos[1][1]*400)), int(radius*400), 0)
        pygame.draw.circle(DISPLAYSURF, yellow, (int(pos[2][0]*400), int(pos[2][1]*400)), int(radius*400), 0)
        pygame.draw.circle(DISPLAYSURF, green, (int(pos[3][0]*400), int(pos[3][1]*400)), int(radius*400), 0)
        t+=1
        
        clock.tick(1000)
        
        pygame.display.update()
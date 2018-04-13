import pygame, random, sys
import random
from pygame.locals import *

def nran(k, l):
        while True:
                m=int(random.uniform(k, l+1))
                if m<=l: return m

                
DISPLAYSURF=pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Double Pendulum problem")

WHITE=(255, 255, 255)
RED=(255, 0, 0)
BLACK=(0, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
SKY=(0, 255, 255)
SILVER=(192, 192, 192)
MAROON=(128, 0, 0)
PURPLE=(128, 0, 128)
NAVY=(0, 0, 128)
TEAL=(0, 128, 128)

clock=pygame.time.Clock()

K=9
M=3
k=1

P=range(1, K+1)
C=[BLACK, RED, GREEN, BLUE, SKY, MAROON, PURPLE, NAVY, TEAL]

DISPLAYSURF.fill(WHITE)
pygame.draw.circle(DISPLAYSURF, BLACK, (30, 200 - 10), 8, 0)
pygame.draw.circle(DISPLAYSURF, RED, (150, 200 - 10), 8, 0)
pygame.draw.circle(DISPLAYSURF, GREEN, (270, 200 - 10), 8, 0)
pygame.draw.circle(DISPLAYSURF, BLUE, (390, 200 - 10), 8, 0)
pygame.draw.circle(DISPLAYSURF, SKY, (510, 200 - 10), 8, 0)
pygame.draw.circle(DISPLAYSURF, MAROON, (630, 200 - 10), 8, 0)
pygame.draw.circle(DISPLAYSURF, PURPLE, (750, 200 - 10), 8, 0)
pygame.draw.circle(DISPLAYSURF, NAVY, (870, 200 - 10), 8, 0)
pygame.draw.circle(DISPLAYSURF, TEAL, (990, 200 - 10), 8, 0)

while True:
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.image.save(DISPLAYSURF, 'Random Permutation.png')
                        pygame.quit()
                        sys.exit()
        
##        if k==9:
##                pygame.image.save(DISPLAYSURF, 'Random Permutation.png')
##                pygame.quit()
##                sys.exit()
                
        if k==9: k=1
        
        DISPLAYSURF.fill(WHITE)
        clock.tick(1)
        l=nran(k, K)
        temp=C[l-1]
        C[l-1]=C[k-1]
        C[k-1]=temp

        pygame.draw.circle(DISPLAYSURF, C[0], (30, 200 - 10), 8, 0)
        pygame.draw.circle(DISPLAYSURF, C[1], (150, 200 - 10), 8, 0)
        pygame.draw.circle(DISPLAYSURF, C[2], (270, 200 - 10), 8, 0)
        pygame.draw.circle(DISPLAYSURF, C[3], (390, 200 - 10), 8, 0)
        pygame.draw.circle(DISPLAYSURF, C[4], (510, 200 - 10), 8, 0)
        pygame.draw.circle(DISPLAYSURF, C[5], (630, 200 - 10), 8, 0)
        pygame.draw.circle(DISPLAYSURF, C[6], (750, 200 - 10), 8, 0)
        pygame.draw.circle(DISPLAYSURF, C[7], (870, 200 - 10), 8, 0)
        pygame.draw.circle(DISPLAYSURF, C[8], (990, 200 - 10), 8, 0)
      
        

        k+=1
        pygame.display.update()

import pygame, random, sys, pylab
from pygame.locals import *
import numpy as np

def gauss(sigma):
        phi=random.uniform(0, 2*math.pi)
        Upsilon=-math.log(random.uniform(0, 1))
        r=sigma*math.sqrt(2*Upsilon)
        x=r*math.cos(phi)
        y=r*math.sin(phi)
        return math.sqrt(x**2+y**2)

def levy_free_path(X, Beta):
    N=len(X)
    del_tau=Beta/N
    for k in range(1, N-1):
        del_tau_primed=(N-k)*del_tau
        xk_mean=(del_tau_primed*X[k-1]+del_tau*X[-1])/(del_tau+del_tau_primed)
        sigma=(1./del_tau+1./del_tau_primed)**(-0.5)
        X[k]=xk_mean+gauss(sigma)
    return X

Beta=8.
#X=[-2.5, 0., 1.2, -3.3, 2.4, 3.9, 0.7, -5.1]
X=[0.0]*6
N=len(X)-1
Y=[k*Beta/N for k in range(N+1)]

DISPLAYSURF=pygame.display.set_mode((500, 500))
pygame.display.set_caption("Random Permutation")

RED=(255, 0, 0)
BLUE=(0, 0, 255)
WHITE=(255, 255, 255)

clock=pygame.time.Clock()

DISPLAYSURF.fill(WHITE)
for i in range(len(Y)):pygame.draw.circle(DISPLAYSURF, RED, (165+int(X[i]*30), int(Y[i]*50)+80), 6, 0)
for i in range(len(Y)-1):pygame.draw.line(DISPLAYSURF, BLUE, [165+int(X[i]*30), int((Y[i]*50)+80)], [165+int(X[i+1]*30), int((Y[i+1]*50)+80)], 2)
              
while True:
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.image.save(DISPLAYSURF, 'Naive-path-sampling.png')
                        pygame.quit()
                        sys.exit()

        DISPLAYSURF.fill(WHITE)
        clock.tick(10)
        X=levy_free_path(X, Beta)
        for i in range(len(Y)):pygame.draw.circle(DISPLAYSURF, RED, (165+int(X[i]*30), int(Y[i]*50)+80), 6, 0)
        for i in range(len(Y)-1):pygame.draw.line(DISPLAYSURF, BLUE, [165+int(X[i]*30), int((Y[i]*50)+80)], [165+int(X[i+1]*30), int((Y[i+1]*50)+80)], 2)
                
        pygame.display.update()

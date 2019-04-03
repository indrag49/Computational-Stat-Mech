import pygame, random, sys
from pygame.locals import *
import numpy as np

def nran(k, l):
        while True:
                m=int(random.uniform(k, l+1))
                if m<=l: return m

def rho_free(x, xprime, beta): return math.exp(-(x-xprime)**2/(2*Beta))/math.sqrt(2*math.pi*Beta)


def naive_harmonic_path(X, Beta, delta):
        N=len(X)
        del_tau=Beta/N
        k=nran(0,N-1)
        k_plus,k_minus=(k+1)%N,(k-1)%N
        xp=X[k]+random.uniform(-delta, delta)
        pi_a=rho_free(X[k_minus], X[k], del_tau)*rho_free(X[k], X[k_plus], del_tau)*math.exp(-del_tau*X[k]**2/2.)
        pi_b=rho_free(X[k_minus], xp, del_tau)*rho_free(xp, X[k_plus], del_tau)*math.exp(-del_tau*xp**2/2.)
        Upsilon=pi_a/pi_b
        if random.uniform(0,1)<Upsilon: X[k]=xp
        return X

Beta=8.
X=[-2.5, 0., 1.2, -3.3, 2.4, 3.9, 0.7, -5.1]
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
        X=naive_harmonic_path(X, Beta, 1)
        for i in range(len(Y)):pygame.draw.circle(DISPLAYSURF, RED, (165+int(X[i]*30), int(Y[i]*50)+80), 6, 0)
        for i in range(len(Y)-1):pygame.draw.line(DISPLAYSURF, BLUE, [165+int(X[i]*30), int((Y[i]*50)+80)], [165+int(X[i+1]*30), int((Y[i+1]*50)+80)], 2)
                
        pygame.display.update()


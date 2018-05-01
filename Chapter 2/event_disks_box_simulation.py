from sympy import oo
import numpy as np
import math as m
import pygame, random, sys
from pygame.locals import *
import numpy as np

pygame.font.init()

def pair_time(pos_k, vel_k, pos_l, vel_l, radius):
        """ pos_k, pos_l, vel_k, vel_l all have two elements as a list """
        t_0=0.0
        pos_x=pos_l[0]-pos_k[0]
        pos_y=pos_l[1]-pos_k[1]
        Delta_pos=np.array([pos_x, pos_y])
        
        vel_x=vel_l[0]-vel_k[0]
        vel_y=vel_l[1]-vel_k[1]
        Delta_vel=np.array([vel_x, vel_y])

        Upsilon=(Delta_pos.dot(Delta_vel))**2-(Delta_vel.dot(Delta_vel))*((Delta_pos.dot(Delta_pos))-4.0*radius**2)

        if Upsilon>0.0 and Delta_pos.dot(Delta_vel)<0.0: return t_0-(Delta_pos.dot(Delta_vel)+m.sqrt(Upsilon))/(Delta_vel.dot(Delta_vel))
        else: return float(oo)

def wall_time(pos, vel, radius): return (1.0-radius-pos)/vel if vel>0.0 else (pos-radius)/abs(vel) if vel<0.0 else float(oo)

white=(255, 255, 255)
green=(51, 255, 51)
red=(255, 0, 0)
yellow=(255, 255, 51)
blue=(0, 0, 255)
black=(0, 0, 0)
pink=(255, 0, 255)

DISPLAYSURF=pygame.display.set_mode((500, 500))
pygame.display.set_caption('Event-Box')

DISPLAYSURF.fill(white)

t=0.0

pos=[[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75], [0.5, 0.5]]
vel=[[0.21, 0.12], [0.71, 0.18], [-0.23, 0.79], [0.78, 0.1177], [0.55, -0.22]]
singles=[(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (4, 1)]
pairs=[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
radius=0.12
clock=pygame.time.Clock()
        
myfont=pygame.font.SysFont('Comic Sans MS', 30)
while True:
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.image.save(DISPLAYSURF, 'Random Permutation.png')
                        pygame.quit()
                        sys.exit()

        DISPLAYSURF.fill(white)
        textsurface=myfont.render('Time = '+str(t), False, black)
        DISPLAYSURF.blit(textsurface, (120, 10))

        wall_times=[wall_time(pos[k][l], vel[k][l], radius) for k, l in singles]
        pair_times=[pair_time(pos[k], vel[k], pos[l], vel[l], radius) for k,l in pairs]
        next_event=min(wall_times+pair_times)
        t+=next_event

        for k, l in singles:pos[k][l]+=vel[k][l]*next_event
        
        if min(wall_times)<min(pair_times):
                collision_disk, direction=singles[wall_times.index(next_event)]
                vel[collision_disk][direction]*=-1.0
        else:
                a, b=pairs[pair_times.index(next_event)]
                del_x=[pos[b][0]-pos[a][0], pos[b][1]-pos[a][1]]
                abs_x=m.sqrt(del_x[0]**2+del_x[1]**2)
                e_perp=[c/abs_x for c in del_x]
                del_v=[vel[b][0]-vel[a][0], vel[b][1]-vel[a][1]]
                scal=del_v[0]*e_perp[0]+del_v[1]*e_perp[1]
                for k in range(2):
                        vel[a][k]+=e_perp[k]*scal
                        vel[b][k]-=e_perp[k]*scal
        
        pygame.draw.circle(DISPLAYSURF, red, (int(pos[0][0]*500), int(pos[0][1]*500)), int(radius*500), 0)
        pygame.draw.circle(DISPLAYSURF, blue, (int(pos[1][0]*500), int(pos[1][1]*500)), int(radius*500), 0)
        pygame.draw.circle(DISPLAYSURF, yellow, (int(pos[2][0]*500), int(pos[2][1]*500)), int(radius*500), 0)
        pygame.draw.circle(DISPLAYSURF, green, (int(pos[3][0]*500), int(pos[3][1]*500)), int(radius*500), 0)
        pygame.draw.circle(DISPLAYSURF, pink, (int(pos[4][0]*500), int(pos[4][1]*500)), int(radius*500), 0)
        
        clock.tick(20)
        
        pygame.display.update()

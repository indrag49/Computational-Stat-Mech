#Buffon's needle

import pylab
import random
import math as m

def direct_needle(N, a, b):
        assert a<=b, "a must be <= b"
        N_hits=0
        for i in range(1, N+1):
                x_center=random.uniform(0, b/2.)
                phi=random.uniform(0, m.pi/2)
                x_tip=x_center-(a/2.)*m.cos(phi)
                if x_tip<0: N_hits+=1
        return (N*a*2.)/(N_hits*b)

def direct_needle_patch(N,a, b):
        N_hits=0        
        for i in range(1, N+1):
            x_center=random.uniform(0, b/2.)
            while True:
                delta_x=random.uniform(0, 1)
                delta_y=random.uniform(0, 1)
                S=np.sqrt(delta_x**2+delta_y**2)
                if S<=1.: break
            x_tip=x_center-(a/2.)*delta_x/S
            if x_tip<0: N_hits+=1
        return (N*a*2.)/(N_hits*b)

>>> direct_needle_patch(2000, 0.6, 0.6)

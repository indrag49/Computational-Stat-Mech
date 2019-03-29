import random
import math

def naive_piston_particles(N, L, T, P, delta):
    Kb=1.3807*10**(-23)
    Beta=1/(Kb*T)
    x=[0]*N
    for i in range(N):
        x[i]=random.uniform(0,L)
    xmax=max(x)
    Delta_L=random.uniform(-delta, delta)
    Upsilon=math.exp(-Beta*P*Delta_L)
    if random.uniform(0,1)<Upsilon and L+Delta_L>xmax:
        L+=Delta_L
    return [L, x]

def naive_piston_particles_patch(N, L, T, P, delta):
    Kb=1.3807*10**(-23)
    Beta=1/(Kb*T)
    x=[0]*N
    for i in range(N):
        x[i]=random.uniform(0,L)
    xmax=max(x)
    Delta_L=-math.log(random.uniform(0, 1))/(Beta*P)
    L=xmax+Delta_L
    return [L, x]

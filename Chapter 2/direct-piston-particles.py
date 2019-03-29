import random
import math

def direct_piston_particles(N, T, P):
    Kb=1.3807*10**(-23)
    Beta=1/(Kb*T)
    Upsilon=random.uniform(0,1)
    alpha=[0]*N
    for k in range(N):
        alpha[k]=random.uniform(0,1)
        Upsilon*=random.uniform(0,1)
    L=-math.log(Upsilon)/(Beta*P)
    for i in range(N):
        alpha[i]*=L
    return [L, alpha]
        

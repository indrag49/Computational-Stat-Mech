import numpy as np
import random

def tower_sample(Pi):
        L=[0]
        K=len(Pi)
        for l in range(1, K+1): L+=[L[l-1]+Pi[l-1], ]
        Upsilon=random.uniform(0, L[-1])

        for k in range(1, len(L)+1):
                if (Upsilon>L[k-1] and  Upsilon<L[k]):
                        return k


A=np.array(([2, 4, 0, 0], [3, 5, 1, 0], [0, 6, 2, 0],
              [5, 7, 0, 1], [6, 8, 4, 2], [0, 9, 5, 3],
              [8, 0, 0, 4], [9, 0, 7, 5], [0, 0, 8, 6]))
                
def Nbr(n, k): return A.T[n-1, k-1]

L=3
N=L**2
sigma=[random.choice([-1, 1]) for i in range(N)]
##sigma=[-1, 1, -1, 1, -1, 1, 1, 1, -1]
print("sigma=",sigma)

def energy_ising(sigma):
    N=len(sigma)
    E=0
    for k in range(1, N+1):
        for n in range(1, 3):
            j=Nbr(n,k)
            if j!=0: E-=sigma[k-1]*sigma[j-1]
    return E

def dynamic_ising(t, sigma, T):
    Beta=1./T
    #N=len(sigma)
    p=[0.]*N
    for k in range(N):
        S=sigma[:]
        S[k]*=-1
        del_E=energy_ising(S)-energy_ising(sigma)
        p[k]=min(1, math.exp(-Beta*del_E))/N
    L=1-sum(p)
    del_t=1+int(math.log(random.random())/math.log(L))
    l=tower_sample(p)
    sigma[l]*=-1
    t+=del_t
    return [t, sigma]

t=0
T=5.
while t<=100:
    [t, sigma]=dynamic_ising(t, sigma, T)
    print(t, sigma)

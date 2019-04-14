import numpy as np
import random, math

A=np.array(([2, 4, 0, 0], [3, 5, 1, 0], [0, 6, 2, 0],
              [5, 7, 0, 1], [6, 8, 4, 2], [0, 9, 5, 3],
              [8, 0, 0, 4], [9, 0, 7, 5], [0, 0, 8, 6]))

L=3
N=L**2
E=-2*N

def Nbr(n, k): return A.T[n-1, k-1]

sigma=[random.choice([1, -1]) for i in range(N)]
print("sigma=", sigma)
print(" ")

def nran(k, l):
        while True:
                m=int(random.uniform(k, l+1))
                if m<=l: return m
                
def markov_spin_glass(sigma, E, T):
    Beta=1./T
    k=nran(1, N)
    h=0
    for l in range(1, 3):
        j=Nbr(l, k)
        h+=sigma[j-1]*random.choice([-1, 1])
    del_E=h*sigma[k-1]
    Upsilon=math.exp(-Beta*del_E)
    if random.uniform(0, 1)<Upsilon:
        sigma[k-1]=-sigma[k-1]
        E+=del_E
    return [sigma, E]

for i in range(100):
    [sigma, E]=markov_spin_glass(sigma, E, 2.)
    print(sigma, E)

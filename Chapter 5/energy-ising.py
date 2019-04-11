import numpy as np
import random

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

print(energy_ising(sigma))

import numpy as np
import random

A=np.array(([2, 4, 0, 0], [3, 5, 1, 0], [0, 6, 2, 0],
              [5, 7, 0, 1], [6, 8, 4, 2], [0, 9, 5, 3],
              [8, 0, 0, 4], [9, 0, 7, 5], [0, 0, 8, 6]))
                
def Nbr(n, k): return A.T[n-1, k-1]

def gray_flip(tau):
    k=tau[0]
    N=len(tau)-1
    if k>N: exit
    tau[k-1]=tau[k]
    tau[k]=k+1
    if k!=1: tau[0]=1
    return [k, tau]

def enumerate_ising(N):
    density=[0. for i in range(-2*N, 2*N+1)]
    sigma=[-1]*N
    tau=[i+1 for i in range(N+1)]
    E=-2*N
    density[E+2*N]=2
    for i in range(1, 2**N):
        k=gray_flip(tau)[0]
        h=0
        for n in range(1, 3):
            j=Nbr(n, k)
            h+=sigma[j-1]
        E+=2*sigma[k-1]*h
        density[E+2*N]+=2
        sigma[k-1]=-sigma[k-1]
        print(density, sigma, E)


L=3
N=L**2
enumerate_ising(N)

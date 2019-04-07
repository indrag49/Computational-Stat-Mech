import random, math
import numpy as np

def tower_sampling(Pi):
        L=[0]
        K=len(Pi)
        for l in range(1, K+1): L+=[L[l-1]+Pi[l-1], ]
        Upsilon=random.uniform(0, L[-1])
        for k in range(1, len(L)+1):
                if (Upsilon>L[k-1] and  Upsilon<L[k]):
                        return k
                    
def Rho_free(x, xk, Beta): return math.sqrt(1/(2*math.pi*Beta))*math.exp(-(x-xk)**2/(2*Beta))

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

def levy_periodic_path(X, L, Beta):
    Pi=[]
    for w1 in range(-3, 4):
        Pi+=[Rho_free(X[0], X[-1]+w1*L, Beta), ]
    w=tower_sampling(Pi)
    X[-1]+=(w*L)
    return levy_free_path(X, Beta)

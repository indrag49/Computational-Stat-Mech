import numpy as np
import random, math

def gauss(sigma):
        phi=random.uniform(0, 2*math.pi)
        Upsilon=-math.log(random.uniform(0, 1))
        r=sigma*math.sqrt(2*Upsilon)
        x=r*math.cos(phi)
        y=r*math.sin(phi)
        return math.sqrt(x**2+y**2)

def vecs(d, N):
    return map(lambda x: x / np.linalg.norm(x),
               [np.random.standard_normal(d) for i in range(N)])

X=vecs(3, 10)

def resize_disks(X, r):
    N=len(X)
    d=len(X[0])
    gamma=0.005
    k=random.randint(0, N-1)
    del_X=[gauss(0.01) for i in range(d)]
    X1=[]
    D=[]
    for j in range(d):
        X1+=[(X[k][j]+del_X[j])/np.abs(X[k][j]+del_X[j]), ]
    for l in range(N):
        D+=[math.sqrt(sum([(X1[i]-X[l][i])**2 for i in range(d)])), ] 
    Upsilon=min(D)/2
    r+=gamma*(Upsilon-r)
    if Upsilon>r: X[k]=X1
    return X

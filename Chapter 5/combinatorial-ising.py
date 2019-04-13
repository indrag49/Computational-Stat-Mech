import numpy as np
import random, math, cmath

A=np.array(([2, 4, 0, 0], [3, 5, 1, 0], [0, 6, 2, 0],
              [5, 7, 0, 1], [6, 8, 4, 2], [0, 9, 5, 3],
              [8, 0, 0, 4], [9, 0, 7, 5], [0, 0, 8, 6]))
                
def Nbr(n, k): return A.T[n-1, k-1]

U=np.array(([[random.random()for i in range(5)] for j in range(5)]))
L=3
N=3**2

def combinatorial_ising(T):
    Beta=1./T
    nu=math.tanh(Beta)
    alpha=cmath.exp(1j*math.pi/4)*math.tanh(Beta)
    alpha_not=cmath.exp(-1j*math.pi/4)*math.tanh(Beta)
    u_right=np.array(([nu, alpha, 0., alpha_not], [0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 0.]))
    u_up=np.array(([0., 0., 0., 0.], [nu, alpha, 0., alpha_not],[0., 0., 0., 0.], [0., 0., 0., 0.]))
    u_left=np.array(([0., 0., 0., 0.], [0., 0., 0., 0.], [nu, alpha, 0., alpha_not], [0., 0., 0., 0.]))
    u_down=np.array(([0., 0., 0., 0.], [0., 0., 0., 0.], [0., 0., 0., 0.], [nu, alpha, 0., alpha_not]))
    U=np.array(([[0.+0j for i in range(4*N+1)] for j in range(4*N+1)]))
    
    for k in range(1, N+1):
        for n in range(1, 5):
            j=4*(k-1)+n
            U[j-1, j-1]=1
            for n1 in range(1, 5):
                k1=Nbr(1, k)
                if k1!=0:
                    j1=4*(k1-1)+n1
                    U[j-1, j1-1]=u_right[n-1, n1-1]
                k1=Nbr(2, k)
                if k1!=0:
                    j1=4*(k1-1)+n1
                    U[j-1, j1-1]=u_up[n-1, n1-1]
                k1=Nbr(3, k)
                if k1!=0:
                    j1=4*(k1-1)+n1
                    U[j-1, j1-1]=u_left[n-1, n1-1]
                k1=Nbr(4, k)
                if k1!=0:
                    j1=4*(k1-1)+n1
                    U[j-1, j1-1]=u_down[n-1, n1-1]
    return U

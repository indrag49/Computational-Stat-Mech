import math
import numpy as np
import pylab
X=np.linspace(-2., 2., 25)
L=len(X)

def Rho_free(x, xk, Beta): return math.sqrt(1/(2*math.pi*Beta))*math.exp(-(x-xk)**2/(2*Beta))

# The Density matrix for the Harmonic Oscillator can be produced using the Trotter Decomposition and the free density matrix, Rho_free
def V(x): return x**2/2.


def Rho_ho(Beta):
    R=[[0.0 for i in range(L)] for j in range(L)]
    for i in range(L):
        for j in range(L):
            R[i][j]=math.exp(-Beta*V(X[i])/2.)*Rho_free(X[i], X[j], Beta)*math.exp(-Beta*V(X[j])/2.)
    return np.array(R)



def matrix_Square(Beta):
    R=Rho_ho(Beta)
    return np.dot(R,R)


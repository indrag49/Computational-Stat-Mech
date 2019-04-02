import math
import numpy as np
import pylab
def harmonic_wavefunction(x, N):
    psi=[0, (math.pi)**(-1./4)*math.exp(-x**2/2.)]
    for n in range(2, N+1):
        psi+=[math.sqrt(2./n)*x*psi[n-1]-math.sqrt((n-1)/n)*psi[n-2], ]
    return psi[1:]

def E(n): return n+0.5
def Z(Beta): return 0.5/math.sinh(Beta/2.)

def harmonic_density(xmin, xmax, N, Beta):
    L=np.linspace(xmin, xmax, 15)
    l=len(L)
    rho=[[0.0 for i in range(l)] for j in range(l)]
    for i in range(l):
        for j in range(l):
            for n in range(N):
                rho[i][j]+=harmonic_wavefunction(L[i], N)[n]*harmonic_wavefunction(L[j], N)[n]*math.exp(-Beta*E(n))
    return rho


def Prob(x, xmin, xmax, N, Beta):
    L=np.linspace(xmin, xmax, 15)
    L=L.tolist()
    i=L.index(x)
    return np.array(harmonic_density(xmin, xmax, N, Beta))[i, i]/Z(Beta)
#print(Prob(0., -2., 2., 100, 8.))

X=np.linspace(-2., 2., 15)
P=[Prob(i, -2., 2., 100, 8) for i in X]
pylab.plot(X, P)
pylab.show()

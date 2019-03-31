import math
def harmonic_wavefunction(x, N):
    psi=[0, (math.pi)**(-1./4)*math.exp(-x**2/2)]
    for n in range(2, N+2):
        psi+=[math.sqrt(2./n)*x*psi[n-1]-math.sqrt((n-1)/n)*psi[n-2], ]
    return psi


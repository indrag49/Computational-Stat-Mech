import math
def harmonic_wavefunction(x, N):
    psi=[0, (math.pi)**(-1./4)*math.exp(-x**2/2)]
    for n in range(2, N):
        psi+=[math.sqrt(2./n)*x*psi[n-1]-math.sqrt((n-1)/n)*psi[n-2], ]
    return psi

def E(n): return n+0.5

def harmonic_density(xmin, xmax, N, Beta):
    rho=[[0.0 for i in range(xmin, xmax+1)] for j in range(xmin, xmax+1)]
    for x in range(xmin, xmax+1):
        for xprime in range(xmin, xmax+1):
            for n in range(N):
                rho[x][xprime]+=harmonic_wavefunction(x, N)[n]*harmonic_wavefunction(xprime, N)[n]*math.exp(-Beta*E(n))
    return rho

print(harmonic_density(-2, 2, 100, 8))

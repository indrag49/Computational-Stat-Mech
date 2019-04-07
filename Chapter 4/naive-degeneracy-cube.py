import math
def Naive_degeneracy_cube(Emax):
    """N(E) for a periodic cube box of edge length sqrt(2*pi)"""
    N=[0]*(Emax+1)
    nmax=int(math.sqrt(Emax))
    for nx in range(-nmax, nmax+1):
        for ny in range(-nmax, nmax+1):
            for nz in range(-nmax, nmax+1):
                E=nx**2+ny**2+nz**2
                if abs(E)<=Emax:
                    N[E]+=1
    return N
                

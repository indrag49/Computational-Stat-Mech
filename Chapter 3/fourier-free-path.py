import math, random

def gauss(sigma):
        phi=random.uniform(0, 2*math.pi)
        Upsilon=-math.log(random.uniform(0, 1))
        r=sigma*math.sqrt(2*Upsilon)
        x=r*math.cos(phi)
        y=r*math.sin(phi)
        return math.sqrt(x**2+y**2)

def fourier_free_path(Beta, N):
    c,x=[],[]
    for n in range(1, N):
        Upsilon=2*N**2*math.sin(n*math.pi/(2.*N))**2
        c+=[gauss(math.sqrt(Beta/Upsilon)), ]
    for k in range(N+1):
        x+=[sum([c[n]*math.sin(n*math.pi*k/N) for n in range(len(c))]), ]
    return x

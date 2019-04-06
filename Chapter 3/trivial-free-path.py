import math, random

def gauss(sigma):
        phi=random.uniform(0, 2*math.pi)
        Upsilon=-math.log(random.uniform(0, 1))
        r=sigma*math.sqrt(2*Upsilon)
        x=r*math.cos(phi)
        y=r*math.sin(phi)
        return math.sqrt(x**2+y**2)

def trivial_free_path(Beta, N):
    x, Upsilon=[0], [0]
    for k in range(1, N+1):
        Upsilon+=[Upsilon[k-1]+gauss(math.sqrt(Beta/N)), ]
    for k in range(1, N+1):
        x+=[Upsilon[k]-Upsilon[-1]*k/N, ]
    return x

print(trivial_free_path(8., 8))

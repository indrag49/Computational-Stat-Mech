import math, random

def gauss(sigma):
        phi=random.uniform(0, 2*math.pi)
        Upsilon=-math.log(random.uniform(0, 1))
        r=sigma*math.sqrt(2*Upsilon)
        x=r*math.cos(phi)
        y=r*math.sin(phi)
        return math.sqrt(x**2+y**2)

def fourier_gen_path(L, del_t, Beta, zeta):
    """All quantum paths and all random walks has roughness exponent (zeta)=0.5"""
    sigma, a, b=[0.]*10000, [0.]*10000, [0.]*10000
    for n in range(1, 10001):
        sigma[n-1]=(math.pi*n)**(-0.5)*(L/(2.*math.pi*n))**zeta
        a[n-1]=gauss(sigma[n-1])
        b[n-1]=gauss(sigma[n-1])
    t=0
    x=[]
    while t<=L*1.0:
        x+=[sum([a[n-1]*math.cos(2*math.pi*n*t/L)+b[n-1]*math.sin(2*math.pi*n*t/L) for n in range(1, 10001)]), ]
        t+=del_t
    return x

print(fourier_gen_path(10., 0.1, 8., 0.2))

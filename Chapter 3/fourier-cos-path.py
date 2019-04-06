import math, random

def gauss(sigma):
        phi=random.uniform(0, 2*math.pi)
        Upsilon=-math.log(random.uniform(0, 1))
        r=sigma*math.sqrt(2*Upsilon)
        x=r*math.cos(phi)
        y=r*math.sin(phi)
        return math.sqrt(x**2+y**2)

def fourier_cos_path(L, del_t, Beta, zeta):
    sigma, c, x=[0.]*10000, [0.]*10000, []
    for n in range(1, 10001):
        sigma[n-1]=(2./(math.pi*n))*(L/(math.pi*n))**zeta
        c[n-1]=gauss(sigma[n-1])
    t=0
    while t<=L*1.0:
        x+=[sum([c[n-1]*math.cos(n*math.pi*t/L) for n in range(1, 10001)]), ]
        t+=del_t
    return x

print(fourier_cos_path(10., 0.1, 8., 0.2))

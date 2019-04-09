import math, cmath

def f(E, N, Beta, Lambda): return (1-cmath.exp(1j*(N+1)*Lambda))/(1-cmath.exp(1j*Lambda)) if E==0 else 1/(1-cmath.exp(-Beta*E+1j*Lambda))

def n(E): return (E+1)*(E+2)/2

def canonic_bosons(del_mu, T, N, Emax):
    Beta=1./T
    Z, E_mean=0, 0
    Lambda=-math.pi
    while Lambda<=math.pi:
        Z_lambda=f(0, N, Beta, Lambda)
        E_lambda=0
        for E in range(1, Emax+1):
            Z_lambda*=f(E, N, Beta, Lambda)**n(E)
            E_lambda+=n(E)*E*cmath.exp(-Beta*E+1j*Lambda)/(1-cmath.exp(-Beta*E+1j*Lambda))
        Z+=Z_lambda*cmath.exp(-1j*N*Lambda)*del_mu/(2*math.pi)
        E_mean+=E_lambda*Z_lambda*cmath.exp(-1j*N*Lambda)*del_mu/(2*math.pi)
        Lambda+=del_mu
    E_mean/=Z
    return [T/N**(1./3), Z, E_mean/N]



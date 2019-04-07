import math, random

def j(l, r):
    if l==0: return math.sin(r)/r
    elif l==1: return math.sin(r)/r**2-math.cos(r)/r
    else: return (2*l-1)*j(l-1, r)/r-j(l-2, r)

def y(l, r):
    if l==0: return -math.cos(r)/r
    elif l==1: return -math.cos(r)/r**2-math.sin(r)/r
    else: return (2*l-1)*y(l-1, r)/r-y(l-2, r)

def R(sigma, k, l, r):
    delta=math.atan(j(l, 2*k*sigma)/y(l, 2*k*sigma))
    return j(l, k*r)*math.cos(delta)-y(l, k*r)*math.sin(delta)

def naive_rad_wavefunction(n, l, sigma, L, del_k, del_r):
    k=del_k
    P=[]
    X=[]
    while True:
        if R(sigma, k+del_k, l, L)*R(sigma, k, l, L)<0.0:
            kn=k
            Upsilon=0.0005
            r=2*sigma
            
            while r<=L*1.0:
                Rdel=R(sigma, kn, l, r)
                Upsilon+=del_r*(r*Rdel)**2
                #print(sigma, kn, l, r)
                X+=[r, ]
                P+=[Rdel/math.sqrt(Upsilon), ]
                r+=del_r
            return [X, P]
        k+=del_k


            

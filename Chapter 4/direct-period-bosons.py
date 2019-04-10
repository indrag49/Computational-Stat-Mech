import math, random

def E(n, L): return 2*(math.pi*n/L)**2
def z_cube(L, k, Beta): return sum([math.exp(-k*Beta*E(n, L)) for n in range (-10**5, 10**5)])**3
def der_z_cube(L, k, Beta): return -3*k*sum([math.exp(-k*Beta*E(n, L)) for n in range(-10**5, 10**5)])**2*sum([E(n, L)*math.exp(-k*Beta*E(n, L)) for n in range(-10**5, 10**5)])

##for k in range(1, 9):
##    print([k, z_cube(2, k, 0.5), der_z_cube(2, k, 0.5)])

def tower_sample(Pi):
        L=[0]
        K=len(Pi)
        for l in range(1, K+1): L+=[L[l-1]+Pi[l-1], ]
        Upsilon=random.uniform(0, L[-1])

        for k in range(1, len(L)+1):
                if (Upsilon>L[k-1] and  Upsilon<L[k]):
                        return k

def Rho_free(x, xk, Beta): return math.sqrt(1/(2*math.pi*Beta))*math.exp(-(x-xk)**2/(2*Beta))

def gauss(sigma):
        phi=random.uniform(0, 2*math.pi)
        Upsilon=-math.log(random.uniform(0, 1))
        r=sigma*math.sqrt(2*Upsilon)
        x=r*math.cos(phi)
        y=r*math.sin(phi)
        return math.sqrt(x**2+y**2)

def levy_free_path(X, Beta):
    N=len(X)
    del_tau=Beta/N
    for k in range(1, N-1):
        del_tau_primed=(N-k)*del_tau
        xk_mean=(del_tau_primed*X[k-1]+del_tau*X[-1])/(del_tau+del_tau_primed)
        sigma=(1./del_tau+1./del_tau_primed)**(-0.5)
        X[k]=xk_mean+gauss(sigma)
    return X

def levy_periodic_path(X, L, Beta):
    Pi=[]
    for w1 in range(-3, 4):
        Pi+=[Rho_free(X[0], X[-1]+w1*L, Beta), ]
    w=tower_sample(Pi)
    X[-1]+=(w*L)
    return levy_free_path(X, Beta)

def canonic_recursion(L, N, Beta):
    z=[z_cube(L, k, Beta) for k in range(1, N+1)]
    Z=[1]+[0]*N
    for M in range(1, N+1): Z[M]=sum([z_cube(L, k, Beta)*Z[M-k] for k in range(1, M+1)])/M
    return [z, Z]

def direct_cycles(z, Z):
    N=len(Z)
    m=[0]*N
    M=N
    while M>0:
        k=tower_sample([z[i]*Z[M-i] for i in range(1, M+1)])
        M-=k
        m[k]+=1
    return m

def direct_period_bosons(L, N, Beta):
    [z, Z]=canonic_recursion(L, N, Beta)
    #print(z, Z)
    Z=Z[:-1]
    z=[0]+z
    X=[0]*N
    m=direct_cycles(z, Z)
    l=0
    for k in range(len(m)):
        if m[k]!=0:
            k1=k+1
            for i in range(1, m[k]+1):
                X=levy_periodic_path(X, L, k1*Beta)
    return X
                
                

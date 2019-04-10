import math, random
def tower_sample(Pi):
        L=[0]
        K=len(Pi)
        for l in range(1, K+1): L+=[L[l-1]+Pi[l-1], ]
        Upsilon=random.uniform(0, L[-1])

        for k in range(1, len(L)+1):
                if (Upsilon>L[k-1] and  Upsilon<L[k]):
                        return k

def z(k, Beta): return (1/(1-math.exp(-k*Beta)))**3

def canonic_recursion(N, Beta):
    Z=[1]+[0]*N
    for M in range(1, N+1): Z[M]=sum([z(k, Beta)*Z[M-k] for k in range(1, M+1)])/M
    return Z[:-1]

def direct_cycles(N, Beta):
    zp=[0]+[z(k, Beta) for k in range(1, N+1)]
    Z=canonic_recursion(N, Beta)
    m=[0]*N
    M=N
    while M>0:
        k=tower_sample([zp[i]*Z[M-i] for i in range(1, M+1)])
        print([zp[i]*Z[M-i] for i in range(1, M+1)])
        print(k)
        M-=k
        m[k]+=1
    return m


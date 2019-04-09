import math

def z(k, Beta): return (1/(1-math.exp(-k*Beta)))**3

def canonic_recursion(N, Beta):
    Z=[1]+[0]*N
    for M in range(1, N+1): Z[M]=sum([z(k, Beta)*Z[M-k] for k in range(1, M+1)])/M
    return Z[-1]

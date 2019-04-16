import random, math

def direct_pin(N, sigma, L):
    y=[]
    x=[0.]*N
    for k in range(N): y+=[random.uniform(0, L-2*N*sigma), ]
    y.sort()
    for k in range(1, N+1): x[k-1]=y[k-1]+(2*k-1)*sigma
    return x

for i in range(1000):
    print(direct_pin(15, 0.05, 2))

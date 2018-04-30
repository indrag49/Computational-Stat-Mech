import random
import pylab

def direct_pi(N):
    N_hits=0.
    for i in range(1, N+1):
        x=random.uniform(-1, 1)
        y=random.uniform(-1, 1)
        if x**2+y**2<1:N_hits+=1
    return N_hits*4.0/N
    
def plot_direct_pi():
    X=[]
    Y=[]
    for i in range(1, 10000):
        X+=[i, ]
        Y+=[direct_pi(i), ]
    pylab.plot(X, Y, 'k-')
    pylab.show()

import random
import pylab
import numpy as np
def Markov_pi(N, delta):
        N_hits=0
        x, y=1, 1
        for i in range(1, N+1):
                Delta_x=random.uniform(-delta, delta)
                Delta_y=random.uniform(-delta, delta)
                if abs(x+Delta_x)<1 and abs(y+Delta_y)<1:
                        x+=Delta_x
                        y+=Delta_y
                if x**2+y**2<1: N_hits+=1
        return N_hits*4.0/N

def plot_Markov_pi_1(delta):
    X=[]
    Y=[]
    for i in range(1, 10000):
        X+=[i, ]
        Y+=[Markov_pi(i, delta), ]
    pylab.plot(X, Y, '-')
    pylab.show()

def plot_Markov_pi_2(N):
    X=[]
    Y=[]
    for delta in np.arange(-2, 2.05, 0.01):
        X+=[delta, ]
        Y+=[Markov_pi(N, delta), ]
    pylab.plot(X, Y, 'r-')
    pylab.xlabel('$\delta$')
    pylab.ylabel('Estimated value of pi')
    pylab.title('N=%s'%(N))
    pylab.show()

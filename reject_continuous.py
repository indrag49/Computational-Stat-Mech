import math as m
import random
import numpy as np

def Prob(x): return m.exp(-x**2/2.)/m.sqrt(2*m.pi)

def reject_continuous(x_min, x_max):
        X=np.arange(x_min, x_max, 0.01)
        P=[Prob(i) for i in X]
        while True:                
                x=random.uniform(x_min, x_max)
                Upsilon=random.uniform(0, max(P))
                if Upsilon<=Prob(x): return x


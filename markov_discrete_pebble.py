import numpy as np
import random
A=np.array(([2, 4, 0, 0], [3, 5, 1, 0], [0, 6, 2, 0],
              [5, 7, 0, 1], [6, 8, 4, 2], [0, 9, 5, 3],
              [8, 0, 0, 4], [9, 0, 7, 5], [0, 0, 8, 6]))
print A

def nran(k, l):
        while True:
                m=int(random.uniform(k, l+1))
                if m<=l: return m
                
def Nbr(n, k): return A.T[n-1, k-1]

def markov_discrete_pebble(k):
        n=random.choice(range(1, 5))
        if Nbr(n, k)!=0: k=Nbr(n, k)
        return k

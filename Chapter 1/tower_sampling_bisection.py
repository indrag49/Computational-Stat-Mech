import random
import numpy as np

def bisection_search(Upsilon, L):
        k_min=0
        k_max=len(L)
        i=1
        while True:
                k=(k_min+k_max)/2
                if L[k]<Upsilon: k_min=k
                elif L[k-1]>Upsilon: k_max=k
                else: return k

def tower_sample(Pi):
        L=[0]
        K=len(Pi)
        for l in range(1, K+1): L+=[L[l-1]+Pi[l-1], ]
        Upsilon=random.uniform(0, L[-1])

        return bisection_search(Upsilon, L)



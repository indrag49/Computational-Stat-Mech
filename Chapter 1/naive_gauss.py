import random
import math as m

def naive_gauss(K):
        sigma=m.sqrt(K/12.)
        S=0
        for k in range(1, K+1): S+=random.uniform(-0.5, 0.5)
        return S/sigma
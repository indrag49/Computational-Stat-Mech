import random

def nran(k, l):
        while True:
                m=int(random.uniform(k, l+1))
                if m<=l: return m
def ran_combination(K, M):
        assert M<K, "M must be less than K"
        P=range(1, K+1)
        for k in range(1, M+1):
                l=nran(k, K)
                temp=P[l-1]
                P[l-1]=P[k-1]
                P[k-1]=temp
        return P
import random

def nran(k, l):
        while True:
                m=int(random.uniform(k, l+1))
                if m<=l: return m
def ran_perm(K):
        P=range(1, K+1)
        print(P)
        for k in range(1, K):
                l=nran(k, K)
                temp=P[l-1]
                P[l-1]=P[k-1]
                P[k-1]=temp
                print(P)
        return P

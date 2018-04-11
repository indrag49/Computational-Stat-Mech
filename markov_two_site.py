# Sampling sites 0 and 1 with stationary probabilities Pi(0) and Pi(1) by the Metropolis Algorithm

import random
def Pi(k):
        assert k==0 or k==1, "k(present site) must be 0 or 1"
        return 0.25 if k==0 else 0.75
def markov_two_site(k):
        """k = 0 or 1"""
        assert k==0 or k==1, "k(present site) must be 0 or 1"
        l=1-k
        Upsilon=Pi(l)/Pi(k)
        if random.uniform(0, 1)<Upsilon: k=l
        return k
k=1
for i in range(100):
        print(k)
        k=markov_two_site(k)

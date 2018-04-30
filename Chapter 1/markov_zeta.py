import random

def markov_zeta(delta, zeta, x):
        x_=x+random.uniform(-delta, delta)
        if x_>0. and x_<1.:
                p=(x_/x)**zeta
                if random.uniform(0, 1)<p: x=x_
        return x
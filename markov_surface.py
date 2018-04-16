import numpy as np
import math as m
import random

def markov_surface(d, delta):
        """d is the dimension of the hypersphere, delta is the step size"""
        sigma=1/m.sqrt(d)
        x=np.array([random.uniform(-1, 1) for i in range(d)])
        x=x/m.sqrt(x.dot(x))
        epsilon=np.array([gauss(sigma)[0] for i in range(d)])
        S=epsilon.dot(x)
        epsilon=epsilon-S*x
        epsilon=epsilon/m.sqrt(epsilon.dot(epsilon))
        Upsilon=random.uniform(-delta, delta)
        x=x+Upsilon*epsilon
        x=x/m.sqrt(x.dot(x))
        return x
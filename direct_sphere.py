import random
import math as m

def gauss(sigma):
        phi=random.uniform(0, 2*m.pi)
        Upsilon=-m.log(random.uniform(0, 1))
        r=sigma*m.sqrt(2*Upsilon)
        x=r*m.cos(phi)
        y=r*m.sin(phi)
        return [x, y]

def direct_sphere(d, sigma):
        """ d is the dimension of the sphere, sigma is the standard deviation of the gaussian"""
        S=0
        x=[0]*d
        for k in range(d):
                x[k]=gauss(sigma)[1]
                S+=x[k]**2
        Upsilon=random.uniform(0, 1)**(1./d)
        for k in range(d): x[k]=Upsilon*x[k]/m.sqrt(S)
        return x
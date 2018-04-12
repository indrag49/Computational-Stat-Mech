import random
import math as m

def gauss(sigma):
        phi=random.uniform(0, 2*m.pi)
        Upsilon=-m.log(random.uniform(0, 1))
        r=sigma*m.sqrt(2*Upsilon)
        x=r*m.cos(phi)
        y=r*m.sin(phi)
        return [x, y]
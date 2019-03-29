import random
import math
def maxwell_boundary(vx, vy, T):
    Upsilon=random.uniform(0,1)
    Kb=1.3807*10**(-23)
    Beta=1/(Kb*T)
    vx=math.sqrt(-2*math.log(Upsilon)/Beta)
    return [vx, vy]

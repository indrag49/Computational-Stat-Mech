import random
import math

def gamma_cut(N, x_cut):
    x_star=1-N/x_cut
    if x_star<0: exit
    while True:
        Delta_x=-math.log(random.uniform(0,1))/x_star
        x=x_cut+Delta_x
        Upsilon_dashed=(x/x_cut)**N*math.exp(-(1-x_star)*Delta_x)
        if random.uniform(0,1)<=Upsilon_dashed: return x_cut+Delta_x

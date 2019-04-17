import math, random

def fast_throw():
    L=5./6
    t=0
    i=1
    while True:
        del_t=1+int(math.log(random.random())/math.log(L))
        t+=del_t
        print(t+del_t)

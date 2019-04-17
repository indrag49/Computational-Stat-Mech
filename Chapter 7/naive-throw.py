import random

def naive_throw():
    t=1
    while True:
        Upsilon=random.randint(1, 6)
        if Upsilon==1: return t
        t+=1

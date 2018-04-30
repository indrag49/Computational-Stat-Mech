import random

def naive_bayes_pi():
        while True:
                pi_test=random.uniform(0, 4)
                N_hits=0
                for i in range(1, 4001):
                        if random.uniform(0, 1)<pi_test/4.: N_hits+=1
                if N_hits ==3156: return pi_test
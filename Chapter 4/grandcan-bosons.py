import math

def n(E): return (E+1)*(E+2)/2.

def N_mean(Beta, mu): return sum([n(E)*math.exp(-Beta*(E-mu))/(1-math.exp(-Beta*(E-mu))) for E in range(10**5)])

def grandcan_bosons(n_mean, mu_min, Beta):
    mu_max=0
    for i in range(1, 100):
        mu=(mu_min+mu_max)/2.
        if N_mean(Beta, mu)<n_mean: mu_min=mu
        else: mu_max=mu
    mu=(mu_min+mu_max)/2.
    return mu

## To produce Table 4.5
nmean=[400, 800, 1000, 1200, 1400, 2000, 5000, 10000]
for i in nmean:
    print([i, grandcan_bosons(i, -12., 0.1)])

import math

def naive_bosons(t):
    Beta=1./t
    E=[0.]*1+[1.]*3+[2.]*6+[3.]*10+[4.]*15
    Z_btm=0
    E_mean=0
    N0_mean=0
    for sigma1 in range(35):
        for sigma2 in range(sigma1, 35):
            for sigma3 in range(sigma2, 35):
                for sigma4 in range(sigma3, 35):
                    for sigma5 in range(sigma4, 35):
                        Etot=E[sigma1]+E[sigma2]+E[sigma3]+E[sigma4]+E[sigma5]
                        N0=[sigma1, sigma2, sigma3, sigma4, sigma5].count(0)
                        Z_btm+=math.exp(-Beta*Etot)
                        E_mean+=Etot*math.exp(-Beta*Etot)
                        N0_mean+=N0*math.exp(-Beta*Etot)
    E_mean/=Z_btm
    N0_mean/=Z_btm
    return [t, Z_btm, E_mean/5, N0_mean/5]

t=0.1
while t<=1.0:
    print(naive_bosons(t))
    t+=0.1
    

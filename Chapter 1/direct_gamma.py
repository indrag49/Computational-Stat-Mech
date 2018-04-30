import random
import math as m

def direct_gamma(gamma, N):
        S=0.
        s=0.
        for i in range(N):
                x=random.uniform(0, 1)
                S+=x**gamma
                s+=x**(2*gamma)
        mean=S*1./N
        y=s*1./N
        var=m.sqrt(y-mean**2)
        error=var/m.sqrt(N)
        return [mean, error]


import pylab
S=0.
RE=[]
for i in range(1, 800001):
        x=random.uniform(0, 1)
        S+=x**(-0.8)
        RE+=[S/i, ]
pylab.plot(range(1, 800001), RE, 'r-')
pylab.ylabel("$\Sigma_i$/i")
pylab.xlabel("Number of samples i")
import random

def direct_gamma_zeta(gamma, zeta, N):
        S=0
        s=0
        for i in range(N):
                x=random.uniform(0, 1)**(1/(zeta+1.))
                S+=x**(gamma-zeta)
                s+=x**(2*(gamma-zeta))
        mean=S*1./N
        y=s*1./N
        var=m.sqrt(y-mean**2)
        error=var/m.sqrt(N)
        return [mean, error]

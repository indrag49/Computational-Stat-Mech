def direct_gamma_zeta(gamma, zeta, N):
        S=0
        s=0
        for i in range(N):
                x=random.uniform(0, 1)**(1/(zeta+1.))
                S+=x**(gamma-zeta)
        return S/N
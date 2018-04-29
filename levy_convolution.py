def levy_convolution(Pi, X):
        """ Pi is a list of probabilities with K+1 elements"""
        assert len(Pi)==len(X), "lengths of Pi and X must be equal"""
        K=len(X)-1
        alpha=1.25
        A_plus=1.25
        Delta=0.5
        for k in range(K+1, 2*K+1):
                X+=[X[0]+k*Delta, ]
                Pi+=[A_plus/(X[k]**(1+alpha)), ]
        x=[]
        p=[]
        for k in range(0, 2*K+1):
                x+=[(X[0]+X[k])/(2**(1/alpha)), ]
                p+=[Delta*sum([Pi[l]*Pi[k-l] for l in range(k+1)])*(2**(1/alpha)), ]
        return [x, p]
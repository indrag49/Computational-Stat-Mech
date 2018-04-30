import math as m

def data_bunch(X):
        """X is the list of Markov-chain data containing 2N elements"""
        assert len(X)%2==0, 'length of X must be even'
        S=0
        s=0
        N=len(X)/2
        x=[]
        for i in range(N):
                S+=X[2*i]+X[2*i+1]
                s+=X[2*i]**2+X[2*i+1]**2
                x+=[(X[2*i]+X[2*i+1])/2., ]
        error=m.sqrt(s/(2.*N)-(S/(2.*N))**2)/m.sqrt(2.*N)
        return [S/(2.*N), error, x]
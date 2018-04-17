def binomial_convulation(Pi, theta):
        """Pi is a list of N+1 probabilities; {pi_0, pi_1,...pi_N}(N trials)"""
        n=len(Pi)
        N=n-1
        Pi_=[(1-theta)*Pi[0]]
        for k in range(1, N+1):
                Pi_+=[theta*Pi[k-1]+(1-theta)*Pi[k], ]
        Pi_+=[theta*Pi[N]]
        return Pi_
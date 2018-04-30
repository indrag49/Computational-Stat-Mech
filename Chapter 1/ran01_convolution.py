def ran01_convulation(Pi,l):
        """Pi is a list of N+1 values: probabilities for sum of N variables"""
        """Discretize the interval [0,1] into l equal intervals"""
        Pi1=[0]*(l+1)
        Pi1[0]=Pi1[-1]=0.5/l
        for i in range(1, l):Pi1[i]=1./l
        Nl=len(Pi)-1
        Pi_=[]
        for k in range(Nl+l+1):
                Pi_+=[sum([Pi[k-m]*Pi1[m] for m in range(max(0, k-Nl), min(l, k)+1)]), ]
                print Pi_
        return Pi_
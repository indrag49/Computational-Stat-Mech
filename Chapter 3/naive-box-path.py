import math, random

X=[0.]*4
L=0.5
Beta=8.0

def gauss(sigma):
        phi=random.uniform(0, 2*math.pi)
        Upsilon=-math.log(random.uniform(0, 1))
        r=sigma*math.sqrt(2*Upsilon)
        x=r*math.cos(phi)
        y=r*math.sin(phi)
        return math.sqrt(x**2+y**2)
    
def naive_box_path(X, L, Beta):
    N=len(X)
    K=int(math.log(N, 2))
    for k in range(K):
        delk=2**k
        del_tau=Beta/delk
        for i in range(N/delk):
            j=i*delk
            k_plus=j+delk
            k_minus=j-delk
            mean=0.5*(X[k_plus-1]+X[k_minus])
            X[j]=mean+gauss(math.sqrt(2/del_tau))
            if X[j]<0 or X[j]>L:continue
        continue
    return X

j=1
while j<10:
    print X
    X=naive_box_path(X, L, Beta)
    j+=1
    

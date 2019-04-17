import random, math

def tower_sample(Pi):
        L=[0]
        K=len(Pi)
        for l in range(1, K+1): L+=[L[l-1]+Pi[l-1], ]
        Upsilon=random.uniform(0, L[-1])

        for k in range(1, len(L)+1):
                if (Upsilon>L[k-1] and  Upsilon<L[k]):
                        return k

def direct_triangle(X):
    """Length of X should be 3""" 
    Upsilon1, Upsilon2=random.uniform(0, 1), random.uniform(0, 1)
    if Upsilon1+Upsilon2>1:
        Upsilon1=1-Upsilon1
        Upsilon2=1-Upsilon2
    x=X[0][0]+Upsilon1*(X[1][0]-X[0][0])+Upsilon2*(X[2][0]-X[0][0])
    y=X[0][1]+Upsilon1*(X[1][1]-X[0][1])+Upsilon2*(X[2][1]-X[0][1])
    return [x, y]

def direct_polygon(X):
    """X is a list of vertices for a polygon with n>3 vertices"""
    n=len(X)
    s1, s2=0., 0.
    for i in range(n):
        s1+=X[i][0]
        s2+=X[i][1]
    Xc=[s1/n, s2/n]
    X+=[X[0], ]
    A=[0]*n
    for k in range(n):
        A[k]=(Xc[0]*X[k][1]+X[k][0]*X[k+1][1]+X[k+1][0]*Xc[1]-X[k][0]*Xc[1]-X[k+1][0]*X[k][1]-Xc[0]*X[k+1][1])/2.
    k=tower_sample(A)
    x=direct_triangle([Xc, X[k], X[k+1]])
    return x

def fast_deposition(R, t, L, r):
    """ box of area=L*L, radius of each identical circle=r"""
    A_tot=L**2
    A1=[]
    s=0.
    K=len(R)
    for X in range(K):
        n=len(X)
        s1, s2=0., 0.
        for i in range(n):
            s1+=X[i][0]
            s2+=X[i][1]
        Xc=[s1/n, s2/n]
        X+=[X[0], ]
        A=[0]*n
        for k in range(n):
            A[k]=(Xc[0]*X[k][1]+X[k][0]*X[k+1][1]+X[k+1][0]*Xc[1]-X[k][0]*Xc[1]-X[k+1][0]*X[k][1]-Xc[0]*X[k+1][1])/2.
        A1+=[sum(A), ]
        s+=sum(A)
    L=1-s/A_tot
    del_t=1+int(math.log(random.random())/math.log(L))
    k=tower_sample(A1)
    
    flag=0
    while True:
        p=[direct_polygon(R[k])]
        for l in range(len(R[k])):
            if min([math.sqrt((p[0]-P[0])**2+(p[1]-P[1])**2) for P in pos])>=2*radius:
                pos+=[p, ]
                flag=1
                break

        t+=1
        if flag==1:break
    return t, R

import random, math

def dist(k, l, Lx, Ly):
        dx=abs(k[0]-l[0])%Lx
        delta_x=min(dx, Lx-dx)
        dy=abs(k[1]-l[1])%Ly
        delta_y=min(dy, Ly-dy)
        return m.sqrt(delta_x**2+delta_y**2)

def gamma_cut(N, x_cut):
    x_star=1-N/x_cut
    if x_star<0: exit
    while True:
        Delta_x=-math.log(random.uniform(0,1))/x_star
        x=x_cut+Delta_x
        Upsilon_dashed=(x/x_cut)**N*math.exp(-(1-x_star)*Delta_x)
        if random.uniform(0,1)<=Upsilon_dashed: return x_cut+Delta_x

def rescale_volume(Lx, Ly, X, Beta, P, sigma):
    """x is a list of positions of N particles"""
    V=Lx*Ly
    N=len(X)
    pairs=[]
    for i in range(N-1):
            for j in range(i+1, N): pairs+=[[i, j], ]
    pos=[(random.uniform(0, Lx), random.uniform(0, Ly)) for i in range(N)]
    sigma_cut=min(dist(pos[i], pos[j], Lx, Ly) for i, j in pairs)
    x_cut=Beta*P*V*(sigma/sigma_cut)**2
    V_new=gamma_cut(N, x_cut)/(Beta*P)
    Upsilon=math.sqrt(V_new/V)
    Xnew=[]
    for i in range(N):
        Xnew+=[Upsilon*X[i], ]
    return [Upsilon*Lx, Upsilon*Ly, Xnew]
    

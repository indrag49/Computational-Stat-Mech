import random, math as m
def dist(k, l, Lx, Ly):
        """Calculates the distance between the two particles k and l. Lx and Ly are the lengths of the boundaries"""
        dx=abs(k[0]-l[0])%Lx
        delta_x=min(dx, Lx-dx)
        dy=abs(k[1]-l[1])%Ly
        delta_y=min(dy, Ly-dy)
        return m.sqrt(delta_x**2+delta_y**2)

def direct_disks_any(N, Lx, Ly):
        """N is the number of particles in a box of dimension Lx X Ly"""
        pairs=[]
        for i in range(N-1):
                for j in range(i+1, N): pairs+=[[i, j], ]
        pos=[(random.uniform(0, Lx), random.uniform(0, Ly)) for i in range(N)]
        sigma=min(dist(pos[i], pos[j], Lx, Ly) for i, j in pairs)/2.0
        eta_max=N*m.pi*sigma**2/(Lx*Ly)
        return eta_max
import random, math

L=3
N=L**2
T=2.
Pi=1-math.exp(-2.0 / T)
Nbr=[[1, 3, 2, 6], [2, 4, 0, 7], [0, 5, 1, 8],
     [4, 6, 5, 0], [5, 7, 3, 1], [3, 8, 4, 2],
     [7, 0, 8, 3], [8, 1, 6, 4], [6, 2, 7, 5]]

sigma = [random.choice([1, -1]) for k in range(N)]
def cluster_spin_glass(sigma):
    j=random.randint(1, N)
    P, C=[j-1], [j-1]
    while P != []:
        k=random.choice(P)
        for l in Nbr[k]:
            if sigma[l-1]*random.choice([1, -1])*sigma[k-1]>0 and l not in C:
                if random.uniform(0.0, 1.0)<Pi:
                    P+=[l, ]
                    C+=[l, ]
        P.remove(k)
    for j in C:
        sigma[j-1]=-sigma[j-1]
    return sigma

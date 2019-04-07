def Naive_degeneracy(Emax):
    N=[0]*(Emax+1)
    for Ex in range(Emax+1):
        for Ey in range(Emax+1):
            for Ez in range(Emax+1):
                E=Ex+Ey+Ez
                if E<=Emax:
                    N[E]+=1
    return N

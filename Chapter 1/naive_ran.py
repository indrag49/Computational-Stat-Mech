# ran(0, 1)

def naive_ran(idum):
        m=134456
        n=8121
        k=28411
        idum=(idum*n+k)%m
        ran=idum/(m*1.)
        return [idum, ran]

idum=123456
for i in range(1, 101):
        X=naive_ran(idum)
        print(i, X)
        idum=X[0]
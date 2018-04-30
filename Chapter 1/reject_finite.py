import random
import pylab
def reject_finite(Pi):
        "Pi is the collection of probabilities of all possible events"
        Pi_max=max(Pi)
        K=len(Pi)
        while True:
                k=nran(1, K)
                Upsilon=random.uniform(0, Pi_max)
                if Upsilon<=Pi[k-1]: return k-1

Z=[0.005, 0.095, 0.3, 0.5, 0.1]
print(sum(Z))
K=len(Z)
l=[]

for i in range(1, 50001):
        l+=[reject_finite(Z), ]
L=[l.count(i) for i in range(K)]

pylab.bar(range(K), L, align="center")
pylab.xlabel("k")
pylab.show()
import random
def naive_pin(N, sigma, L):
    x=[0.]*N
    for k in range(1, N+1):
        x[k-1]=random.uniform(sigma, L-sigma)
        for l in range(1, k):
            if abs(x[k-1]-x[l-1])<2*sigma: return naive_pin(N, sigma, L)
    return x

for i in range(1000):
    print(naive_pin(8, 0.4, 20))

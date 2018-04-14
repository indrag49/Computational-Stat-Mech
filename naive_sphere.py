import random
import pylab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def naive_sphere(d):
        """ d is the dimension of the unit sphere"""
        x=[0]*d
        S=0
        for k in range(d):
                x[k]=random.uniform(-1, 1)
                S+=x[k]**2
                if S>1: return naive_sphere(d)
        return x

X=[]
Y=[]
Z=[]
for i in range(5000):
        l=naive_sphere(3)
        X+=[l[0], ]
        Y+=[l[1], ]
        Z+=[l[2], ]
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.scatter3D(X, Y, Z, c=Y, cmap="Reds", s=10)
ax.set_title("naive_sphere.png (3 dimensions)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
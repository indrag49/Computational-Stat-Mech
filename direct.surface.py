import random
import math as m

def gauss(sigma):
        phi=random.uniform(0, 2*m.pi)
        Upsilon=-m.log(random.uniform(0, 1))
        r=sigma*m.sqrt(2*Upsilon)
        x=r*m.cos(phi)
        y=r*m.sin(phi)
        return [x, y]

def direct_surface(d, sigma):
        """ d is the dimension of the sphere, sigma is the standard deviation of the gaussian"""
        sigma=1./m.sqrt(d)
        S=0
        x=[0]*d
        for k in range(d):
                x[k]=gauss(sigma)[1]
                S+=x[k]**2
        for k in range(d):x[k]/=m.sqrt(S)
        return x
        
X=[]
Y=[]
Z=[]
for i in range(5000):
        l=direct_surface(3, 0.5)
        X+=[l[0], ]
        Y+=[l[1], ]
        Z+=[l[2], ]
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.scatter3D(X, Y, Z, c=X, cmap="prism_r", s=10)
ax.set_title("direct_surface.png (d=3, $\sigma$=0.5)")
ax.set_xlabel("X")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
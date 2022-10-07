from Sierpinski3dClass import *
import matplotlib.pyplot as plt
import numpy as np
import time


def random_params(n):
    assert n < 8
    params = -np.ones(8,dtype=int)
    indicies = np.random.choice(8,n,False)
    syms = np.random.choice(48,n,True)
    params[indicies] = syms
    return params

x = 7
y = 5
params = np.zeros([x,y,8],dtype = int)
for i in range(x):
    for j in range(y):
        params[i,j,:] = random_params(i+1)

#params[4,0,:] = [0,-1,-1,0,-1,0,0,-1]
iterations = [7,7,7,6,5,5,5]

sc = 5
fig, axs = plt.subplots(x,y,figsize = (sc*y,sc*x),subplot_kw={'projection': '3d'})
print(axs)
for i in range(x):
    for j in range(y):
        print(params[i,j,:])
        frac = Sierpinski3d(list(params[i,j,:]))
        cubical, c_cube = frac.cubical_complex_midpoints(iterations[i] ,color = True)
        axs[i,j].scatter(cubical[:,0],cubical[:,1],cubical[:,2],c = c_cube, s = .5)
        axs[i,j].set_xlim(-1,1)
        axs[i,j].set_ylim(-1,1)
        axs[i,j].set_zlim(-1,1)
        axs[i,j].xaxis.set_ticks(np.array([-1,0,1]))
        axs[i,j].yaxis.set_ticks(np.array([-1,0,1]))
        axs[i,j].zaxis.set_ticks(np.array([-1,0,1]))
#plt.show()
plt.savefig("random_fracs")

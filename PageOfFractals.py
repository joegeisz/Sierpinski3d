from Fractals.Sierpinski3d import Sierpinski3d
from Fractals.Utilities import random_params
import matplotlib.pyplot as plt
import numpy as np
import time

if __name__ == "__main__":

    x = 7 # number of classes
    y = 5 # number of fractals in each class
    params = np.zeros([x,y,8],dtype = int)
    for i in range(x):
        for j in range(y):
            params[i,j,:] = random_params(i+1)

    #params[4,0,:] = [0,-1,-1,0,-1,0,0,-1]
    iterations = [7,7,7,6,5,5,5]

    sc = 5
    fig, axs = plt.subplots(x,y,figsize = (sc*y,sc*x),subplot_kw={'projection': '3d'})
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

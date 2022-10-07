import time, math
import matplotlib
import matplotlib.pyplot as plt
from Sierpinski3dClass import *
import itertools
import matplotlib.animation as animation
import copy
matplotlib.use("Qt4Agg")



def gen_all_params(n):
    for i, subcubes in enumerate(itertools.combinations(range(8),n)):
        for j, symmetries in enumerate(itertools.product(range(48),repeat = n)):
            params = -np.ones(8,dtype = int)
            for k, cube in enumerate(subcubes):
                params[cube] = symmetries[k]
            yield list(params)

def random_params(n):
    assert n < 8
    params = -np.ones(8,dtype=int)
    indicies = np.random.choice(8,n,False)
    syms = np.random.choice(48,n,True)
    params[indicies] = syms
    return list(params)


def random_geometry(params):
    for i in range(8):
        if params[i] != -1:
            params[i] = np.random.choice(48)
    return params



n = 4
its = 5
s = 1
while True:
    #params = random_params(n)
    params = random_geometry([-1,-1,0,0,0,0,-1,-1])
    print(params)
    frac = Sierpinski3d(params)
    ptcld, c = frac.cubical_complex_midpoints(its ,color = True)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(ptcld[:,0],ptcld[:,1],ptcld[:,2],c = c,s = s)
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    plt.show()

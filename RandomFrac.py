import matplotlib.pyplot as plt
from Fractals.Sierpinski3d import *
from Fractals.Utilities import *
import matplotlib.animation as animation



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

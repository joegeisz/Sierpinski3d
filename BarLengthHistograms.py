from Fractals.Sierpinski3d import *
from Fractals.Utilities import random_params
import gudhi
import matplotlib.pyplot as plt
import numpy as np



if __name__ == "__main__":

    #params = [0,0,0,0,0,0,0,-1]
    params = random_params(5)
    npts = 200000

    frac = Sierpinski3d(params)
    #ptcld, c = frac.cubical_complex_midpoints(iterations ,color = True)
    ptcld, c = frac.IFS_pointcloud(npts ,color = True)

    alpha_complex = gudhi.AlphaComplex(points=ptcld)
    simplex_tree = alpha_complex.create_simplex_tree()
    pers = simplex_tree.persistence()

    lengths = [[],[],[]]
    for dim, x in pers:
        if x[1] != np.inf:
            lengths[dim].append(x[1]-x[0])

    L0 = np.array(lengths[0])
    L1 = np.array(lengths[1])
    L2 = np.array(lengths[2])

    fig, axs = plt.subplots(1,3)

    axs[0].hist(L0, bins = 100, log = True)
    axs[1].hist(L1, bins = 100, log = True)
    axs[2].hist(L2, bins = 100, log = True)


    plt.show()

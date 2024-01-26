from Fractals.Sierpinski3d import *
from Fractals.Utilities import random_params
import gudhi
import matplotlib.pyplot as plt
import numpy as np
import time


if __name__ == "__main__":

    npts = 10000
    params = [0,-1,-1,0,-1,0,0,-1]
    frac = Sierpinski3d(params)
    ptcld = frac.IFS_pointcloud(npts)

    alpha_complex = gudhi.AlphaComplex(points=ptcld)
    simplex_tree = alpha_complex.create_simplex_tree()

    # #All bars
    pers = simplex_tree.persistence()

    ns = np.arange(0.0,0.5,0.01)
    pbns = np.zeros([ns.size,3])
    rho = 0.0001
    print(rho)
    for i, n in enumerate(ns):
        if rho < n:
            bettis = simplex_tree.persistent_betti_numbers(rho,n)
            pbns[i,0] = bettis[0]
            pbns[i,1] = bettis[1]
            pbns[i,2] = bettis[2]
        else:
            pbns[i,0] = 0
            pbns[i,1] = 0
            pbns[i,2] = 0

    lines = [np.polyfit(np.ma.log(ns),np.ma.log(pbns[:,i]),1) for i in range(3)]
    plt.plot(np.ma.log(ns),np.ma.log(pbns))
    for line in lines:
        plt.plot(np.ma.log(ns), line[0]*np.ma.log(ns)+line[1])
    plt.legend([0,1,2])
    print(lines)
    plt.show()

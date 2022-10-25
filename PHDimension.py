from Fractals.Sierpinski3d import *
import gudhi
import matplotlib.pyplot as plt
import numpy as np

def Ls(params,ns):
    Ls = []
    for npts in ns:
        frac = Sierpinski3d(params)
        #ptcld, c = frac.cubical_complex_midpoints(iterations ,color = True)
        ptcld, c = frac.IFS_pointcloud(npts ,color = True)

        alpha_complex = gudhi.AlphaComplex(points=ptcld)
        simplex_tree = alpha_complex.create_simplex_tree()
        pers = simplex_tree.persistence()

        L = [0,0,0]
        for dim, x in pers:
            b = x[0]
            d = x[1]
            if d < np.inf:
                L[dim] += (d-b)

        Ls.append(L)

    Ls = np.array(Ls)
    return Ls


# def frac_dims()


if __name__ == "__main__":

    #params = [0,-1,-1,0,-1,0,0,-1]
    params = [0,0,0,0,0,0,0,-1]
    #ns = range(100,10000,200)
    #ns = [10,100,1000,10000]

    es = np.arange(3,4,0.005)
    ns = [int(10**e) for e in es]
    print(ns)

    Ls = Ls(params,ns)

    #plt.plot(ns,Ls)
    lines = [np.polyfit(np.log10(ns),np.log10(Ls[:,i]),1) for i in range(3)]
    fig, axs = plt.subplots(1,2)
    axs[0].plot(np.log10(ns),np.log10(Ls))
    axs[1].plot(ns,Ls)
    for line in lines:
        axs[0].plot(np.log10(ns), line[0]*np.log10(ns)+line[1])
    axs[0].legend([0,1,2])
    print("d0: ", lines[0][0])
    print("d1: ", lines[1][0])
    print("d2: ", lines[2][0])
    plt.show()

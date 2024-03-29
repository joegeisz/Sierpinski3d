from Fractals.Sierpinski2d import *
import gudhi
import matplotlib.pyplot as plt
import numpy as np
import time, os
from functools import partial
from multiprocessing import Pool
import pandas as pd


def Ls(params,ns):
    LL = []
    for npts in ns:
        frac = SierpinskiRelative(params)
        #ptcld, c = frac.cubical_complex_midpoints(iterations ,color = True)
        ptcld, c = frac.IFS_pointcloud(npts ,color = True)

        alpha_complex = gudhi.AlphaComplex(points=ptcld)
        simplex_tree = alpha_complex.create_simplex_tree()
        pers = simplex_tree.persistence()

        L = [0,0]
        for dim, x in pers:
            b = x[0]
            d = x[1]
            if d < np.inf:
                L[dim] += (d-b)

        LL.append(L)

    LL = np.array(LL)
    return LL

def frac_dims(ns,L):
    lines = [np.polyfit(np.log10(ns),np.log10(L[:,i]),1) for i in range(2)]
    d0 = 1.0/(1.0-lines[0][0])
    d1 = 1.0/(1.0-lines[1][0])
    return d0, d1

def plotLs(ns,L, savefig = None):
    lines = [np.polyfit(np.log10(ns),np.log10(L[:,i]),1) for i in range(2)]
    fig, axs = plt.subplots(1,2)
    axs[0].plot(np.log10(ns),np.log10(L))
    axs[1].plot(ns,L)
    for line in lines:
        axs[0].plot(np.log10(ns), line[0]*np.log10(ns)+line[1])
    axs[0].legend([0,1])
    if savefig:
        plt.savefig(savefig)
        plt.close()
    return fig


def analyze(params, ns = [10,20,30]):
    L = Ls(params,ns)
    d0, d1 = frac_dims(ns,L)
    plt_name = "PHDim_" + str(params[0]) + "_" + str(params[1]) + "_"  + str(params[2]) + ".png"
    plt_name = os.path.join("2dphdim",plt_name)
    plt_name = os.path.join("Outputs",plt_name)
    plotLs(ns,L,savefig = plt_name)
    print(params)
    return d0,d1



# def frac_dims()


if __name__ == "__main__":
    t0 = time.time()
    param_list = [[i,j,k] for i in range(8) for j in range(8) for k in range(8)]
    #param_list = [[0,0,i] for i in range(5)]
    es = np.arange(3,4,0.01)
    ns = [int(10**e) for e in es]
    func = partial(analyze,ns = ns)
    results = pd.DataFrame()
    with Pool(6) as p:
        dims = p.map(func, param_list)
    results["Parameters"] = param_list
    dims = np.array(dims)
    results["d0"] = dims[:,0]
    results["d1"] = dims[:,1]
    results.to_csv("Outputs/Results.csv")
    print("Time: ", time.time()-t0)

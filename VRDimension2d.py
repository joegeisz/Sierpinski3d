from Fractals.Sierpinski2d import *
from Fractals.Utilities import random_params
import gudhi
import matplotlib.pyplot as plt
import numpy as np
import time, os
import pandas as pd
from multiprocessing import Pool


def calc_rho(simplex_tree):
    isolated = np.zeros(simplex_tree.num_vertices())
    for simp, filt in simplex_tree.get_filtration():
        if len(simp) == 2:
            if isolated[simp[0]] == 0:
                isolated[simp[0]] = filt
            if isolated[simp[1]] == 0:
                isolated[simp[1]] = filt
    return isolated.max()


def dims(params, npts = 100000):
    # Make Filtration from point cloud
    frac = SierpinskiRelative(params)
    ptcld = frac.IFS_pointcloud(npts)
    alpha_complex = gudhi.AlphaComplex(points=ptcld)
    simplex_tree = alpha_complex.create_simplex_tree()

    # Calculate rho and range of data
    rho = calc_rho(simplex_tree)
    min_persistence = rho
    print(params,rho)
    max = 0.1
    es = np.linspace(np.log10(rho),np.log10(max),1000)[1:]
    ns = np.power(10,es)

    # Calculate persistence and get betti numbers
    pers = simplex_tree.persistence(min_persistence = rho)
    pbns = np.zeros([ns.size,2])


    for i, n in enumerate(ns):
        if rho < n:
            bettis = simplex_tree.persistent_betti_numbers(rho, n)
            pbns[i,0] = bettis[0]
            pbns[i,1] = bettis[1]
        else:
            pbns[i,0] = np.nan
            pbns[i,1] = np.nan

    # Calculate line of best fit for log log data
    lines = [np.polyfit(np.ma.log10(ns*2.0),np.ma.log10(pbns[:,i]),1) for i in range(2)]

    # return slopes
    d0 = lines[0][0]
    d1 = lines[1][0]

    fig, axs = plt.subplots(2,2,figsize = (10,10))

    axs[0,0].scatter(ptcld[:,0],ptcld[:,1], s = 0.01)

    # Plot persistence plots
    gudhi.plot_persistence_barcode(pers, legend = True, alpha = 1.0, max_intervals = 0, axes = axs[0,1])
    gudhi.plot_persistence_diagram(pers, legend = True, axes = axs[1,0])

    axs[1,1].scatter(np.ma.log10(ns*2.0),np.ma.log10(pbns[:,0]), c = 'blue', s = 0.1)
    axs[1,1].scatter(np.ma.log10(ns*2.0),np.ma.log10(pbns[:,1]), c = 'red', s = 0.1)
    #plt.plot(np.ma.log10(ns),np.ma.log10(pbns))
    for line in lines:
        axs[1,1].plot(np.ma.log10(ns*2.0), line[0]*np.ma.log10(ns*2.0)+line[1])

    axs[1,1].legend([0,1])
    fig.savefig(os.path.join("Outputs/2dvrdim", "VRDim_Analysis_" + str(params[0]) + "_" + str(params[1]) + "_"  + str(params[2]) + ".png"))
    plt.close()



    return d0, d1

if __name__ == "__main__":

    param_list = [[i,j,k] for i in range(8) for j in range(8) for k in range(8)]
    #param_list = [[0,0,i] for i in range(5)]
    #param_list = [[0,0,0]]
    func = dims
    results = pd.DataFrame()
    with Pool(6) as p:
        dims = p.map(func, param_list)
    #print(dims(param_list[0]))
    results["Parameters"] = param_list
    dims = np.array(dims)
    results["d0"] = dims[:,0]
    results["d1"] = dims[:,1]
    results.to_csv("Outputs/VRResults.csv")

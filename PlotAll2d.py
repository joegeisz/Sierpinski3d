from Fractals.Sierpinski2d import *
import matplotlib.pyplot as plt
import numpy as np
import time, os
from functools import partial
from multiprocessing import Pool


def plot(params,ifs_points = 100000, outputfolder = "Outputs/2dFractals"):
    """Plots the fractal and saves it to outputfolder"""
    frac = SierpinskiRelative(params)
    ifs, c_ifs = frac.IFS_pointcloud(ifs_points,  color = True)
    fig = plt.figure(figsize = (5,5))
    ax = fig.add_subplot()
    ax.scatter(ifs[:,0],ifs[:,1],c = c_ifs,s = .01)
    ax.axis('equal')
    filename = os.path.join(outputfolder,"Sierpinski2d_" + str(params[0]) + "_" + str(params[1]) + "_"  + str(params[2]) + ".png")
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    t0 = time.time() # timing

    # Make a complete list of all possible parameters for relatives
    param_list = [[i,j,k] for i in range(8) for j in range(8) for k in range(8)]

    # Plot each one, using multiprocessing to speed it up
    with Pool(5) as p:
        print(p.map(plot, param_list))

    print("Time: ", time.time()-t0) # timing

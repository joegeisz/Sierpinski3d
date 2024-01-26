from Fractals.Sierpinski2d import *
import gudhi
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Polygon
import numpy as np


if __name__ == "__main__":

    # Parameters to visualize
    params = [0,0,1] # which fractal
    npts = 2000 # number of IFS points
    frames = 100 # frames
    filt_start_stop = [0, 0.2] #filtration interval

    # Create pointcloud and compute filtration
    frac = SierpinskiRelative(params)
    ptcld = frac.IFS_pointcloud(npts)
    alpha_complex = gudhi.AlphaComplex(points=ptcld)
    simplex_tree = alpha_complex.create_simplex_tree()
    pers = simplex_tree.persistence()

    # Get lists of edges and triangles
    lines = []
    lines_filt = []
    triangles = []
    tris_filt = []
    for sim, filt in simplex_tree.get_filtration():
        if len(sim) == 1:
            pass
        elif len(sim) == 2:
            lines.append(np.array([ptcld[sim[0]],ptcld[sim[1]]]))
            lines_filt.append(filt)
        elif len(sim) == 3:
            triangles.append(np.array([ptcld[sim[0]],ptcld[sim[1]],ptcld[sim[2]]]))
            tris_filt.append(filt)
        else:
            print("Cant plot simplices with dim > 2")

    # Setup plot
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_aspect('equal', adjustable='box')
    ax.scatter(ptcld[:,0],ptcld[:,1], s = 10)

    # function to update image
    def func(frame):
        i = 0
        filt = 0.0
        ax.set_title(str(frame))
        while filt < frame:
            if filt > frame - (filt_start_stop[1]-filt_start_stop[0])/frames:
                ax.plot(lines[i][:,0],lines[i][:,1],color = "blue")
            i += 1
            filt = lines_filt[i]
        i = 0
        filt = 0.0
        while filt < frame:
            if filt > frame - (filt_start_stop[1]-filt_start_stop[0])/frames:
                ax.add_patch(Polygon(triangles[i],color= [0,0,1,0.5]))
            i += 1
            filt = tris_filt[i]

    # animate frames
    ani = animation.FuncAnimation(fig, func, np.arange(filt_start_stop[0],filt_start_stop[1],(filt_start_stop[1]-filt_start_stop[0])/frames), repeat=False)
    plt.show()

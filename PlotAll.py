from Fractals.Sierpinski3d import Sierpinski3d
from Fractals.Utilities import gen_all_params
import itertools
import matplotlib.animation as animation
import time, math
import matplotlib.pyplot as plt

def main():
    numframes = 1000
    gen = gen_all_params(4)
    params = next(gen)
    frac = Sierpinski3d(list(params))
    ptcld, c = frac.cubical_complex_midpoints(6 ,color = True)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    scat, = ax.plot(ptcld[:,0],ptcld[:,1],ptcld[:,2], linestyle="", marker="*")
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)

    ani = animation.FuncAnimation(fig, update_plot, frames=range(numframes),
                                  fargs=(gen,scat),blit = False)
    plt.show()

def update_plot(i, params_gen,scat):
    params = next(params_gen)
    frac = Sierpinski3d(list(params))
    ptcld, c = frac.cubical_complex_midpoints(6 ,color = True)
    print(params)
    scat.set_data(ptcld[:,0],ptcld[:,1])
    scat.set_3d_properties(ptcld[:,2])

main()

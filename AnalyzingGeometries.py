import numpy as np
from Fractals.Sierpinski3d import *
from Fractals.Symmetries import *

def transform_by_O(i,ptcld):
    transform = O(i).transform()
    tptcld = ptcld.copy()
    for i in range(tptcld.shape[0]):
        tptcld[i,:] = transform.apply(tptcld[i,:])
    return tptcld


geometries = [
    [0,-1,-1,-1,-1,-1,-1,-1], #1
    [0,0,-1,-1,-1,-1,-1,-1], #2,1
    [0,-1,-1,0,-1,-1,-1,-1], #2,2
    [0,-1,-1,-1,-1,-1,-1,0], #2,3
    [0,0,0,-1,-1,-1,-1,-1], #3,1
    [0,0,-1,-1,-1,-1,-1,0], #3,2
    [0,-1,-1,0,-1,-1,0,-1], #3,3
    [0,0,0,0,-1,-1,-1,-1], #4,1
    [0,0,0,-1,0,-1,-1,-1], #4,4
    [0,0,0,-1,-1,0,-1,-1], #4,3
    [0,0,0,-1,-1,-1,-1,0], #4,2
    [0,0,-1,-1,-1,-1,0,0], #4,5
    [0,-1,-1,0,-1,0,0,-1], #4,6
    [-1,-1,-1,0,0,0,0,0], #5,1
    [-1,-1,0,0,0,0,0,-1], #5,2
    [-1,0,0,-1,0,0,-1,0], #5,3
    [-1,0,0,0,0,0,0,0], #7
    ]

for params in geometries:
    frac = Sierpinski3d(list(params))
    ptcld, _ = frac.cubical_complex_cube_corners(0)
    ptcld = np.unique(ptcld,axis = 0)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(ptcld[:,0],ptcld[:,1],ptcld[:,2])
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    plt.show()

    number_symmetries = 0
    for i in range(48):

        tptcld = transform_by_O(i,ptcld)
        numsame = 0

        for pt1 in tptcld:
            for pt2 in ptcld:
                if (pt1 == pt2).all():
                    numsame += 1

        if numsame == ptcld.shape[0]:
            #print("This is a symmetry",i)
            number_symmetries += 1

    print("Total symmetries: ", number_symmetries)

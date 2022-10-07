import time, math
import matplotlib
import matplotlib.pyplot as plt
from Sierpinski3dClass import *
import itertools
import matplotlib.animation as animation
import copy
matplotlib.use("Qt4Agg")



def gen_all_params(n):
    for i, subcubes in enumerate(itertools.combinations(range(8),n)):
        for j, symmetries in enumerate(itertools.product(range(48),repeat = n)):
            params = -np.ones(8,dtype = int)
            for k, cube in enumerate(subcubes):
                params[cube] = symmetries[k]
            yield list(params)



shifts = np.ones((8,3))

for i,cube in enumerate(range(8)):
    if cube%2 == 1:
        shifts[i,0] = -1
    if (cube//2)%2 == 1:
        shifts[i,1] = -1
    if (cube//4)%2 == 1:
        shifts[i,2] = -1

print(shifts)

mats = []
for i in range(48):
    mats.append(O(i).rotation_matrix())

invs = np.zeros(48,dtype = int)
for i, Oi in enumerate(mats):
    for j, Oj in enumerate(mats):
        res = np.matmul(Oi,Oj)
        if (res == np.eye(3)).all():
            invs[i] = j
            break

n = 2
for params in gen_all_params(n):
    print(params)
    frac = Sierpinski3d(params)
    relevant_params = []
    for p in params:
        if p != -1:
            relevant_params.append(p)
    for di in range(48):
        rotated_params = -np.ones(8,dtype=int)
        print("\n\n Rotation: ", di)
        for l, transform_index in enumerate(zip(frac.transforms,relevant_params)):
            T, p = transform_index
            Tp = copy.deepcopy(T)
            Tp.matrix = 2*np.matmul(O(di).rotation_matrix(),T.matrix)
            Tp.matrix = np.matmul(Tp.matrix,O(invs[di]).rotation_matrix())
            #print("Matrix number" , l, ":\n ", Tp.matrix)
            for j, mat in enumerate(mats):
                if (mat == Tp.matrix).all():
                    #print("Element ", j)
                    break

            Tp.shift = 2*np.matmul(O(di).rotation_matrix(),T.shift)
            #print("Shift " , l, ":\n ", Tp.shift)
            for k, shift in enumerate(shifts):
                if (shift == Tp.shift).all():
                    #print("Subcube ", k)
                    break
            rotated_params[k] = j
        print(rotated_params)
        rotated = Sierpinski3d(list(rotated_params))
        ptcld, c = rotated.cubical_complex_midpoints(4 ,color = True)
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(ptcld[:,0],ptcld[:,1],ptcld[:,2],c = c)
        ax.set_xlim(-1,1)
        ax.set_ylim(-1,1)
        ax.set_zlim(-1,1)
        plt.show()

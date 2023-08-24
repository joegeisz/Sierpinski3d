import numpy as np
from itertools import permutations, combinations, product
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.transforms import Affine2D

class transformation:
    def __init__(self,matrix,vector):
        self.matrix = matrix
        self.shift = vector

    def __repr__(self):
        return "\nMatrix: " + str(self.matrix) + "\nShift: " + str(self.shift)

    def apply(self,vec):
        return np.matmul(self.matrix,vec) + self.shift


class square_symmetry():
    def __init__(self,i):
        arr = np.eye(2)
        perms = list(permutations(arr))
        arr = np.array(perms[i//4])
        if i%2 == 1:
            arr[:,0] = -arr[:,0]
        if (i//2)%2 == 1:
            arr[:,1] = -arr[:,1]
        self.matrix = arr
        self.transform = transformation(self.matrix, np.zeros(2))

    def visualize(self):
        fig, [ ax1, ax2 ]   = plt.subplots(1,2)
        ax1.set_xlim(-1,1)
        ax1.set_ylim(-1,1)
        ax1.set_aspect(1)

        ax2.set_xlim(-1,1)
        ax2.set_ylim(-1,1)
        ax2.set_aspect(1)

        r1 = Rectangle((-.75,-.75),.5,1.5)
        r2 = Rectangle((-.75,-.75),1.0,.5)
        mat = np.eye(3)
        mat[:2,:2] = self.matrix
        trans = Affine2D(mat) + ax2.transData
        r3 = Rectangle((-.75,-.75),.5,1.5, transform = trans)
        #r3 = Rectangle((-.75,-.75),.5,1.5)#, transform = trans)
        r4 = Rectangle((-.75,-.75),1.0,.5, transform = trans)
        #r4 = Rectangle((-.75,-.75),1.0,.5)#, transform = trans)
        ax1.add_patch(r1)
        ax1.add_patch(r2)
        ax2.add_patch(r3)
        ax2.add_patch(r4)
        plt.show()


class O:
    def __init__(self,i):
        assert i >= 0
        assert i < 48
        self.i = i

    def rotation_matrix(self):
        i = self.i
        arr = np.eye(3)
        perms = list(permutations(arr))
        arr = np.array(perms[i//8])
        if i%2 == 1:
            arr[:,0] = -arr[:,0]
        if (i//2)%2 == 1:
            arr[:,1] = -arr[:,1]
        if (i//4)%2 == 1:
            arr[:,2] = -arr[:,2]
        return arr

    def is_inversion(self):
        if np.linalg.det(self.rotation_matrix()) == -1:
            return True
        else:
            return False

    def transform(self):
        return transformation(self.rotation_matrix(),np.array([0,0,0]))

    def visualize(self):
        fig, ax = plt.subplots(1,2,subplot_kw={'projection': '3d'})
        cube = np.array([[1,1,1],[-1,1,1],[1,-1,1],[1,1,-1],[-1,-1,1],[1,-1,-1],[-1,1,-1],[-1,-1,-1]])
        cube_T = np.zeros_like(cube)
        for i,c in enumerate(cube):
            cube_T[i,:] = self.transform().apply(c)
        ax[0].scatter(cube[:,0],cube[:,1],cube[:,2],c = range(len(cube)),cmap = 'Paired',s=100)
        ax[1].scatter(cube_T[:,0],cube_T[:,1],cube_T[:,2],c = range(len(cube)),cmap = 'Paired',s=100)
        plt.show()

import numpy as np

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

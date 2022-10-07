import numpy as np
from itertools import permutations, combinations, product
import matplotlib.pyplot as plt

class transformation:
    def __init__(self,matrix,vector):
        self.matrix = matrix
        self.shift = vector

    def __repr__(self):
        return "\nMatrix: " + str(self.matrix) + "\nShift: " + str(self.shift)

    def apply(self,vec):
        return np.matmul(self.matrix,vec) + self.shift


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



class Sierpinski3d:
    def __init__(self,params):
        assert len(params) == 8

        #Number of non-empty subcubes
        self.num = 8 - params.count(-1)

        #Set IFS transforms
        self.transforms = []
        for i, p in enumerate(params):
            assert p >= -1
            if p >= 0:
                self.transforms.append(self.get_transformation(p,i))

    def get_transformation(self,o_index,cube):
        el = O(o_index)
        matrix = el.rotation_matrix()
        shift = np.array([1,1,1])
        if cube%2 == 1:
            shift[0] = -1
        if (cube//2)%2 == 1:
            shift[1] = -1
        if (cube//4)%2 == 1:
            shift[2] = -1
        return transformation(0.5*matrix,0.5*shift)


    def IFS_pointcloud(self, num_pts, ip = np.array([0,0,0]), head = 100, color = False):
        rand_func = np.random.randint(0,self.num,num_pts + head)
        pt_list = []
        last_pt = ip
        for i in rand_func:
            next_pt = self.transforms[i].apply(last_pt)
            pt_list.append(next_pt)
            last_pt = next_pt
        if color == True:
            color_list = []
            last_color = np.array([0,0,0])
            for i in rand_func:
                next_color = 0.5*(last_color + (self.transforms[i].shift + 0.5*np.array([1,1,1])))
                color_list.append(next_color)
                last_color = next_color
            return np.array(pt_list)[head:,:], np.array(color_list)[head:,:]
        return np.array(pt_list)[head:,:]


    def cubical_complex_filtered(self,iterations):
        c_complex = np.full((pow(2,iterations+1),pow(2,iterations+1),pow(2,iterations+1)),np.inf)
        points = np.array([t.shift for t in self.transforms])
        tmp_pts = points + np.array([0.5,0.5,0.5])
        indicies = tmp_pts.astype(int)
        for j in indicies:
            k = pow(2,iterations)
            c_complex[k*j[0]:k*(j[0]+1),k*j[1]:k*(j[1]+1),k*j[2]:k*(j[2]+1)] = iterations

        for i in range(iterations):
            new_points = []
            for pt in points:
                for transform in self.transforms:
                    new_point = transform.apply(pt)
                    new_points.append(new_point)
            points = np.array(new_points)
            factor = pow(2,i+1)
            tmp_pts = points*factor + np.array([factor-.5,factor-.5,factor-.5])
            indicies = tmp_pts.astype(int)
            for j in indicies:
                k = pow(2,iterations-i-1)
                c_complex[k*j[0]:k*(j[0]+1),k*j[1]:k*(j[1]+1),k*j[2]:k*(j[2]+1)] -= 1

        return c_complex

    def cubical_complex_midpoints(self,iterations,color = False):
        points = np.array([t.shift for t in self.transforms])
        for i in range(iterations):
            new_points = []
            for pt in points:
                for transform in self.transforms:
                    new_point = transform.apply(pt)
                    new_points.append(new_point)
            points = np.array(new_points)
        if color == True:
            colors = np.array([t.shift + 0.5*np.array([1,1,1]) for t in self.transforms])
            for i in range(iterations):
                new_colors = []
                for cl in colors:
                    for transform in self.transforms:
                        new_color = 0.5*(cl + (transform.shift + 0.5*np.array([1,1,1])))
                        new_colors.append(new_color)
                colors = np.array(new_colors)
            return points,colors

        return points

    def cubical_complex_cube_corners(self,iterations,color = False):
        points = np.array([t.shift for t in self.transforms])
        for i in range(iterations):
            new_points = []
            for pt in points:
                for transform in self.transforms:
                    new_point = transform.apply(pt)
                    new_points.append(new_point)
            points = np.array(new_points)

        full_points = np.zeros((points.shape[0]*8,points.shape[1]))
        corners = np.array(list(product([-1,1],repeat=3)))
        for i, corner in enumerate(corners):
            full_points[i*points.shape[0]:(i+1)*points.shape[0],:] = points + (corner*pow(.5,iterations+1))

        full_colors = None
        if color == True:
            colors = np.array([t.shift + 0.5*np.array([1,1,1]) for t in self.transforms])
            for i in range(iterations):
                new_colors = []
                for cl in colors:
                    for transform in self.transforms:
                        new_color = 0.5*(cl + (transform.shift + 0.5*np.array([1,1,1])))
                        new_colors.append(new_color)
                colors = np.array(new_colors)

            full_colors = np.zeros((colors.shape[0]*8,colors.shape[1]))
            for i, corner in enumerate(corners):
                full_colors[i*colors.shape[0]:(i+1)*colors.shape[0],:] = colors

        return full_points, full_colors



if __name__ == "__main__":
    frac = Sierpinski3d([0,-1,-1,0,-1,0,0,-1])
    ptcld, c = frac.cubical_complex_midpoints(4 ,color = True)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(ptcld[:,0],ptcld[:,1],ptcld[:,2],c = c)
    plt.show()

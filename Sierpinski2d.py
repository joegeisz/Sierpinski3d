import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations, combinations, product
from Sierpinski3dClass import transformation

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


class SierpinskiRelative():

    def __init__(self,params):
        assert len(params) == 3

        self.transforms = []
        for i, p in enumerate(params):
            sym = self.get_transformation(i,p)
            self.transforms.append(sym)

    def get_transformation(self,i,p):
        sym = square_symmetry(p)
        if i == 0:
            shift = np.array([-1,-1])
        if i == 1:
            shift = np.array([-1,1])
        if i == 2:
            shift = np.array([1,-1])
        matrix = 0.5*sym.matrix
        shift = 0.5*shift
        return transformation(matrix,shift)

    def IFS_pointcloud(self, num_pts, ip = np.array([0,0]), head = 100, color = False):
        rand_func = np.random.randint(0,3,num_pts + head)
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
                next_color = 0.5*(last_color + (np.array([self.transforms[i].shift[0],self.transforms[i].shift[1],0]) + 0.5*np.array([1,1,1])))
                color_list.append(next_color)
                last_color = next_color
            return np.array(pt_list)[head:,:], np.array(color_list)[head:,:]
        return np.array(pt_list)[head:,:]





def s1(x,y):
    return x/2, y/2

def s2(x,y):
    return (x+1)/2, y/2

def s3(x,y):
    return x/2, (y+1)/2

def symmetry(i):
    arr = np.eye(2)
    perms = list(permutations(arr))
    arr = np.array(perms[i//4])
    if i%2 == 1:
        arr[:,0] = -arr[:,0]
    if (i//2)%2 == 1:
        arr[:,1] = -arr[:,1]
    return arr

def transform(pt,s,i):
    mat = symmetry(i)
    pt = pt - 0.5
    pt = np.matmul(pt,mat)
    pt = pt + 0.5
    if s == 0:
        return s1(pt[0],pt[1])
    if s == 1:
        return s2(pt[0],pt[1])
    if s == 2:
        return s3(pt[0],pt[1])
    else:
        raise "Nope"

def ptcloud(a,b,c,numpts = 50000):
    IFS = [a,b,c]
    ip = np.array([0,0.5])
    n = 50000
    pts = np.zeros([n,2])
    for i in range(n):
        pts[i,:] = ip
        sym = np.random.randint(3)
        ip[0], ip[1] = transform(ip,sym,IFS[sym])
    return pts

if __name__=="__main__":
    # Draw Sierpinski Gasket
    pts = ptcloud(0,0,0)

    fig1, ax1 = plt.subplots()
    ax1.set_aspect('equal')
    ax1.scatter(pts[10:,0],pts[10:,1],s=.5)
    plt.show()

    #Draw 4 random

    fig2, axs = plt.subplots(1,4,figsize = (16,4))
    for ax in axs:
        pts = ptcloud(np.random.randint(8),np.random.randint(8),np.random.randint(8))
        ax.set_aspect('equal')
        ax.scatter(pts[10:,0],pts[10:,1],s=.5)
    plt.show()

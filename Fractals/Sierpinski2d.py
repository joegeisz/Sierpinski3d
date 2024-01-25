import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations, combinations, product
from .Symmetries import *

class SierpinskiRelative():
    """
    SierpinskiRelative represents a fractal created similarly to the sierpinski gasket. It is 
        specified by 3 parameters, representing elements of the dihedral symmetry group, here thought
        of as the symmetries of the square. 
    """
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




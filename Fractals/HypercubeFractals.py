import numpy as np
import math 

class HypercubeFractalReport:
    """Reports facts about the Hypercube Fractals in a given dimension"""
    def __init__(self,dim):
        self.dim = dim 
        self.subcubes = 2**dim 
        self.groupElements = 2**dim*np.math.factorial(dim)
        self.totalFracs = (self.groupElements+1)**self.subcubes
        self.totalFracsInteresting = self.totalFracs - 1 - (self.groupElements)**self.subcubes
        print("In dimension %i" % dim)
        print("A %i dimensional hypercube is made up of %i sub-hypercubes" % (dim, self.subcubes))
        print("The hyper-octahedral group of dimension %i has %i elements in it" % (dim, self.groupElements))
        print("There are %i possible parameter values" % self.totalFracs)
        print("Eliminating the zero and %i subsets, that is %i" % (self.subcubes,self.totalFracsInteresting))

    def subsets(self):
        for i in range(1,self.subcubes):
            self.subset(i)

    def subset(self, i):
        print("For a fractal with %i IFS functions" % i)
        print("There will be %i possible attractors" % self.groupElements**i)
        print("But dividing by the total symmetries there are %i remaining" % self.groupElements**(i-1))
        print("The fractal dimension of this subset will be %f" % (math.log(i)/math.log(2)))
        print("\n")


class HypercubeFractal:
    """Any-dimensional analog of the Sierpinski Relatives"""
    def __init__(self,dim,params):
        pass
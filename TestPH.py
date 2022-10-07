import gudhi
import matplotlib.pyplot as plt
import numpy as np
import time

def plot_filt(pts,filt):
    plt.figure()
    ptarr = np.array(pts)
    plt.scatter(ptarr[:,0],ptarr[:,1])
    for simplex, val in filt:
        if len(simplex)==1:
            pass
        if len(simplex) == 2:
            plt.plot(ptarr[simplex,0],ptarr[simplex,1],c='green')
            plt.pause(0.01)
        else:
            t = plt.Polygon(ptarr[simplex,:])
            plt.gca().add_patch(t)
            plt.pause(0.01)
    plt.show()



gudhi.persistence_graphical_tools._gudhi_matplotlib_use_tex=False
#pts = [[1, 1], [7, 0], [4, 6], [9, 6], [0, 14], [2, 19], [9, 17]]
#pts = np.random.rand(100,2)
#'''
times = []
ns = range(10,100000,5000)
#ns = [100]
for n in ns:
    t1 = time.time()
    randangle = np.random.rand(n)*2*3.141592
    randrad = np.random.rand(n)*.5+2
    pts = np.transpose([np.multiply(np.sin(randangle),randrad),np.multiply(np.cos(randangle),randrad)])
    #'''
    alpha_complex = gudhi.AlphaComplex(points=pts)

    simplex_tree = alpha_complex.create_simplex_tree()
    result_str = 'Alpha complex is of dimension ' + repr(simplex_tree.dimension()) + ' - ' + \
        repr(simplex_tree.num_simplices()) + ' simplices - ' + \
        repr(simplex_tree.num_vertices()) + ' vertices.'
    print(result_str)
    times.append(time.time()-t1)
    #fmt = '%s -> %.2f'
    #for filtered_value in simplex_tree.get_filtration():
        #print(fmt % tuple(filtered_value))

plt.plot(ns,times)
plt.show()

#gudhi.plot_persistence_barcode(simplex_tree.persistence(), legend = True)
gudhi.plot_persistence_diagram(simplex_tree.persistence(), legend = True)
#plot_filt(pts,simplex_tree.get_filtration())

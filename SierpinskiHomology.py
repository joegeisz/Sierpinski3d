from Sierpinski3dClass import *
import gudhi
import matplotlib.pyplot as plt
import numpy as np
import time


def random_params(n,seed = None):
    assert n < 8
    if seed is not None:
        np.random.seed(seed)
    params = -np.ones(8,dtype=int)
    indicies = np.random.choice(8,n,False)
    syms = np.random.choice(48,n,True)
    params[indicies] = syms
    return list(params)

if __name__ == "__main__":
    '''
    gudhi.persistence_graphical_tools._gudhi_matplotlib_use_tex=False
    i = j = 5
    fig,axs = plt.subplots(i,j,figsize = (10,10),subplot_kw={'projection':'3d'})
    for x in range(i):
        for y in range(j):
            randparams = np.random.randint(0,48,4)
            randparams = np.concatenate((randparams,[-1,-1,-1,-1]))
            np.random.shuffle(randparams)
            frac = Sierpinski3d(list(randparams))
            ptcld, c = frac.cubical_complex_midpoints(3 ,color = True)
            axs[x,y].scatter(ptcld[:,0],ptcld[:,1],ptcld[:,2],c = c)
    plt.show()




    '''
    iterations = 5
    params = random_params(7,seed = 0)
    #params = random_params(3)
    print(params)
    frac = Sierpinski3d(params)
    ptcld, c = frac.cubical_complex_midpoints(iterations ,color = True)
    #print(ptcld)


    alpha_complex = gudhi.AlphaComplex(points=ptcld)
    simplex_tree = alpha_complex.create_simplex_tree()

    # #All bars
    pers = simplex_tree.persistence()
    #gudhi.plot_persistence_barcode(pers, legend = True, alpha = 1.0)
    #gudhi.plot_persistence_diagram(pers, legend = True)
    #
    # #One dimension at a time
    simplex_tree.compute_persistence()
    # pers = simplex_tree.persistence_intervals_in_dimension(2)
    # gudhi.plot_persistence_barcode(pers, legend = False, alpha = 1.0)
    # gudhi.plot_persistence_diagram(pers, legend = False)


    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(ptcld[:,0],ptcld[:,1],ptcld[:,2],c = c)

    ns = np.arange(0.0,0.05,0.001)
    bns = np.zeros([ns.size,3])
    for i, n in enumerate(ns):
        bettis = simplex_tree.persistent_betti_numbers(n,n)
        bns[i,0] = bettis[0]
        bns[i,1] = bettis[1]
        bns[i,2] = bettis[2]

    fig2,axs = plt.subplots(3,1)
    axs[0].plot(ns,bns[:,0])
    axs[1].plot(ns,bns[:,1])
    axs[2].plot(ns,bns[:,2])
    fig2.suptitle("Betti Numbers")


    pbns = np.zeros([ns.size,3])
    rho = np.sqrt(3)*(0.5)**(iterations+4)
    print(rho)
    #rho = 0.1
    for i, n in enumerate(ns):
        if rho < n:
            bettis = simplex_tree.persistent_betti_numbers(rho,n)
            pbns[i,0] = bettis[0]
            pbns[i,1] = bettis[1]
            pbns[i,2] = bettis[2]
        else:
            pbns[i,0] = 0
            pbns[i,1] = 0
            pbns[i,2] = 0

    fig3,axs3 = plt.subplots(3,1)
    axs3[0].plot(ns,pbns[:,0])
    axs3[0].plot([rho,rho],[0,pbns[:,0].max()])

    axs3[1].plot(ns,pbns[:,1])
    axs3[1].plot([rho,rho],[0,pbns[:,1].max()])

    axs3[2].plot(ns,pbns[:,2])
    axs3[2].plot([rho,rho],[0,pbns[:,2].max()])
    fig3.suptitle("Persistent Betti Numbers")

    fig4,axs4 = plt.subplots(3,1)
    axs4[0].plot(np.ma.log(ns),np.ma.log(pbns[:,0]))
    axs4[0].plot(np.ma.log([rho,rho]),np.ma.log([0,pbns[:,0].max()]))

    axs4[1].plot(np.ma.log(ns),np.ma.log(pbns[:,1]))
    axs4[1].plot(np.ma.log([rho,rho]),np.ma.log([0,pbns[:,1].max()]))

    axs4[2].plot(np.ma.log(ns),np.ma.log(pbns[:,2]))
    axs4[2].plot(np.ma.log([rho,rho]),np.ma.log([0,pbns[:,2].max()]))
    fig4.suptitle("Persistent Betti Numbers loglog")

    plt.show()


    '''
    #frac = Sierpinski3d([0,-1,-1,0,-1,0,0,-1])
    frac = Sierpinski3d([-1,0,0,0,0,0,0,0])

    cc_eps = frac.cubical_complex(5)
    cc = gudhi.CubicalComplex(top_dimensional_cells = cc_eps)
    pers = cc.persistence()
    gudhi.plot_persistence_barcode(pers, legend = True)
    gudhi.plot_persistence_diagram(pers, legend = True)
    ptcld, c = frac.IFS_pointcloud(10000, color = True)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(ptcld[:,0],ptcld[:,1],ptcld[:,2],c = c)
    plt.show()
    '''

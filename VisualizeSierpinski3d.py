from Fractals.Sierpinski3d import Sierpinski3d
import matplotlib.pyplot as plt


if __name__ == "__main__":
    
    # Set parameters
    params = [0,-1,-1,0,-1,0,0,-1] # Sierpinski Tetrahedron
    #params = [0,2,21,-1,-1,-1,9,-1]
    #params = [0, -1, 0, 0, 0, 0 , 0, 0] # Dense fractal
    iterations = 4
    ifs_points = 10000

    # Create Fractal
    frac = Sierpinski3d(params)
    cubical, c_cube = frac.cubical_complex_midpoints(iterations ,color = True)
    ifs, c_ifs = frac.IFS_pointcloud(ifs_points,  color = True)

    # Plot points representing midpoints of cubical complex
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(cubical[:,0],cubical[:,1],cubical[:,2],c = c_cube)
    plt.show()

    # Plot random IFS points
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(ifs[:,0],ifs[:,1],ifs[:,2],c = c_ifs)
    plt.show()

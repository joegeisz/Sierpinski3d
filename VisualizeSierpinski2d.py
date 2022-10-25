from Fractals.Sierpinski2d import SierpinskiRelative
import matplotlib.pyplot as plt


if __name__ == "__main__":

    # Set parameters
    params = [0,7,1]
    ifs_points = 10000

    # Create Fractal
    frac = SierpinskiRelative(params)
    ifs, c_ifs = frac.IFS_pointcloud(ifs_points,  color = True)

    # Plot random IFS points
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(ifs[:,0],ifs[:,1],c = c_ifs)
    plt.show()

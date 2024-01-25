from Fractals.Sierpinski2d import SierpinskiRelative
import matplotlib.pyplot as plt

# Set the parameters for the Sierpinski Relative
params = [0,0,0]
num_pts = 100000

# Create the points using the IFS/Chaos Game
frac = SierpinskiRelative(params)
ifs, c_ifs = frac.IFS_pointcloud(num_pts,  color = True)

# Plot the points
fig = plt.figure(figsize = (5,5))
ax = fig.add_subplot()
ax.scatter(ifs[:,0],ifs[:,1],c = c_ifs,s = .01)
ax.axis('equal')
plt.show()
# Import the class
import kmapper as km
from Sierpinski3dClass import *
import numpy as np

#params = [0,-1,-1,0,-1,0,0,-1]
#params = [0,2,21,-1,-1,-1,9,-1]
#params = [0,-1,0,0,0,0,0,0]
params = [0,-1,0,-1,47,-1,0,0]

ifs_points = 10000

frac = Sierpinski3d(params)
data, c_ifs = frac.IFS_pointcloud(ifs_points,  color = True)

# Initialize
mapper = km.KeplerMapper(verbose=1)

# Fit to and transform the data
projected_data = mapper.fit_transform(data, projection=[0,1,2]) # X-Y axis

# Create a cover with 10 elements
cover = km.Cover(n_cubes=10)

# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(projected_data, data, cover=cover)

#help(mapper.visualize)
# Visualize it
mapper.visualize(graph,
                color_values = np.append(data,np.ones([len(data),1]),1),
                color_function_name = ('x value','y value','z value',"ones"),
                #color_values = data[:,0],
                #color_function_name = 'x value',
                node_color_function = ("mean", "sum"),
                path_html="Mapper/Sierpinski4_3.html",
                 title="Sierpinski 3d")


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(data[:,0],data[:,1],data[:,2],c = c_ifs)
plt.show()

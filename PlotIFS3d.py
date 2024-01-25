from Fractals.Sierpinski3d import Sierpinski3d
import matplotlib.pyplot as plt

params = [0,0,0,-1,-1,0,0,-1]
num_pts = 10000

frac = Sierpinski3d(params)
ptcld, c = frac.IFS_pointcloud(num_pts, color = True)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(ptcld[:,0],ptcld[:,1],ptcld[:,2],color = c)
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(-1,1)

plt.show()

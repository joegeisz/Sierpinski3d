import time, math
import matplotlib.pyplot as plt
from Sierpinski3dClass import *

params = [0,0,0,-1,-1,0,0,-1]

frac = Sierpinski3d(params)
ptcld, c = frac.cubical_complex_midpoints(6 ,color = True)

backcol = 'black'

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(ptcld[:,0],ptcld[:,1],ptcld[:,2],color = c)

# fig.patch.set_facecolor(backcol)
# plt.axis('off')
# ax.set_facecolor(backcol)
# ax.grid(False)
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])
# ax.xaxis.pane.fill = False
# ax.yaxis.pane.fill = False
# ax.zaxis.pane.fill = False
# ax.xaxis.pane.set_edgecolor(backcol)
# ax.yaxis.pane.set_edgecolor(backcol)
# ax.zaxis.pane.set_edgecolor(backcol)

ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(-1,1)
plt.show()

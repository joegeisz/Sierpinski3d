import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 4)
v = np.linspace(0, np.pi, 4)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
print(x.shape,y.shape,z.shape)
print(x)

x = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
y = -x
z = x
ax.plot_surface(x, y, z)

plt.show()

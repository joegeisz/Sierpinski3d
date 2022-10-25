from Fractals.Sierpinski3d import *

params = [0,-1,-1,0,-1,0,0,-1]
iterations = 5
frac = Sierpinski3d(params)

# Create Fractal
frac = Sierpinski3d(params)
cubical, c_cube = frac.cubical_complex_midpoints(iterations ,color = True)

# Plot points representing midpointd of cubical complex
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(cubical[:,0],cubical[:,1],cubical[:,2],c = c_cube)
ax.set_title("F(0,-1,-1,0,-1,0,0,-1)")
plt.savefig("Tetrahedron.png")

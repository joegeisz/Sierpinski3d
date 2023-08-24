import gudhi
import numpy as np

pts = np.array([[0.0,0.0],[0.0,1.0],[0.5,0.0]])
alpha_complex = gudhi.AlphaComplex(points=pts)
simplex_tree = alpha_complex.create_simplex_tree()
pers = simplex_tree.persistence()

print(alpha_complex)
print(simplex_tree.dimension(),simplex_tree.num_simplices(), simplex_tree.num_vertices())
for i in simplex_tree.get_filtration():
    print(i)
print(pers)

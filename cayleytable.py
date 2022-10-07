from Sierpinski3dClass import *
import numpy as np


table = np.zeros((48,48))
print(table.shape)

mats = []
for i in range(48):
    mats.append(O(i).rotation_matrix())

for i, Oi in enumerate(mats):
    for j, Oj in enumerate(mats):
        res = np.matmul(Oi,Oj)
        for k, O in enumerate(mats):
            if (res == O).all():
                table[i,j] = k
                break

invs = np.zeros(48)
for i, Oi in enumerate(mats):
    for j, Oj in enumerate(mats):
        res = np.matmul(Oi,Oj)
        if (res == np.eye(3)).all():
            invs[i] = j
            break

print(invs)
plt.imshow(table)
plt.show()

from Fractals.Symmetries import *
import numpy as np
import pandas as pd

param_list = [[i,j,k] for i in range(8) for j in range(8) for k in range(8)]
sym = square_symmetry(4)
df = pd.DataFrame()
invs = []
for param in param_list:
    inv = [0,0,0]
    inv0mat = np.matmul(np.matmul(sym.matrix, square_symmetry(param[0]).matrix),sym.matrix)
    inv2mat = np.matmul(np.matmul(sym.matrix, square_symmetry(param[1]).matrix),sym.matrix)
    inv1mat = np.matmul(np.matmul(sym.matrix, square_symmetry(param[2]).matrix),sym.matrix)
    #print(inv0mat)#,inv1mat,inv2mat)
    for i in range(8):
        mat = square_symmetry(i).matrix
        #print(mat)
        if np.array_equal(inv0mat, mat):
            inv[0] = i
        if np.array_equal(inv1mat, mat):
            inv[1] = i
        if np.array_equal(inv2mat, mat):
            inv[2] = i
    invs.append(inv)

df["Parameters"] = param_list
df["Reflection"] = invs
df.to_csv("Outputs/2dSymmetrics.csv")

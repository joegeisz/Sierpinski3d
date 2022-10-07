import numpy as np

def random_params(n):
    assert n < 8
    params = -np.ones(8,dtype=int)
    indicies = np.random.choice(8,n,False)
    syms = np.random.choice(48,n,True)
    params[indicies] = syms
    return list(params)

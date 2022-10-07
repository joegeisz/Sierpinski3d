import numpy as np

def random_params(n):
    assert n < 8
    params = -np.ones(8,dtype=int)
    indicies = np.random.choice(8,n,False)
    syms = np.random.choice(48,n,True)
    params[indicies] = syms
    return list(params)


def gen_all_params(n):
    for i, subcubes in enumerate(itertools.combinations(range(8),n)):
        for j, symmetries in enumerate(itertools.product(range(48),repeat = n)):
            params = -np.ones(8,dtype = int)
            for k, cube in enumerate(subcubes):
                params[cube] = symmetries[k]
            yield params

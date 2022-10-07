import numpy as np

number_symmetries = np.array([
    48/6,
    48**2/4 + 48**2/4 + 48**2/12,
    48**3/2 + 48**3/2 + 48**3/6,
    48**4/8 + 48**4/2 + 48**4/2 + 48**4/6 + 48**4/8 + 48**4/24,
    48**5/2 + 48**5/2 + 48**5/6,
    48**6/4 + 48**6/4 + 48**6/12,
    48**7/6 ],dtype = int)
print(number_symmetries)
print(number_symmetries.sum())

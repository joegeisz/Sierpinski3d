import numpy as np

def b(k):
    a = 91*pow(7,k)/24
    b = 27*pow(3,k)/8
    c = 7/12
    return a-b+c

for k in range(30):
    print(b(k))

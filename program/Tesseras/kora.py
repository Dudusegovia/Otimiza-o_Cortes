from numba import cuda, njit
import numpy as np
@njit(target_backend='cuda')
def soma(a):
    for k in range(1000):
        a[k]+=1
        
a = np.ones(1000)

soma(a)
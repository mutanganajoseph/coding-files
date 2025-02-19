import numpy as np 

A = np.array([
    [2,3],
    [3,2],
    [4,-2]
])

B = np.array([1,1,1])

det_A = np.linalg.norm(A)
print(A.shape)
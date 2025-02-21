import numpy as np

A = np.array([
    [2, 3, 3],
    [3, 2, -5],
    [4, -2, 3]
])

B =[1, 1]
B.append(2)

# Append B as a new row to A
A = np.vstack([A, B])

#append new element
# A = np.append(A, 2)

print(A)

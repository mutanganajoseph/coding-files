import numpy as np 

A = np.array([1,2,3])
B = np.array([-1,3,2])

matrix_a = np.array([[1,2,3],[4,5,6]])

matrix_b = np.array([[7,8],[9,10],[11,12]])

magnitude_a = np.linalg.norm(A)
dotProduct_ab = np.dot(A,B)
crossProduct_ab = np.cross(A,B)
matrixProduct = np.dot(matrix_a, matrix_b)

print(f"Magnitude of A = {magnitude_a}")
print(f"Dot product of A and B = {dotProduct_ab}\nCroos product of A and B = {crossProduct_ab}\nMatrix Product = \n{matrixProduct}")



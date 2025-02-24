import numpy as np 

A = np.array([1,2,3])
B = np.array([4,5,6])
C = np.array([7,8,9])


matrix_a = np.array([[1,2,3],[4,5,6]])

matrix_b = np.array([[7,8],[9,10],[11,12]])

magnitude_a = np.linalg.norm(A)
magnitude_b = np.linalg.norm(B)
dotProduct_ab = np.dot(A,B)
dot = sum([x*y for x,y in zip(A,B)])
crossProduct_ab = np.cross(A,B)
crossProduct_ac = np.cross(A,C)
crossProduct_bc = np.cross(B,C)

matrixProduct = np.dot(matrix_a, matrix_b)

area_ab = np.linalg.norm(crossProduct_ab)
area_ac = np.linalg.norm(crossProduct_ac)
area_bc = np.linalg.norm(crossProduct_bc)

surface_area = area_ab+area_ac+area_bc


volume = abs(np.dot(A, np.cross(B,C)))

print(f"Area of paralleralpiped is {surface_area:.1f}")
print(f"Volume of paralleralpiped is {volume:.1f}")
print(f"Magnitude of A = {magnitude_a:.1f}")
print(f"Magnitude of A = {magnitude_b:.1f}")
print(f"Dot product of A and B = {dot}\nDot product of A and B = {dotProduct_ab}\nCroos product of A and B = {crossProduct_ab}\nMatrix Product = \n{matrixProduct}")



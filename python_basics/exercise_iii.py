import numpy as np


area_of_paralelogram = lambda v, u: np.linalg.norm(np.cross(v, u))


volume_of_parallelopiped = lambda u, v, w: abs(np.dot(u, np.cross(v, w)))


u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
w = np.array([7, 8, 9])


area = area_of_paralelogram(u, v)
volume = volume_of_parallelopiped(u, v, w)

print(f"Parallelogram Area: {area:.2f}")
print("Parallelepiped Volume:", volume)

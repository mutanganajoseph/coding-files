import numpy as np 
cross = lambda v, u: np.linalg.norm(np.cross(u,v))


u = np.array([3,-2,1])
v = np.array([1,4,3])

dotProduct_uv = sum([x*y for x,y in zip(u,v) ])

sum = u+v
mult = u*v
print(f"{dotProduct_uv}\n{sum}\n{mult}")
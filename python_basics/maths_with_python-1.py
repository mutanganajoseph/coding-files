# Operations on vectors
# Tuples, Lists and dictionaries

# 1. Tuples
tuple1 = (1, -3.5, 7.8, 10.9)
tuple2 = (-5.9, 10.7, 1.414)
# Concatenation of tuples
print(tuple1 + tuple2)

# Get the length of tuples
print(len(tuple1))

# Create a tuple from a string
tuesday = tuple("Tuesday")

# 2. Lists
list1 = [0.2, 5.6, 100, 5.7]
list2 = [-2.5, 4.78, 5.23, 100]

# Concatenate lists
print(list1 + list2)

# Accessing tuple elements (by indices)
print(list2[3])

# Sum of 2 vectors stored as lists
list12 = [x + y for x, y in zip(list1, list2)]
print(list12)

# Scalar product - use a loop
list1sc = [x * 10 for x in list1]  # Multiplying by 10
print(list1sc)

# Vector product
dl1l2 = sum([x * y for x, y in zip(list1, list2)])
print(dl1l2)

# Vectors
v1 = [0.2, 10.4, 5.6]
v2 = [1.5, 7.5, 5.3]

# Cross product
cv1v2 = [
    v1[1] * v2[2] - v1[2] * v2[1],
    v1[2] * v2[0] - v1[0] * v2[2],
    v1[0] * v2[1] - v1[1] * v2[0],
]
print(cv1v2)

# Verify cross product
print(sum([x * y for x, y in zip(cv1v2, v1)]))  # Must be close to 0

# ND array using numpy library

# Copying arrays
# Syntax --> newArray = oldArray.copy()

import numpy as np

# N-Dimensional
# Matrix - 2-dimensional
# Vector - 1-dimensional
# Point - 0-dimensional

# Defining lists as nd arrays

print(np.cross())

v1array = np.array([0.2, 10.4, 5.6])
v2array = np.array([1.5, 7.5, 5.3])
print(v1array)

# Cross product
cpv1v2 = np.cross(v1, v2)
print(cpv1v2)

# + operation gives vector addition
print(v1array + v2array)


# Angle betweeen vectors
# In Radians
v1v2angle_in_rad = np.arccos(
    v1array @ v2array / ((np.linalg.norm(v1array)) * (np.linalg.norm(v2array)))
)
# In degrees
v1v1angle_in_deg = v1v2angle_in_rad * 180 / np.pi

# Lambda function
f = lambda x: np.sqrt(1 + x**2) / np.exp(x)
print(f(0))  # Outputs 1, f(1), f(2) and so on...

# Lambda function for obtaining the dot product
v1array @ v2array  # Dot product by numpy

dotProductLambdaFunction = (
    lambda v1array, v2array: v1array @ v2array
)  # Lambda functions will only work with nd arrays
dotl1l2 = dotProductLambdaFunction(np.array(l1), np.array(l2))

# Lambda function to find the angle between 2 vectors
angleLambdaFunction = (
    lambda A, B: np.arccos((A @ B) / (np.linalg.norm(A) * np.linalg.norm(B)))
    * 180
    / np.pi
)

anglel1l2 = angleLambdaFunction(np.array(l1), np.array(l2))


# method writing in python
def angleab(A, B):
    numerator = A @ B
    denominator = np.linalg.norm(A) * np.linalg.norm(B)
    angleRad = np.arccos(numerator / denominator)
    angleDeg = angleRad * 180 / np.pi
    return {rad: angleRad, deg: angleDeg}


print(angleab(np.array(l1), np.array(l2)))

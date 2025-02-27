
import numpy as np 
import itertools

A = (1,2,3,1)


jumps = 0
for i in range(len(A)-1):
    
    for j in range(i+1, len(A)):
        if A[i] > A[j]:
            jumps +=1
    if jumps % 2 == 0:
        sign = "+"

    else:
        sign = "-"
print(A, jumps, sign)

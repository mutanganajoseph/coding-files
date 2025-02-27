
import numpy as np 
import itertools



n = int(input("Enter a Number: "))
numbers = list(range(1, n+1))
perms = list(itertools.permutations(numbers))
jumps = 0
for perm in perms:

    for i in range(len(perm)-1):
        
        for j in range(i+1, len(perm)):
            if perm[i] > perm[j]:
                jumps +=1

    if jumps % 2 == 0:
        sign = "+"
    else:
        sign = "-"

print(jumps, sign)


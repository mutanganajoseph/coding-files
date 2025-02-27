
import numpy as np 
import itertools

n = int(input("Enter A Number: "))

numbers = list(range(1, n+1))
perms = list(itertools.permutations(numbers))
count=0

print(perms)

# for perm in perms:
#     count+=1
#     jump=0
#     sign = "+"
#     for i in range(len(perm) - 1):
#         if perm[i] > perm[i+1]:
#             jump +=1
#             if jump % 2 == 0:
#                 sign = "+"
#             else:
#                 sign = "-"

#     print(f"Permutation {count} is {perm} | Jumps {jump} | Sign {sign}")


import itertools
import math
import os

try:
    n = int(input("\n\nEnter a number to get permutations: "))

    if n <= 0:
        print(f"\nThere is No Permutation for n <= 0,  {n}.")

    if n <= 7 and n > 0:
        numbers = list(range(1, n + 1))
        permutations = list(itertools.permutations(numbers))
        print(f"\nHere is {math.factorial(n)} Permutations.\n")

        original_order = numbers  # [1, 2, 3, ..., n]

        # Iterate through all permutations
        for perm in permutations:
            jumps = 0  # Initialize jump counter
            perm_list = list(perm)  # Convert tuple to list for easier manipulation
            visited = [False] * n  # To track which elements have been already checked

            # Count jumps by detecting cycles in the permutation
            for i in range(n):
                if visited[i] or perm_list[i] == original_order[i]:
                    continue  # Skip if the element is already visited or in the correct place
                
                # Cycle detection
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = perm_list.index(original_order[j])  # Move to the next index in the cycle
                    cycle_size += 1
                
                # If cycle size is greater than 1, it's a jump
                if cycle_size > 1:
                    jumps += cycle_size - 1  # A cycle of size k means k-1 jumps

            # Determine the sign based on the number of jumps
            jump_sign = "+" if jumps % 2 == 0 else "-"

            print(f"{perm} | Jumps: {jumps} | Sign of Jumps: {jump_sign}")

    if n > 7:
        print("\nThe Number You Enter is Very Large. Try n>0 , n<=7\n")

except ValueError:
    _ = os.system("clear")
    print("\nInvalid Input.\n")

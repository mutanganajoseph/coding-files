

import numpy as np
A = np.empty((0, 3), int)  
def get_row(row_number):
    while True:
        try:
            
            row = input(f"Enter 3 elements for row {row_number} (separated by spaces): ")
            
            
            row = list(map(int, row.split()))
            
            
            if len(row) == 3:
                return np.array(row)
            else:
                print("Error: Please enter exactly 3 elements for this row.")
        except ValueError:
            print("Error: Please enter valid integers separated by spaces.")



for i in range(1, 4):
    row = get_row(i)
    A = np.vstack([A, row])  



print("\nMatrix A:")
print(A)
det = np.linalg.det(A)
print(f"\nThe determinant of A is: {det}")
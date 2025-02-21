import numpy as np

# Initialize an empty array for A
A = np.empty((0, 3), int)  # Start with an empty array with 3 columns

# Function to prompt user for a row with 3 elements
def get_row(row_number):
    while True:
        try:
            # Ask the user to enter 3 elements for the row
            row = input(f"Enter 3 elements for row {row_number} (separated by spaces): ")
            
            # Convert the input string into a list of integers
            row = list(map(int, row.split()))
            
            # Check if the row has exactly 3 elements
            if len(row) == 3:
                return np.array(row)
            else:
                print("Error: Please enter exactly 3 elements for this row.")
        except ValueError:
            print("Error: Please enter valid integers separated by spaces.")


for i in range(1, 4):
    row = get_row(i)
    A = np.vstack([A, row])  # Append the row to A using vstack


print("\nMatrix A:")
print(A)


det = np.linalg.det(A)
print(f"\nThe determinant of A is: {det}")

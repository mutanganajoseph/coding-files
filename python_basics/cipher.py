import numpy as np

def hill_cipher_encrypt(message, matrix):
    # Convert letters to numbers (A=0, B=1, ..., Z=25)
    message = message.upper().replace(" ", "")  # Ensure uppercase and no spaces
    if len(message) % 2 == 1:
        message += "X"  # Padding with 'X' if odd length

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_to_num = {letter: i for i, letter in enumerate(alphabet)}
    num_to_letter = {i: letter for i, letter in enumerate(alphabet)}

    # Convert message to number pairs
    num_message = [letter_to_num[char] for char in message]
    
    # Reshape into 2-row vectors
    num_message = np.array(num_message).reshape(-1, 2).T  # Shape (2, n)

    # Encrypt using matrix multiplication
    matrix = np.array(matrix)
    encrypted_nums = np.dot(matrix, num_message) % 26  # Mod 26

    # Convert back to letters
    encrypted_text = "".join(num_to_letter[num] for num in encrypted_nums.T.flatten())

    return encrypted_text

# Given matrix
matrix = [[1, -1], [-5, 2]]

# Encrypt "RESEARCH"
message = "RESEARCH"
encrypted_message = hill_cipher_encrypt(message, matrix)
print("Encrypted Message:", encrypted_message)

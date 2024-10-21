import os

def count_text_file(file_path):
    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            lines = file.readlines()  # Read all lines in the file
            
            line_count = len(lines)  # Count the number of lines
            word_count = 0  # Initialize word count
            character_count = 0  # Initialize character count

            # Iterate through each line to count words and characters
            for line in lines:
                words = line.split()  # Split the line into words
                word_count += len(words)  # Count the words in the line
                character_count += len(line)  # Count characters in the line

        # Display the counts
        print(f"\nNumber of lines: {line_count}")
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {character_count}\n")

    except FileNotFoundError:
        print(f"\nThe file '{file_path}' was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Print the current working directory
print("\nCurrent Working Directory:", os.getcwd())

file_name = input("\nEnter the path to the text file: ")
count_text_file(file_name)

marks = 0

print("\n\nWelcome to the quiz! \n")

# Question 1
print("What is the sum of 20 + 20?")
print("1. 30")
print("2. 20")
print("3. 40")
while True:
    choice = input("> ")

    if choice == "1":
        print("1. Incorrect!, Correct answer is 3.\n")
        break
    elif choice == "2":
        print("2. Incorrect!, Correct answer is 3.\n")
        break
    elif choice == "3":
        print("3. Correct!\n")
        marks += 2
        break
    else:
        print("Wrong Choice! Please enter 1, 2, or 3.")

# Question 2
print("What is the subtract of 50 - 30?")
print("1. 30")
print("2. 20")
print("3. 40")
while True:
    choice = input("> ")

    if choice == "1":
        print("1. Incorrect!, Correct answer is 2.\n")
        break
    elif choice == "2":
        print("2. Correct!\n")
        marks += 2
        break
    elif choice == "3":
        print("3. Incorrect!, Correct answer is 2.\n")
        break
    else:
        print("Wrong Choice! Please enter 1, 2, or 3.")

print(f"\nYour marks: {marks}\n")

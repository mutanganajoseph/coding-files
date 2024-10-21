secret_number = 4
max_attempts = 3

while True:
    attempts = max_attempts
    while attempts > 0:
        guess = int(input("Guess the number: "))
        if guess == secret_number:
            print("You won the task!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Incorrect! You have", attempts, "attempt(s) remaining.")
            else:
                print("You failed the task!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes" and play_again !="y":
        break
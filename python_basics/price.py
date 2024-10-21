

while True:
    print("Choose an option:")
    choice = input("A. Buy Tomatoes, B. Buy Rice, C. Calculator, F. Factorize number, Q. Quit: ")

    if choice.upper() == "A":
        print("You're going to buy tomatoes")
        price = float(input("Enter price: "))
        kg = float(input("How many KG: "))
        total = price * kg 
        print("Total price of tomatoes:", total)
        print("DONE!!")
    elif choice.upper() == "B":
        print("You're going to buy rice")
        price = float(input("Enter price: "))
        kg = float(input("How many KG: "))
        total = price * kg
        print("Total price of rice:", total)
        print("DONE!!")
    elif choice.upper() == "C":
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            print("Result:", num1, "+", num2, "=", num1 + num2)
        elif operator == '-':
            print("Result:", num1, "-", num2, "=", num1 - num2)
        elif operator == '*':
            print("Result:", num1, "*", num2, "=", num1 * num2)
        elif operator == '/':
            if num2 != 0:
                print("Result:", num1, "/", num2, "=", num1 / num2)
            else:
                print("Cannot divide by zero!")
        else:
            print("Invalid operator!")
    elif choice.upper() == "F": 
        while True:
            num = int(input("Enter number to factorize: "))
            factorial = 1
            if num < 0:
                print("Factorial does not exist for negative numbers")
            elif num == 0:
                print("The factorial of 0 is 1")
            else:
                for i in range(1, num + 1):
                    factorial = i * factorial
                print("The factorial of", num, "is", factorial)
            
            cont = input("Do you want to factorize another number? (yes/no): ")
            if cont.lower() != "yes":
                break
    elif choice.upper() == "Q":
        print("Exiting...")
        break
    else:
        print("Invalid input. Please choose A, B, C, F, or Q.")
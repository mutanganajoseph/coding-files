airtel_balance = 2000
mtn_balance = 2500

choice = input(">")

if choice.upper() == "*182#":
    print("1. MTN")
    print("2. AIRTEL")
    choice = input(">")

    if choice.upper() == "1":
        print("1. Send Money")
        print("2. Buy")
        print("3. Bank Services")
        print("4. Pay Bill")
        print("5. My MoMo Account")
        print("6. Stop")
        choice = input(">")

        if choice.upper() == "1":
            number = input("Enter number start with (078/079): ")
            if not number.startswith(("078", "079")):
                print("Invalid Number! Number should start with 078 or 079.")
            elif len(number) != 10:
                print("Invalid Number! Number should be exactly 10 digits long.")
            else:
                amount = float(input("Enter amount to send: "))
                if amount > mtn_balance:
                    print("Insufficient Balance!")
                elif amount < 1:
                    print("Invalid amount!")
                else:
                    pin = int(input("Enter pin: "))
                    if pin != 12345:
                        print("Invalid PIN!")
                    else:
                        mtn_balance -= amount
                        recipient_masked_number = number[:3] + '*' * 4 + number[-3:]  # Masking the middle digits
                        print(f"You have sent an amount of {amount}FRW to {recipient_masked_number}. Your new balance is {mtn_balance}FRW.")
                
    elif choice.upper() == "2":
        print("1. Send Money")
        print("2. Buy")
        print("3. Bank Services")
        print("4. Pay Bill")
        print("5. My Airtel Account")
        print("6. Stop")
        choice = input(">")

        if choice.upper() == "1":
            number = input("Enter number start with (072/073): ")
            if not number.startswith(("072", "073")):
                print("Invalid Number! Number should start with 072 or 073.")
            elif len(number) != 10:
                print("Invalid Number! Number should be exactly 10 digits long.")
            else:
                amount = float(input("Enter amount to send: "))
                if amount > airtel_balance:
                    print("Insufficient Balance!")
                elif amount < 1:
                    print("Invalid amount!")
                else:
                    pin = int(input("Enter pin: "))
                    if pin != 1234:
                        print("Invalid PIN!")
                    else:
                        airtel_balance -= amount
                        recipient_masked_number = number[:3] + '*' * 4 + number[-3:]  # Masking the middle digits
                        print(f"You have sent an amount of {amount}FRW to {recipient_masked_number}. Your new balance is {airtel_balance}FRW.")

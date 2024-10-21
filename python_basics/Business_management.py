import os
import time
import sys
from colorama import init, Fore


DARK_GREEN = '\033[38;5;22m'  
DARK_BLACK = '\033[38;5;232m'
DARK_RED = '\033[38;5;124m'
DARK_GREEN = '\033[38;5;22m'
DARK_YELLOW = '\033[38;5;178m'
DARK_BLUE = '\033[38;5;32m'
DARK_MAGENTA = '\033[38;5;125m'
DARK_CYAN = '\033[38;5;44m'
DARK_WHITE = '\033[38;5;231m'
RESET = '\033[0m'

DARK_BLACK_BG = '\033[48;5;232m'   # Dark Black
DARK_RED_BG = '\033[48;5;124m'     # Dark Red
DARK_GREEN_BG = '\033[48;5;22m'    # Dark Green
DARK_YELLOW_BG = '\033[48;5;178m'   # Dark Yellow
DARK_BLUE_BG = '\033[48;5;32m'     # Dark Blue
DARK_MAGENTA_BG = '\033[48;5;125m'  # Dark Magenta
DARK_CYAN_BG = '\033[48;5;44m'     # Dark Cyan
DARK_WHITE_BG = '\033[48;5;231m'   # Dark White


UNDERLINE = '\033[4m'



def clear():
    _=os.system("clear")

def current_balance():
    print (f"{DARK_YELLOW}Your current balance is {balance:.2f}FRW {RESET}")

def get_current_time():
    return time.strftime("%d/%m/%Y %H:%M:%S")


def print_uppercase(message):
    print(f"{DARK_BLUE}\n{message.upper()}{RESET}\n")

def Start_business():
    global message
    global balance
    global stock
    global name_of_business
    balance = 0
    message = []
    stock = []


    print_uppercase("Welcome to business zone! we help you to start your business You should start by naming your business.")
    
    while True:
        name_of_business = input(f"\n{Fore.YELLOW}Name your business: ").strip()
        
        if not name_of_business:
            clear()
            print(f"{DARK_RED}Business must have a name!{RESET}")
            continue  # Restart the loop

        message.append(f"{get_current_time()} You created a business called {name_of_business}.")
        add_goods()
        break  # Exit the loop once the business is named

def add_goods():
    clear()
    while True:
        list_items = input(f"\n{DARK_WHITE}What would you like to add in stock of {name_of_business}?: ").strip().upper()
        if not list_items:
             clear()
             print(f"{DARK_RED}Item cannot be empty. Please add a valid item.")
             continue
        
        if list_items in stock:
            clear()
            print(f"\n{DARK_RED}{list_items} already exist!{RESET}")
            continue
        
        if list_items:  # Check if input is not empty
            stock.append(list_items)
            message.append(f"{get_current_time()} You added '{list_items}' to the stock.")
        else:
            print(f"{DARK_RED}Item cannot be empty. Please add a valid item.")
        clear()
        while True:

            
            choice = input(f"\n{DARK_BLUE}Do you want to add more items to stock? (Y/N): ").lower()
            if choice == "y":
                clear()
                break # Stay in the loop to add more items
            elif choice == "n":
                clear()
                goods()  # Call the menu function to proceed
                return  # Exit the loop
            else:
                clear()
                print(f"\n{Fore.RED}Invalid choice! Please enter Y or N.")



def stocks():
    clear()
    while True:
        print(f"{UNDERLINE}{Fore.GREEN}\nStock statement:{RESET}\n")
        if stock:
            for index, entry in enumerate(stock, start=1):  # Start numbering from 1
                print(f"{Fore.WHITE}{index}. {entry}")
            choice = input("\nDo you want to clear Stock Y/N or press 'A' to add item in the stock. to remove item in stock press 'R': ").lower()
            if choice == "y":
                if stock:
                    stock.clear()
                    clear()
                    choice = input(f"\n{DARK_GREEN}Stock cleared succefully. would you like to add items in stock? Y/N or 'M' back to menu:{RESET} ").lower()                    
                    if choice == "y":
                        add_goods()
                    elif choice== "m":
                        clear()
                        menu()  
                    else:
                        clear()
                        goods()
                else:
                    choice = input(f"\n{DARK_WHITE}Nothing to  clear. would you like to add items in stock? Y/N: {RESET}").lower()

                    if choice == "y":
                        add_goods()
                    else:
                        clear()
                        goods()            
            elif choice == "n":
                    clear()
                    menu()
            elif choice == "a":
                add_goods()
            elif choice =="r":
                remove_item()
            else:
                clear()
                print(f"{DARK_RED}Invalid input!{RESET}")     
        else:
            choice = input(f"\n{DARK_BLUE}No items in stock. would you like to add items in stock? Y/N:{RESET} ").lower()
            if choice == "y":
                add_goods()
            else:
                clear()
                goods()  

def remove_item():
    clear()
    while True:
        print(f"{UNDERLINE}{DARK_RED}Deletion process:\n{RESET}")
        if stock:
            for index, entry in enumerate(stock, start=1):
                print(f"{DARK_WHITE}{index}. {entry}{RESET}")
            choice = input("\nEnter item you want to remove: ").upper()

            if choice.isdigit():
                index = int(choice) - 1  # Convert to zero-based index
                if 0 <= index < len(stock):
                    choice = stock[index]  # Get the actual item from stock
                    stock.remove(choice)
                    clear()
                    print(f"\n{DARK_YELLOW}'{choice}' Removed succefully!{RESET}")
                    message.append(f"{get_current_time()} '{choice}' was removed from stock.")
                    break
            else:
                clear()
                print(f"\n{DARK_RED}Item does not exist! Please select a valid number.{RESET}")

def messages():
    clear()
    while True:
         print(f"\n{UNDERLINE}{DARK_GREEN}Messages:\n{RESET}")
         if message:
             for entry in message:
                 print(entry)
             choice = input(f"{DARK_WHITE}\n1. Back\n2. Creal messages\n\n> ").lower()
             if choice == "1":  
                clear()             
                menu()
             elif choice == "2":
                message.clear()
                clear()
                print(f"\n{DARK_GREEN}Message cleared succefully!")
                continue
             else:
                 clear()
                 print(f"{DARK_RED}Invalid input!{RESET}")
         else:
                clear()
                choice =input("No messages available press 'M' back to menu: ").lower()
                if choice == "m":
                   clear()
                   menu()


def edit_name():
     clear()
     global name_of_business
     while True:
        new_bussiness_name = input(f"{DARK_WHITE}Enter new name of your business: ")
        if new_bussiness_name == name_of_business:
            clear()
            print(f"{new_bussiness_name} is Already the name of you business!\n")
            continue
        else:
            name_of_business = new_bussiness_name
            message.append(f"{get_current_time()} Name of business changed to '{new_bussiness_name}'.")
            clear()
            print(f"{DARK_GREEN}Name changed successfully!{RESET}")
            menu()
                    
def menu():
    
    while True:
        print(f"\n{UNDERLINE}{DARK_GREEN}{name_of_business} Status: {RESET}\n")
        choice = input(f"{Fore.WHITE}1. Stock\n2. Message\n3. Edit name of your business\n4. Back to your goods.\n5. Balance\n\n{RESET}> ").strip().lower()
        
        if choice == "1":
            stocks()
        elif choice == "2":
            messages()
        elif choice == "3":
            edit_name()    
        elif choice == "4":
            clear()
            goods()
        elif choice=="5":
            clear()
            current_balance()
            continue
        else:
            clear()
            print(f"\n{DARK_RED} Wrong choice! Please select a valid option.{RESET}\n")

def goods():
    global balance
    while True:
        print(f"\n{UNDERLINE}{DARK_GREEN}{name_of_business} available goods.{RESET}\n")
        if stock:
            for index, item in enumerate(stock, start=1):  # Start numbering from 1
                print(f"{Fore.WHITE}{index}. {item}")
                
            choice = input(f"{Fore.BLUE}\nSelect an item by number or check Menu by pressing 'M': {RESET}").strip()
            
            if choice.upper() == "M":
                clear()
                menu()
                continue
            if choice.upper() =="EXIT":
                sys.exit()
            
            # Check if the input is a digit and within range
            if choice.isdigit():
                index = int(choice) - 1  # Convert to zero-based index
                if 0 <= index < len(stock):
                    choice = stock[index]  # Get the actual item from stock
                else:
                    clear()
                    print(f"\n{DARK_RED}Item does not exist! Please select a valid number.{RESET}")
                    continue
            else:
                clear()
                print(f"\n{DARK_RED}Invalid input! Please enter a valid input.{RESET}")
                continue
            
            # Now we can proceed with selling the item
    
            while True:
                try:

                    cost = float(input(f"\nHow much is {choice} per Kilo?: "))
                    if cost <= 0:
                        clear()
                        print(f"{DARK_RED}Cost must be greater than 0!{RESET}")
                        continue
                except ValueError:
                        clear()
    
                        print(f"\n{DARK_RED}Invalid input! Please enter numeric values{RESET}.")
                        continue

                while True:
                    try:
                        kg = float(input(f"\nHow many kilos of {choice} do you want?: "))
                        if kg <= 0:
                            clear()
                            print(f"{DARK_RED}\nKilos cannot be less than or equal to 0!{RESET}")
                            continue
                        else:
                            total = cost * kg
                            balance += total
                            clear()
                            print(f"\n{DARK_YELLOW}{get_current_time()} You sold {kg} kilos of {choice} at a cost of {cost} per Kg. Your new balance is {balance:.2f} FRW.")
                            message.append(f"{get_current_time()} You sold {kg} kilos of {choice} at a cost of {cost} FRW per Kg. Your new balance is {balance:.2f} FRW.")
                            goods()  # Exit the inner selling loop
                    except ValueError:
                        clear()
                        print(f"\n{DARK_RED}Invalid input! Please enter numeric values.{RESET}")
                        continue

           

        else:
            choice = input(f"{DARK_RED}No goods available. Would you like to add some goods (Y/N): ").lower()
            if choice == "y":
                add_goods()
            else:
                clear()
                print("You don't have goods in stock!")


Start_business()
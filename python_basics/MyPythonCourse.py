import os
import time
#money = float(input("money in FRW"))
#Rwf = money / 1000print(f"In USD ${Rwf}")
#money = float(input("money in USD "))
#USD = money * 1000print(f" In RWf{USD}")

#index name =('Joseph')print (name[:0])

#amount_house = 1000000 
#is_good_credit = False 
#if is_good_credit: 
   #discount = 0.1 
  # discounted = amount_house * 0.1 
 #  amount_house = amount_house *  (1-discount) 
#else:
  # discount = 0.2 discounted = amount_house * 0.2 
 #  amount_house = amount_house * (1-discount) 
#print(f'Discount was {discount * 100}%[{discounted}]  Amount to pay is ${amount_house}')
#name= ('joe') print(name.upper())

#name = ('Mutangana') 
#print('mu' in name)

#i = 1 
#while i <= 5: 
 #   print('*' * i)
#    i +=1 
#print('Done')

#name = input('Enter your name \n\n>')

#if len(name) < 3:
   # print("\n\nName is to short ")
#elif len(name) > 50:
   # print('\n\nMaximum chracter of name is 50')
#else:
   # print('\n\nName looks good ')

#started = False


#while True:
   # command = input("\n> ").upper()


    #if command == "HELP":
       # print("""\n\n 
       # Press Start to start the car 
       # Press stop to stop the car
       # Press Quit to exit
       # \n\n""")
    #elif command == "START":
       # if not started:
         #   print("\nCar started\n")
           # started= True
        #else:
           #     print("\nCar already started")
    #elif command == "STOP":
        #if started:
         #   print("\nCar stopped \n")
         #   started = False
        #else:
          #      print("\ncar already stopped\n")
    #elif command == "QUIT":
      #  print("\n\nExiting...\n")
       # break
    #else:
       # print("\nI do not understand use Help to get support\n")    


#prices = [10,20,30]



#for loop
#total = 0
#for price in prices:
   # total += price
#print(f"Total :{total}")



# nested loop
#for x in range (3):
 #   for y in range (2):
  #      print(f"({x}, {y})")
       
#numbers = [5 , 2 , 5 , 2 , 2]
#for x_count in numbers:
   # print (x_count * 'X')


#numbers = [2, 3, 8 ,9, 3, 2,4 , 2 ]

#max = numbers[0]

#for number in numbers:
 #   if number > max:
  #      max = number
        
#print(f"Larger number is {max}")
#numbers.append(10)
#print(numbers)
#print(numbers.index(9))# to print an index of number
#print(numbers.count(2)) # to count how many numbers of 2 in the lis
#numbers.sort()
#print(f"sorted number{numbers}")
#numbers.reverse()
#print(f"reversed number {numbers}")
#numbers.pop() #to remove last number in the list
#print(numbers)
#numbers.remove(9)
#print(numbers)
#numbers.clear()
#print(numbers)

#uniques = []
#for number in numbers:
   #if number not in uniques:
      #uniques.append(number)
#print (uniques)

#tuple list you can not add ,remove, clear or pop 
#numbers = (3,2,4,6)
#print(numbers[3])

# cordinates featers in  python

#cordinates = [1,2,3,]
#x,y,z = cordinates
#cordinates = x * y * z
#print(y)
#print(cordinates)

#Dictionaly 

#customer = {
   #"name": "Mutangana",
  # "Age" : 22,
  # "phone" : 101,
#}

#print(customer.get("name", "!" ))

#phone = input("Phone: ")
#translate = {
 #  "1": "One",
 ##  "2": "Two",
  # "3": "Three",
  # "4": "Four",
  # "5": "Five",
  # "6": "Six",
  # "7": "Seven",
  # "8": "Eight",
  # "9": "Nine",
  # "0": "Zero",
#}

#translation = ""
#for ch in phone:
 #translation +=translate.get(ch , "!") + " " 
 
 #print (translation)


#message =input("> ")
#words = message.split(' ')
#emoji = {
 #  "::happy": "🙂", 
  # "::sad": "😔",
   #"::hello": "👋"
   #}
#output = ""
#for word in words:
 #  output +=emoji.get(word , word) + " "
#print(output)

#def ask_user(name):
  # name = input("What is your name? : ")
  # if len(name) < 3:
   ##   print("Ohhh Yur name is too short!!")
    #  ask_user() 
   #else:
   #   print(f"Ohhh it's pleasure to know you {name} !!")


#print("hello")  
#ask_user()

#def sum(num1, num2):
 #  sum = num1 + num2
 #  print(f"{num1} + {num2} = {sum}")
   

#_ =os.system('clear')
#a = int (input(" Enter first number "))
#_ = os.system('clear')
#b = int (input(" Enter second number "))
#_ =os.system('clear')
#sum(a,b)   

#def power(number, mult_time_to_power):
 #  powered = number ** mult_time_to_power
 #  print(f"{number} power {mult_time_to_power} is {powered}")


#_ =os.system('clear')
#a = int (input("Enter number "))   
#b = int(input(f"Enter other number to power to {a} : "))
#power(a,b)




#Exceptions: this used to handle code crush exited with code 1 we want our code to be done successfull exit with code 0.

#try:
 #  age = int(input("Age :"))
#  print(f"{age}")
  # Money = float(input("How much money do you want to give to peaple? "))
 #  peaple = int(input("How many peaple do you want to give tha money? "))
  #print(f"Now each person will get {each_person_share}.")
#except ValueError:
 #  print("Invalid Age.")
#except ZeroDivisionError:
 #  print("people can not be 0.")










                                       #My prifile.py
                                      #Class in python





#class profile:
 #  def name(self):
#      print("I'm Joe.")
      
#   def age(self):
#      print("I'm 22 years old.")  


#run = profile()
#run.name() 
#run.age()

                                       #My random.py
                                      #Random values in python


#import random


#for i in range(3):
  # print(random.random())






                         #My random.py





#import random


#class dice:
#   def roll(self):
 #      first = random.randint(1,6)
  #     second = random.randint(1,6)
   #    return(first, second)

#run = dice()
#print(run.roll())




                            #My path.py




#from pathlib import Path #check if dir is exists

#path = Path(("Docs"))
#print(path.exists())

 
 #from pathlib import Path #make directory

#path = Path(("Docs"))
#print(path.mkdir())


                              



                              #THis was For MAking BArchart in Excel





#from pathlib import Path #remove directory

#path = Path(("Docs"))
#print(path.rmdir())
#import openpyxl as xl
# Importing necessary classes from openpyxl.chart
# from openpyxl.chart import BarChart, Reference

# Define a function to process an Excel workbook
# def process_workbook(filename):
#    # Load the workbook and select the sheet named 'Sheet1'
#    wb = xl.load_workbook(filename)
#    sheet = wb['Sheet1']

#    # Iterate through each row starting from the second row
#    for row in range(2, sheet.max_row + 1):
#       # Get the value of the cell in the third column of the current row
#       cell = sheet.cell(row, 3)
#       # Calculate the corrected price as 90% of the original price
#       corrected_price = cell.value * 0.9
#       # Access the cell in the fourth column of the current row
#       corrected_price_cell = sheet.cell(row, 4)
#       # Assign the corrected price to the fourth column cell
#       corrected_price_cell.value = corrected_price

#    # Create a reference for the bar chart data (from column 4)
#    values = Reference(sheet,
#             min_row=2,
#             max_row=sheet.max_row,
#             min_col=4,
#             max_col=4)

#    # Create a bar chart object
#    chart = BarChart()
#    # Add the data to the chart
#    chart.add_data(values)
#    # Add the chart to the sheet at cell E2
#    sheet.add_chart(chart, 'e2')

#    # Save the workbook with the changes
#    wb.save(filename)



                        #MY currentTime.py





# Get the current time on screen
#now = time.strftime("[%d/%m/%Y   %H:%M:%S]")

#Print the current time in a readable format
#_ =os.system("clear")
#print(f"current time:{now}")
# 




                    #MY oddnumber.py






#def oddNumber(num):
 #  try:
 #     number = int(input("\nEnter a number: "))
  # except ValueError:
 #     print("\nInvalid number!")
  # else:
   #   print(f"Odd number in {number} are")

    #  for i in range (1, number + 1):
     #    if i % 2 !=0:
      #     print(i)

#for i in range(1, 5):
 #   print(i)


#import random

#list1 = [1 , 2 , 3 , 4 , 5]
#list2 = [2 , 8 , 9 , 7 , 6]

#random_list1 = random.choice(list1)  #Here i can use random.sample to pick how many numbers i want to print in the list1
#random_list2 = random.choice(list2)  #Here i can use random.sample to pick how many numbers i want to print in the list2


#result = [random_list1 , random_list2]
#print(result)


#list = [1,1,2,2,3,4,5,5,6,6]

#remove_duplication =[]

#for check in list:
 #   if check not in remove_duplication:
        
  #      remove_duplication.append(check)
#print(remove_duplication)        

#number = int(input("Enter number of elements: "))

#elements=[]

#for i in range (number):
    
 #   element = int(input(f"Enter element {i+1}: "))
   
  #  elements.append(element)
   # sum = 0

    #for s in elements:
     #   sum+=s
    #unique = []

    #for element in set (elements):
     #   if elements.count(element) ==1:
      #      unique.append(element)  
    #duplicates = []  
    #for element in set(elements):
     #   if elements.count(element) > 1:
      #      duplicates.append(element)
    
#print(f"\nYour array of {number} elements is {elements}, sum of elements is ({sum}), unique elements is {unique}, duplicated number is {duplicates}.")




#              MY AI.py




# names = ""

# def about():
#     global names  # Use the global variable
#     if names != "":
#         print(f"\nYes I know you, you are {names}.")
#     else:
#         print("\nNo, I don't know you! Maybe you can tell me about you.")
#         while True:
#             names = input("\nWhat is your name? \n\n> ").strip()

#             if not names:
#                 print("Sorry! Names can not be blank!")

#             if names:
#                 print(f"\nHello {names}, now I know your name.")
#                 break

# def main():
#     global names  # Access the global variable
#     while True:
#         write = input("\n> ").strip().lower()

#         if not write:
#             print("I did not see anything! blank type!")
#             continue
#         if write == "do you know me" or write == "do you know me?":
#             if names != "":
#                 print(f"\nYes I know you, you are {names}.")
#             else:
#                 about()
#         elif write == "1":
#             print("This is one.")
#         elif write == "hello":
#             print("\nHello there, what can I help?")
#         elif write == "who are you" or write == "who are you?":
#             print("\nI am your friendly assistant!")
#         elif write == "okay" or write == "okay." or write == "great" or write == "nice" or write == "ohh" or write == "done":
#             print("\nNo problem, if you need other help do not hesitate to ask.")
#         elif write == "thanks." or write == "thanks":
#             print("\nYou are welcome!")
#         elif write == "really?" or write == "really":
#             print(f"\nYeah!")
#         else:
#             print("\nHello there! I do not know this because I'm still learning.")
            
# if __name__ == "__main__":
#     main()




                            #My fibonacci.py



#Fibonacci Sequence

#Write a function that generates the first 10 numbers in the Fibonacci sequence. 
# #The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, #
# starting from 0 and 1. For example, the first 10 numbers are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.









#def fibonacci(n):
  #  sequence = []
   # a, b = 0, 1
    #for _ in range(n):  # Iterate n times
     #   sequence.append(a)  # Append the current Fibonacci number to the list
      #  a, b = b, a + b  #Calculating the Next Fibonacci Number: This line updates the values of a and b. The new value of a becomes the old value of b, and the new value of b becomes the sum of the old values of a and b. This is how the Fibonacci sequence is generated:

    #return sequence  

#num = int(input("\nEnter a number: "))
#sequence = fibonacci(num)  # Get the Fibonacci sequence
#print(f"\nThe first {num} Fibonacci numbers are: {sequence}")





                                #My palindrome.py





# Palindrome Checker

#Write a function that checks if a given string is a palindrome. 
# A palindrome is a word, phrase, number, 
# or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
#  For example, "radar" and "level" are palindromes.




# import string

# def is_palindrome(s):
#     # Clean the input: remove punctuation, spaces, and convert to lowercase
#     cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
#     # Check if the cleaned string is the same forwards and backwards
#     return cleaned == cleaned[::-1]
   
# # Example usage
# while True:
#     # Prompt the user for input
#     user_input = input("\nEnter a string: ").strip()

#     # Exit condition for the loop
#     if user_input == "exit":
#         break

#     # Validate the input: must be lowercase and non-empty
#     if not user_input or any(char.isupper() for char in user_input) or not user_input.isalnum():
#         print("\nInvalid text! Text must be in lowercase and non-empty.")
     
#     # Check if the input string is a palindrome
#     elif is_palindrome(user_input):
#         print(f'\n"{user_input}" is a palindrome!\n')
#     else:
#         print(f'\n"{user_input}" is not a palindrome.\n')





                   #MY chat.py





# class Chat:

#    def user_1(self, name='Joe'):
#       while True:
#           text = input(f"\n{name}: ").strip()

#           if not text:
#               self.user_1()

#           words = text.split()
#           
#           emojis = {
#               ":smile": "😊",
#               ":sad": "😔",
#               ":happy": "🙂",
#               ":laugh": "🤣",
#               ":heart": "❤️",
#               ":like": "👍",
#               ":hello": "👋",
#           }

#           output = ""

#           for word in words:
#               output += emojis.get(word, word) + " "
#               _ = os.system("clear")
#               
#           print(f"{name}: {output}")

#           self.user_2()

#    def user_2(self, name='Jeanne'):
#       while True:
#           text = input(f"\n{name}: ").strip()

#           if not text:
#               self.user_2()

#           words = text.split()
#           emojis = {
#               ":smile": "😊",
#               ":sad": "😔",
#               ":happy": "🙂",
#               ":laugh": "🤣",
#               ":heart": "❤️",
#               ":like": "👍",
#               ":hello": "👋",
#           }

#           output = ""

#           for word in words:
#               output += emojis.get(word, word) + " "
#               _ = os.system("clear")
#               
#           print(f"{name}: {output}")

#           self.user_1()

# open_chat = Chat()
# open_chat.user_1()





                                      #My text_encrypt.py



#import random
#import string

#def encrypt():
#    history = []

#    while True:
#        chars = " " + string.punctuation + string.digits + string.ascii_letters
#        chars = list(chars)

#        key = chars.copy()
#        random.shuffle(key)

#        plain_text = input("\nEnter message to encrypt: ").strip()
#        if not plain_text:
#            print("\nUser input must be non-empty!")
#            history.append("You entered wrong input for encrypt")
#            continue

#        history.append(f"Your plain text was: {plain_text}")
#        cipher_text = ""

#        for letter in plain_text:
#            index = chars.index(letter)
#            cipher_text += key[index]

#        print(f"\nOriginal message: {plain_text}")
#        print(f"Encrypted message: {cipher_text}")

#        history.append(f"Encrypted was: {cipher_text}")

#        encrypt_text = input("\nEnter the encrypted result to check if it matches: ").strip()
#        if not encrypt_text:
#            print("\nUser input must be non-empty!")
#            continue

#        history.append(f"Here you entered to check if it matches: {encrypt_text}")

#        if encrypt_text != cipher_text:
#            print("\nYour input does not match the encrypted result!")
#            history.append("Your input did not match result!")
#            continue
#        else:
#            print("\nYou got it!")
#            history.append("Your input matched result!")

#        decrypted_text = ""
#        for letter in encrypt_text:
#            index = key.index(letter)
#            decrypted_text += chars[index]
#        print(f"\nEncrypted message: {encrypt_text}")
#        print(f"Decrypted message: {decrypted_text}")

#        while True:
#            choice = input("\nDo you want to exit (Y/N) or check your history (H)? ").strip().lower()
#            history.append(f"Here your option between Y/N or 'H' for history you chose: {choice}")
#            if choice == "y":
#                print("\nThank You!")
#                return
#            elif not choice:
#                print("\nInput can't be empty!\n")
#                history.append("Empty input!")
#            elif choice == "n":
#                print("\nThank you for staying!")
#                history.append("Oh, you liked to stay! We appreciate that!")
#                break
#            elif choice == "h":
#                print("\nHistory:\n")
#                for entry in history:
#                    print(entry)
#            else:
#                print("\nInvalid input! Please enter 'Y', 'N', or 'H'.")
#                history.append("You chose an invalid option!")

#encrypt()



                                                          #my Guess.py




# import random

# while True:
#     secret = random.randint(0, 10)  # Random number between 0 and 9
#     count = 3  # Number of attempts

#     while count > 0:  # User has 3 attempts
#         try:
#             guess = int(input("Guess the number (0-9): "))  # Get user's guess

#             if guess < secret:
#                 print("\nYour input is less than number to Guess!")
#             elif guess > secret:
#                 print("\nYour input is greater than number to Guess!")
#             if guess != secret:
#                 print("Incorrect. Try again!")
#                 count -= 1
#                 print(f"You have {count} time left.")
#             else:
#                 print(f"\nYou won! The number to guess was {secret}.")
#                 break  # Exit the guessing loop if guessed correctly
#         except ValueError:
#             print("Invalid input! Please enter a number.")
    
#     if count == 0:
#         print(f"\nTime's up! The number was {secret}.")
    
#     # Ask the player if they want to play again
#     choice = input("\nDo you want to guess again? Y/N: ").lower()
#     if choice != "y":
#         print("Thanks for playing!")
#         break  # Exit the game if the player doesn't want to play again





import random
import string

def generate_password(length):
    # Create a base password store
    password_store = string.ascii_letters + string.digits  

    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    # Generate a random password
    password = ''.join(random.sample(password_store, length))  
    return password
try:
    user_length = int(input("Enter desired password length: "))  
    generated_password = generate_password(user_length)
    print(f"Generated Password: {generated_password}") 
except ValueError:
    print("Invalid Length!") 
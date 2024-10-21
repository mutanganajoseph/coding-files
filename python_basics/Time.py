print("Profile form!")
name = input("What is your name? ")
while not name:
    print("Name field can not be empty!")
    name = input("Please enter your name: ")

age = input(f"{name}, how old are you? ")
while not age.isdigit():
    print("Age must be a number!")
    age = input("Please enter your age: ")
age = int(age)

email = input(f"{name}, please provide your email: ")
while not email:
    print("Email field cannot be empty!")
    email = input("Please enter your email: ")

print(f"Thank you, {name}, for providing your profile!")
print(f"Your name is: {name}")
print(f"Your age is: {age}")
print(f"Your email is: {email}")
print("Please make sure the provided information is correct.")

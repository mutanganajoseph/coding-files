# # import sys
# # import os

# # def sum(a,b):
# #     return a+b

# # def diff(a,b):
# #     return a-b

# # def pro(a,b):
# #     return a*b


# # def div(a,b):
# #     return a/b

# # def Exit_Stay():
     

# #      while True:
# #         choice = input("\nWant to calculate other Y/N :").lower()
# #         if not choice =="y":
# #             sys.exit()
# #         else:
           
# #             calculate()


# # def calculate():
     

# #     while True:
# #         _= os.system("clear")

# #         print("\n*****************")
# #         print("Python Calculator")
# #         print("*****************\n")
# #         num1 = float(input("Enter first number :"))

# #         choice = input("\nChoose operation:\n\n1.Divide \n2.Multplication \n3.Diffrent \n4.Add \n>").lower()


# #         if choice == "1":
# #             result 
# #             num2 = float(input("\nEnter second number : "))
# #             result = div(num1,num2)
# #             print(f"\nResult{num1} / {num2} = {result:.2f}")
# #             Exit_Stay()


# #         if choice == "2":
# #             num2 = float(input("\nEnter second number :  "))
# #             result = pro(num1,num2)
# #             print(f"\nResult {num1} * {num2} = {result:.2f}")
# #             Exit_Stay()


# #         if choice == "3":
# #             num2 = float(input("\nEnter second number : "))
# #             result = diff(num1,num2)
# #             print(f"\nResult {num1} - {num2} = {result:.2f}")
# #             Exit_Stay()



# #         if choice == "4":
# #             num2 = float(input("\nEnter second number : "))
# #             result = sum(num1,num2)
# #             print(f"\nResult {num1} + {num2} = {result:.2f}\n")
# #             Exit_Stay()
# #         else:
# #             print("\nInvalid Operation!")
            


# # if __name__ == "__main__":
   
# #     calculate()


# class calculotor:
#     def  __init__(self):
#         self.num1 = 0
#         self.num2 = 0

#     def get_input(self):
#         self.num1 = float(input("\nFirts Number  :"))
#         self.num2 = float(input("Second Number :"))
#         self.display()


#     def calculateSum(self):
#         return self.num1 + self.num2 
    
#     def display(self):
#         result = self.calculateSum()
#         print(f"{self.num1} + {self.num2} = {result}")


# class Car:
#     def __init__(self , make , model):
#          self.make = make
#          self.model = model
         

#     def display_info(self):
#         print(f"{self.make} {self.model}")
      
# car1 = Car("\nToyota", "Corolla")
# car2 = Car("Honda", "Civic")

    

# open = calculotor()
# car1.display_info()
# open.get_input()



for i in range(1,11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    
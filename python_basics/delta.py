import math

def calculate_delta(a,b,c):
    return (b**2) - (4*a*c)



def calculate_x1(a,b,delta):
   if delta >= 0:
       sqrt_delta = math.sqrt(delta)
        
       return (-b + sqrt_delta) /(2*a)
   
def calculate_x2(a,b,delta):
    if delta >= 0:
        sqrt_delta = math.sqrt(delta)
        return (-b - sqrt_delta) / (2*a)


def main():
  
    a = float(input("Enter value of a : "))
    b = float(input("Enter value of b: "))
    c = float(input("Enter value of c: "))
    try:
        if a == 0:
            if c == 0:
                print("This equation have infinite solution")
            else:
                print("this is not quadartic equation.")
                return
    
    

        delta = calculate_delta(a,b,c)

        if delta >=0:
            sqrt_delta = math.sqrt(delta)
            x1 = (-b + sqrt_delta) / (2*a)
            x2 = (-b - sqrt_delta) / (2*a)
            print(f"\nDelta = {delta:.2f}\nSqrt_delta = {sqrt_delta:.2f}\nx1 = {x1:.2f}\nx2 = {x2:.2f}")
        
            
    except ZeroDivisionError:
        print("ZeroDivisionError")
        return

   

    
if __name__ == "__main__":
    main()


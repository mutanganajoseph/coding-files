




weight = float(input("weight: "))
unit = input ("(K)g or(L)bs: ")

if unit.upper() =="K":
    converted = weight / 0.45
    
    print("weight in ls: )" + str (converted))
    
elif unit.upper() =="L":
    converted = weight * 0.45
    print("weight in kg: " + str (converted))
else: print("invalid input (use K or L)")
    
    
    
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# User Input
try:
    weight = float(input("\nEnter your weight in kilograms: "))

    height = float(input("Enter your height in meters: "))
    if height <= 0:
        print("Your height can't be a zero!")

    if height > 0:
      
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        print(f"Your BMI is {bmi:.2f}, which is considered '{category}'.")

except ValueError:
    print("Invalid height or weight!")



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
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculation
bmi = calculate_bmi(weight, height)
category = categorize_bmi(bmi)

# Output
print(f"Your BMI is {bmi:.2f}, which is considered '{category}'.")

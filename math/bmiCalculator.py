# A simple script to calculate your BMI

height = float(input("Enter Height (cm): "))
weight = float(input("Enter Weight (kg): "))

# BMI = weight (kg) / (height (m))^2
bmi = weight / (height/100)**2

healthStatus = "None"
if bmi < 18.4:
    healthStatus = "Underweight"
elif (bmi > 18.4) and (bmi < 24.9):
    healthStatus = "Normal Weight"
elif (bmi >= 25) and (bmi <= 29.9):
    healtStatus = "Over Weight"
elif (bmi > 29.9):
    healthStatus = "Obese"

print(f"BMI: {round(bmi,2)}")
print(f"Health Status: {healthStatus}")
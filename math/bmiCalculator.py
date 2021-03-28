# A simple script to calculate your BMI

height = float(input("Enter Height (cm): "))
weight = float(input("Enter Weight (kg): "))

# BMI = weight (kg) / (height (m))^2
bmi = weight / (height/100)^2
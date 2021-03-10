# A simple script that converts Celsius to Farenheit
# and vice versa

def toFarenheit(celsius):
    return ((celsius * (9/5)) + 32)

def toCelsius(farenheit):
    return ((farenheit - 32) * (5/9))

print("Please pick an option:")
print("1. Convert from Farenheit to Celsius")
print("2. Convert from Celsius to Farenheit")

degree = int(input("Option (1,2): "))
temperature = int(input("Temperature: "))

if(degree == 1):
    print(toCelsius(temperature), " Celsius")
elif(degree == 2):
    print(toFarenheit(temperature), " Farenheit")
else:
    print("Invalid Option")

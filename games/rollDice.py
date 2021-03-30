# A simple Roll-Dice Simulator 
# Using the random module

import random 

def diceValue():
    diceVal = random.randint(1,6)
    results.append(diceVal)
    return diceVal

results = []
print(diceValue())

while True:
    choice = input("Roll again? (y/n): ")
    if choice.lower() == "y":  
        print(diceValue())
    else: 
        break
print("Results: ")    
print(','.join(str(res) for res in results))

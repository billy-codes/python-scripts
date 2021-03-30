# A simple Roll-Dice Simulator 
# Using the random module

import random 

def diceValue():
    return random.randint(1,6)

results = []
diceValue = diceValue()
print(diceValue)
results.append(diceValue)
while True:
    
    choice = input("Roll again? (y/n): ")
    if choice.lower() == "y":
        diceValue = diceValue()
        results.append(diceValue)
        print(diceValue())
    else: 
        break

print("Dice Roll Ended")
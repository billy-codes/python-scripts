# A simple guessing game

import random

print("Hey there! What's your name?")
myName = input()
print("Welcome " + myName + "!\n")

numberTarget = random.randint(1,10)
print("The winning number is between 1 & 10")
print("Can you guess it?")

chances = 5
for i in range(1,chances+1):
    myNumber = int(input())
    if myNumber > numberTarget:
        print("Too high! Try again.")
    elif myNumber < numberTarget:
        print("Too low! Try again.")
    else:
        break
if(myNumber == numberTarget):
    print(f"Congratulations {myName}, your guess for " + \
        str(myNumber) + " is correct!")
else:
    print("Sorry, you've used all " + str(i) + " chances")
    print("The correct number was " + str(numberTarget))

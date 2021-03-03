# A simple Rock Paper Scissors Game

from random import randint

# list of options
option = ["Rock","Paper", "Scissors"]

computer = option[randint(0,2)] # computer's choice
turns = 3   # no. of turns

print("1. Rock  2. Paper  3. Scissors")
print("Pick an option (1,2,3): ")

user = int(input()) # user's choice
user-=1

tie = 0
user_score = 0
computer_score = 0
for i in range(0,turns):
    if(user == computer):
        print("It's a tie!")
        tie+=1
    elif((user == 0) & (computer == 1)):
        print(option[1] + " covers" + option[0])
        computer_score+=1
        print("User Score: " + str(user_score))
        print("Computer Score: " + str(computer_score))
    elif((user == 0) & (computer == 2)):
        print(option[0] + " breaks " + option[2])
        user_score+=1
        print("User Score: " + str(user_score))
        print("Computer Score: " + str(computer_score))
    elif((user == 1) & (computer == 0)):
        print(option[1] + " covers " + option[0])



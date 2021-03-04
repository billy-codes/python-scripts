# A simple Rock Paper Scissors Game

from random import randint

print("1. Rock  2. Paper  3. Scissors")
print("Pick an option (1,2,3): ")

# list of options
option = ["Rock","Paper", "Scissors"]
turns = 3   # no. of turns
tie = 0
user_score = 0
computer_score = 0

for i in range(1,turns+1):
    print("Round: " + str(i))
    computer = randint(0,2) # computer's choice
    user = int(input()) # user's choice
    user-=1 # subtract 1 to match array index
    if(user == computer):
        print("It's a tie!")
        tie+=1
    elif((user == 0) and (computer == 1)):
        print(option[1] + " covers" + option[0])
        computer_score+=1
        print("User Score: " + str(user_score))
        print("Computer Score: " + str(computer_score))
    elif((user == 0) and (computer == 2)):
        print(option[0] + " breaks " + option[2])
        user_score+=1
        print("User Score: " + str(user_score))
        print("Computer Score: " + str(computer_score))
    elif((user == 1) and (computer == 0)):
        print(option[1] + " covers " + option[0])
        user_score+=1
        print("User Score: " + str(user_score))
        print("Computer Score: " + str(computer_score))
    elif((user == 1) and (computer == 2)):
        print(option[2] + " cuts through " + option[1])
        computer_score+=1
        print("User Score: " + str(user_score))
        print("Computer Score: " + str(computer_score))
    elif((user == 2) and (computer == 0)):
        print(option[0] + " beats " + option[2])
        computer_score+=1
        print("User Score: " + str(user_score))
        print("Computer Score: " + str(computer_score))
    elif((user == 2) and (computer == 1)):
        print(option[2] + " cuts through " + option[1])
        user_score+=1
        print("User Score: " + str(user_score))
        print("Computer Score: " + str(computer_score))
    else:
        print("Invalid Option")
print("Final Score")
print("User Score: " + str(user_score))
print("Computer Score: " + str(computer_score))




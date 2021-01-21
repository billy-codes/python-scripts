# A simple script that allows you to reverse strings
# Using 2 methods

message = input("Enter your text here: ")

# Method #1: Slicing
reversed_result = message[::-1]

# Method #2: Loops
position = len(message) - 1
reversed_message = []
for i in range(0, len(message)):
	reversed_message.append(message[position])
	position -= 1
print(''.join(x for x in reversed_message))



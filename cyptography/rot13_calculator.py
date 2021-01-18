# A ROT13 cipher simply means to shift a character 13 steps forwards.
# This script will help encode/decode ROT13 strings
# Methods will be both manual and automated (using functions)


# using the manual method
# we will first convert characters to ascii
# second, we will shift that character 13 steps forward
# finally, convert from ascii to its original value



# USING ord() and chr()
# This method is not accurate as it returns unicode

charac = "test"
results = []
for letter in charac:
		# ord() converts text to ascii
		to_ascii = ord(letter)

		# if condition exceeds ascii value for 'm'
		# subtract 13 else add 13
		if(to_ascii >= 109 #ascii for 'm'):
			# convert to rot13 
			encode = to_ascii - 13
		else:
			encode = to_ascii + 13

		# chr() converts ascii to text
		to_text = chr(encode)
		results.append(to_text)	
		
print("ROT 13: ", results)

# A ROT13 cipher simply means to shift a character 13 steps forwards.
# This script will help encode/decode ROT13 strings
# Methods will be both manual and automated (using functions)

import argparse

parser = argparse.ArgumentParser(
	description = "ROT13 Cipher Tool",
	usage = "rot13_calculator.py -e \"Hello World\"",
	epilog = "Author: Billy Khaled, billy.codes@gmail.com")

parser.add_argument("-e", "--encode", metavar='',required=False, help="Encode with ROT13")
parser.add_argument("-d", "--decode", metavar='', required=False, help="Decode with ROT13")
args, unknown = parser.parse_known_args()

# [MATH] using ord() and chr()
# using the math method
# we will first convert characters to ascii
# second, we will shift that character 13 steps forward/backward
# finally, convert from ascii to its original value

results = []
def rot13_encode(string):
	for letter in string:
		# ord() converts text to ascii
		to_ascii = ord(letter)

		# if condition exceeds ascii value for 'm'
		# subtract 13 else add 13
		# 109 is ascii for 'm'
		if(to_ascii >= 109):
			# convert to rot13 
			encode = to_ascii - 13
		else:
			encode = to_ascii + 13

		# chr() converts ascii to text
		to_text = chr(encode)
		results.append(to_text)	
	return ''.join(x for x in results)

def rot13_decode(string):
	for letter in string:
		to_ascii = ord(letter)
		if(to_ascii <= 109): 
			decode = to_ascii + 13
		else:
			decode = to_ascii - 13
		to_text = chr(decode)
		results.append(to_text)	
	return ''.join(x for x in results)

# [TRANSLATION] using translate() 
# maketrans() is no longer a method of string package in Python 2.x
# therefore, we need to incorporate str to invoke maketrans()	
rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
def rot13encode(string):
	return string.translate(rot13trans)

def rot13decode(string):
	return string.translate(rot13trans.translate(rot13trans))

if __name__ == '__main__':
	# use either [TRANSLATION] or [MATH]
	if(args.encode):
		print("ROT 13: ", rot13encode(args.encode))
	elif(args.decode):
		print("ROT 13: ", rot13decode(args.decode))


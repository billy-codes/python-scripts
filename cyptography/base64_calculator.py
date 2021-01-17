# A simple base64 encoder/decoder 

import base64
import argparse

parser = argparse.ArgumentParser(
	description = 'Encode/Decode Strings with Base-64',
	usage = "./base64.py -e \"Hello World!\"",
	epilog = "Author: Billy Khaled, billy.codes@gmail.com")

# parameter metavar='' formats the help menu better
parser.add_argument('-e', '--encode', metavar='',required=False, help='Encode to Base-64')
parser.add_argument('-d', '--decode', metavar='',required=False, help='Encode to Base-64')
args, unknown = parser.parse_known_args() # parse unknown arguments

def encode(string):
	# use .encode() function to convert to bytes
	return base64.b64encode(string.encode()) 
def decode(string):
	return base64.b64decode(string.encode())

if __name__ == '__main__': # add this to avoid duplicates of output
	if(args.encode):
		# use .decode() function convert bytes back to string
		# .decode() removes the trail b' from the output
		print(encode(args.encode).decode())
	elif(args.decode):
		print(decode(args.decode).decode())


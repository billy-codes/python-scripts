# Use this script to grab source codes from Web Pages
# Using either urllib2 module or request module
# Future Features: 
#	- Using Beautiful module to parse source codes and results
#	- Command-line interface for parsing arguments

# Current Feature:
#	- Grab Web Page source code
#	- Save results into a text file
#	- Get current working directory

# Programming Principles
#	- File Handling
#	- Using a module and manipulating object results
#	- Custom User input

import urllib2
import request
import os

site = input("Enter target URL: ")
response = urllib2.urlopen(site)
source_code = response.read()	# response object

output_file = open("results.txt", "w")
output_file.write(source_code)
output_directory = os.getcwd() + "results.txt"
print("Output saved into: ", output_directory)

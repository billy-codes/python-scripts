# Use this script to grab source codes from Web Pages
# Using either urllib2 module or request module

# Future Features: 
#	- Using Beautiful module to parse source codes and results
#	- Command-line interface for parsing arguments
#	- Validation for target URL

# Current Feature:
#	- Grab Web Page source code
#	- Save results into a text file
#	- Get current working directory
#	- Calculate Time Taken

# Programming Principles
#	- File Handling
#	- Using a module and manipulating object results
#	- Custom User input

from urllib.request import urlopen
import os
import time

site = input("Enter target URL: ")

timeStart = time.time()
response = urlopen(site)
source_code = response.read()	# response object

output_file = open("results.txt", "wb")
output_file.write(source_code)
output_directory = os.getcwd() + "\\results.txt"
print("Output saved into: ", output_directory)

timeEnd = time.time()
totalTime = timeEnd - timeStart
print("Total time: ", round(totalTime,2), "(s)")

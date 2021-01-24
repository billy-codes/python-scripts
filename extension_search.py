# A simple script that will search for files with 
# the extension provided in the current directory

import os

ext_input = input("Enter desired file extension: ")
directory = os.listdir(".")

file_search = []
for names in directory:
	if names.endswith(ext_input):
		file_search.append(names)

results = '\n'.join(x for x in file_search)
print(results)

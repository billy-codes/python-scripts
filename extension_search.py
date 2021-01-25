# A simple script that will search for files 
# in the current directory with the extension 
# provided 



import os

ext_input = input("Enter desired file extension: ")
directory = os.listdir(".")

file_search = []
for names in directory:
	if names.endswith(ext_input):
		file_search.append(names)
results = '\n'.join(x for x in file_search)
print(results)

# one-liner solution
[print(i) for i in directory if i.endswith(".py")]

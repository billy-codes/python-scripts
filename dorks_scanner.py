# Use this script to grab links from Bing using Dorks

# Author: Billy Khaled
# Date: 16/01/2021

# Future Features: 
#	- Multithreading functionality
#	- Command-line interface for parsing arguments
#	- Ability to use Google

# Current Feature:
#	- Bing Webscraping Functions
#	- Single Threaded
#	- Save results into a text file
#	- Get current working directory
#	- Calculate Time Taken

# Programming Principles
#	- File Handling
#	- Using a module and manipulating object results
#	- Custom User input
#	- Arrays

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import urllib.request
import time
import os

# Setup
bing_url = "https://www.bing.com/search?q="
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')]
urllib.request.install_opener(opener)
dork = input("Enter dork: ")  #"inurl:'.php?id='" 
dorks = input("Enter desired number of links to generate: ")
pages = -(-int(dorks)//10)
page_param = "&first="
file_name = 'dorks_output.txt'

interval = 0
links = 0
timeStart = time.time()
for x in range(0, pages):	
	
	bing_dork = bing_url + dork + page_param + str(interval)

	# make request to page
	client = urlopen(bing_dork)
	source_code = bs(client.read(), "html.parser")
	client.close()

	# filter response
	response = source_code.findAll("li", {"class","b_algo"})

	for i in range(0, len(response)):
		if(links == int(dorks)):
			break
		response_filter = response[i].findAll("a")

		# write to file
		file = open(file_name, 'a')
		file.write(response_filter[0].get('href') + "\n")
		file.close()

		# print results
		print("[",links+1,"]",response_filter[0].get('href'))	
		links += 1

	interval += 11

file_path = os.getcwd() + "\\" + file_name
print("\n")
print("Total Time: ", round(time.time() - timeStart,2), "(s)")
print("Total Links: ", links)
print("Output saved into: ",file_path.strip())




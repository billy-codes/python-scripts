# A simple script to download wallpapers from Wallhaven
# It's good to copy the HTML source into a note editor 
# and beautify it to know what to filter

# Author: Billy Khaled
# Date: 15/01/2021

#	Future Features
#	- Print current working directory
#	- Multithreading option
#	- Give users option to download n number of wallpapers
#	- Give users option to specify types of wallpapers

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import urllib.request
import time

website = "https://wallhaven.cc/toplist"
# header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
# request = urllib.request.Request(website, headers=header)

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')]
urllib.request.install_opener(opener)

client = urlopen(website)
source_code = bs(client.read(), "html.parser")
client.close()

response = source_code.findAll("div", {"class","thumbs-container thumb-listing infinite-scroll"})
response = response[0].findAll("a")

timeStart = time.time()
downloads = 0
for i in range(0, len(response) - 10): # subtract 10 to eliminate page hyperlinks (redundant)
	if response[i].get('href') == None:
		continue
	else:
		link = response[i].get('href')

		# parse image URLs in preview page
		link_open = urlopen(link)
		link_code = bs(link_open.read(), "html.parser")
		link_open.close()

		link_response = link_code.findAll("img",{"id":"wallpaper"})
		image = link_response[0].get('src')

		file_name = image.split("/")[-1]	# manipulate URL and extract image name

		# download image
		urllib.request.urlretrieve(image, file_name)
		print("Downloaded: ", file_name)
		downloads += 1

print("Total Wallpapers: ", downloads)		
print("Total Time: ", round(time.time() - timeStart,2), "(s)")




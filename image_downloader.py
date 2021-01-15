# A simple image download tool using urllib.requests module and shutil
import urllib.request

link = "https://w.wallhaven.cc/full/g7/wallhaven-g7jg63.png"
file_name = link.split("/")[-1] # -1 outputs last element of array

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')]
urllib.request.install_opener(opener)
status = urllib.request.urlopen(link).getcode()

if status == 200:
	# code segment below downloads the image	
	urllib.request.urlretrieve(link, file_name)
else:
	print("Invalid URL")
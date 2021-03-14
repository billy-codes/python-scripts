# A simple Python script to download
# files over an open directory.
# Allows your to filter filetypes

# Future Features:
# 1. Automatically navigate through directories 
#    and download files until none left

import argparse
import os
from bs4 import BeautifulSoup as bs
import urllib.request
from urllib.request import urlopen

links = []
parser = argparse.ArgumentParser(
    description = "Open Directory Files Downloader w/ Filters",
    usage = os.path.basename(__file__) + " -u <URL> -f <filetype filter",
    epilog = "Author: Billy Khaled, billy.codes@gmail.com"
)

parser.add_argument("-u", "--url", metavar='', required=True, help="Enter Open Directory URL")
parser.add_argument("-f", "--filter", metavar='', help="Enter Filetype Extension Ex: pdf")

args, unknown = parser.parse_known_args()

# add headers for better web scraping evasion
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')]
urllib.request.install_opener(opener)

# make requests and grab links
client = urlopen(args.url)
sourceCode = bs(client.read(), 'html.parser')
client.close()

response = sourceCode.findAll("a")

for link in response:
    links.append(link.get('href'))
print(links[5:])

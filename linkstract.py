# A simple script to extract links from webpages
# Uses BeautifulSoup module

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import urllib.request

webpage = "https://www.yahoo.com"

# implement headers to bypass anti-webscrapers
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')]
urllib.request.install_opener(opener)

client = urlopen(webpage)
source = bs(client.read(), "html.parser")
client.close()

response = source.findAll("a")
count = 0
for i in range(0, len(response)):
    print(response[i].get('href'))
    count+=1
print("Total Links: ", count)

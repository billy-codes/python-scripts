# A simple script to download all images
# on a webpage

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import argparse
import time
import urllib.request
import os

parser = argparse.ArgumentParser(
    description = "Grab all web page images",
    usage = os.path.basename(__file__) + "-u <webpage>",
    epilog = "Author: Billy Khaled, billy.codes@gmail.com"
)

parser.add_argument("-u", "--url", metavar='', help="Webpage URL", require=True)
args, unknown = parser.parse_known_args()

# add headers to bypass web scraping
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')]
urllib.request.install_opener(opener)

if __name__ == '__main__':
    client = urlopen(args.url)
    source_code = bs(client.read(), "html.parser")
    client.close()

    response = source_code.findAll("img")

    timeStart = time.time()
    downloads = 0

    image = response.get('src')
    fileName = image.split("/")[-1]

    #download image
    urllib.request.urlretrieve(image, fileName)
    print("Downloaded: ", fileName)
    downloads +=1

    print("Total Images: ", downloads)
    print("Total Time: ", round(time.time() - timeStart,2), "(s")



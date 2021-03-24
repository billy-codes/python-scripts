# A simple script to download all images
# on a webpage

import argparse
from bs4 import BeautifulSoup as soup
import time
import os

parser = argparse.ArgumentParser(
    description = "Grab all web page images",
    usage = os.path.basename(__file__) + "-u <webpage>",
    epilog = "Author: Billy Khaled, billy.codes@gmail.com"
)

parser.add_argument("-u", "--url", metavar='', help="Webpage URL", require=True)
args, unknown = parser.parse_known_args()


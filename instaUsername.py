# A simple script that checks the availability
# and validity of an Instagram username

# Rules of an Instagram username
# 1. Only 3 - 30 characters
# 2. Only letters, numbers, periods, and underscores

import argparse
import os
import re
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup as bs

parser = argparse.ArgumentParser(
    description = "Checks validity and availability of username",
    usage = os.path.basename(__file__) + " -u <username>",
    epilog = "Author: Billy Khaled, billy.codes@gmail.com"
)

parser.add_argument("-u", "--username", metavar='', help="Instagram Username")
args, unknown = parser.parse_known_args()

def validate(username):
    regex = "([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)"
    if(re.search(regex,username)):
        return True


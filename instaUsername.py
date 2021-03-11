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

def availability(username):
    # use instausername.com to check for availability
    url = "https://instausername.com/availability?q="
    instaProfile = url + username

    opener = urllib.request.build_opener()
    opener. addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')]
    urllib.request.install_opener(opener)
    client = urlopen(instaProfile)
    sourceCode = bs(client.read(), "html.parser")
    client.close()
    
    response = sourceCode.findAll("div", {"class","frm--msg sccs"})
    if "free" in str(response): 
        return True

if __name__ == '__main__':
    print("Checking Username...")
    if(validate(args.username)):
        print("Username is Valid!")
        if(availability(args.username)):
            print("Username is Available!")
        else:
            print("Username is not available")
    else:
        print("Username is not valid")
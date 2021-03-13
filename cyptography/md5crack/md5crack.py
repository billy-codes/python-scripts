# A simple script that will attempt to crack
# MD5 hashes using a wordlist (Dictionary Attack)

# Future Features:
# 1. Multithreading
# 2. Crack different types of Hashes

import hashlib
import argparse
import os
import time

parser = argparse.ArgumentParser(
    description = "Simple MD5 Hash Cracker",
    usage = os.path.basename(__file__) + " -h <MD5 Hash> -w <Wordlist.txt>",
    epilog = "Author: Billy Khaled, billy.codes@gmail.com"
)

parser.add_argument("-m", "--md5", metavar='', required=True, help="Enter MD5 Hash to Crack")
parser.add_argument("-w", "--wordlist", metavar='', required=True, help="Wordlist File in .txt")

args, unknown = parser.parse_known_args()

userHash = args.md5
wordlist = args.wordlist

def hashed(string):
    return hashlib.md5(string.encode()).hexdigest()

try:
    file1 = open(wordlist, 'r')
    lines = file1.readlines()
except:
    print("Error Reading Wordlist")

cracked = 0
if __name__ == '__main__':
    timeStart = time.time()
    for line in lines:
        if(userHash == hashed(line.strip())):
            print("Hashed Cracked!")
            print("MD5 Hash: ", userHash)
            print("Plaintext: ", line)
            cracked = 1
            break
    if(not cracked):
        print("No Plaintext found")

    print("Total Time: ", round(time.time() - timeStart, 4), "(s)")
    



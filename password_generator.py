#!/usr/bin/env python3

import string
import random
import argparse

parser = argparse.ArgumentParser(
    description = "A simple password generator",
    usage = "password_generator.py -c 6",
    epilog = "Author: Billy Khaled, billy.codes@gmail.com"
)

parser.add_argument("-c", "--characters", metavar='', required=True, help="Generate with number of characters")
args, unknown = parser.parse_known_args()

if __name__ == '__main__':
    if(args.characters and args.characters.isnumeric()):
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation, k=int(args.characters)))
        print("Generated Password: ",password)
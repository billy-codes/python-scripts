# A simple python script that takes
# user inputs and generates a QR Code
# using the qrcode module 

# User inputs can include links or texts
# First Install: pip3 install qrcode

#!/usr/bin/python

import qrcode
import argparse

# Setup parser
parser = argparse.ArgumentParser(
    description = "Generate QR Codes",
    usage = __file__ + "-q 'Text/Link'",
    epilog = "Author: Billy Khaled, billy.codes@gmail.com"
)
parser.add_argument("-q", "--qrcode", metavar='', required=True, help="Generate QR Code")
args, unknown = parser.parse_known_args()

if __name__ == '__main__':
    data = args.qrcode
    image = qrcode.make(data)

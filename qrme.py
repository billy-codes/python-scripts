# A simple python script that takes
# user inputs and generates a QR Code
# using the qrcode module 

# User inputs can include links or texts
# We need to install Pillow module to generate image
# First Install: pip3 install qrcode
# Second Install: pip3 install image 

#!/usr/bin/python

import qrcode
import argparse
import image
import string
import random

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
    # customize QR Code by creating an object
    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    if(data):
        title = "".join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k = 5))
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color = "black", back_color = "white")
        qr_title = title + "_QR.png"
        img.save(qr_title)
        print("Successfully Generated QR Code")

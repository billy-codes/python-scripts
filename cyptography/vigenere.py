# A Viginere Cipher takes an input of text
# and a key that is used to encrypt it
# using the Vigenere table.
# Refer to the image

import argparse
import os

parser = argparse.ArgumentParser(
    description = "Encrypt/Decrypt using Vigenere Cipher",
    usage = os.path.basename(__file__) + " -e <text> -k <key>",
    epilog = "Author: Billy Khaled, billy.codes@gmail.com"
)

parser.add_argument("-e", "--encrypt", metavar='', help="Encrypt Text")
parser.add_argument("-d", "--decrypt", metavar='', help="Decrypt Text")
parser.add_argument("-k", "--key", metavar='', required=True, help="Cipher Key")
args, unknown = parser.parse_known_args()

class Vigenere:
    def encrypt(self, text, key):
        encoded = []
        for x, y in zip(text, key):
            shift = ord(x) - 65 # 65 is ascii for first letter 'A'
            ciphered = shift + ord(y)
            if(ciphered > 90):
                ciphered = ciphered - 91 + 65
            encoded.append(chr(ciphered))
        return ''.join(l for l in encoded)

    def decrypt(self, encrypted, key):
        decoded = []
        for x,y in zip(encrypted, key):
            shift_count = 1
            start = ord(y)
            while start != ord(x):
                start+=1
                shift_count+=1
                if(start == 90): # if char reaches 'Z'
                    start = 65
            deciphered = 65 + shift_count
            decoded.append(chr(deciphered))
        return ''.join(l for l in decoded)


if __name__ == '__main__':
    en = Vigenere()
    if(args.encrypt):
        print("Plain Text: ", args.encrypt)
        print("Key: ", args.key)
        print("Ciphered: ", en.encrypt(args.encrypt.upper(), args.key.upper()))
    elif(args.decrypt):
        print("Ciphered Text: ", args.decrypt)
        print("Key: ", args.key)
        print("Deciphered Text: ", en.decrypt(args.decrypt.upper(), args.key.upper()))




        

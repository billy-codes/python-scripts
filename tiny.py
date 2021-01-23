# A simple URL shortner 
# This script does not contain features that will 
# support API and it does not use databases.
# Future Development will achieve these.
import random
import string
tiny_domain = "https://tiny.url/"
input("Enter domain name: ")

# generate 6 random characters using random.choices()
url_code = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=6))
tiny_url = tiny_domain + url_code

print("Generated URL: ", tiny_url)
import re
import urllib.request
from smtplib import SMTP

# use partition() or split() function
def get_user(email):
	username = email.split("@")			
	#username = email.partition("@")[0]	# using partition() function
	return username[0]

def get_domain(email):
	domain = email.partition("@")[2]	
	# domain = email.split("@")
	# return domain[1]
	return domain

def validate_email(email):
	regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[\._]?[a-z]+$"
	if(re.search(regex,email)):
		return True

def is_online(domain):
	status = urllib.request.urlopen(domain).getcode()
	if status == 200:
		return True

email = "intan@fiske.com.my"
port = 25
mail_server = "mail." + get_domain(email)

try:
    with SMTP(mail_server, port) as smtp:
        result = smtp.verify(email)
        print("SMTP CODE: {} \nMESSAGE: {}".format(*result))
except:
    	print("Error")


# smtpTest = SMTP(mail_server, port)
# result = s
# print(mail_server)
# if(validate_email(email)):
# 	print("Valid Email Format")

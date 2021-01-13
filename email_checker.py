#	A simple email format validator using regex
#	Future Features:
#		- Email user validator (Email Status)
#		- Check whether email is professional or commercial (Email Type)
#		- Check whether email host is up or offline (Server Status)
#
#	Current Features:
#		- Email format validation

import re

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

email = "intan@fiske.com.my"

if(validate_email(email)):
	print("Email: ", email, " is valid")
else:
	print("Email: ", email, " is invalid")

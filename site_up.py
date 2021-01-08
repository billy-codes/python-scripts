# This simple script will return response codes after communicating with the server
# We will use this script to check whether a site/host is up or offline
# Using the popular urllib.request module in Python

# Use this script to play with response codes for your other tools
import urllib.request

site = input("Enter website: ")
status = urllib.request.urlopen(site).getcode()
if status == 200:
	print("Online")





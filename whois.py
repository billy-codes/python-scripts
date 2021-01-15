# 	A simple WHOIS tool by parsing HTML
# 	Using the website https://who.is
# 	All variables have been named according to the HTML
#	tags and div classes used in the website	

#	 Current Features:
#		- Gets complete WHOIS data from target
#		- Uses BeautifulSoup to parse HTML code
#		- Utilizes findAll() function to grab specific HTML element data
#		- Equipped with a timer to show process duration

# 	Future Features:
#		- Implement Multithreading for bulk targets search
#		- Write data into a .csv file
#		- Bulk WHOIS search
#		- Interactive options for custom results output

# 	Programming Principles
#		- String manipulation
#		- HTML parsing
#		- Manipulating array(s) data

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

whois_website = "https://who.is/whois/"

domain = input("Enter target domain: ")
domain = domain.replace("www.","").replace("https://","").replace("http://","")
target = whois_website + domain

url_client = urlopen(target)
data_source = bs(url_client.read(), "html.parser")
url_client.close()

# Headers and Titles
response_headers = data_source.findAll("div", {"class": "col-md-12 queryResponseHeader"})
registrar_info_header = response_headers[0].text
important_dates_header = response_headers[1].text
similar_domains_header = response_headers[2].text
registrar_data_header = response_headers[3].text

# Data corresponding to headers
response_body = data_source.findAll("div", {"class": "col-md-12 queryResponseBody"})
registrar_info_body = response_body[0].text
important_dates_body = response_body[1].text
similar_domains_body = response_body[3].text
registrar_data_body = data_source.findAll("div", {"class": "col-md-12 queryResponseBodyValue"})
registrar_data_body = registrar_data_body[1].findAll("div", {"class": "row"})

# Results Section
print("##### Registrar Data #####")
print(registrar_data_header)
for i in range(0, len(registrar_data_body)):
	r_label = registrar_data_body[i].findAll("strong")
	r_desc = registrar_data_body[i].findAll("div", {"class","col-md-7"})
	print(r_label[0].text,": ",r_desc[0].text)


print("##### Registrar Info #####")
print(registrar_info_header)
print(registrar_info_body.strip())
print("###########################\n")

print("##### Important Dates #####")
print(important_dates_header)
print(important_dates_body.strip())
print("###########################\n")

print("##### Similar Domains #####")
print(similar_domains_header)
print(similar_domains_body.strip())
print("###########################\n")



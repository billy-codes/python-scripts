# A simple script to resolve the IP address's country using ipapo.co

# Features:
#	- Bypass anti-scraping using headers
#	- Grabs GeoIP location from 4 different sources

# Future Features
#	[ ] Resolve multiple IP Addresses
#	[ ] Save results to text file
# 	[ ] Validate IP Address before tracing
#	[ ] Error handling

from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import argparse
import time

parser = argparse.ArgumentParser(
		description = "Resolve IP Address Geolocation",
		usage = "geoip_resolver.py -ip 127.0.0.1",
		epilog = "Author: Billy Khaled, billy.codes@gmail.com")

parser.add_argument("-ip", "--ipaddress", metavar='', required=True, help="Trace IP")
args, unknown = parser.parse_known_args()

if __name__ == '__main__':
	timeStart = time.time()
	print("Tracing IP Address:")
	url = "https://ipapi.co/"
	full_url = url + args.ipaddress
	header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',}

	# ROR methodology = Request, Open, Read
	req = request.Request(full_url, headers = header)
	response = request.urlopen(req)
	source_code = soup(response.read(), "html.parser")
	table_row = source_code.findAll("tr", {"class" : "ip-striped"})

	print("########## RESULTS ##########")
	for i in range(0, len(table_row)):
		table_data = table_row[i].findAll("td")
		if not table_data[0].text: # if data is empty
			continue
		results = table_data[0].text.strip() + " : " + table_data[1].text.strip()
		print(results)
print("Total Time: ", round(time.time() - timeStart,2), "(s)")

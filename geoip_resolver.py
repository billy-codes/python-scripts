# A simple script to resolve the IP address's country

# Features:
#	- Submits POST requests using requests.post()
#	- Bypass webscraping blockage
#	- Grabs GeoIP location from 4 different sources

from urllib import request, parse
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

url = "https://www.whatismyip.com/wp-content/themes/understrap-wimi/inc/response.php"
ip_address = "175.136.205.184"

header = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
			'cache-control': 'max-age=0',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://www.whatismyip.com',
			'referer': 'https://www.whatismyip.com/ip-address-lookup/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'x-requested-with': 'XMLHttpRequest',
			'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
}
post_data = {"ip" : ip_address, "action" : "ip-lookup"}

data = parse.urlencode(post_data).encode('ascii')
req = request.Request(url,data = data,  headers = header)
response = request.urlopen(req)
source_code = response.read()

print(source_code)
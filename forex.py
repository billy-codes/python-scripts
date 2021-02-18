# This script uses the domain free.currconv.com API
# to grab currency exchange data in JSON format

# The site is free and you can sign up for an API key
import requests
import json

api_key = "e30725ac9b6590924a5f"
curr_A = "USD"  # currency A
curr_B = "SGD"  # currency B 

convert = f'{curr_A}_{curr_B}'
url = f"https://free.currconv.com/api/v7/convert?q={convert}&compact=ultra&apiKey={api_key}"

response = requests.get(url)
if(response.status_code == 200):
    json_res = response.json()
    print(json_res)

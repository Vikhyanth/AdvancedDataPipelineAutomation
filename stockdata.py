import requests


import requests

url = "https://api.marketstack.com/v1/eod?access_key=91ae6b6717bce0ae3c9c98e05b1da3cc"

querystring = {"symbols":"AAPL"}

response = requests.get(url, params=querystring)

print(response.json())
import requests
import json

# API URL and parameters
url = "http://api.marketstack.com/v1/eod"
querystring = {
    "access_key": "91ae6b6717bce0ae3c9c98e05b1da3cc",
    "symbols": "AAPL"
}

# Make the GET request
response = requests.get(url, params=querystring)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Save the JSON data to a file
    with open("marketstack_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    print("JSON data has been saved to 'marketstack_data.json'")
else:
    print(f"Failed to fetch data: {response.status_code}, {response.text}")

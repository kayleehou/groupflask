# Request Digital Coin
# RapidAPI page https://rapidapi.com/Coinranking/api/coinranking1/

# Begin Rapid API Code
import requests

url = "https://mcu-comics-and-characters.p.rapidapi.com/mcu/comics"
querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc","limit":"50","offset":"0"}
headers = {
	"X-RapidAPI-Key": "edd538bb27msh43c7f0fbf4c760ap16a5a1jsna5a07305b454",  # place your key here
	"X-RapidAPI-Host": "mcu-comics-and-characters.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
# End Rapid API Code
json = response.json()  # convert response to python json object

# Observe data from an API.  This is how data transports over the internet in a "JSON" text form
# - The JSON "text" is formed in dictionary {} and list [] divisions
# - To read the result, Data Scientist of  Developer converts JSON into human readable form
# - Review the first line, look for the keys --  "status" and "data"
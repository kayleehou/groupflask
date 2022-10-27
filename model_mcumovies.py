import requests

url = "https://marvel-quote-api.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "40507ace9fmshcdcac9ccdd404c3p1d6853jsn21cc92ac2d5e",
	"X-RapidAPI-Host": "marvel-quote-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
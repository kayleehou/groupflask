
# RapidAPI page https://rapidapi.com/gorlavasudeva/api/mcu-comics-and-characters/

# Begin Rapid API Code
import requests

url = "https://mcu-comics-and-characters.p.rapidapi.com/mcu/comics"

headers = {
	"X-RapidAPI-Key": "40507ace9fmshcdcac9ccdd404c3p1d6853jsn21cc92ac2d5e",
	"X-RapidAPI-Host": "mcu-comics-and-characters.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
#print(response.text)
# End Rapid API Code
#json = response.json()  # convert response to python json object

print("MCU List:")
movies = response.json()

#for item in mculist:	
	#for k,v in item:
		#print(k,v)
  
for movie in movies:
    print(movie["title"]) 
    print("\t" + movie["link"])
    print("\t" + movie["source"])
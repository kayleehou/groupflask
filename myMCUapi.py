from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests 

mcu_api = Blueprint('mcu_api', __name__,
                   url_prefix='/api/mcu')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(mcu_api)

url = "https://mcu-comics-and-characters.p.rapidapi.com/mcu/comics"

headers = {
	"X-RapidAPI-Key": "40507ace9fmshcdcac9ccdd404c3p1d6853jsn21cc92ac2d5e",
	"X-RapidAPI-Host": "mcu-comics-and-characters.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

comics = response.json()

comics.pop(0)
  
for comic in comics:
    print(comic["title"]) 
    print("\t" + comic["link"])
    

    

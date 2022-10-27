from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_mcu import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/mcu')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'http://escaperoom.nighthawkcodescrums.gq/' # run from web
    url = server + "/api/mcu"
    responses = []  # responses list

    # get count of jokes on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']


    # obtain a random joke
    responses.append(
        requests.get(url+"/random")  # read a random joke
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")
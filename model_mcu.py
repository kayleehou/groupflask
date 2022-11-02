from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
# import time

# Blueprints enable python code to be organized in multiple files and directories https://flask.palletsprojects.com/en/2.2.x/blueprints/
mcu_api = Blueprint('mcu_api', __name__,
                   url_prefix='/api/mcu')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(mcu_api)

"""Time Keeper
Returns:
    Boolean: is it time to update?
"""
# def updateTime():
#     global last_run  # the last_run global is preserved between calls to function
#     try: last_run
#     except: last_run = None
    
#     # initialize last_run data
#     if last_run is None:
#         last_run = time.time()
#         return True
    
#     # calculate time since last update
#     elapsed = time.time() - last_run
#     if elapsed > 86400:  # update every 24 hours 60*60*24
#         last_run = time.time()
#         return True
    
#     return False

"""API Handler
Returns:
    String: API response
"""   
def getMCUAPI():
    global mcu_data  # the covid_data global is preserved between calls to function
    try: mcu_data
    except: mcu_data = None

    """
    Preserve Service usage / speed time with a Reasonable refresh delay
    """
  # request Covid data

url = "https://mcu-comics-and-characters.p.rapidapi.com/mcu/comics"
headers = {
    "X-RapidAPI-Key": "40507ace9fmshcdcac9ccdd404c3p1d6853jsn21cc92ac2d5e",
    "X-RapidAPI-Host": "mcu-comics-and-characters.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers)
mcu_data = response


"""API with Country Filter
Returns:
    String: Filter of API response
"""   
def getMCU(filter):
    # Request MCU Data
    response = getMCUAPI()
    # Look for Comic   
    comics.pop(0)
    comics = response.json().get('MCU List')
    for comic in comics:  # countries is a list
        if comic["title"].lower() == filter.lower():  # this filters for country
            return comic["link"]
    
    return {"error": filter + " not in our database... sorry :(. Try searching something else!"}


"""Defines API Resources 
  URLs are defined with api.add_resource
"""   
class MCUAPI:
    """API Method to GET all MCU Data"""
    class _Read(Resource):
        def get(self):
            return getMCUAPI().json()
        
    """API Method to GET Covid Data for a Specific Comic"""
    class _ReadMCU(Resource):
        def get(self, filter):
            return jsonify(getMCU(filter))
    
    # resource is called an endpoint: base usr + prefix + endpoint
    api.add_resource(_Read, '/')
    api.add_resource(_ReadMCU, '/<string:filter>')


"""Main or Tester Condition 
  This code only runs when this file is "played" directly
"""        
if __name__ == "__main__": 
    """
    Using this test code is how I built the backend logic around this API.  
    There were at least 10 debugging session, on handling updateTime.
    """
    
    print("-"*30) # cosmetic separator

    # This code looks for "world data"
    response = getMCUAPI()
    print("MCU List:")
    comics = response.json()
    comics.pop(0)
    for comic in comics:
        print(comic["title"]) 
        print("\t" + comic["link"])

    print("-"*30)

    # This code looks for USA in "MCU List"
    comic = getMCU("Avengers: Endgame Prelude")
    print("Avengers: Endgame Prelude Link")
    for key, value in comic.items():
        print(key, value)
        
    print("-"*30)



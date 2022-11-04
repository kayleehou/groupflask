from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import time

# Blueprints enable python code to be organized in multiple files and directories https://flask.palletsprojects.com/en/2.2.x/blueprints/
MCU_api = Blueprint('MCU_api', __name__,
                   url_prefix='/api/MCU')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(MCU_api)

"""Time Keeper
Returns:
    Boolean: is it time to update?
"""
def updateTime():
    global last_run  # the last_run global is preserved between calls to function
    try: last_run
    except: last_run = None
    
    # initialize last_run data
    if last_run is None:
        last_run = time.time()
        return True
    
    # calculate time since last update
    elapsed = time.time() - last_run
    if elapsed > 86400:  # update every 24 hours
        last_run = time.time()
        return True
    
    return False

"""API Handler
Returns:
    String: API response
"""   
def getMCUAPI():
    global MCU_data  # the covid_data global is preserved between calls to function
    try: MCU_data
    except: MCU_data = None

    """
    Preserve Service usage / speed time with a Reasonable refresh delay
    """
    if updateTime(): 
        """
        RapidAPI is the world's largest API Marketplace. 
        Developers use Rapid API to discover and connect to thousands of APIs. 
        """
        url = "https://mcu-comics-and-characters.p.rapidapi.com/mcu/comics"
        headers = {
            "X-RapidAPI-Key": "40507ace9fmshcdcac9ccdd404c3p1d6853jsn21cc92ac2d5e",
	        "X-RapidAPI-Host": "mcu-comics-and-characters.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers)
        MCU_data = response.json()
        MCU_data.pop(0)

    return MCU_data


"""API with Country Filter
Returns:
    String: Filter of API response
"""   
def getMCU(filter):
    # Request Covid Data
    response = getMCUAPI()
    # Look for Country    
  
    comics = response.get('comic name')
    for comic in comics:  # countries is a list
        if comic["title"].lower() == filter.lower():  # this filters for country
            return comic
    
    return {"message": filter + " not found"}


"""Defines API Resources 
  URLs are defined with api.add_resource
"""   
class MCUAPI:
    """API Method to GET all Covid Data"""
    class _Read(Resource):
        def get(self):
            return getMCUAPI()
        
    """API Method to GET Covid Data for a Specific Country"""
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
    comics = response.json()
    comics.pop(0)
  
    for comic in comics:
        print(comic["title"]) 
        print("\t" + comic["link"])

    print("-"*30)

    # This code looks for USA in "countries_stats"
    comic = getMCU("Ant-Man Prelude")
    print("Ant-Man Link")
    for comic["title"], comic["link"] in comic.items():
        print(comic["title"], comic["link"])
        
    print("-"*30)

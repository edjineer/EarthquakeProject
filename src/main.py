#!/usr/bin/python3
import requests
import sys
import datetime
import json
from EarthquakeClass import Earthquake


def globals(api):
    global WEATHERKEY
    WEATHERKEY = api
    return


# Requires: Lat and Long Data
def getWeatherAPIInfo(p_lat, p_lon):
    # p_lat = latitude value of the earthquake
    # p_lon = longitude value of the earthquake

    # my_api_key = the API key obtained with my free account
    method = "GET"
    url_base = "https://api.weatherapi.com/v1/current.json"
    pars = {"q": f"{p_lat},{p_lon}", "key": WEATHERKEY}
    response_json = requests.request(method=method, url=url_base, params=pars).json()
    temp_f = response_json["current"]["temp_f"]
    return temp_f


def createEQList(featuresList):
    returnList = []
    [returnList.append(createEqItem(f)) for f in featuresList]
    return returnList


def createEqItem(feature):
    newE = Earthquake(9, 9, 9, 9, 9, 9, 0)  # TODO Initialize class better
    # Coordinates are returned long, lat, depth
    # https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
    newE.long = feature["geometry"]["coordinates"][0]
    newE.lat = feature["geometry"]["coordinates"][1]
    newE.title = feature["properties"]["title"]
    newE.temp = getWeatherAPIInfo(newE.lat, newE.long)
    newE.timestamp = feature["properties"]["time"]
    return newE


def getEarthquakeAPI():
    method = "query"
    rightNow = datetime.datetime.utcnow().isoformat()
    hourPrior = (datetime.datetime.utcnow() - datetime.timedelta(hours=1)).isoformat()
    # url = f"https://earthquake.usgs.gov/fdsnws/event/1/{method}?starttime={hourPrior}format=geojson"
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/{method}?starttime={hourPrior}&format=geojson"
    response = json.loads(requests.request("GET", url).text)
    eqClassList = createEQList(response["features"])
    return eqClassList


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            f"Not enough arguments passed in, only saw {len(sys.argv)}: must provide the n and an API key"
        )
    else:
        globals(sys.argv[1])
        n = sys.argv[2]
        eqClassList = getEarthquakeAPI()
        print("EarthQuake Data from within the last hour:")
        for i in eqClassList:
            print(f"{i.title}, temp_f={i.temp}, avg of last {n}: TODO")

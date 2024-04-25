#!/usr/bin/python3
import requests
import sys


# Requires: Lat and Long Data
def getWeatherAPIInfo(my_api_key, p_lat, p_lon):
    # p_lat = latitude value of the earthquake
    # p_lon = longitude value of the earthquake

    # my_api_key = the API key obtained with my free account
    method = "GET"
    url_base = "https://api.weatherapi.com/v1/current.json"
    pars = {"q": f"{p_lat},{p_lon}", "key": my_api_key}
    response_json = requests.request(method=method, url=url_base, params=pars).json()
    temp_f = response_json["current"]["temp_f"]
    print(temp_f)


def getEarthquakeAPI():
    pass


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            f"Not enough arguments passed in, only saw {len(sys.argv)}: must provide the n and an API key"
        )
    else:
        getWeatherAPIInfo(sys.argv[1], 0, 0)

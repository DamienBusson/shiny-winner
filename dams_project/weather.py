# pylint: disable=missing-docstring
import sys
import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    url = f"{BASE_URI}/api/location/search/?query={query}"
    responses = requests.get(url).json()
    if len(responses) == 0:
        print(f"There is no city with the name '{query}' in our database.")
        return None
    elif len(responses) > 1:
#        print("Please be more specific:")
#        for response in responses:
#            print(f"{response['title']}")
#            return None
        #print(responses[0])
        return responses[0]
    else:
        #print(responses[0])
        return responses[0]


def weather_forecast(woeid):
    url = f"{BASE_URI}/api/location/{woeid}/"
    responses = requests.get(url).json()
#    print(responses['consolidated_weather'])
    return responses['consolidated_weather']


def main_func():
    query = input("City?\n> ")
    city = search_city(query)
    if city is None:
        pass
    else:
        woeid = city['woeid']
        forecast = weather_forecast(woeid)
        print(f"Here's the weather in {city['title']}")
        for prediction in forecast:
            print(f"{prediction['applicable_date']}: {prediction['weather_state_name']} {prediction['the_temp']} °C")

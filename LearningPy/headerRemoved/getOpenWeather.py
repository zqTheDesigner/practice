#! python3
# getOpenWeather.py

APPID = 'e2498d59925072bebba44efbabc8da03'

import json, sys, requests

# Compute location from command line arguments
if len(sys.argv) < 2:
	print('Usage: getOpenWeather.py city_name 2-letter_country_code')
	sys.exit()

location = ' '.join(sys.argv[1:])

#TODO Download the JSON data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/onecall?lat=38.8&lon=12.09&appid=%s' %(APPID)

response = requests.get(url)
response.raise_for_status()

# Raw json text
# print(response.text)

weatherData = json.loads(response.text)

# Print weather descriptions.
# w = weatherData['list']
print(weatherData)

# TODO: Load JSON data in to a Python Variable



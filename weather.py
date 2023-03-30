import requests

GEOCODING_URL = 'https://geocoding-api.open-meteo.com/v1/'
OPEN_METEO_URL = 'https://api.open-meteo.com/v1/'

city_name = input("Enter a city name: ")
city_coordinates = requests.get(f"{GEOCODING_URL}search?name={city_name}&count=1")

try:
    latitude = float(city_coordinates.json().get('results')[0]['latitude'])
    longitude = float(city_coordinates.json().get('results')[0]['longitude'])
except TypeError:
    print("Invalid name.")
else:
    query_params = {'latitude': latitude, 'longitude': longitude, 'current_weather': True}

    weather = requests.get(f"{OPEN_METEO_URL}forecast", params=query_params)
    current_weather = weather.json().get('current_weather')

    print(f"Current weather in {city_name} is following:")
    for item in current_weather.keys():
        print(f"{item}: {current_weather[item]}")
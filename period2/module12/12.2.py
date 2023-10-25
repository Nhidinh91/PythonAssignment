import requests
import json

def convert_F_to_C(k_degrees):
    c_degrees = round(k_degrees - 273.15)
    return c_degrees


API_key = "4bc5b60fcb39a3e8b945502bda2ff464"
city_name = input("Please in put a city name:\n")

request = "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + API_key

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        weather_description = json_response["weather"][0]["description"]
        print(f"The weather in {city_name} now is {weather_description}.")
        k_degrees = json_response["main"]["temp"]
        c_degrees = convert_F_to_C(k_degrees)
        print(f"The temperature of {city_name} is {c_degrees}'C")
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")
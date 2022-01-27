#!/usr/lib/python3 
 
import requests

API_KEY = "458a211f60b1f99b874015a5581ff978"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    
    temperature = round(data['main']['temp'] - 273.1, 2)
    print(f'Weather: {weather}\nTemperature: {temperature}')
else:
    print("Error")






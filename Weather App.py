#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 22:50:33 2023

@author: luthorcorp
"""


import requests

def get_weather_data(city_name, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data['cod'] == 200:
        main_data = data['main']
        weather_data = data['weather'][0]
        print(f"Weather in {data['name']}: {weather_data['main']}")
        print(f"Description: {weather_data['description']}")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Humidity: {main_data['humidity']}%")
        print(f"Pressure: {main_data['pressure']} hPa")
    else:
        print(f"Error: {data['message']}")

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = '6aa38e95985bfb66f14b15cb378e956d'
city_name = input("Enter city name: ")
weather_data = get_weather_data(city_name, api_key)
display_weather(weather_data)

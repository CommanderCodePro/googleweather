from flask import Flask, render_template, request
from datetime import datetime
from matplotlib import pyplot as plt
import requests

app = Flask(__name__)

@app.route('/')
def home():
    api_key = "8649ce5dac17fa487efbd14f7cd30f9e"
    city = "http://ip-api.com/json/"
    location_response = requests.get(city).json().get("city")
    # print(location_response)
    weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + location_response + "&APPID=" + api_key
    print(weather_url)
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast?q=" + location_response + "&APPID=" + api_key
    print(forecast_url)
    response_1 = requests.get(forecast_url).json()
    response_2 = requests.get(weather_url).json()
    # print(response)

    # Weather Data
    location = response_2.get('name'),
    timezone = response_2.get('timezone')
    timestamp =response_2.get('dt')
    date_time = datetime.fromtimestamp(timestamp)
    local_timestamp = ""
    description = response_2.get('weather')[0].get('description')
    temp_k = response_2.get('main').get('temp')
    temp_c = temp_k - 273.15
    wind_speed = response_2.get('wind').get('speed')
    icon = response_2.get('weather')[0].get('icon')
    icon_url = "http://openweathermap.org/img/w/" + icon + ".png"

    my_list = [api_key, city, weather_url, response_2, location, timezone, timestamp, date_time, local_timestamp, description,
               temp_k, temp_c, wind_speed, icon, icon_url]
    print(my_list)


    # Forecast Data
    index = 0
    forecast_list = response_1['list']
    print("************************\n")
    print(forecast_list)
    print(len(forecast_list))
    while index < len(forecast_list):
        # Time
        print(forecast_list[index]['dt_txt'])
        # Put here how to do the day
        # Temperature
        print(forecast_list[index]['main']['temp'] - 273.15)
        print(forecast_list[index]['main']['temp_max'] - 273.15)
        print(forecast_list[index]['main']['temp_max'] - 273.15)
        print(forecast_list[index]['main']['feels_like'] - 273.15)
        # Additional
        print(forecast_list[index]['wind']['speed'])
        print(forecast_list[index]['main']['humidity'])
        print(forecast_list[index]['main']['pressure'])
        # Description and Icon
        print(forecast_list[index]['weather'][0]['description'])
        print(forecast_list[index]['weather'][0]['icon'])
        print("http://openweathermap.org/img/w/" + icon + ".png")
        index += 8

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
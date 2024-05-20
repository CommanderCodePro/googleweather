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
    # weather_location = response_2.get('name'),
    # weather_timezone = response_2.get('timezone')
    # weather_timestamp =response_2.get('dt')
    # weather_date_time = datetime.fromtimestamp(timestamp)
    # weather_local_timestamp = ""
    # weather_description = response_2.get('weather')[0].get('description')
    # weather_temp_k = response_2.get('main').get('temp')
    # weather_temp_c = temp_k - 273.15
    # weather_wind_speed = response_2.get('wind').get('speed')
    # weather_icon = response_2.get('weather')[0].get('icon')
    # weather_icon_url = "http://openweathermap.org/img/w/" + icon + ".png"
    #
    # my_list = [api_key, city, weather_url, response_2, weather_location, weather_timezone, weather_timestamp, weather_date_time, weather_local_timestamp, weather_description,
    #            weather_temp_k, weather_temp_c, weather_wind_speed, weather_icon, weather_icon_url]
    # print(my_list)


    # Forecast Data
    forecast_data = []
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
        # print(forecast_list[index]['main']['temp'] - 273.15)
        # forecast_list[index]['main']['temp_max'] - 273.15)
        # forecast_list[index]['main']['temp_min'] - 273.15)
        # forecast_list[index]['main']['feels_like'] - 273.15)
        # # Additional
        # forecast_list[index]['wind']['speed'])
        # (forecast_list[index]['main']['humidity'])
        # (forecast_list[index]['main']['pressure'])
        # Description and Icon
        dt_text = forecast_list[index]['dt_txt']
        temp = round(forecast_list[index]['main']['temp'] - 273.15, 2)
        temp_max = round(forecast_list[index]["main"]['temp_max'] - 273.15, 2)
        temp_min = round(forecast_list[index]["main"]['temp_min'] - 273.15, 2)
        # Put here how to do the day
        # Temperature
        description = forecast_list[index]['weather'][0]['description']
        icon = forecast_list[index]['weather'][0]['icon']


        # Convert the string to a datetime object
        date_object = datetime.strptime(dt_text, '%Y-%m-%d %H:%M:%S')
        # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
        day_of_week = date_object.weekday()
        print(day_of_week)
        # You can also get the day name
        day_name = date_object.strftime('%A')
        print(day_name)


        dict = {
            "dt_text": dt_text,
            "temp": temp,
            "temp_max": temp_max,
            "temp_min": temp_min,
            "description": description,
            "icon_url": "http://openweathermap.org/img/w/" + icon + ".png"

        }
        forecast_data.append(dict)
        index += 8
    print(forecast_data)

    return render_template('home.html', forecast_data = forecast_data)

if __name__ == '__main__':
    app.run(debug=True)
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

    index = 0
    forecast_list = response_1['list_1']
    weather_list = response_2['list_2']
    while index < len(forecast_list):
        # Time
        print(forecast_list[index]['dt_txt'])
        print('server_time ' + forecast['dt_txt'])
        print('local ' + str(datetime.fromtimestamp(forecast['dt'])))
        # Temperature
        print(forecast_list[index]['main']['temp'] - 273.15)
        print(weather_list[index]['main']['temp_max'] - 273.15)
        print(weather_list[index]['main']['temp_max'] - 273.15)
        print(weather_list[index]['main']['feels_like'] - 273.15)
        # Additional
        print(weather_list[index]['wind']['speed'])
        print(weather_list[index]['main']['humidity'])
        print(weather_list[index]['main']['pressure'])
        # Description and Icon
        print(weather_list[index]['weather']['description'])
        print(weather_list[index]['weather']['icon'])
        print("http://openweathermap.org/img/w/" + icon + ".png";)

        index += 8

    return render_template('home.html', forecast_data=forecast_data)

if __name__ == '__main__':
    app.run(debug=True)
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
    url = "https://api.openweathermap.org/data/2.5/forecast?q=" + location_response + "&APPID=" + api_key
    print(url)
    response = requests.get(url).json()
    # print(response)

    forecast_list = response['list']
    print(forecast_list)
    for forecast in forecast_list:
        temp_k = response.get('main').get('temp')
        print(temp_k)
    timestamp = response.get('dt_txt')[0],
    #Temperature
    temp_min_k = response.get('main').get('temp_min')
    temp_min_c = temp_min_k - 273.15
    temp_max_k = response.get('main').get('temp_max')
    temp_max_c = temp_max_k - 273.15
    temp_k = response.get('main').get('temp')
    temp_c = temp_k - 273.15
    #Additional
    wind_speed = response.get('wind').get('speed')
    humidity = response.get('main').get('humidity')
    description = response.get('forecast')[0].get('description')
    #Icon
    icon = response.get('forecast')[0].get('icon')
    icon_url = "http://openweathermap.org/img/w/" + icon + ".png";
    my_list = [api_key, city, location_response, url, response, weather_data, timestamp, temp_min_c, temp_max_c,temp_c, description,
                           wind_speed, humidity, icon, icon_url]
    print(my_list)

    forecast_list = response['list']
    print(forecast_list)
    for forecast in forecast_list:
        print('server_time ' + forecast['dt_txt'])
        print('local ' + str(datetime.fromtimestamp(forecast['dt'])))
        print(forecast['main']['temp_min'])
        print(forecast['main']['temp_max'])


    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
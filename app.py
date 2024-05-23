from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    api_key = "8649ce5dac17fa487efbd14f7cd30f9e"
    city = "http://ip-api.com/json/"
    location_response = requests.get(city).json().get("city")

    if not location_response:
        return "Location not found."

    weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + location_response + "&APPID=" + api_key
    print(weather_url)
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast?q=" + location_response + "&APPID=" + api_key
    print(forecast_url)

    response_1 = requests.get(forecast_url).json()
    response_2 = requests.get(weather_url).json()

    if 'list' not in response_1 or 'main' not in response_2:
        return "Error fetching weather data."

    # Weather Data
    weather_data = []
    weather_list = response_2
    weather_location = weather_list['name']
    weather_timezone = response_2['timezone']
    weather_description = weather_list['weather'][0]['description']
    weather_temp = round(weather_list['main']['temp'] - 273.15)
    weather_wind_speed = weather_list['wind']['speed']
    weather_icon = weather_list['weather'][0]['icon']
    weather_icon_url = "http://openweathermap.org/img/w/" + weather_icon + ".png"
    weather_pressure = weather_list['main']['pressure']
    weather_humidity = weather_list['main']['humidity']

    weather_data = {
        'location': weather_location,
        'timezone': weather_timezone,
        'description': weather_description,
        'temp': weather_temp,
        'wind_speed': weather_wind_speed,
        'icon_url': weather_icon_url,
        'pressure': weather_pressure,
        'humidity': weather_humidity
    }

    # Forecast Data
    forecast_data = []
    index = 0
    forecast_list = response_1['list']

    while index < len(forecast_list):
        dt_text = forecast_list[index]['dt_txt']
        # Temperature
        temp = round(forecast_list[index]['main']['temp'] - 273.15)
        temp_min = round(forecast_list[index]["main"]['temp_min'] - 273.15)
        temp_max = round(forecast_list[index]["main"]['temp_max'] - 273.15)
        description = forecast_list[index]['weather'][0]['description']
        icon = forecast_list[index]['weather'][0]['icon']

        # Additional
        wind_speed = forecast_list[index]['wind']['speed']
        humidity = forecast_list[index]['main']['humidity']
        pressure = forecast_list[index]['main']['pressure']

        # Convert the string to a datetime object
        date_object = datetime.strptime(dt_text, '%Y-%m-%d %H:%M:%S')
        day_name = date_object.strftime('%A')

        forecast_dict = {
            "dt_text": dt_text,
            "temp": temp,
            "temp_min": temp_min,
            "temp_max": temp_max,
            "description": description,
            "wind_speed": wind_speed,
            "humidity": humidity,
            "pressure": pressure,
            "icon_url": "http://openweathermap.org/img/w/" + icon + ".png",
            "day_name": day_name,
            "date_object": date_object,
        }
        forecast_data.append(forecast_dict)
        index += 8

    return render_template('home.html', weather_data=weather_data, forecast_data=forecast_data)


if __name__ == '__main__':
    app.run(debug=True)

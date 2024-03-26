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
    url = "https://api.openweathermap.org/data/2.5/forecast?q=" + location_response + "&APPID=" + api_key
    print(url)
    response = requests.get(url).json()
    print(response)

    weather_data = [0]
    for item in response['list']:
        'timestamp': item['dt'],
        'temperature': item['main']['temp'],
        'description': item['weather'][0]['description'],
        'icon': item['weather'][0]['icon']


    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
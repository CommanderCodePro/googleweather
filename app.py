from flask import Flask, render_template, requests
from datetime import datetime
from datetime import datetimeimport requests
from matplotlib import pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
        app.run(debug=True)
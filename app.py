from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'default_key')

@app.route('/weather/<city>')
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

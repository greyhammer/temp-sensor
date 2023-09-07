import Adafruit_DHT
from flask import Flask, jsonify, request

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

app = Flask(__name__)

@app.route("/")
def get_data():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:

        f_temp = (temperature * 9/5) + 32
        env_data = {}
        env_data['temp'] = f_temp
        env_data['humd'] = humidity
        print(env_data)

        return env_data
    else:
        return "Failed to retrieve data from humidity sensor"
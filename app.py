from flask import Flask
import random

app = Flask(__name__)

def ocen_jakosc_powietrza(pm10):
    if pm10 <= 13:
        return "Bardzo dobra"
    elif pm10 <= 35:
        return "Dobra"
    elif pm10 <= 75:
        return "Średnia"
    elif pm10 <= 150:
        return "Zła"
    else:
        return "Bardzo zła"

@app.route("/")
def index():
    temperature = round(random.uniform(-30.0, 35.0), 1)
    humidity = round(random.uniform(10.0, 99.0), 1)
    dustPM25 = round(random.uniform(0.0, 200.0), 1)
    dustPM10 = round(random.uniform(0.0, 300.0), 1)
    jakosc = ocen_jakosc_powietrza(dustPM10)

    return f"""
    <h1>Symulator jakości powietrza</h1>
    <p>Temperatura: {temperature}°C</p>
    <p>Wilgotność: {humidity}%</p>
    <p>Pył PM2.5: {dustPM25} µg/m³</p>
    <p>Pył PM10: {dustPM10} µg/m³</p>
    <p><strong>Jakość powietrza: {jakosc}</strong></p>
    """



import random
import time

# definicja wartosci
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

# Losowanie wartosci
temperature = round(random.uniform(-30.0, 35.0), 1)
humidity = round(random.uniform(10.0, 99.0), 1)
dustPM25 = round(random.uniform(0.0, 200.0), 1)
dustPM10 = round(random.uniform(0.0, 300.0), 1)

print("Monitorowanie wilgotności i temperatury powietrza")

while True:
    # Wartości rosnące i malejące
    temperature += round(random.uniform(-0.2, 0.2), 1)  # Zmiana o max ±0.2°C
    humidity += round(random.uniform(-2.0, 2.0), 1)     # Zmiana o max ±2%
    dustPM25 += round(random.uniform(-3.0, 3.0), 1)     # Zmiana o max ±3 ug/m3
    dustPM10 += round(random.uniform(-4.0, 4.0), 1)     # Zmiana o max ±4 ug/m3

    # Wartości min i max
    temperature = max(-30.0, min(temperature, 35.0))   
    humidity = max(10.0, min(humidity, 99.0))          
    dustPM25 = max(0.0, min(dustPM25,300))             
    dustPM10 = max(0.0, min(dustPM10,400))            

    # Jakość powietrza
    jakosc_powietrza = ocen_jakosc_powietrza(dustPM10)

    # Wynik
    print(f"Temperatura: {temperature:.1f}°C  Wilgotność: {humidity:.1f}% Pył_PM_2.5: {dustPM25:.1f}ug/m3 Pył_PM_10: {dustPM10:.1f}ug/m3 Jakość powietrza: {jakosc_powietrza}")
    
    time.sleep(2)  # Odczyt co 2 sekundy

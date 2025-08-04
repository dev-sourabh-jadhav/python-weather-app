import requests
from api_file import API_KEY

BASE_URL = "http://api.weatherapi.com/v1/forecast.json"

city = input("Enter your City Name: ")
days = 3

url = f"{BASE_URL}?key={API_KEY}&q={city}&days={days}"

try:
    response = requests.get(url)
    data = response.json()
    location = data["location"]
    current = data["current"]
    forecast_days = data["forecast"]["forecastday"]

    print(f"\n Location: {location['name']}, {location['country']}")
    print(f" Local Time: {location['localtime']}")
    print(f" Current Temp: {current['temp_c']} °C")
    print(f" Condition: {current['condition']['text']}\n")

    for day in forecast_days:
        date = day["date"]
        day_info = day["day"]
        print(f"Date: {date}")
        print(f" => Avg Temp: {day_info['avgtemp_c']} °C")
        print(f" => Condition: {day_info['condition']['text']}")
        print(f" => Max Temp: {day_info['maxtemp_c']} °C")
        print(f" => Min Temp: {day_info['mintemp_c']} °C")
        print(f" => Humidity: {day_info['avghumidity']}%")
        print(f" => Rain Chance: {day_info['daily_chance_of_rain']}%")
        print("-" * 30)

except Exception as e:
    print(f"WRONG {e}")

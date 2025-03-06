import requests
import json


def get_weather():
    #name = request.args.get('name', '')
    #city = request.args.get('city', '')
    name = "John"
    city = "Vancouver"
    api_key = "354d2edc64403794046f6fb8a76710d4"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    return data
    """
    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temp = int(data["main"]["temp"])
        feels_like = data["main"]["feels_like"]
        city_name = data["name"]
        ftemp = (temp * 1.8) + 32

        return (name, city_name, weather_desc, temp, ftemp, feels_like)
    """
print(get_weather())
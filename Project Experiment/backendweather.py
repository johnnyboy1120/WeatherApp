import requests
import json
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(HOME_HTML)

HOME_HTML = """
<HTML>
    <head>
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
        <title>WeatherApp</title>
    </head>
    <body>
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/about">About Us</a>
            <a href="/citations">Citations</a>
        </div>
        <h2>WeatherApp</h2>
        <form action="/backend">
            What's your name? <input type='text' name='name' autocomplete='off'><br>
            Enter the city (e.g. Vancouver, Richmond, Paris): <input type='text' name='city' autocomplete='on'><br>
            <input type='submit' value='Continue'>
        </form>
    </body>
</HTML>
"""

@app.route('/about')
def about():
    return render_template_string(ABOUT_HTML)

ABOUT_HTML = """
<HTML>
    <head>
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
        <title>About Us</title>
    </head>
    <body>
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/about">About Us</a>
            <a href="/citations">Citations</a>
        </div>
        <h2>About Us</h2>
        <p>This is the About Us page.</p>
    </body>
</HTML>
"""

@app.route('/citations')
def citations():
    return render_template_string(CITATIONS_HTML)

CITATIONS_HTML = """
<HTML>
    <head>
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
        <title>Citations</title>
    </head>
    <body>
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/about">About Us</a>
            <a href="/citations">Citations</a>
        </div>
        <h2>Citations</h2>
        <p>This is the Citations page.</p>
    </body>
</HTML>
"""

@app.route('/backend')
def get_weather():
    name = request.args.get('name', '')
    city = request.args.get('city', '')
    api_key = "354d2edc64403794046f6fb8a76710d4"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:  # Check if request is successful 
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        city_name = data["name"]
        temp = int(temp)
        ftemp = (temp * 1.8) + 32
        #°F = °C × (9/5) + 32
        # msg = f"Weather in {city_name}: {weather_desc}. Temperature: {temp}°C, Feels Like: {feels_like}°C"
        return WEATHER_HTML.format(name, city_name, weather_desc, temp, ftemp, feels_like)

    else:
        return """
        <html><body>
            <h2>Error</h2>
            <p>There was an error retrieving the weather data. Please try again later.</p>
            <a href="/">Home Page</a>
        </body></html>
        """
        
WEATHER_HTML = """
    <html>
        <head>
            <title> WeatherAppInfo </title>
            <h2> WeatherApp </h2>
        </head>

        <body>
        <h2>Hello {0}! Weather in {1}: </h2>
        <h4> Description - {2}. </h4>
        <h4> Temperature - {3}°C or {4}°F </h4>
        <h4> Feels like - {5}.
        </body>

    </html>
"""

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)
import requests
import json
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(HOME_HTML)

HOME_HTML = """
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
        <title>WeatherApp</title>
    </head>
    <body>
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/about">About Us</a>
            <a href="/citations">Citations</a>
        </div>
        <br>
        <br>
        <hr>
        <h2> WeatherApp - Powered By: <a href="https://openweathermap.org/">OpenWeather</a>. </h2>
        <hr>
        <form action="/backend">
            What's your name? <input type='text' name='name' autocomplete='on'><br>
            Enter a city: <input type='text' name='city' autocomplete='on'><br>
            <br>
            <input type='submit' value='Continue'>
        </form>
    </body>
</html>
"""

@app.route('/about')
def about():
    return render_template_string(ABOUT_HTML)

ABOUT_HTML = """
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
        <title>About Us</title>
    </head>
    <body>
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/about">About Us</a>
            <a href="/citations">Citations</a>
        </div>
        <br>
        <br>
        <h2>About Us</h2>
        <p>This is the About Us page.</p>
    </body>
</html>
"""

@app.route('/citations')
def citations():
    return render_template_string(CITATIONS_HTML)

CITATIONS_HTML = """
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
        <title>Citations</title>
    </head>
    <body>
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/about">About Us</a>
            <a href="/citations">Citations</a>
        </div>
        <br>
        <br>
        <h2>Citations</h2>
        <p>This is the Citations page.</p>
    </body>
</html>
"""

@app.route('/backend')
def get_weather():
    name = request.args.get('name', '')
    city = request.args.get('city', '')
    api_key = "354d2edc64403794046f6fb8a76710d4"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    weather_desc = data["weather"][0]["description"]

    
    if weather_desc == "clear sky":
        image_url = "https://png.pngtree.com/thumb_back/fw800/background/20220506/pngtree-cirrus-cloud-in-blue-sky-square-wispy-sky-photo-image_34178.jpg"
    elif weather_desc in ["few clouds", "scattered clouds"]:
        image_url = "https://live.staticflickr.com/2106/1909487867_de140c7eb8_b.jpg"
    elif weather_desc in ["broken clouds", "overcast clouds"]:
        image_url = "https://www.eoas.ubc.ca/courses/atsc113/flying/met_concepts/01-met_concepts/01c-cloud_coverage/images-01c/g5.jpg"
    elif "rain" in weather_desc:
        image_url = "https://t3.ftcdn.net/jpg/07/72/70/56/360_F_772705633_2YtqcfyWAEveld6wZTBOdjI3NxJTQhzp.jpg"
    elif "snow" in weather_desc:
        image_url = "https://media.istockphoto.com/id/535513443/photo/pedestrians-crossing-the-street-on-a-snowy-day.jpg?s=612x612&w=0&k=20&c=LMV-TeSDb0MAJ-W8wIoz3Vj_-8nj31s9-Wg2vll7Mlw="
    elif "thunderstorm" in weather_desc:
        image_url = "https://www.vmcdn.ca/f/files/via/images/weather/lightning-vancouver-may-2021-thunderstorm.jpg;w=960"
    elif weather_desc in ["mist", "haze", "fog", "smoke"]:
        image_url = "https://media.macphun.com/img/uploads/customer/blog/1691416474/169141676764d0f8bfd123b6.17928475.jpg?q=85&w=1680"
    else:
        image_url = "https://stonelockphotography.co.uk/wp-content/uploads/2017/06/2017-06-28_0003.jpg"  # Fallback image

    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temp = int(data["main"]["temp"])
        feels_like = data["main"]["feels_like"]
        city_name = data["name"]
        f = (temp * 1.8) + 32
        f = float(f)
        ftemp = round(f, 2)

        return render_template_string(WEATHER_HTML.format(name, city_name, weather_desc, temp, ftemp, feels_like, image_url))

    else:
        return render_template_string(ERROR_HTML)
    
    

ERROR_HTML = """
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
        <title>WeatherAppInfo</title>
    </head>
    <body>
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/about">About Us</a>
            <a href="/citations">Citations</a>
        </div>
        <br>
        <br>
        <h2>Error</h2>
        <p>There was an error retrieving the weather data. Please try again later.</p>
        <a href="/">Home Page</a>
    </body>
</html>
"""

WEATHER_HTML = """
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
        <title>WeatherAppInfo</title>
    </head>
    <body>
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/about">About Us</a>
            <a href="/citations">Citations</a>
        </div>
        <br>
        <br>
        <h1><strong>WeatherApp</strong></h1>
        <hr>
        <h2>Hello <em>{0}</em>! Weather in {1}:</h2>
        <h4>Description: {2}.</h4>
        <h4>Temperature: {3}°C or {4}°F</h4>
        <h4>Feels like: {5}°C.</h4>
        <br>
        
        <img src="{6}" width="200" usemap="#workmap" >
        <map name="workmap">
            <area shape="rect" coords="34,44,150,190" href="/easteregg">
        <br>
        <br>
        <a href="/" 
        style="display: inline-block; padding: 7px 12px; font-size: 16px; color: white; background-color: #333; text-decoration: none; border-radius: 5px;">Home</a>
        <hr>
    </body>
</html>
"""

@app.route('/easteregg')
def easteregg():
    return render_template_string(EGG_HTML)

EGG_HTML = """
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
        <title>Citations</title>
    </head>
    <body>
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/about">About Us</a>
            <a href="/citations">Citations</a>
        </div>
        <br>
        <br>
        <h1> Warriors is back 💪 - EASTER EGG FOUND! </h1>
        <h3> (just replace klay with butler) </h3>
        <img src = "https://cdn.nba.com/teams/uploads/sites/1610612744/2023/12/feat-image-big-3-20231201.gif?im=Resize=(640)" width='5000'>
    </body>
</html>
"""


if __name__ == "__main__":
    app.run(host="localhost", debug=True)

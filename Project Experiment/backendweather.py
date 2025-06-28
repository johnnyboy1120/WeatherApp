import requests
import json
from flask import Flask, request, render_template, render_template_string
import urllib3
from flask import Flask, render_template, request, redirect, url_for, session
import json
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/citations')
def citations():
    return render_template('citations.html')

@app.route('/backend', methods=['GET'])
def get_weather():

    action = request.args.get('action', '')  # Get which button was pressed
    city = request.args.get('city', 'Vancouver')

    if action == 'My Location':
        city = get_location()  # Use the user's actual location
        print(f"Using user's location: {city}")  # Debugging
    else:
        print(f"City entered by user: {city}")  # Debugging

    print(f"City parameter received: {city}")  # Debugging

    api_key = os.environ.get("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "weather" in data:
        weather_desc = data["weather"][0]["description"]
        temp = int(data["main"]["temp"])
        feels_like = data["main"]["feels_like"]
        city_name = data["name"]
        ftemp = (temp * 1.8) + 32
        ftemp = round(ftemp, 2)

        return render_template('weather.html', city_name=city_name, weather_desc=weather_desc, temp=temp, ftemp=ftemp, feels_like=feels_like)
    else:
        return render_template('error.html')


def get_location():
    http = urllib3.PoolManager()
    response = http.request('GET', 'http://ipinfo.io/json')
    city = json.loads(response.data.decode('utf-8'))['city']
    print(city)
    return city
    
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_FILE = os.path.join(BASE_DIR, 'users.json')

"""# Login Functions
def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as file:
            # Add default admin user if no file exists
            json.dump({"admin": "password123"}, file, indent=4)

    with open(USER_FILE, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file, indent=4)
    print("Updated Users:", users)"""

"""@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()  # Load users from the JSON file

        if username in users and users[username] == password:
            session['username'] = username  # Store info in session
            return redirect("/home")
        else:
            return render_template_string(INVALID_HTML)

    return render_template('login.html')"""

INVALID_HTML = """
<html>
<head>
    <p>Invalid username or password. </p>
    <a href="/">Return</a>
<html>
"""

"""@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_username = request.form['username']
        new_password = request.form['password']

        users = load_users()  # Load users from the JSON file

        if new_username in users:
            return 'Username already exists! Try a different one.'
        else:
            users[new_username] = new_password  # Add new user
            save_users(users)  # Save updated users to the JSON file
            return 'Registration successful! <a href="/">Login now</a>'

@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear session
    return redirect(url_for('login'))
    


@app.route('/home')
def home():
    if 'username' in session:
        return f"Welcome, {session['username']}! <br><a href='/logout'>Logout</a>"
    return redirect(url_for('login'))"""

if __name__ == "__main__":
    app.run(host="localhost", debug=True)


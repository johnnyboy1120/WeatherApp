# filepath: /c:/Users/johns/Desktop/WeatherApp/HTML stuff/app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('file.html')

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
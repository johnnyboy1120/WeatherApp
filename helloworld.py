"""
from flask import Flask
import json


app = Flask(__name__)

@app.route("/")
def helloworld():
    name = input("Enter your name: ")
    return("Hello, ", name)

@app.route("/secret data")
def secret_data():
    data = {
        "name": "John Doe",
        "email": "email@hotmail.com",
        "number": 1234567890
    }
    return json.dumps(data)

if __name__ == "__main__":
    app.run()
"""
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """<html><body>
        <h1>Hello, world!</h1>
        The time is """ + str(datetime.now()) + """.
        How are you today?
        </body></html>"""
@app.route('/weather')
def weatherget():
    weather = "sunny"

    return """<html><body>
        <h1>Weather</h1>
        The weather is: """+ weather +""".
        </body></html>"""

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)
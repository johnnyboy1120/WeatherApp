from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return HELLO_HTML

HELLO_HTML = """
    <html><body>
        <h1>Hello, world!</h1>
        Click <a href="/time">here</a> for the time.
    </body></html>
    """

@app.route('/time')
def time():
    return TIME_HTML.format(datetime.now())

TIME_HTML = """
    <html><body>
        The time is {0}.
        <br>
        <a href="/">Back</a>
        <br>
        <a href="/time">Refresh</a>
        <br>
        Thanks for visiting!
        <br>
        <a href="/secret">Notes</a>

    </body></html>
    """
@app.route('/secret')
def secret():
    return NOTES_HTML

NOTES_HTML = """
    <html><body>
        <h1>Notes</h1>
        <p>These are some notes that I have taken.</p>
        <ul>
            <li>First note</li>
            <li>Second note</li>
            <li>Third note</li>
        </ul>
        <a href="/time">Check Time</a>
        <br>
        <a href="/">Back</a>
    """
   


if __name__ == "__main__":
    app.run(host="localhost", debug=True)


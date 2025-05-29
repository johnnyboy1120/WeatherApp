from flask import Flask, render_template, request, redirect, url_for, session
from flask import render_template_string
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for sessions

# Get the folder path where app.py lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_FILE = os.path.join(BASE_DIR, 'users.json')

# Load users from the JSON file
def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as file:
            # Add default admin user if no file exists
            json.dump({"admin": "password123"}, file, indent=4)

    with open(USER_FILE, 'r') as file:
        return json.load(file)

# Save users to the JSON file
def save_users(users):
    with open(USER_FILE, 'w') as file:
        json.dump(users, file, indent=4)
    print("Updated Users:", users)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        users = load_users()  # Load users from the JSON file

        if username in users and users[username] == password:
            session['username'] = username  # Store info in session
            return redirect(url_for('home'))
        else:
            return render_template_string(INVALID_HTML)

    return render_template('login.html')

INVALID_HTML = """
<html>
<head>
    <p>Invalid username or password. </p>
    <a href="/">Return</a>
<html>
"""


@app.route('/home')
def home():
    if 'username' in session:
        return f"Welcome, {session['username']}! <br><a href='/logout'>Logout</a>"
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear session
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
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

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

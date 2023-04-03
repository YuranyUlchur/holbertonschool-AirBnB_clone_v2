#!/usr/bin/python3
"""
script that starts a Flask web application with an routes 
"""
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def text():
    return "C {}".format(text.replace('_', ' '))

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)
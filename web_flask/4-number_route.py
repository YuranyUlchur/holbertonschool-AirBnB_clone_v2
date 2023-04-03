#!/usr/bin/python3
"""
script that starts a Flask web application with an route /hbnb
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

@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is_cool'):
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>/', strict_slashes=False)
def display_n(n):
    return f'{n} is a number'

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)
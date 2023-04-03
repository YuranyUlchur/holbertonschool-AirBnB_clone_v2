#!/usr/bin/python3
"""
script that starts a Flask web application with an route /hbnb
"""
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000)
#!/usr/bin/python3
"""
script that starts a Flask web application with an route
"""
from flask import Flask

"""instance creation"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """creation the route"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

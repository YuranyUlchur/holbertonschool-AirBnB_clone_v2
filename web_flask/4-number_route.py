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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """creation the route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """text value is replaced by _ with a blank space."""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is_cool'):
    """
    Takes a text parameter from the URL
    but if not provided, the default value is is_cool
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>/', strict_slashes=False)
def display_n(n):
    """shows the value of the integer"""
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

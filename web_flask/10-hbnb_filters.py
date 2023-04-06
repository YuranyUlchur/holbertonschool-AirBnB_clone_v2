#!/usr/bin/python3
"""
script that starts a Flask web application with an route /hbnb
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_context(self):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State)
    return render_template('10-hbnb_filters.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id():
    states = storage.all(State)
    if states.id == id:
        return render_template('10-hbnb_filters.html', state=states)
    else:
        return render_template('10-hbnb_filters.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

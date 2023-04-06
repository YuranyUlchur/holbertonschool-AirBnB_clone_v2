#!/usr/bin/python3
"""
script that starts a Flask web application with an route

"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

"""instance creation"""
app = Flask(__name__)
"""
add option where URLs with and without
a trailing slash will be treated as equivalent.
"""
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_func(self):
    """
    Call in this method
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """handles HTTP requests to the path /states"""
    data = storage.all(State)
    return render_template('9-states.html', states=data, mode="none")


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
    id is a path parameter that represents the ID of a specific state
    """
    data = storage.all(State)
    for state in data.values():
        if state.id == id:
            return render_template('9-states.html', state=state, mode="id")
    else:
        return render_template('9-states.html', states=data, mode="not")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

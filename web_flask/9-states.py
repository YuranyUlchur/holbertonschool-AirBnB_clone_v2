#!/usr/bin/python3
"""
script that starts a Flask web application with an route

"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
"""
If this option is disabled, Flask will treat URLs
with and without a trailing slash as equivalent.
|
v
"""
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_func(self):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    data = storage.all(State)
    return render_template('9-states.html', states=data)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    data = storage.all(State)
    for state in data.values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', states=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

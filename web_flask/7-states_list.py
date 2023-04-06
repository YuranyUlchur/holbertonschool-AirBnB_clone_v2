#!/usr/bin/python3
"""
script that starts a Flask web application with an route
"""
from flask import Flask, render_template
from models import storage
from models.state import State


"""instance creation"""
app = Flask(__name__)


@app.teardown_appcontext
def teardown_context(self):
    """
    Call in this method
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    handles HTTP requests related to the status list.
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

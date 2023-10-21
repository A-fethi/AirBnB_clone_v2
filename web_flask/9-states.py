#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays a HTML page"""
    states = storage.all(State)
    return render_template("9-states.html", state=states, mode='all')


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays a HTML page"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state, mode='id')
        return render_template("9-states.html", state=state, mode='none')


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

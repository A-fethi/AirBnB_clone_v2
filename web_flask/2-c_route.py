#!usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<username>", strict_slashes=False)
def new_route(username):
    """Returns HBNB"""
    new_username = username.replace("_", " ")
    return f"C {new_username}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

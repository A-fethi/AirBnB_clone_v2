#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Displays "C ", followed by the value of the text variable
    underscore _ symbols replaced with a space"""
    new_text = text.replace("_", " ")
    return f"C {new_text}"


@app.route("/python/", strict_slashes=False)
def python_default(text="is cool"):
    """Displays the default value of text"""
    return f"Python {text}"


@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Displays "Python ", followed by the value of the text variable
    underscore _ symbols replaced with a space"""
    new_text = text.replace("_", " ")
    return f"Python {new_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays “n is a number” only if n is an integer"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

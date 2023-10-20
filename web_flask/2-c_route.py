#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Define a route that displays "Hello HBNB!"
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Define a route that displays "HBNB"
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """
    Define a route that displays "C " followed by the value of the text variable.
    Replace underscores (_) with spaces.
    """
    text = text.replace('_', ' ')
    return "C " + text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

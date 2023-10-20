#!/usr/bin/python3
"""This module starts a flask application with 6 routes."""

from web_flask import app
from flask import render_template


@app.route('/', strict_slashes=False)
def index():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display 'C' and value of 'text' underscore replaced with space"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text='is cool'):
    """Display 'Python and value of text."""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    """Display '<n> is a number' if n is int."""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp_route(n):
    """Display '<n> is a number' if n is int."""
    if isinstance(n, int):
        h1 = f"Number: {n}"
        return render_template('5-number.html', h1=h1)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_temp_route_odd_even(n):
    """Display '<n> is a number' if n is int."""
    if isinstance(n, int):
        even = n % 2 == 0
        string = 'even'
        if not even:
            string = 'odd'
        h1 = f"Number: {n} is {string}"
        return render_template('5-number.html', h1=h1)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

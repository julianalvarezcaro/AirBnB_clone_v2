#!/usr/bin/python3
"""Simple application of Flask
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    """Returns Hello HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Returns HBNB
    """
    return 'HBNB'


@app.route('/c/<string:text>')
def c_isfun(text):
    """Returns C + text
    """
    string = text.replace('_', ' ')
    return 'C ' + string


@app.route('/python')
@app.route('/python/<string:text>')
def python_iscool(text="is cool"):
    """Returns Python + text, or is cool
    """
    string = text.replace('_', ' ')
    return 'Python ' + string


@app.route('/number/<int:n>')
def number(n):
    """Returns n is a number if it is
    """
    return str(n) + " is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """Returns n is a number if it is
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_evenodd(n):
    """Returns a different header whether n is odd or even
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

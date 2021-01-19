#!/usr/bin/python3
"""Simple application of Flask
"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

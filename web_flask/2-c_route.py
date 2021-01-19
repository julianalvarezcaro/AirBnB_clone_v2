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
    """Returns Hello HBNB
    """
    return 'HBNB'


@app.route('/c/<string:text>')
def c_isfun(text):
    """Returns Hello HBNB
    """
    string = text.replace('_', ' ')
    return 'C ' + string


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

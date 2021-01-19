#!/usr/bin/python3
"""Simple application of Flask
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Returns Hello HBNB
    """
    return 'Hello HBNB!'


app.run(host="0.0.0.0", port=5000)

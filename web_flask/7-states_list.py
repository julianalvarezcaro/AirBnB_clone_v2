#!/usr/bin/python3
"""Simple application of Flask
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

data = storage.all(State)


@app.teardown_appcontext
def teardown_func(self):
    """Will excecute after each request
    Closes current sqlalchemy session
    """
    storage.close()


@app.route('/states_list')
def list_states():
    """Returns Hello HBNB
    """
    return render_template('7-states_list.html', states=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

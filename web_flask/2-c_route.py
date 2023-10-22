#!/usr/bin/python3
""" Hello Flask! """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ content of the home page """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
    """ content of hbnb page """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ display C followed by the value of the text """
    return f"C {text.replace("_", " ")}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask
from flask_sslify import SSLify


app = Flask(__name__)

SSLify(app)

file = "bla.txt"


def empty():
    with open(file, "w"):
        pass

empty()


@app.route("/get")
def get():
    with open(file, "r") as f:
        c = f.read()
    empty()
    return c


@app.route("/set")
def set():
    with open(file, "r") as f:
        f.write("true")
    return "true"

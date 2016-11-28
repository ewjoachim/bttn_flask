from flask import Flask, Response
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
    resp = Response(c)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route("/set")
def set():
    with open(file, "w") as f:
        f.write("true")

    resp = Response("true")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

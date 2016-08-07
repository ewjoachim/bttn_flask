from flask import Flask
from flask_sslify import SSLify

app = SSLify(Flask(__name__))


@app.route("/")
def hello():
    return "Hello World!"

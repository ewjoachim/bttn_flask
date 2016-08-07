from flask import Flask
from flask_sslify import SSLify


app = Flask(__name__)

SSLify(app)


@app.route("/")
def hello():
    return "Hello World!"

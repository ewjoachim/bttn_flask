from flask import Flask, Response, abort
from flask_sslify import SSLify
from datetime import date
import json

app = Flask(__name__)

SSLify(app)


@app.route("/<continent>/<region>/<int:year>/<int:month>/<int:day>")
def get(continent, region, year, month, day):
    try:
        cal_class = getattr(
            __import__("workalendar.{}".format(continent), fromlist=[region]),
            region)
        d = date(year, month, day)
    except (ImportError, AttributeError, ValueError):
        abort(404)

    holiday = cal_class().is_working_day(d)

    resp = Response(json.dumps(holiday))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

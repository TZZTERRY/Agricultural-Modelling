import os

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from agri_service.s_weather import SWeather
from agri_service.s_price import SPrice
from agri_service.s_yield import SYield
from agri_service.s_weblink import SWeblink
from agri_service.s_resource import SResource
from flask import send_from_directory
from flask import render_template, make_response
import sqlite3
from flask import g
import json

app = Flask(__name__)

REGION_SHORT_NAME = (("nsw", "NSW.html"),
                     ("vic", "VIC.html"),
                     ("qld", "QLD.html"),
                     ("tas", "TAS.html"),
                     ("wa", "WA.html"),
                     ("sa", "SA.html"))

DATABASE = 'agri_database/agri_db'


@app.route('/home/')
def hello_world():
    return render_template("HomePage.html")


@app.route('/about/')
def about_page():
    return render_template("AboutPage.html")


@app.route('/overview/')
def overview_page():
    return render_template("AustraliaOverview.html")

@app.route('/download/')
def download_page():
    return render_template('Download.html')


@app.route('/region/<short_name>/')
def region_page(short_name):
    short_name_lower = short_name.lower()

    for n, html_file in REGION_SHORT_NAME:
        if short_name_lower == n:
            return render_template(html_file)

    raise Exception("No such region short name: "+short_name)


@app.route('/weather', methods=['GET', 'POST'])
def get_weather_data():
    region = request.args.get('region')
    vtype = request.args.get('vtype')

    print("region: ", region)
    print("vtype: ", vtype)

    return my_response(weather_obj.get_data())


@app.route('/price', methods=['GET', 'POST'])
def get_price_data():
    region = request.args.get("region")
    ispre = request.args.get("ispre")
    starty = request.args.get('starty')
    endy = request.args.get('endy')
    cropid = request.args.get('cropid')

    print("region: ", region)
    print("ispre: ", ispre)
    print("starty: ", starty)
    print("endy: ", endy)
    print("cropid: ", cropid)

    return my_response(price_obj.get_data())


@app.route('/yield', methods=['GET', 'POST'])
def get_yield_data():
    region = request.args.get("region")
    ispre = request.args.get("ispre")
    starty = request.args.get('starty')
    endy = request.args.get('endy')
    cropid = request.args.get('cropid')

    cropid = int(cropid)
    ispre = int(ispre)

    res = query_db(f"select * from yield_price "
             f"where crop_id = {cropid} and region_name = '{region}' and is_predict = {ispre}")
    years = []
    values = []

    crop_name = res[0]["crop_name"]
    for r in res:
        years.append(r["year"])
        values.append(r['yield'])
    json_obj = {"years": years, "values": values, "crop name": crop_name, "cropid": cropid, "isPredict": ispre, "regionName": region}
    return my_response(json.dumps(json_obj))


@app.route('/weblink', methods=['GET', 'POST'])
def get_weblink():
    return my_response(weather_obj.get_data())


@app.route('/resource', methods=['GET', 'POST'])
def get_resource():
    resourceid = request.args.get('resourceid')
    type_num = int(request.args.get('type'))
    file_format = request.args.get('file_format')

    return resource_obj.get_data(resourceid, type_num, file_format)
    # return send_from_directory("", resource_path)


def my_response(my_body):
    res = make_response(my_body)
    res.status = '200'
    res.headers['Access-Control-Allow-Origin'] = "*"
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET'
    return res


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


if __name__ == "__main__":
    weather_obj = SWeather()
    price_obj = SPrice()
    yield_obj = SYield()
    weblink_obj = SWeblink()
    resource_obj = SResource()
    app.run(host='0.0.0.0', debug=True)

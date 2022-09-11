from flask import Flask
from flask import request
from flask import jsonify
from agri_service.s_weather import SWeather
from agri_service.s_price import SPrice
from agri_service.s_yield import SYield
from agri_service.s_weblink import SWeblink
from agri_service.s_resource import SResource

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/weather', methods=['GET', 'POST'])
def get_weather_data():
    region = request.args.get('region')
    vtype = request.args.get('vtype')

    print("region: ", region)
    print("vtype: ", vtype)

    return weather_obj.get_data()


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

    return price_obj.get_data()


@app.route('/yield', methods=['GET', 'POST'])
def get_yield_data():
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

    return yield_obj.get_data()


@app.route('/weblink', methods=['GET', 'POST'])
def get_weblink():
    return weather_obj.get_data()


@app.route('/resource', methods=['GET', 'POST'])
def get_resource():
    resourceid = request.args.get('resourceid')
    type = request.args.get('type')

    print("resourceid: ", resourceid)
    print("type: ", type)
    return resource_obj.get_data()


if __name__ == "__main__":
    weather_obj = SWeather()
    price_obj = SPrice()
    yield_obj = SYield()
    weblink_obj = SWeblink()
    resource_obj = SResource()
    app.run(host='0.0.0.0', debug=True)

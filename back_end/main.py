from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/weather', methods=['GET', 'POST'])
def get_weather_data():
    region = request.args.get('region')
    vtype = request.args.get('vtype')

    print("region: ", region)
    print("vtype: ", vtype)

    return "Pass"


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

    return "Pass"


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

    return "Pass"


@app.route('/weblink', methods=['GET', 'POST'])
def get_weblink():
    return "Pass"


@app.route('/resource', methods=['GET', 'POST'])
def get_resource():
    resourceid = request.args.get('resourceid')
    type = request.args.get('type')

    print("resourceid: ", resourceid)
    print("type: ", type)
    return "Pass"

if __name__ == "__main__":
    app.run(port=8080, host="localhost", debug=True)

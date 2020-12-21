# server manages the routing of request and response
from flask import Flask, request, jsonify, render_template
#import util
import server.util as util

app = Flask(__name__, static_url_path='/client', static_folder='../client', template_folder='../client')

@app.route('/')
def index():
    if request.method == "GET":
        return render_template("app.html")

@app.route('/get_location_names') #expose http end point, get = when a user loads the website
def get_location_names():
    response = jsonify({ #to return a json object
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST']) # the default method is get, post when a user submits some input
def predict_home_price():
    total_sqft = float(request.form['total_sqft']) #extract data incoming from users like dictionary
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    reponse = jsonify({
        'estimated_price' : util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    reponse.headers.add('Access-Control-Allow-Origin', '*')
    return reponse

if __name__ == "__main__":
    print("Starting Python Flask Server for Home price predictions...")
    app.run(debug=True)
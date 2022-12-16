from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient('localhost', 27017)
# client = MongoClient('localhost', 27017, username='username', password='password') put authentication
db = client.flask_db
raw_data = db.raw_data

#static data for now

obj1 = {
	"criteria": {
		"Comfort" : {
		     "Luminosity" : {
                "Room 1" : 1,
                "Room 2" : 4,
                "Room 3" : 9
             },
		     "Temperature" : {
                "Room 1" : 1,
                "Room 2" : 1,
                "Room 3" : 1
             },
		     "Noise" : {
                "Room 1" : 1,
                "Room 2" : 1,
                "Room 3" : 1
             }
		},
		"Health": {
			"CO2" : {
                "Room 1" : 1,
                "Room 2" : 1,
                "Room 3" : 1
             },
		     "Humidity" : {
                "Room 1" : 1,
                "Room 2" : 1,
                "Room 3" : 1
             },
		     "Air Pressure" : {
                "Room 1" : 1,
                "Room 2" : 1,
                "Room 3" : 1
             }
        },
		"Usage":{
			"Furniture" : {
                "Room 1" : 1,
                "Room 2" : 1,
                "Room 3" : 1
             },
		     "Accessibility" : {
                "Room 1" : 1,
                "Room 2" : 1,
                "Room 3" : 1
             }
		}
	}
}

ROOMS = [obj1]

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/getfrom_rpi', methods=('GET', 'POST'))
def create_record():
    if request.method == 'POST':
        print("post")
        record = json.loads(request.data)
        raw_data.insert_one(record)
        return redirect(url_for('index')) 
    print("get")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

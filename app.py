from flask import Flask, render_template, request, url_for, redirect
import pymongo
import os
from pymongo import MongoClient
import json

app = Flask(__name__)

#static data for now
client = MongoClient(host=os.environ['MONGODB_HOSTNAME'],
                         port=27017, 
                         username=os.environ['MONGODB_USERNAME'], 
                         password=os.environ['MONGODB_PASSWORD'],
                        authSource="admin")
db = client.flask_db
raw_data = db.raw_data
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

def get_db():
    client = MongoClient(host=os.environ['MONGODB_HOSTNAME'],
                         port=27017, 
                         username=os.environ['MONGODB_USERNAME'], 
                         password=os.environ['MONGODB_PASSWORD'],
                        authSource="admin")
    db = client["db"]
    return db

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

@app.route('/table1')
def get_table1():
    db = get_db()
    _table1 = db.table1.find()
    table1 = [{"id": entry["id"], "name": entry["name"], "type": entry["type"]} for entry in _table1]
    return jsonify({"table1": table1})

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
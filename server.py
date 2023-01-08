from flask import Flask, render_template, request, url_for, redirect, jsonify
from pymongo import MongoClient
from flask_mqtt import Mqtt
import json

app = Flask(__name__)

client = MongoClient('localhost', 27017)
# client = MongoClient('localhost', 27017, username='username', password='password') # put authentication
db = client.local
raw_data = db.raw_data

# static data for now
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


# MQTT configuration

app.config['MQTT_BROKER_URL'] = 'broker.emqx.io'
app.config['MQTT_BROKER_PORT'] = 1883
# app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
# app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
app.config['MQTT_TLS_ENABLED'] = False  # If your server supports TLS, set it True
topic = '/flask/mqtt'
mqtt_client = Mqtt(app)


@mqtt_client.on_connect()
def handle_connect(clients, userdata, flags, rc):
   if rc == 0:
       print('Connected successfully')
       mqtt_client.subscribe(topic) # subscribe topic
   else:
       print('Bad connection. Code:', rc)

@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
   data = dict(
       topic=message.topic,
       payload=message.payload.decode()
  )
   print('Received message on topic: {topic} with payload: {payload}'.format(**data))


@app.route('/publish', methods=['POST'])
def publish_message():
   request_data = request.get_json()
   publish_result = mqtt_client.publish(request_data['topic'], request_data['msg'])
   return jsonify({'code': publish_result[0]})  

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/getfrom_rpi', methods=('GET', 'POST'))
def create_record():
    print("test")
    if request.method == 'POST':
        print("post")
        record = json.loads(request.data)
        raw_data.insert_one(record)
        return render_template('index.html')
    print("get")
    return render_template('index.html')

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000)
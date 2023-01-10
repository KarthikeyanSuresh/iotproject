# This file contains all the necessary helper functions for the functioning of the application

import json
import random


# Static JSON object is updated with values imported from different Arduino sensor payloads, one for each room 
# Values unobtainable from the Arduino sensors are initialized with a random value and modeled in a later function
def addRoomToObject(i, msg, obj):
    # Convert iterating variable to string ot append it to the JSON object as a room number 
    i = str(i)

    # Appends data to the existing object for a room number specified by the iterating variable
    obj["criteria"]["Comfort"]["Luminosity"]["Room " + i] = msg["light"]
    obj["criteria"]["Comfort"]["Temperature"]["Room " + i] = msg["temperature"]
    obj["criteria"]["Comfort"]["Noise"]["Room " + i] = msg["noise"]
    obj["criteria"]["Health"]["Humidity"]["Room " + i] = msg["humidity"]
    obj["criteria"]["Health"]["CO2"]["Room " + i] = 0
    obj["criteria"]["Health"]["Air Pressure"]["Room " + i] = 0
    obj["criteria"]["Usage"]["Furniture"]["Room " + i] = 1
    obj["criteria"]["Usage"]["Accessibility"]["Room " + i] = 1

    return obj


def modelValues(obj):
    # Creating and adding modeled data for CO2, Air Pressure, Furniture and Accessibility
    for room in obj["criteria"]["Health"]["Air Pressure"]:
        obj["criteria"]["Health"]["Air Pressure"][room] = 101325 + random.randint(-1000, 1500)
        # print(obj["criteria"]["Health"]["Air Pressure"][room])

    for room in obj["criteria"]["Health"]["CO2"]:
        obj["criteria"]["Health"]["CO2"][room] = 600 + random.randint(-500, 500)
        #  print(obj["criteria"]["Health"]["CO2"][room])
    
    for room in obj["criteria"]["Usage"]["Accessibility"]:
        obj["criteria"]["Usage"]["Accessibility"][room] = 1 + random.randint(-3, 0)*0.1
    
    for room in obj["criteria"]["Usage"]["Furniture"]:
        obj["criteria"]["Usage"]["Furniture"][room] = 1 + random.randint(-3, 0)*0.1        



def cleanValues(obj):
    # Normalization
    for keys in obj['criteria']:
        for key in obj["criteria"][keys]:
            for room in obj["criteria"][keys][key]:

                # Normalizing Luminance Data
                if key == "Luminosity":
                    if obj["criteria"][keys][key][room] >= 73:
                        obj["criteria"][keys][key][room] = 0.001
                    elif obj["criteria"][keys][key][room] < 73 and obj["criteria"][keys][key][room] >= 43:
                        obj["criteria"][keys][key] = 1
                    elif obj["criteria"][keys][key][room] < 43 and obj["criteria"][keys][key][room] >= 23:
                        obj["criteria"][keys][key][room] = 0.5
                    else:
                        obj["criteria"][keys][key][room] = 0.001
            

                # Normalizing Noise Data
                elif key == "Noise":
                    if obj["criteria"][keys][key][room] <= 55:
                        obj["criteria"][keys][key][room] = 1
                    elif obj["criteria"][keys][key][room] > 55 and obj["criteria"][keys][key][room] <= 70:
                        obj["criteria"][keys][key][room] = 0.8
                    elif obj["criteria"][keys][key][room] > 70 and obj["criteria"][keys][key][room] <= 80:
                        obj["criteria"][keys][key][room] = 0.5
                    elif obj["criteria"][keys][key][room] > 80 and obj["criteria"][keys][key][room] <= 85:
                        obj["criteria"][keys][key][room] = 0.2
                    else:
                        obj["criteria"][keys][key][room] = 0.001
                

                # Normalizing Temperature Data
                elif key == "Humidity":
                    if obj["criteria"][keys][key][room] <= 10:
                        obj["criteria"][keys][key][room] = 0.001
                    elif obj["criteria"][keys][key][room] > 10 and obj["criteria"][keys][key][room] <= 20:
                        obj["criteria"][keys][key][room] = 0.2
                    elif obj["criteria"][keys][key][room] > 20 and obj["criteria"][keys][key][room] <= 30:
                        obj["criteria"][keys][key][room] = 0.5
                    elif obj["criteria"][keys][key][room] > 30 and obj["criteria"][keys][key][room] <= 40:
                        obj["criteria"][keys][key][room] = 0.8
                    elif obj["criteria"][keys][key][room] > 40 and obj["criteria"][keys][key][room] <= 50:
                        obj["criteria"][keys][key][room] = 1
                    elif obj["criteria"][keys][key][room] > 50 and obj["criteria"][keys][key][room] <= 60:
                        obj["criteria"][keys][key][room] = 0.6
                    elif obj["criteria"][keys][key][room] > 60 and obj["criteria"][keys][key][room] <= 80:
                        obj["criteria"][keys][key][room] = 0.2
                    else:
                        obj["criteria"][keys][key][room] = 0.001
                                    
                
                # Normalizing Humidity Data
                elif key == "Temperature":
                    if obj["criteria"][keys][key][room] <= 15:
                        obj["criteria"][keys][key][room] = 0.001
                    elif obj["criteria"][keys][key][room] > 15 and obj["criteria"][keys][key][room] <= 18:
                        obj["criteria"][keys][key][room] = 0.4
                    elif obj["criteria"][keys][key][room] > 18 and obj["criteria"][keys][key][room] <= 22:
                        obj["criteria"][keys][key][room] = 1
                    elif obj["criteria"][keys][key][room] > 22 and obj["criteria"][keys][key][room] <= 25:
                        obj["criteria"][keys][key][room] = 0.5
                    elif obj["criteria"][keys][key][room] > 25 and obj["criteria"][keys][key][room] <= 28:
                        obj["criteria"][keys][key][room] = 0.3
                    elif obj["criteria"][keys][key][room] > 28 and obj["criteria"][keys][key][room] <= 30:
                        obj["criteria"][keys][key][room] = 0.1
                    else:
                        obj["criteria"][keys][key][room] = 0.001


                # Normalizing CO2 Data                        
                elif key == "CO2":
                    if obj["criteria"][keys][key][room] >= 10000:
                        obj["criteria"][keys][key][room] = 0.001
                    elif obj["criteria"][keys][key][room] < 10000 and obj["criteria"][keys][key][room] >= 4000:
                        obj["criteria"][keys][key][room] = 0.2
                    elif obj["criteria"][keys][key][room] < 4000 and obj["criteria"][keys][key][room] >= 2000:
                        obj["criteria"][keys][key][room] = 0.4
                    elif obj["criteria"][keys][key][room] < 2000 and obj["criteria"][keys][key][room] >= 1000:
                        obj["criteria"][keys][key][room] = 0.5
                    elif obj["criteria"][keys][key][room] < 1000 and obj["criteria"][keys][key][room] >= 400:
                        obj["criteria"][keys][key][room] = 0.8
                    else:  
                        obj["criteria"][keys][key][room] = 1


                # Normalizing Air Pressure Data                        
                elif key == "Air Pressure":
                    if obj["criteria"][keys][key][room] <= 100000:
                        obj["criteria"][keys][key][room] = 0.001
                    elif obj["criteria"][keys][key][room] > 100000 and obj["criteria"][keys][key][room] <= 100300:
                        obj["criteria"][keys][key][room] = 0.3
                    elif obj["criteria"][keys][key][room] > 100300 and obj["criteria"][keys][key][room] <= 100800:
                        obj["criteria"][keys][key][room] = 0.5
                    elif obj["criteria"][keys][key][room] > 100800 and obj["criteria"][keys][key][room] <= 101300:
                        obj["criteria"][keys][key][room] = 0.8
                    elif obj["criteria"][keys][key][room] > 101300 and obj["criteria"][keys][key][room] <= 101900:
                        obj["criteria"][keys][key][room] = 1
                    elif obj["criteria"][keys][key][room] > 101900 and obj["criteria"][keys][key][room] <= 103000:
                        obj["criteria"][keys][key][room] = 0.5
                    else:
                        obj["criteria"][keys][key][room] = 0.001


# msg is a JSON object array containing the payloads from the rooms (number determined beforehand), it is to be created from the different databases using another function
def processRawData(msg):
    # object skeleton with initialized values that will be overwritten and new room data can be appended when iterated in a loop
    obj = {
        "criteria": {
            "Comfort" : {
                "Luminosity" : {
                        "Room 1" : 0
                    },
                "Temperature" : {
                        "Room 1" : 0
                    },
                "Noise" : {
                        "Room 1" : 0
                    }
            },
            "Health": {
                "CO2" : {
                    "Room 1" : 400
                    },
                "Humidity" : {
                    "Room 1" : 0
                    },
                "Air Pressure" : {
                    "Room 1" : 103000
                    }
            },
            "Usage":{
                "Furniture" : {
                    "Room 1" : 1
                    },
                "Accessibility" : {
                    "Room 1" : 0.7
                    }
                }
            }
        }

    # iterating considering 5 rooms in this case
    for i in range (1,6):
        addRoomToObject(i, msg[i], obj)

    # print(json.dumps(obj, sort_keys=True, indent=4))
    return obj 
    

def createJSONobjectArray(k):
    msg = []
    # get payload from each database and add it to the array, using index variable k 

    # Do this for each db
    # payload = object from db query
    # msg.append(payload)
    return msg


# Start Process
# Generate a random value to query the databases with
# Call createJSONobjectArray() and obtain "msg", the list of the payloads collected from the Arduino values databases for each room
# Call processRawData(msg), which creates a skeletal object and iterates n times (n set beforehand) and in turn calls addRoomToObject(i, msg, obj)
# Call modelValues(obj), which models the values for the criteria for which data cannot be obtained from the Arduino
# Send the modeled JSON object to database to store for admin use
# Call cleanValues(obj), which normalizes the values of the object based on the optimal value ranges obtained from research
# Now the data is usable for ahp.py for AHP calculations 

def startProcess():
    k = random(0,1440)
    msg = createJSONobjectArray(k)
    obj = processRawData(msg)
    modelValues(obj)
    cleanValues(obj)
    return obj
# This file contains all the necessary helper functions for the functioning of the application

import json
import random


# Static JSON object is updated with values imported from three different Arduino sensor payloads, one for each room; values unobtainable from the Arduino sensors are initialized with a random value and modeled in a later function
def createObject(msg1, msg2, msg3):

    obj = {
        "criteria": {
            "Comfort" : {
                "Luminosity" : {
                    "Room 1" : msg1["light"],
                    "Room 2" : msg2["light"],
                    "Room 3" : msg3["light"]
                },
                "Temperature" : {
                    "Room 1" : msg1["temperature"],
                    "Room 2" : msg2["temperature"],
                    "Room 3" : msg3["temperature"]
                },
                "Noise" : {
                    "Room 1" : msg1["noise"],
                    "Room 2" : msg2["noise"],
                    "Room 3" : msg3["noise"]
                }
            },
            "Health": {
                "CO2" : {
                    "Room 1" : 400,
                    "Room 2" : 350,
                    "Room 3" : 1000
                },
                "Humidity" : {
                    "Room 1" : msg1["humidity"],
                    "Room 2" : msg2["humidity"],
                    "Room 3" : msg3["humidity"]
                },
                "Air Pressure" : {
                    "Room 1" : 103000,
                    "Room 2" : 101325,
                    "Room 3" : 100000
                }
            },
            "Usage":{
                "Furniture" : {
                    "Room 1" : 1,
                    "Room 2" : 0.7,
                    "Room 3" : 0.6
                },
                "Accessibility" : {
                    "Room 1" : 0.7,
                    "Room 2" : 1,
                    "Room 3" : 0.8
                }
            }
        }
    }
    return obj


def modelValues(obj):
    # Creating and adding modeled data for CO2 and Airpressure
    for room in obj["criteria"]["Health"]["Air Pressure"]:
        obj["criteria"]["Health"]["Air Pressure"][room] = 101325 + random.randint(-1000, 1500)
        # print(obj["criteria"]["Health"]["Air Pressure"][room])

    for room in obj["criteria"]["Health"]["CO2"]:
        obj["criteria"]["Health"]["CO2"][room] = 600 + random.randint(-500, 500)
        #  print(obj["criteria"]["Health"]["CO2"][room])


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


def processRawData(msg1, msg2, msg3):
    obj = createObject(msg1, msg2, msg3)
    # print(json.dumps(obj, sort_keys=True, indent=4))
    modelValues(obj)
    cleanValues(obj)



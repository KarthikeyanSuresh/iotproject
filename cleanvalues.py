import os
import json


obj = {
    "criteria": {
        "Comfort": {
            "Luminosity": 43,
            "Noise": 20,
            "Temperature": 24
        },
        "Health": {
            "CO2": 1,
            "Humidity": 45,
            "Pressure": 1
        },
        "Usage": {
            "Cost": 1,
            "Furniture": 1
        }
    },
    "options": [
        "Room 1",
        "Room 2",
        "Room 3"
    ]
}


for keys in obj['criteria']:
  for key in obj["criteria"][keys]:

    # Normalizing Luminance Data
    if key == "Luminosity":
        if obj["criteria"][keys][key] >= 73:
            obj["criteria"][keys][key] = 0
        else:
            if obj["criteria"][keys][key] < 73 and obj["criteria"][keys][key] >= 43:
                obj["criteria"][keys][key] = 1
            else: 
                if obj["criteria"][keys][key] < 43 and obj["criteria"][keys][key] >= 23:
                    obj["criteria"][keys][key] = 0.5
                else:
                    obj["criteria"][keys][key] = 0
    

    # Normalizing Noise Data
    if key == "Noise":
        if obj["criteria"][keys][key] <= 55:
            obj["criteria"][keys][key] = 1
        else:
            if obj["criteria"][keys][key] > 55 and obj["criteria"][keys][key] <= 70:
                obj["criteria"][keys][key] = 0.8
            else: 
                if obj["criteria"][keys][key] > 70 and obj["criteria"][keys][key] <= 80:
                    obj["criteria"][keys][key] = 0.5
                else:
                    if obj["criteria"][keys][key] > 80 and obj["criteria"][keys][key] <= 85:
                        obj["criteria"][keys][key] = 0.2
                    else:
                        obj["criteria"][keys][key] = 0
    

    # Normalizing Temperature Data
    if key == "Humidity":
        if obj["criteria"][keys][key] <= 10:
            obj["criteria"][keys][key] = 0
        else:
            if obj["criteria"][keys][key] > 10 and obj["criteria"][keys][key] <= 20:
                obj["criteria"][keys][key] = 0.2
            else: 
                if obj["criteria"][keys][key] > 20 and obj["criteria"][keys][key] <= 30:
                    obj["criteria"][keys][key] = 0.5
                else:
                    if obj["criteria"][keys][key] > 30 and obj["criteria"][keys][key] <= 40:
                        obj["criteria"][keys][key] = 0.8
                    else:
                        if obj["criteria"][keys][key] > 40 and obj["criteria"][keys][key] <= 50:
                            obj["criteria"][keys][key] = 1
                        else:  
                            if obj["criteria"][keys][key] > 50 and obj["criteria"][keys][key] <= 60:
                                obj["criteria"][keys][key] = 0.6
                            else:
                                if obj["criteria"][keys][key] > 60 and obj["criteria"][keys][key] <= 80:
                                    obj["criteria"][keys][key] = 0.2
                                else:
                                    obj["criteria"][keys][key] = 0
                        
    
    # Normalizing Humidity Data
    if key == "Temperature":
        if obj["criteria"][keys][key] <= 15:
            obj["criteria"][keys][key] = 0
        else:
            if obj["criteria"][keys][key] > 15 and obj["criteria"][keys][key] <= 18:
                obj["criteria"][keys][key] = 0.4
            else: 
                if obj["criteria"][keys][key] > 18 and obj["criteria"][keys][key] <= 22:
                    obj["criteria"][keys][key] = 1
                else:
                    if obj["criteria"][keys][key] > 22 and obj["criteria"][keys][key] <= 25:
                        obj["criteria"][keys][key] = 0.5
                    else:
                        if obj["criteria"][keys][key] > 25 and obj["criteria"][keys][key] <= 28:
                            obj["criteria"][keys][key] = 0.3
                        else:  
                            if obj["criteria"][keys][key] > 28 and obj["criteria"][keys][key] <= 30:
                                obj["criteria"][keys][key] = 0.1
                            else:
                                obj["criteria"][keys][key] = 0


    # Normalizing Humidity Data                        
    if key == "CO2":
        if obj["criteria"][keys][key] <= 15:
            obj["criteria"][keys][key] = 0
        else:
            if obj["criteria"][keys][key] > 15 and obj["criteria"][keys][key] <= 18:
                obj["criteria"][keys][key] = 0.4
            else: 
                if obj["criteria"][keys][key] > 18 and obj["criteria"][keys][key] <= 22:
                    obj["criteria"][keys][key] = 1
                else:
                    if obj["criteria"][keys][key] > 22 and obj["criteria"][keys][key] <= 25:
                        obj["criteria"][keys][key] = 0.5
                    else:
                        if obj["criteria"][keys][key] > 25 and obj["criteria"][keys][key] <= 28:
                            obj["criteria"][keys][key] = 0.3
                        else:  
                            if obj["criteria"][keys][key] > 28 and obj["criteria"][keys][key] <= 30:
                                obj["criteria"][keys][key] = 0.1
                            else:
                                obj["criteria"][keys][key] = 0
                        

        # print(obj["criteria"][keys][key])

    




print(json.dumps(obj, sort_keys=True, indent=4))
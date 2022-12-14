import os
import json

obj = {
	"criteria": {
		"Comfort" : {
		     "Luminosity" : {
                "Room 1" : 25,
                "Room 2" : 4,
                "Room 3" : 90
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


for keys in obj['criteria']:
  for key in obj["criteria"][keys]:
    for room in obj["criteria"][keys][key]:

    # Normalizing Luminance Data
        if key == "Luminosity":
            if obj["criteria"][keys][key][room] >= 73:
                obj["criteria"][keys][key][room] = 0
            else:
                if obj["criteria"][keys][key][room] < 73 and obj["criteria"][keys][key][room] >= 43:
                    obj["criteria"][keys][key] = 1
                else: 
                    if obj["criteria"][keys][key][room] < 43 and obj["criteria"][keys][key][room] >= 23:
                        obj["criteria"][keys][key][room] = 0.5
                    else:
                        obj["criteria"][keys][key][room] = 0
    

    # Normalizing Noise Data
    if key == "Noise":
        if obj["criteria"][keys][key][room] <= 55:
            obj["criteria"][keys][key][room] = 1
        else:
            if obj["criteria"][keys][key][room] > 55 and obj["criteria"][keys][key][room] <= 70:
                obj["criteria"][keys][key][room] = 0.8
            else: 
                if obj["criteria"][keys][key][room] > 70 and obj["criteria"][keys][key][room] <= 80:
                    obj["criteria"][keys][key][room] = 0.5
                else:
                    if obj["criteria"][keys][key][room] > 80 and obj["criteria"][keys][key][room] <= 85:
                        obj["criteria"][keys][key][room] = 0.2
                    else:
                        obj["criteria"][keys][key][room] = 0
    

    # Normalizing Temperature Data
    if key == "Humidity":
        if obj["criteria"][keys][key][room] <= 10:
            obj["criteria"][keys][key][room] = 0
        else:
            if obj["criteria"][keys][key][room] > 10 and obj["criteria"][keys][key][room] <= 20:
                obj["criteria"][keys][key][room] = 0.2
            else: 
                if obj["criteria"][keys][key][room] > 20 and obj["criteria"][keys][key][room] <= 30:
                    obj["criteria"][keys][key][room] = 0.5
                else:
                    if obj["criteria"][keys][key][room] > 30 and obj["criteria"][keys][key][room] <= 40:
                        obj["criteria"][keys][key][room] = 0.8
                    else:
                        if obj["criteria"][keys][key][room] > 40 and obj["criteria"][keys][key][room] <= 50:
                            obj["criteria"][keys][key][room] = 1
                        else:  
                            if obj["criteria"][keys][key][room] > 50 and obj["criteria"][keys][key][room] <= 60:
                                obj["criteria"][keys][key][room] = 0.6
                            else:
                                if obj["criteria"][keys][key][room] > 60 and obj["criteria"][keys][key][room] <= 80:
                                    obj["criteria"][keys][key][room] = 0.2
                                else:
                                    obj["criteria"][keys][key][room] = 0
                        
    
    # Normalizing Humidity Data
    if key == "Temperature":
        if obj["criteria"][keys][key][room] <= 15:
            obj["criteria"][keys][key][room] = 0
        else:
            if obj["criteria"][keys][key][room] > 15 and obj["criteria"][keys][key][room] <= 18:
                obj["criteria"][keys][key][room] = 0.4
            else: 
                if obj["criteria"][keys][key][room] > 18 and obj["criteria"][keys][key][room] <= 22:
                    obj["criteria"][keys][key][room] = 1
                else:
                    if obj["criteria"][keys][key][room] > 22 and obj["criteria"][keys][key][room] <= 25:
                        obj["criteria"][keys][key][room] = 0.5
                    else:
                        if obj["criteria"][keys][key][room] > 25 and obj["criteria"][keys][key][room] <= 28:
                            obj["criteria"][keys][key][room] = 0.3
                        else:  
                            if obj["criteria"][keys][key][room] > 28 and obj["criteria"][keys][key][room] <= 30:
                                obj["criteria"][keys][key][room] = 0.1
                            else:
                                obj["criteria"][keys][key][room] = 0


    # Normalizing CO2 Data                        
    if key == "CO2":
        if obj["criteria"][keys][key][room] <= 15:
            obj["criteria"][keys][key][room] = 0
        else:
            if obj["criteria"][keys][key][room] > 15 and obj["criteria"][keys][key][room] <= 18:
                obj["criteria"][keys][key][room] = 0.4
            else: 
                if obj["criteria"][keys][key][room] > 18 and obj["criteria"][keys][key][room] <= 22:
                    obj["criteria"][keys][key][room] = 1
                else:
                    if obj["criteria"][keys][key][room] > 22 and obj["criteria"][keys][key][room] <= 25:
                        obj["criteria"][keys][key][room] = 0.5
                    else:
                        if obj["criteria"][keys][key][room] > 25 and obj["criteria"][keys][key][room] <= 28:
                            obj["criteria"][keys][key][room] = 0.3
                        else:  
                            if obj["criteria"][keys][key][room] > 28 and obj["criteria"][keys][key][room] <= 30:
                                obj["criteria"][keys][key][room] = 0.1
                            else:
                                obj["criteria"][keys][key][room] = 0
                        

        # print(obj["criteria"][keys][key])

    




print(json.dumps(obj, sort_keys=True, indent=4))

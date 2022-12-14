import ahpy
import json
import itertools

def make_pairs(crit):
   return list(itertools.combinations(crit, 2))

def get_values(val_dict, obj):
   for key1 in obj['criteria']:
      for key2 in obj["criteria"][key1]:
         val = []
         for key3 in obj["criteria"][key1][key2]:
            val.append(obj["criteria"][key1][key2][key3])
         val_dict[key2] = val
   return val_dict


# Sample JSON
obj ={
    "criteria": {
        "Comfort": {
            "Luminosity": {
                "Room 1": 0.5,
                "Room 2": 0.001,
                "Room 3": 0.001
            },
            "Noise": {
                "Room 1": 1,
                "Room 2": 0.8,
                "Room 3": 0.5
            },
            "Temperature": {
                "Room 1": 0.001,
                "Room 2": 0.5,
                "Room 3": 0.1
            }
        },
        "Health": {
            "Air Pressure": {
                "Room 1": 0.5,
                "Room 2": 0.8,
                "Room 3": 0.5
            },
            "CO2": {
                "Room 1": 1,
                "Room 2": 1,
                "Room 3": 0.8
            },
            "Humidity": {
                "Room 1": 0.2,
                "Room 2": 0.5,
                "Room 3": 0.6
            }
        },
        "Usage": {
            "Accessibility": {
                "Room 1": 0.7,
                "Room 2": 1,
                "Room 3": 0.8
            },
            "Furniture": {
                "Room 1": 1,
                "Room 2": 0.7,
                "Room 3": 0.6
            }
        }
    }
}

room = obj['criteria']['Comfort']['Luminosity'].keys()

criteria_pairs = make_pairs(obj['criteria'].keys())
comfort_pairs = make_pairs(obj['criteria']['Comfort'].keys())
health_pairs = make_pairs(obj['criteria']['Health'].keys())
usage_pairs = make_pairs(obj['criteria']['Usage'].keys())
room_pairs = make_pairs(obj['criteria']['Comfort']['Luminosity'].keys())

val_dict = {}
val_dict = get_values(val_dict, obj)

print(val_dict)

# Normalizing data (maybe Karthik can send data that is ready so normalizing is not needed anymore)

luminosity_data = dict(zip(room, val_dict["Luminosity"]))
luminosity_normalized = ahpy.Compare('Luminosity', luminosity_data, precision=3)
temperature_data = dict(zip(room, val_dict["Temperature"]))
temperature_normalized = ahpy.Compare('Temperature', temperature_data, precision=3)
noise_data = dict(zip(room, val_dict["Noise"]))
noise_normalized = ahpy.Compare('Noise', noise_data, precision=3)
co2_data = dict(zip(room, val_dict["CO2"]))
co2_normalized = ahpy.Compare('CO2', co2_data, precision=3)
humidity_data = dict(zip(room, val_dict["Humidity"]))
humidity_normalized = ahpy.Compare('Humidity', humidity_data, precision=3)
airpressure_data = dict(zip(room, val_dict["Air Pressure"]))
airpressure_normalized = ahpy.Compare('Air Pressure', airpressure_data, precision=3)
furniture_data = dict(zip(room, val_dict["Furniture"]))
furniture_normalized = ahpy.Compare('Furniture', furniture_data, precision=3)
accessibility_data = dict(zip(room, val_dict["Accessibility"]))
accessibility_normalized = ahpy.Compare('Accessibility', accessibility_data, precision=3)

print(luminosity_normalized.local_weights)
print(temperature_normalized.local_weights)

#Criteria comparisons
#For now, everything is 1 (generic) but need to change when advanced is made
comfort_comparisons = dict(zip(comfort_pairs, itertools.repeat(1)))
health_comparisons = dict(zip(health_pairs, itertools.repeat(1)))
usage_comparisons = dict(zip(usage_pairs, itertools.repeat(1)))

criteria_comparisons = dict(zip(criteria_pairs, itertools.repeat(1)))

#Making the tree
compose = ahpy.Compose()

compose.add_comparisons([luminosity_normalized, temperature_normalized, noise_normalized, co2_normalized, humidity_normalized, airpressure_normalized, 
furniture_normalized, accessibility_normalized])

comparisons = [('Comfort', comfort_comparisons, 3), ('Health', health_comparisons, 3), ('Usage', usage_comparisons, 3), ('Criteria', criteria_comparisons, 3)]
compose.add_comparisons(comparisons)

#Make heirarchy
hierarchy = {'Criteria': ['Comfort', 'Health', 'Usage'],
'Comfort': ['Luminosity', 'Temperature', 'Noise'],
'Health': ['CO2', 'Humidity', 'Air Pressure'],
'Usage': ['Furniture', 'Accessibility']
}

compose.add_hierarchy(hierarchy)

criteria_report = compose.report('Criteria', show=True)
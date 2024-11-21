import requests
import json
import sys

URL="http://127.0.0.1:1026/ngsi-ld/v1/entities/"
HEADERS = {
    'Accept': 'application/ld+json',
    'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
    'Content-Type': 'application/json',
    'Connection':'close'
}

def create_entity(json_obj):
    payload = json.dumps(json_obj)
    response = requests.request("POST", URL, headers=HEADERS, data=payload)
    if(response.status_code > 299):

        print(str(response.status_code))


# Open the file
with open('templates/buses/bus/bus.json') as f:
    # Load the JSON data from the file
    bus_data = json.load(f)

with open('templates/buses/bus/busAreas.json') as f:
    # Load the JSON data from the file
    bus_area_data = json.load(f)

with open('templates/buses/bus/devices.json') as f:
    # Load the JSON data from the file
    devices = json.load(f)

with open('templates/buses/bus/observations.json') as f:
    # Load the JSON data from the file
    observations = json.load(f)

# Use the data
# print(bus_area_data)

def replace_value(obj, target, new_value):
    if isinstance(obj, str):
        return obj.replace(target, new_value)
    elif isinstance(obj, dict):
        return {k: replace_value(v, target, new_value) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_value(elem, target, new_value) for elem in obj]
    else:
        return obj

if __name__ == "__main__":

    bus_id = sys.argv[1]
    bus = replace_value(bus_data, "$1", bus_id)
    bus_areas = replace_value(bus_area_data, "$1", bus_id)
    devices = replace_value(devices, "$1", bus_id)
    observations = replace_value(observations, "$1", bus_id)


    # print(bus)
    # print(bus_areas)
    # print(devices)
    # print(observations)

    for bus_object in bus:
        create_entity(bus_object)

    for bus_area in bus_areas:
        create_entity(bus_area)

    for device in devices:
        create_entity(device)

    for observation in observations:
        create_entity(observation)

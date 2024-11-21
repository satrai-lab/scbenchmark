import requests
import json
import sys
import random

url = "http://3.68.65.235:1026/ngsi-ld/v1/subscriptions/"

headers = {
    'Content-Type': 'application/json',
    'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w2.org/ns/json-ld#context"; type="application/ld+json"',
    'Connection':'close'
}


def replace_value(obj, target, new_value):
    if isinstance(obj, str):
        return obj.replace(target, new_value)
    elif isinstance(obj, dict):
        return {k: replace_value(v, target, new_value) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_value(elem, target, new_value) for elem in obj]
    else:
        return obj

with open('templates/buses/bus/observations.json') as f:
    # Load the JSON data from the file
    observations = json.load(f)

if __name__ == "__main__":

    bus_id = sys.argv[1]
    observations = replace_value(observations, "$1", bus_id)

    index =  1
    for object in observations:


        id = "urn:ngsi-ld:Subscription:bus_" + str(random.randint(1, 1000000))
        obj = {
        "id": id,
        "description": "Observation",
        "type": "Subscription",
        "entities": [
            {
            "id": object['id'],
            "type": "Observation"
            }
        ],
        "notification": {
            "format": "normalized",
            "endpoint": {
            "uri": "http://3.68.65.235:8888/hook_bus",
            "accept": "application/json"
            }
        }
        }

        payload = json.dumps(obj)

        response = requests.request("POST", url, headers=headers, data=payload)

        if(response.status_code > 299):
            print(response.status_code)
        #print(response.text)
        index = index + 1 


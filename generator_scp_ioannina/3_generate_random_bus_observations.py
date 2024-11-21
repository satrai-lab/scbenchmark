import requests
import time
import random
import json
import sys
from datetime import datetime


from dotenv import dotenv_values

config = dotenv_values(".env")
URL="http://"+config["IP"]+":"+config["PORT"]+"/ngsi-ld/v1/entities/"
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
        print(response.text)
        print(respose.status_code)

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
    observations = replace_value(observations, "$1", bus_id)


# print(observations)

    session = requests.Session()
    for observation in observations:
        id = observation['id']
        observation['measurement']['value']['value'] = random.randint(1, 1000)
        object = observation['measurement']['value']

        # Get the current UTC datetime
        now = datetime.utcnow()

        # Format the datetime in the desired format
        timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        object['observedAt'] = timestamp
        payload = json.dumps(object)

        patch_url = URL + id +"/attrs/measurement"
        response = session.patch(patch_url, headers=HEADERS, data=payload)
        if(response.status_code > 299):

            print(response.status_code)
            print(response.text)

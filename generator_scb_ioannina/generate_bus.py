import requests
import json


url = "http://3.68.65.235:1026/ngsi-ld/v1/entities/"

headers = {
    'Accept': 'application/ld+json',
    'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
    'Content-Type': 'application/json',
    'Connection':'close'
}

data = {}
with open('./buses/bus/bus.json', 'r') as f:
    # Load the JSON data
    data = json.load(f)

for object in data:

    payload = json.dumps(object)
    headers = {
        'Accept': 'application/ld+json',
        'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

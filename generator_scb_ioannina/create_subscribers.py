import requests
import json


url = "http://3.68.65.235:1026/ngsi-ld/v1/subscriptions/"

headers = {
    'Content-Type': 'application/json',
    'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w2.org/ns/json-ld#context"; type="application/ld+json"',
    'Connection':'close'
}

data = {}
with open('./buses/bus/observations.json', 'r') as f:
    # Load the JSON data
    data = json.load(f)

index =  1
for object in data:


    id = "urn:ngsi-ld:Subscription:" + str(index)
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
        "uri": "http://192.168.1.2:8888/hook",
        "accept": "application/json"
        }
    }
    }

    payload = json.dumps(obj)

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)
    print(response.text)
    index = index + 1 


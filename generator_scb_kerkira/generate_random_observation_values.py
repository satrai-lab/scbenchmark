import requests
import json
import random
import time


url = "http://3.68.65.235:1026/ngsi-ld/v1/entities/"

headers = {
    'Accept': 'application/ld+json',
    'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
    'Content-Type': 'application/json',
    'Connection':'close'
}

data = {}
while True:
    with open('./buses/bus/observations.json', 'r') as f:
        # Load the JSON data
        data = json.load(f)

    for object in data:

        
        id = object['id']
        object['measurement']['value']['value'] = random.randint(1, 1000)
        object = object['measurement']['value']
        payload = json.dumps(object)
        print(payload)

        patch_url = url + id +"/attrs/measurement"
        
        response = requests.request("PATCH", patch_url, headers=headers, data=payload)

        print(response.status_code)
        print(response.text)
    time.sleep(9)



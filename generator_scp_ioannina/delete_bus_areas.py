import requests
import json


url = "http://3.68.65.235:1026/ngsi-ld/v1/entities/"

headers = {
    'Accept': 'application/ld+json',
    'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
    'Connection':'close'
}

data = {}
with open('./buses/bus/busAreas.json', 'r') as f:
    # Load the JSON data
    data = json.load(f)


for object in data:
    delete_url = url + object['id']
    payload = ""
    response = requests.request("DELETE", delete_url, headers=headers, data=payload)

    print(response.status_code)

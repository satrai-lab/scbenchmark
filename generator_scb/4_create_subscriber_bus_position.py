import requests
import json


url = "http://3.68.65.235:1026/ngsi-ld/v1/subscriptions/"

headers = {
  'Content-Type': 'application/json',
  'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w2.org/ns/json-ld#context"; type="application/ld+json"',
  'Connection':'close'
}

obj = {
    "description": "Observation",
    "type": "Subscription",
    "entities": [
        {
            "type": "BusPosition"
        }
    ],
    "notification": {
        "format": "normalized",
        "endpoint": {
        "uri": "http://3.68.65.235:8888/hook_position",
        "accept": "application/json"
        }
    }
}

payload = json.dumps(obj)

response = requests.request("POST", url, headers=headers, data=payload)

if(response.status_code > 299):

    print(response.status_code)
    print(response.text)


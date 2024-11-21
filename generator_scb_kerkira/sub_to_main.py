import requests
import json

from dotenv import dotenv_values

config = dotenv_values(".env")
url="http://"+config["IP"]+":"+config["PORT"]+"/ngsi-ld/v1/subscriptions/"


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
            "type": "*"
        }
    ],
    "notification": {
        "format": "normalized",
        "endpoint": {
        "uri": "localhost:8888/hook",
        "accept": "application/json"
        }
    }
}

payload = json.dumps(obj)

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
print(response.text)

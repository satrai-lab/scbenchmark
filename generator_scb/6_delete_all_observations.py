import requests
import json
import time


from dotenv import dotenv_values

config = dotenv_values(".env")
URL="http://"+config["IP"]+":"+config["PORT"]+"/ngsi-ld/v1/subscriptions/"
HEADERS = {
    'Accept': 'application/ld+json',
    'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
    'Content-Type': 'application/json',
    'Connection':'close'
}


def delete_subscription(entity):
    payload = {}
    NEW_URL = URL+entity["id"]
    NEW_URL += "&offset=0&limit=40"
    response = requests.request("DELETE", NEW_URL, headers=HEADERS, data=payload)
    response.close()
    print("DELETING "+ entity["id"] + ":"+ str(response.status_code))

def get_subscriptions():
    payload = {}
    response = requests.request("GET", URL, headers=HEADERS, data=payload)
    return response.json()


jsons = get_subscriptions()
while jsons!=[]:
    for entity in jsons:
        delete_subscription(entity)

    time.sleep(1)
    jsons = get_subscriptions()
    

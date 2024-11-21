import requests
import json
import time


types = [
    "BusPosition",
    "Bus",
    "BusArea",
    "Device",
    "Observation"
]

from dotenv import dotenv_values

config = dotenv_values(".env")
URL="http://"+config["IP"]+":"+config["PORT"]+"/ngsi-ld/v1/entities"
HEADERS = {
    'Accept': 'application/ld+json',
    'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
    'Content-Type': 'application/json',
    'Connection':'close'
}


def delete_entity(entity):
    payload = {}
    NEW_URL = URL+"/"+entity["id"]
    response = requests.request("DELETE", NEW_URL, headers=HEADERS, data=payload)
    response.close()
    print(NEW_URL)
    print("DELETING "+ entity["id"] + ":"+ str(response.status_code))

def get_entities(NEW_URL, type):
    payload = {}
    response = requests.request("GET", NEW_URL, headers=HEADERS, data=payload)
    return response.json()


for type in types:
    OFFSET = 0
    NEW_URL = URL+"?type="+type
    NEW_URL += "&offset=" + str(OFFSET) + "&limit=40"

    jsons = get_entities(NEW_URL, type)
    while jsons != []:
        for entity in jsons:
            if("bus" in entity['id']):
                #print("Deleting entity:{}".format(entity["id"]))
                delete_entity(entity)
        time.sleep(1)
        OFFSET += 10
        NEW_URL = URL+"?type="+type
        NEW_URL += "&offset=" + str(OFFSET) + "&limit=40"
        jsons = get_entities(NEW_URL, type)
        #print(jsons)
    

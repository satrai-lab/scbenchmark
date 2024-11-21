import requests

# URL and headers as provided
URL = "http://127.0.0.1:1026/ngsi-ld/v1/entities/"
HEADERS = {
    'Accept': 'application/json',
    'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
    'Connection': 'close'
}

# Parameters to fetch entities of type "Bus"
params = {
        'id': 'urn:ngsi-ld:Heraklion:Observation_Temperature_S1_bus1'
}

# Make the GET request
response = requests.get(URL, headers=HEADERS, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    entities = response.json()
    # Print the fetched entities
    print(entities[0])
else:
    print(f"Error: Unable to fetch entities. Status code: {response.status_code}")
    print(response.text)


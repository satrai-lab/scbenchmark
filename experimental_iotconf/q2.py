import requests

# URL to fetch specific Observation entities
URL = "http://127.0.0.1:1026/ngsi-ld/v1/entities"

# Headers for the request
HEADERS = {
    'Accept': 'application/json',
    'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
}

# Correctly formatted query parameters for nested property
PARAMS = {
    "type": "Observation",
    "q": "measurement.value>70"  # Add this line to filter for measurement values greater than 70
}

# Make the GET request
response = requests.get(URL, headers=HEADERS, params=PARAMS)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    observations = response.json()
    print(observations)
    # Optionally, print each observation's measurement value
    for observation in observations:
        print(observation['measurement']['value'])
else:
    print(f"Error: Unable to fetch information : {response.status_code}")
    print(response.text)


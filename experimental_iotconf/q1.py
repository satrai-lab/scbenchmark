import subprocess
import requests

# Run the get_random_bus_urn.py script and capture its output
result = subprocess.run(['python3', 'get_random_bus_urn.py'], stdout=subprocess.PIPE, text=True)

# Get the URN from the output
bus_urn = result.stdout.strip()

# URL to fetch the specific bus entity
URL = f"http://127.0.0.1:1026/ngsi-ld/v1/entities/{bus_urn}"

# Headers for the request
HEADERS = {
    'Accept': 'application/json',
    'Link': '<https://raw.githubusercontent.com/SAMSGBLab/iotspaces-DataModels/main/transportation-models/context.json>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
    'Connection': 'close'
}

# Make the GET request
response = requests.get(URL, headers=HEADERS)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    bus_info = response.json()
    print(bus_info)
    
else:
    print(f"Error: Unable to fetch information for bus {bus_urn}. Status code: {response.status_code}")
    print(response.text)


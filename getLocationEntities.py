import requests

import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 5:
    print("Usage: python .py <broker_url> <maxDistance> <lat> <lon>")
    sys.exit(1)

#print(sys.argv)
# Get host and port from command-line arguments

broker_url = sys.argv[1]
maxDistance = sys.argv[2]
lat = sys.argv[3]
lon = sys.argv[4]

# Replace these with your own context broker settings
ORION_BASE_URL = f'{broker_url}/ngsi-ld/v1'
HEADERS = {'Content-Type': 'application/json'}

# Define the entity type you want to retrieve (EnergyMeter in this case)
ENTITY_TYPE = 'WeatherStation'

# Define the query to retrieve all entities of the specified type
QUERY = f'/entities?type={ENTITY_TYPE}&geometry=Point&georel=near;maxDistance=={maxDistance}&coordinates=[{lat},{lon}]'

# Make the GET request to retrieve the entities
try:
    #print(f'{ORION_BASE_URL}{QUERY}')
    response = requests.get(f'{ORION_BASE_URL}{QUERY}', headers=HEADERS)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        entities = response.json()
        #print(f'Found {len(entities)} {ENTITY_TYPE} entities:')
        for entity in entities:
            #print(f'Entity ID: {entity["id"]}')
            #print(f'Entity ID: {entity["id"]} - Value: {entity["energyConsumption"]["value"]}')
            print(f'Entity ID:{entity["id"]} Humidity:{entity["humidity"]["value"]} Temperature:{entity["temperature"]["value"]}')
            # You can access other attributes of the entity as needed
    else:
        print(f'Failed to retrieve entities. Status code: {response.status_code}')
        print(f'{response.text}')
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')


import random
from datetime import datetime, timedelta
import json
import sys
import requests  # Import the requests library

# Simulate data for different locations within the city
locations = [
    {"name": "City Center", "lat": 42.3601, "lon": -71.0589},
    {"name": "North Suburb", "lat": 42.4668, "lon": -70.9495},
    {"name": "South Suburb", "lat": 42.2893, "lon": -71.0710},
]

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python your_script.py <host> <port>")
    sys.exit(1)

# Extract the host and port from command-line arguments
host = sys.argv[1]
port = sys.argv[2]

# Construct the Orion LD endpoint URL
orion_ld_endpoint = f"http://{host}:{port}/ngsi-ld/v1/entities"

# Function to generate synthetic data for different entities
def generate_data(entity_type, location):
    timestamp = datetime.now()
    for _ in range(10):  # Generate data for the past 10 minutes
        entity_id = f"urn:ngsi-ld:SmartCity:Heraklion:{entity_type}:{location['name'].replace(' ', '_').lower()}"
        data = {
            "id": entity_id,
            "type": entity_type,
            "location": {
                "type": "GeoProperty",
                "value": {
                    "type": "Point",
                    "coordinates": [location["lon"], location["lat"]],
                }
            },
        }

        if entity_type == "WeatherStation":
            # Define attributes for WeatherStation entity directly within the JSON object
            data["temperature"] = {
                "value": round(random.uniform(15, 30), 2),
                "type": "Property",  # Attribute type set to "Property"
            }
            data["humidity"] = {
                "value": round(random.uniform(40, 80), 2),
                "type": "Property",  # Attribute type set to "Property"
            }
            # Add other WeatherStation attributes

        elif entity_type == "TrafficSensor":
            # Define attributes for TrafficSensor entity
            data["trafficFlow"] = {
                "value": random.randint(10, 100),
                "type": "Property",  # Attribute type set to "Property"
            }
            # Add other TrafficSensor attributes

        elif entity_type == "AirQualityMonitor":
            # Define attributes for AirQualityMonitor entity
            data["pm25Concentration"] = {
                "value": round(random.uniform(5, 25), 2),
                "type": "Property",  # Attribute type set to "Property"
            }
            # Add other AirQualityMonitor attributes

        elif entity_type == "EnergyMeter":
            # Define attributes for EnergyMeter entity
            data["energyConsumption"] = {
                "value": round(random.uniform(10, 100), 2),
                "type": "Property",  # Attribute type set to "Property"
            }
            # Add other EnergyMeter attributes

        # Check if the entity already exists
        if entity_exists(entity_id):
            update_entity(data)
        else:
            create_entity(data)

        # Update timestamp for the next data point
        timestamp -= timedelta(minutes=1)

# Function to check if an entity already exists in Orion LD
def entity_exists(entity_id):
    headers = {
        "Accept": "application/json",
    }

    try:
        response = requests.get(
            f"{orion_ld_endpoint}/{entity_id}",
            headers=headers,
        )

        return response.status_code == 200

    except Exception as e:
        print(f"Error checking entity existence: {e}")
        return False

# Function to create a new entity in Orion LD
def create_entity(entity_data):
    headers = {
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            orion_ld_endpoint,
            data=json.dumps(entity_data),
            headers=headers,
        )

        if response.status_code == 201:
            print(f"Entity {entity_data['id']} created successfully.")
        else:
            print(f"Failed to create entity {entity_data['id']} - Status Code: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Error creating entity: {e}")

# Function to update an existing entity in Orion LD
def update_entity(entity_data):
    headers = {
        "Content-Type": "application/json",
    }

    try:
        response = requests.patch(
            f"{orion_ld_endpoint}/{entity_data['id']}/attrs",
            data=json.dumps(entity_data),
            headers=headers,
        )

        if response.status_code == 204:
            print(f"Entity {entity_data['id']} updated successfully.")
        else:
            print(f"Failed to update entity {entity_data['id']} - Status Code: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Error updating entity: {e}")

# Generate data for each entity and location
entities = ["WeatherStation", "TrafficSensor", "AirQualityMonitor", "EnergyMeter"]
for entity_type in entities:
    for location in locations:
        generate_data(entity_type, location)


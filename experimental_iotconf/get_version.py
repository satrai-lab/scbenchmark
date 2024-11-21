import requests

# URL to fetch the Orion-LD version
URL = "http://127.0.0.1:1026/version"

# Headers for the request
HEADERS = {
    'Accept': 'application/json',
    'Connection': 'close'
}

# Make the GET request
response = requests.get(URL, headers=HEADERS)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    version_info = response.json()
    # Print the version information
    print(version_info)
else:
    print(f"Error: Unable to fetch version information. Status code: {response.status_code}")
    print(response.text)


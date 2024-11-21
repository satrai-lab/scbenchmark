#!/bin/bash


# Function to print a message in green
print_green() {
	echo -e "\033[32m\u2713 $1\033[0m"
}


# Define the name of your Orion container
ORION_CONTAINER_NAME="orion"

$(sudo docker-compose -f docker-compose-troe.yml stop >/dev/null 2>&1)
$(sudo docker-compose -f docker-compose-troe.yml rm -f >/dev/null 2>&1)
# Check if the Orion container is running
if docker ps --filter "name=${ORION_CONTAINER_NAME}" --format '{{.Names}}' | grep -q "${ORION_CONTAINER_NAME}"; then
    print_green "Docker container with Orion-LD is already running."
else
    # Start the Docker container using docker-compose
    $(sudo docker-compose -f docker-compose-troe.yml up -d >/dev/null 2>&1)
    if [ $? -eq 0 ]; then
        print_green "Docker container with Orion-LD is now running."
    else
        echo "Error: Failed to start the Docker container."
    fi
fi


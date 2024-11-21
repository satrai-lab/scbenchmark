#!/bin/bash

# Function to print a message in green
print_green() {
    echo -e "\033[32m\u2713 $1\033[0m"
}

# Function to print a message in red
print_red() {
    echo -e "\033[31m $1\033[0m"
}

# Function to print loading animation
print_loading_animation() {
    local text="$1"
    local delay=0.5
    while [ -z "$stop_animation" ]; do
        echo -ne "\r$text\033[K"
        sleep "$delay"
        text+="."
        echo -ne "\r$text\033[K"
        sleep "$delay"
        text+="."
        echo -ne "\r$text\033[K"
        sleep "$delay"
        text+="."
        echo -ne "\r$text\033[K"
        sleep "$delay"
        text="$1"
    done
}
python3 sub_to_main.py
print_loading_animation "Starting the synthetic data generator" &
animation_pid=$!

# Check if the Docker container is already running
if ps aux | grep -q "orionld"; then
    # Change directory and suppress output/errors
    cd /home/stratos/temp_scb/generator_scb_heraklion/ >/dev/null 2>&1

    # Check if the directory change was successful
    if [ $? -eq 0 ]; then
        # Run the Python script and suppress output/errors
        python3 0_all_in_one_create.py >/dev/null 2>&1

        # Check if the Python script was executed successfully
        if [ $? -eq 0 ]; then
            stop_animation=true
            kill -9 "$animation_pid" &>/dev/null
	    echo -e "\n" # Print a newline to clear the line
            print_green "Generator Initiated!"
            python3 0_all_in_one_generate.py >/dev/null 2>&1
        else
            stop_animation=true
            kill -9 "$animation_pid" &>/dev/null
	    echo -e "\n" # Print a newline to clear the line
            echo "Error: Failed to run the Python script."
        fi
    else
        stop_animation=true
        kill -9 "$animation_pid" &>/dev/null
	echo -e "\n" # Print a newline to clear the line
        echo "Error: Failed to change directory."
    fi
else
    stop_animation=true
    kill -9 "$animation_pid" &>/dev/null
    print_red "Orion-LD is not running, generator did not start"
fi


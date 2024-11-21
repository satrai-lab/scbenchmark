import requests
import curses
import subprocess
import time

# Define a list of Orion LD Broker URLs to check
orion_urls = [
    "http://192.168.20.1:1026",
    "http://192.168.20.2:1026",
    "http://192.168.20.3:1026",
    "http://192.168.20.4:1026",
    # Add more broker URLs as needed
]

def check_brokers(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    stdscr.addstr(0, 0, "Checking Orion LD Brokers...")

    while True:
        stdscr.clear()
        row = 1  # Initialize the row position

        for i, url in enumerate(orion_urls, start=1):
            output = ""  # Declare 'output' with a default value
            try:
                version_url = url + "/version"
                response = requests.get(version_url)
                status_message = f"Orion LD Broker {i}: "
                stdscr.addstr(row, 0, status_message)  # Green text for "Up and running"
                if response.status_code == 200:
                    status = "Up"
                    stdscr.addstr(row, len(status_message) + 1, status, curses.color_pair(1))  # Green text for "Up and running"
                else:
                    status = "Down"
                    stdscr.addstr(row, len(status_message) + 1, status, curses.color_pair(2))  # Green text for "Up and running"

                row += 1  # Move to the next row

                # Run the getEnergyMeterEntities.py script and capture its output
                if i != 4:
                    try:
                        output = subprocess.check_output(["python3", "getEnergyMeterEntities.py", url])
                        output = output.decode('utf-8', 'ignore')  # Handle Unicode characters
                        stdscr.addstr(row, 0, f"{output}", curses.color_pair(1))  # Display output in green
                        row += 3  # Move to the next row
                    except subprocess.CalledProcessError as e:
                        stdscr.addstr(row, 0, f"getEnergyMeterEntities.py Error: {e}", curses.color_pair(2))  # Display error in red
                        row += 4  # Move to the next row

                    stdscr.addstr(row, 1, "Which EnergyMeter Entities have value bigger than 50?:", curses.A_BOLD)  # Green text for "Up and running"
                    row += 1  # Move to the next row
                    try:
                        output = subprocess.check_output(["python3", "getEnergyMeterEntitiesBiggerThan.py", url, "energyConsumption", "50"])
                        output = output.decode('utf-8', 'ignore')  # Handle Unicode characters
                        stdscr.addstr(row, 0, f"{output}", curses.color_pair(1))  # Display output in green
                        row += 4  # Move to the next row
                    except subprocess.CalledProcessError as e:
                        stdscr.addstr(row, 0, f"getEnergyMeterEntitiesBiggerThan.py Error: {e}", curses.color_pair(2))  # Display error in red
                        row += 1  # Move to the next row

                    stdscr.addstr(row, 1, "What are the temperature and humidity values for the WeatherStation closest to my point?:", curses.A_BOLD)  # Green text for "Up and running"
                    row += 1  # Move to the next row
                    try:
                        output = subprocess.check_output(["python3", "getLocationEntities.py", url, "1000", "-71.0589", "42.3601"])
                        output = output.decode('utf-8', 'ignore')  # Handle Unicode characters
                        stdscr.addstr(row, 0, f"{output}", curses.color_pair(1))  # Display output in green
                        row += 2  # Move to the next row
                    except subprocess.CalledProcessError as e:
                        stdscr.addstr(row, 0, f"getLocationEntities.py Error: {e}", curses.color_pair(2))  # Display error in red
                        row += 1  # Move to the next row

                else:  # Handle the case when i == 4
                    pass
                    output = subprocess.check_output(["python3", "getObservationEntities.py", "http://192.168.20.4:1026", "Heraklion"])
                    output = output.decode('utf-8', 'ignore')  # Handle Unicode characters
                    stdscr.addstr(row, 0, f"{output}", curses.color_pair(1))  # Display output in green
                    row += 1  # Move to the next row
                    output = subprocess.check_output(["python3", "getObservationEntities.py", "http://192.168.20.4:1026", "Ioannina"])
                    output = output.decode('utf-8', 'ignore')  # Handle Unicode characters
                    stdscr.addstr(row, 0, f"{output}", curses.color_pair(1))  # Display output in green
                    row += 1  # Move to the next row
                    output = subprocess.check_output(["python3", "getObservationEntities.py", "http://192.168.20.4:1026", "Kerkira"])
                    output = output.decode('utf-8', 'ignore')  # Handle Unicode characters
                    stdscr.addstr(row, 0, f"{output}", curses.color_pair(1))  # Display output in green
                    row += 1  # Move to the next row


            except requests.ConnectionError:
                status_message = f"Orion LD Broker {i}: "
                stdscr.addstr(row, 0, status_message)  # Green text for "Up and running"
                status = "Down"
                stdscr.addstr(row, len(status_message) + 1, status, curses.color_pair(2))  # Green text for "Up and running"
                row += 1  # Move to the next row

        stdscr.refresh()
        curses.doupdate()  # Update the screen
        time.sleep(1)  # Check every 1 second (adjust as needed)

def main():
    curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Green text on black background
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Red text on black background
    try:
        curses.wrapper(check_brokers)
    except KeyboardInterrupt:
        pass
    curses.endwin()  # Cleanup curses before exiting

if __name__ == "__main__":
    main()


import subprocess
import time
import concurrent.futures



index = 0

#subprocess.run(["python3", "4_create_subscriber_bus_position.py"])
# create buses
for i in range(0,60):
    index = index + 1 
    bus_id = "bus"+str(index)
    subprocess.run(["python3", "1_create_bus_.py", bus_id])
    #subprocess.run(["python3", "2_create_subscribers_.py", bus_id])
    print("creating {}".format(bus_id))




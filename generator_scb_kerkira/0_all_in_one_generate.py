import subprocess
import time
import concurrent.futures

print("Generating random synthetic data")
def generate_random_observations(bus_id):
        subprocess.run(["python3", "3_generate_random_bus_observations.py", bus_id])

while True:
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(generate_random_observations, f"bus{i}") for i in range(1, 61)]

    # Wait for all tasks to finish
    for future in concurrent.futures.as_completed(futures):
        future.result()

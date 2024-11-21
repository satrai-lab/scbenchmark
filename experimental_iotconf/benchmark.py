import time
import subprocess
import statistics

def benchmark(script_path, num_requests):
    latencies = []
    start_time = time.time()

    for _ in range(num_requests):
        request_start = time.time()
        result = subprocess.run(["python3", script_path], capture_output=True, text=True)
        request_end = time.time()
        
        latency = request_end - request_start
        latencies.append(latency)
        
        if result.returncode != 0:
            print(f"Execution failed with return code {result.returncode}: {result.stderr}")

    end_time = time.time()
    total_time = end_time - start_time

    # Compute statistics
    median_latency = statistics.median(latencies)
    average_latency = statistics.mean(latencies)
    min_latency = min(latencies)
    max_latency = max(latencies)
    requests_per_sec = num_requests / total_time

    # Display results
    print(f"Median Latency: {median_latency:.6f} seconds")
    print(f"Average Latency: {average_latency:.6f} seconds")
    print(f"Min Latency: {min_latency:.6f} seconds")
    print(f"Max Latency: {max_latency:.6f} seconds")
    print(f"Requests per Second: {requests_per_sec:.2f} requests/sec")

# Example usage
benchmark("q1.py", 100)

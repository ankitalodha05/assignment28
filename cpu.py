import psutil
import time

def monitor_cpu(threshold=80):
    print("Monitoring CPU usage. Press Ctrl+C to stop.")
    try:
        while True:
            # Get the CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Check if the CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"ALERT: CPU usage is at {cpu_usage}%.")
            
            # Sleep for a short period before checking again
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

# Run the CPU monitor
monitor_cpu()

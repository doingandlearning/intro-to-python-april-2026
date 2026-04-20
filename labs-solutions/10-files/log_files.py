from datetime import datetime

# Step 1: Create the log messages
log_lines = [
    "Sensor initialised",
    "Reading: 3.41",
    "Reading: 3.44",
    "System check passed"
]

# Step 2: Write to the log file
filename = "sensor_log.txt"

with open(filename, 'w') as f:
    for message in log_lines:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} | {message}\n")

print(f"Log written to {filename}")

# Step 3: Read the log back
print("\nReading log contents:")

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        print(line)

# Optional: split and format
print("\nSplit format:")
with open(filename, 'r') as f:
    for line in f:
        ts, msg = line.strip().split(" | ")
        print(f"At {ts}, message was: {msg}")

from datetime import datetime

def write_log(filename, messages):
    """Writes messages to a log file. Messages are expected to be a list of strings."""
    with open(filename, "w") as f:
        for message in messages:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line = f"{timestamp} | {message}\n"
            f.write(line)

messages = [
    "Sensor initialised",
    "Reading: 3.41",
    "Reading: 3.39",
    "Sensor stopped",
]

write_log("sensor_log.txt", messages)

def read_log(filename):
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            timestamp, message = line.split(" | ", 1)
            print(f"Timestamp: {timestamp}")
            print(f"Message: {message}")


read_log("sensor_log.txt")

def filter_log_lines(filename, keyword):
    matches = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            _, message = line.split(" | ", 1)
            if keyword in message:
                print(line)
                matches += 1
    return matches


count = filter_log_lines("sensor_log.txt", "Reading")
print(f"Matches: {count}")

name = input("Enter output filename: ")
msgs = ["Start", "Reading: 5.10", "Reading: 5.08", "Stop"]
write_log(name, msgs)
read_log(name)
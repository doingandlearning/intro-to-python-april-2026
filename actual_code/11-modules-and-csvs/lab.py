readings = (
    (21.1, "2026-04-21", "12:00", "Celsius"),
    (21.4, "2026-04-21", "12:05", "Celsius"),
    (21.0, "2026-04-21", "12:10", "Celsius"),
    (20.8, "2026-04-21", "12:15", "Celsius"),
    (21.2, "2026-04-21", "12:20", "Celsius"),
)

import csv


def write_csv(filename, data):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


readings = (
    (21.1, "2026-04-21", "12:00", "Celsius"),
    (21.4, "2026-04-21", "12:05", "Celsius"),
    (21.0, "2026-04-21", "12:10", "Celsius"),
    (20.8, "2026-04-21", "12:15", "Celsius"),
    (21.2, "2026-04-21", "12:20", "Celsius"),
)

write_csv("sensor_readings.csv", readings)
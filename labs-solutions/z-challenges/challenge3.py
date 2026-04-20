import csv

def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def label(temp_f):
    if temp_f < 50:
        return "cold"
    elif temp_f < 77:
        return "warm"
    else:
        return "hot"

celsius_values = [0, 10, 20, 30, 40]

with open("temperature_table.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Celsius", "Fahrenheit", "Label"])
    for c in celsius_values:
        f_temp = to_fahrenheit(c)
        writer.writerow([c, round(f_temp, 2), label(f_temp)])

print("temperature_table.csv created.")

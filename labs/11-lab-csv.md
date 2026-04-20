# 🧪 Lab 11: Working with CSV Files

---

## 🎯 Objective

You’ll simulate storing a series of temperature readings taken from a sensor into a **CSV file**, then read the data back and display it.

---

## Hints and Tips

- Keep a consistent order for each reading field.
- Use one function to write, one function to read.
- Remember that `csv.reader` returns strings for every column.
- Convert numeric values after reading if you need numeric operations.

---

## 📍Part 1: Write to a CSV File

### Step 1: Create a Structure for the Readings

Use a **tuple of tuples** to represent temperature data. Each reading should include:

- A **float** temperature
- A **date string** (e.g., `'04/05/23'`)
- A **time string** (e.g., `'12:00'`)
- A **scale** (e.g., `'Celsius'`)

📝 Prompt:
Create 5 such readings and store them in a single data structure.

---

### Step 2: Define a Function to Write CSV

Write a function that:

- Accepts a filename and the data structure
- Writes the data to a CSV file (1 row per reading)
- Uses `csv.writer`

📝 Prompt:
What mode do you open the file in?
How do you separate rows?
What should each line contain?

---

### Step 3: Run Your Function

- Call your function with the tuple of readings
- Open the resulting CSV file in PyCharm or a text editor to confirm

---

## 📍Part 2 (Extension): Read Back the File

### Step 1: Use `csv.reader`

Write a second part of the program that:

- Opens the file you just wrote
- Uses `csv.reader` to load each row
- Converts the result into a new tuple of tuples (or a list of tuples if you prefer)

### Step 2: Print the Result

- Print each reading on a separate line
- Try formatting the output so it's easy to read

📝 Prompt:
Remember: all values read from a CSV are strings.
What do you need to convert?
How do you rebuild a tuple from a row?

---

## 🧠 Optional Stretch

- Add a header row (e.g., `['Temperature', 'Date', 'Time', 'Scale']`)
- Validate that all rows have the correct number of columns before printing
- Add input() to let the user name the file

---

<details>
<summary>Example solution code</summary>

```python
import csv


readings = (
    (21.1, '04/05/23', '12:00', 'Celsius'),
    (21.4, '04/05/23', '12:05', 'Celsius'),
    (21.0, '04/05/23', '12:10', 'Celsius'),
    (20.8, '04/05/23', '12:15', 'Celsius'),
    (21.2, '04/05/23', '12:20', 'Celsius'),
)


def write_csv(filename, data):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


def read_csv(filename):
    loaded = []
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            temp = float(row[0])
            date = row[1]
            time = row[2]
            scale = row[3]
            loaded.append((temp, date, time, scale))
    return tuple(loaded)


filename = 'temperature_readings.csv'
write_csv(filename, readings)
loaded_readings = read_csv(filename)

for reading in loaded_readings:
    print(reading)
```

</details>

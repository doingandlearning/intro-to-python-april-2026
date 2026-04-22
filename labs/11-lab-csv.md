# Lab 11: Working with CSV Files

This lab focuses on writing and reading CSV data using the `csv` module.

You will practise:

- storing tabular data with tuples
- writing rows with `csv.writer`
- reading rows with `csv.reader`
- converting CSV strings back to useful types

---

## Hints and Tips

- Keep a fixed column order for every row.
- Use one function for writing and one for reading.
- Remember: `csv.reader` returns strings for every column.
- Convert values (for example temperature) after reading.
- Use `newline=""` when opening CSV files.

---

## Task 1: Create Reading Data

Create a tuple of tuples called `readings`.

Each reading should contain:

1. temperature (float)
2. date string (`YYYY-MM-DD`)
3. time string (`HH:MM`)
4. scale (`"Celsius"`)

Create at least 5 readings.

<details>
<summary>Solution (Task 1)</summary>

```python
readings = (
    (21.1, "2026-04-21", "12:00", "Celsius"),
    (21.4, "2026-04-21", "12:05", "Celsius"),
    (21.0, "2026-04-21", "12:10", "Celsius"),
    (20.8, "2026-04-21", "12:15", "Celsius"),
    (21.2, "2026-04-21", "12:20", "Celsius"),
)
```

</details>

---

## Task 2: Write Readings to CSV

Write a function:

`write_csv(filename, data)`

Rules:

1. Open with `with open(filename, "w", newline="")`.
2. Use `csv.writer`.
3. Write one row per reading tuple.

Call the function with your `readings` data.

<details>
<summary>Solution (Task 2)</summary>

```python
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

write_csv("temperature_readings.csv", readings)
```

</details>

---

## Task 3: Read CSV Back Into Tuples

Write a function:

`read_csv(filename)`

Rules:

1. Open with `with open(filename, "r", newline="")`.
2. Use `csv.reader`.
3. Convert temperature to `float`.
4. Store each row as a tuple.
5. Return all rows as a tuple of tuples.

Then print each reading on a new line.

<details>
<summary>Solution (Task 3)</summary>

```python
import csv


def read_csv(filename):
    loaded = []
    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            temp = float(row[0])
            date = row[1]
            time = row[2]
            scale = row[3]
            loaded.append((temp, date, time, scale))
    return tuple(loaded)


loaded_readings = read_csv("temperature_readings.csv")
for reading in loaded_readings:
    print(reading)
```

</details>

---

## Task 4 (Optional): Add a Header Row

Update your writer and reader so that:

1. The first row is a header:
   `["temperature", "date", "time", "scale"]`
2. The reader skips that first row before processing data.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
import csv


def write_csv_with_header(filename, data):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["temperature", "date", "time", "scale"])
        for row in data:
            writer.writerow(row)


def read_csv_with_header(filename):
    loaded = []
    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            loaded.append((float(row[0]), row[1], row[2], row[3]))
    return tuple(loaded)
```

</details>

---

## Reflection

- Why does CSV reading return strings, even for numbers?
- Where did type conversion matter most?
- When is CSV a better choice than plain text logs?

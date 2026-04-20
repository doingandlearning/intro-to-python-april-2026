# 🧪 Capstone Project: Sensor Data Reporter

You’re going to build a program that lets a user collect sensor readings, process them, and save the data to a CSV file.

---

## ✅ Step 1: Collect Data (20 min)

Write a loop that:

- Asks the user to enter a signal strength (a number)
- Records the current time and date
- Stores the reading in a list (as a tuple)

Stop collecting when the user types `"done"`.

---

## ✅ Step 2: Summarise the Data (30 min)

Write and use functions to:

- Count how many readings were taken
- Print the highest and lowest signal
- Calculate and print the average signal

---

## ✅ Step 3: Save to CSV (20–25 min)

Write the data to a CSV file.

- One row per reading
- Include date, time, and signal value
- Use the `csv.writer` module

---

## 🧠 Optional Stretch Goals (Pick 1 or More)

- Ask the user for a **detector name** and include it in each row
- Let the user choose the filename
- Only allow readings **between 0.0 and 5.0**
- Write a **summary report** to a second file
- Move your functions into a second file and use `import`

---

## 🧾 Example Output

```
> Enter signal: 3.4
> Enter signal: 3.1
> Enter signal: done

Total readings: 2
Average signal: 3.25
Max: 3.4, Min: 3.1
Data saved to sensor_log.csv
```

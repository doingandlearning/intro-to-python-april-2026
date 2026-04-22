# Lab 14: Data Visualization with Matplotlib

This lab focuses on creating simple charts with matplotlib from tabular data.

You will practise:

- creating line and bar charts
- setting chart titles and axis labels
- customizing markers, colors, and grid lines
- plotting data from a pandas DataFrame
- saving charts to image files

---

## Hints and Tips

- Start with a basic plot, then add labels and styling.
- Always label x-axis, y-axis, and title.
- Use `plt.figure(...)` before each chart.
- Use `plt.tight_layout()` before `plt.show()` or `plt.savefig(...)`.
- If plotting from pandas, confirm column names first.

---

## Task 1: Create a Simple Line Chart

Create a script that plots temperature readings over time.

Use:

- `times = ["12:00", "12:05", "12:10", "12:15", "12:20"]`
- `temps = [21.1, 21.4, 21.0, 20.8, 21.2]`

Requirements:

1. Plot a line chart (`times` on x-axis, `temps` on y-axis).
2. Add title, x-label, and y-label.
3. Show the chart.

<details>
<summary>Solution (Task 1)</summary>

```python
import matplotlib.pyplot as plt

times = ["12:00", "12:05", "12:10", "12:15", "12:20"]
temps = [21.1, 21.4, 21.0, 20.8, 21.2]

plt.figure(figsize=(8, 4))
plt.plot(times, temps)
plt.title("Temperature Over Time")
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.tight_layout()
plt.show()
```

</details>

---

## Task 2: Improve the Chart Style

Take Task 1 and improve readability.

Requirements:

1. Add markers to each point.
2. Change line color.
3. Add a grid.
4. Rotate x-axis labels for readability.

<details>
<summary>Solution (Task 2)</summary>

```python
import matplotlib.pyplot as plt

times = ["12:00", "12:05", "12:10", "12:15", "12:20"]
temps = [21.1, 21.4, 21.0, 20.8, 21.2]

plt.figure(figsize=(8, 4))
plt.plot(times, temps, marker="o", color="teal")
plt.title("Temperature Over Time")
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

</details>

---

## Task 3: Create a Bar Chart Summary

Create a bar chart showing average temperature by sensor.

Use:

- `sensors = ["S1", "S2", "S3", "S4"]`
- `avg_temps = [21.3, 22.0, 20.7, 21.8]`

Requirements:

1. Use `plt.bar(...)`.
2. Add title and axis labels.
3. Show the chart.

<details>
<summary>Solution (Task 3)</summary>

```python
import matplotlib.pyplot as plt

sensors = ["S1", "S2", "S3", "S4"]
avg_temps = [21.3, 22.0, 20.7, 21.8]

plt.figure(figsize=(7, 4))
plt.bar(sensors, avg_temps, color="orange")
plt.title("Average Temperature by Sensor")
plt.xlabel("Sensor ID")
plt.ylabel("Average Temperature (C)")
plt.tight_layout()
plt.show()
```

</details>

---

## Task 4: Plot Directly from a CSV with Pandas

Use pandas to load `sensor_readings.csv` (from the previous lab), then plot:

1. a line chart of `temperature_c` over `timestamp`
2. only the first 15 rows to keep the chart readable

Requirements:

- Use `pd.read_csv(...)`
- Use matplotlib for plotting

<details>
<summary>Solution (Task 4)</summary>

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sensor_readings.csv")
small_df = df.head(15)

plt.figure(figsize=(10, 4))
plt.plot(small_df["timestamp"], small_df["temperature_c"], marker="o")
plt.title("Temperature from CSV (First 15 Rows)")
plt.xlabel("Timestamp")
plt.ylabel("Temperature (C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
```

</details>

---

## Task 5 (Optional): Save Plots to Files

Update one of your plots so it is saved to disk.

Requirements:

1. Use `plt.savefig("temperature_plot.png")`.
2. Save before `plt.show()`.
3. Keep `plt.tight_layout()`.

<details>
<summary>Solution (Task 5 Optional)</summary>

```python
import matplotlib.pyplot as plt

times = ["12:00", "12:05", "12:10", "12:15", "12:20"]
temps = [21.1, 21.4, 21.0, 20.8, 21.2]

plt.figure(figsize=(8, 4))
plt.plot(times, temps, marker="o", color="purple")
plt.title("Temperature Over Time")
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_plot.png")
plt.show()
```

</details>

---

## Reflection

- Which chart type was easier to interpret for this data?
- Which formatting choices made the biggest readability difference?
- When should you save a chart to file instead of only showing it on screen?

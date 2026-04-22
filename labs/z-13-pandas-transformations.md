# Lab 13: Pandas Transformations

This lab focuses on using pandas to transform CSV data into analysis-ready data.

You will practise:

- loading CSV data into a DataFrame
- inspecting structure and data types
- creating and updating columns
- filtering, sorting, and grouping data
- exporting transformed results to CSV

---

## Hints and Tips

- Use `df.head()` and `df.info()` early to understand the data.
- Keep transformations in small steps so each change is easy to check.
- Use clear column names before doing analysis.
- After filtering, check row counts with `len(df)` or `df.shape`.
- Save the final transformed result to a new file (do not overwrite raw data).

---

## Task 1: Load and Inspect a CSV

Create a script that:

1. Imports pandas as `pd`.
2. Loads a CSV file named `sensor_readings.csv` into a DataFrame.
3. Prints:
   - first 5 rows
   - column names
   - DataFrame shape

Use this sample structure in your CSV:

- `sensor_id`
- `timestamp`
- `temperature_c`
- `status`

<details>
<summary>Solution (Task 1)</summary>

```python
import pandas as pd

df = pd.read_csv("sensor_readings.csv")

print(df.head())
print(df.columns)
print(df.shape)
```

</details>

---

## Task 2: Create New Columns

Using the same DataFrame, add:

1. `temperature_k` (Kelvin):
   - `temperature_c + 273.15`
2. `is_alert`:
   - `True` when `temperature_c >= 30`
   - `False` otherwise

Then print the first 5 rows including these new columns.

<details>
<summary>Solution (Task 2)</summary>

```python
import pandas as pd

df = pd.read_csv("sensor_readings.csv")

df["temperature_k"] = df["temperature_c"] + 273.15
df["is_alert"] = df["temperature_c"] >= 30

print(df[["sensor_id", "temperature_c", "temperature_k", "is_alert"]].head())
```

</details>

---

## Task 3: Filter, Sort, and Group

Create three outputs:

1. `alerts_df`:
   - only rows where `is_alert` is `True`
2. `sorted_df`:
   - sort by `temperature_c` descending
3. `summary_df`:
   - group by `sensor_id`
   - calculate average temperature and count of readings

Print each output clearly.

<details>
<summary>Solution (Task 3)</summary>

```python
import pandas as pd

df = pd.read_csv("sensor_readings.csv")
df["is_alert"] = df["temperature_c"] >= 30

alerts_df = df[df["is_alert"]]
sorted_df = df.sort_values("temperature_c", ascending=False)
summary_df = (
    df.groupby("sensor_id")
    .agg(avg_temp_c=("temperature_c", "mean"), reading_count=("temperature_c", "count"))
    .reset_index()
)

print("Alerts:")
print(alerts_df)
print("\nSorted by temperature:")
print(sorted_df)
print("\nSummary by sensor:")
print(summary_df)
```

</details>

---

## Task 4: Export Transformed Results

Save two output files:

1. `alerts_only.csv` from `alerts_df`
2. `sensor_summary.csv` from `summary_df`

Rules:

- Use `index=False`.
- Keep the original `sensor_readings.csv` unchanged.

<details>
<summary>Solution (Task 4)</summary>

```python
import pandas as pd

df = pd.read_csv("sensor_readings.csv")
df["is_alert"] = df["temperature_c"] >= 30

alerts_df = df[df["is_alert"]]
summary_df = (
    df.groupby("sensor_id")
    .agg(avg_temp_c=("temperature_c", "mean"), reading_count=("temperature_c", "count"))
    .reset_index()
)

alerts_df.to_csv("alerts_only.csv", index=False)
summary_df.to_csv("sensor_summary.csv", index=False)
```

</details>

---

## Task 5 (Optional): Build a Simple Transformation Function

Write a function:

`transform_sensor_data(input_file, alerts_file, summary_file)`

The function should:

1. Load input CSV
2. Add `temperature_k` and `is_alert`
3. Build alerts and summary DataFrames
4. Save both outputs
5. Return the number of alert rows

<details>
<summary>Solution (Task 5 Optional)</summary>

```python
import pandas as pd


def transform_sensor_data(input_file, alerts_file, summary_file):
    df = pd.read_csv(input_file)
    df["temperature_k"] = df["temperature_c"] + 273.15
    df["is_alert"] = df["temperature_c"] >= 30

    alerts_df = df[df["is_alert"]]
    summary_df = (
        df.groupby("sensor_id")
        .agg(avg_temp_c=("temperature_c", "mean"), reading_count=("temperature_c", "count"))
        .reset_index()
    )

    alerts_df.to_csv(alerts_file, index=False)
    summary_df.to_csv(summary_file, index=False)
    return len(alerts_df)


alert_count = transform_sensor_data(
    "sensor_readings.csv",
    "alerts_only.csv",
    "sensor_summary.csv",
)
print("Alert rows:", alert_count)
```

</details>

---

## Reflection

- Which transformation step was easiest to verify?
- Why is it useful to keep raw and transformed files separate?
- Where did pandas make the workflow simpler than manual loops?

# Lab 8: Containers (Lists and Tuples)

This lab introduces containers in Python by building small tools with:

- **types** (`int`, `float`, `str`)
- **flow control** (`if`, `for`, `while`)
- **functions**
- **containers** (`list`, `tuple`)

---

## Hints and Tips

- Use a **list** when order matters or duplicates are allowed.
- Use a **tuple** when you want a fixed grouped record.
- Keep function jobs small and clear.
- Return results from functions and print outside when possible.

---

## Task 1: Collect and Analyze Three Measurements

Write a function:

`analyze_measurements(values)`

Where `values` is a list of numbers.

The function should return a summary string with:

1. count
2. total
3. average
4. highest value
5. lowest value

Then:

- ask the user for three values
- store them in a list
- call the function
- print the returned summary

<details>
<summary>Solution (Task 1)</summary>

```python
def analyze_measurements(values):
    count = len(values)
    total = sum(values)
    average = total / count
    highest = max(values)
    lowest = min(values)
    return (
        f"Count: {count}, Total: {total}, Average: {average}, "
        f"Highest: {highest}, Lowest: {lowest}"
    )


measurements = []
for i in range(3):
    value = float(input(f"Enter measurement {i + 1}: "))
    measurements.append(value)

summary = analyze_measurements(measurements)
print(summary)
```

</details>

---

## Task 2: Build and Read Tuples

Write a function:

`describe_point(point)`

Where `point` is a tuple with three values:

`(x, y, label)`

For example:

`(12.5, 7.2, "sensor-A")`

Return one string:

`"Label sensor-A is at x=12.5, y=7.2"`

Then create at least two point tuples and print the description for each.

<details>
<summary>Solution (Task 2)</summary>

```python
def describe_point(point):
    x = point[0]
    y = point[1]
    label = point[2]
    return f"Label {label} is at x={x}, y={y}"


point_a = (12.5, 7.2, "sensor-A")
point_b = (3.0, 9.8, "sensor-B")

print(describe_point(point_a))
print(describe_point(point_b))
```

</details>

---

## Task 3: Store Readings as Tuples in a List

Create a list called `readings`.

Each item in the list should be a tuple:

`(time_s, value)`

Example:

`(1, 12.4)`

Write a function:

`average_reading(readings)`

Rules:

1. Use a loop to add up all reading values.
2. Return the average value.
3. If the list is empty, return `None`.

Print the result for a sample `readings` list.

<details>
<summary>Solution (Task 3)</summary>

```python
def average_reading(readings):
    if len(readings) == 0:
        return None

    total = 0
    for reading in readings:
        value = reading[1]
        total += value

    return total / len(readings)


readings = [(1, 12.4), (2, 13.1), (3, 11.9), (4, 12.8)]
print(average_reading(readings))
```

</details>

---

## Task 4 (Optional): Merge Two Lists and Remove Duplicates

Write a function:

`merge_unique(list_a, list_b)`

Return a new list that contains all values from both lists, but without duplicates.
Keep the first-seen order.

Example:

- `list_a = [1, 2, 3, 2]`
- `list_b = [3, 4, 5]`
- result -> `[1, 2, 3, 4, 5]`

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
def merge_unique(list_a, list_b):
    merged = []
    for value in list_a + list_b:
        if value not in merged:
            merged.append(value)
    return merged


print(merge_unique([1, 2, 3, 2], [3, 4, 5]))
```

</details>

---

## Reflection

- Where was a list the best choice?
- Where was a tuple the best choice?
- Which function would you most likely reuse in another file?

# Lab 7: Functions for Useful Mini-Tools

This lab focuses on turning scripts into reusable function-based code.

You will practise:

- organizing programs into logical blocks
- defining functions
- parameter passing
- default parameter values
- named parameters
- returning values

---

## Hints and Tips

- Keep each function responsible for one clear task.
- Use parameters instead of hard-coding values inside functions.
- Prefer `return` for results, and print in a separate place.
- Start simple, test, then improve.

---

## Task 1: Turn Your Factorial Code into a Function

Reuse your previous factorial logic, but move it into a function:

`factorial(n)`

Requirements:

1. If `n` is negative, return `None`.
2. If `n` is `0`, return `1`.
3. Otherwise, return the factorial using a loop.
4. Ask user input, call the function, and print a message.

Example output:

```text
Enter n: 5
5! = 120
```

```text
Enter n: -2
Factorial not defined for negative numbers
```

<details>
<summary>Solution (Task 1)</summary>

```python
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = int(input("Enter n: "))
value = factorial(n)

if value is None:
    print("Factorial not defined for negative numbers")
else:
    print(f"{n}! = {value}")
```

</details>

---

## Task 2: Build a Beam Energy Classifier Function

Write a function:

`classify_beam_energy(energy_gev)`

Return one of these strings:

- `Invalid energy` (energy < 0)
- `No beam` (energy == 0)
- `Setup mode` (0 < energy < 1000)
- `Physics run` (energy >= 1000)

Then ask the user for energy and print the returned label.

<details>
<summary>Solution (Task 2)</summary>

```python
def classify_beam_energy(energy_gev):
    if energy_gev < 0:
        return "Invalid energy"
    if energy_gev == 0:
        return "No beam"
    if energy_gev < 1000:
        return "Setup mode"
    return "Physics run"


energy = float(input("Enter beam energy (GeV): "))
status = classify_beam_energy(energy)
print(status)
```

</details>

---

## Task 3: Distance Converter with Default and Named Parameters

Write a function:

`convert_distance(value, from_unit="km", to_unit="miles")`

Support conversions:

- km -> miles
- miles -> km

Return the converted numeric value.
If the unit pair is not supported, return `None`.

Then call your function in at least three ways:

1. positional parameters
2. using default values
3. named parameters

<details>
<summary>Solution (Task 3)</summary>

```python
def convert_distance(value, from_unit="km", to_unit="miles"):
    if from_unit == "km" and to_unit == "miles":
        return value * 0.6214
    if from_unit == "miles" and to_unit == "km":
        return value / 0.6214
    return None


# positional parameters
print(convert_distance(10, "km", "miles"))

# default parameters
print(convert_distance(10))

# named parameters
print(convert_distance(value=5, from_unit="miles", to_unit="km"))
```

</details>

---

## Task 4 (Optional): Analyze a Run and Return a Summary

Write a function:

`analyze_counts(a, b, c)`

Compute:

1. total (`a + b + c`)
2. average
3. highest value

Return **one summary string** that includes all three results clearly.
Then call the function and print the returned message.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
def analyze_counts(a, b, c):
    total = a + b + c
    average = total / 3
    highest = a

    if b > highest:
        highest = b
    if c > highest:
        highest = c

    return f"Total: {total}, Average: {average}, Highest: {highest}"


message = analyze_counts(120, 95, 140)
print(message)
```

</details>

---

## Reflection

- Which function is easiest to reuse in another file?
- Where did parameters make your code cleaner?
- Which task used return values most effectively?

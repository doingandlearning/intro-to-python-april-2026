# Extension Lab 6: Useful Loop Tasks (Ops + Analysis)

You have factorial working. This extension focuses on small tasks that feel closer to day-to-day technical work, while using the same level of Python.

Use only:

- `input()`
- `isnumeric()`, `len()`, `strip()`
- `int()`
- `if / elif / else`
- `for` loops

---

## Shared Input Step

For every challenge, ask for a non-negative integer `n`.

If input is invalid, print:

`Invalid input: enter a non-negative integer`

<details>
<summary>Solution (Shared input step)</summary>

```python
n_text = input("Enter a non-negative integer: ").strip()

if not n_text.isnumeric():
    print("Invalid input: enter a non-negative integer")
else:
    n = int(n_text)
    print(f"Using n = {n}")
```

</details>

---

## Challenge 1: Total Events in First n Windows

Assume window `i` produced `i` events.
Compute total events from window `1` to `n`.

Example: `n = 4` gives `1 + 2 + 3 + 4 = 10`.

<details>
<summary>Solution (Challenge 1)</summary>

```python
n_text = input("Enter a non-negative integer: ").strip()

if not n_text.isnumeric():
    print("Invalid input: enter a non-negative integer")
else:
    n = int(n_text)
    total_events = 0
    for i in range(1, n + 1):
        total_events += i
    print(f"Total events across first {n} windows: {total_events}")
```

</details>

---

## Challenge 2: Channel Scan IDs

Given `n`, print channel IDs from `1` to `n` in this format:

`CH-001`, `CH-002`, ...

Tip: keep it simple; no extra libraries needed.

<details>
<summary>Solution (Challenge 2)</summary>

```python
n_text = input("Enter number of channels to list: ").strip()

if not n_text.isnumeric():
    print("Invalid input: enter a non-negative integer")
else:
    n = int(n_text)
    for i in range(1, n + 1):
        if i < 10:
            print(f"CH-00{i}")
        elif i < 100:
            print(f"CH-0{i}")
        else:
            print(f"CH-{i}")
```

</details>

---

## Challenge 3: Ramp-Up Pattern

Print a simple ramp display with `#`, one line per step:

For `n = 4`:

```text
#
##
###
####
```

<details>
<summary>Solution (Challenge 3)</summary>

```python
n_text = input("Enter number of ramp steps: ").strip()

if not n_text.isnumeric():
    print("Invalid input: enter a non-negative integer")
else:
    n = int(n_text)
    for i in range(1, n + 1):
        print("#" * i)
```

</details>

---

## Bonus Challenge 4: Batch Capacity Check

Assume each batch can hold `8` items.

Given a total item count `n`:

- print `Exact batches` if `n` divides by `8`
- otherwise print `Partial final batch`

Also print the remainder.

<details>
<summary>Solution (Bonus Challenge 4)</summary>

```python
n_text = input("Enter total item count: ").strip()

if not n_text.isnumeric():
    print("Invalid input: enter a non-negative integer")
else:
    n = int(n_text)
    remainder = n % 8
    if remainder == 0:
        print("Exact batches")
    else:
        print("Partial final batch")
    print(f"Remainder: {remainder}")
```

</details>

---

## When You're Done

- test with `0`, `1`, and a larger value
- check that invalid text input exits cleanly
- keep variable names clear and short


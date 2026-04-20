# Lab 5 (Alternative): CERN Control Room Checks

## Hints and Tips

- Convert user input once, then branch.
- For text options, use `strip().lower()` so input is easier to compare.
- Keep each condition simple and readable.
- If your input might not be numeric, validate the string first.

---

## Exercise 1: Beam Status Classifier

Write a program that asks for beam energy in GeV and prints a simple status.

1. Ask the user:

   ```text
   Enter beam energy (GeV):
   ```

2. Convert to a number (`float` is fine).
3. Classify and print:
   - if energy is less than `0`: `Invalid energy`
   - if energy is exactly `0`: `No beam`
   - if energy is greater than `0` and less than `1000`: `Setup mode`
   - otherwise: `Physics run`

Example runs:

```text
Enter beam energy (GeV): -2
Invalid energy
```

```text
Enter beam energy (GeV): 0
No beam
```

```text
Enter beam energy (GeV): 450
Setup mode
```

```text
Enter beam energy (GeV): 6500
Physics run
```

<details>
<summary>Solution (Exercise 1)</summary>

```python
energy = float(input("Enter beam energy (GeV): "))

if energy < 0:
    print("Invalid energy")
elif energy == 0:
    print("No beam")
elif energy < 1000:
    print("Setup mode")
else:
    print("Physics run")
```

</details>

---

## Exercise 2: Detector Channel Parity Check

In many systems, odd/even channel numbers are used for different routing conventions.

1. Ask for a channel ID as an integer.
2. Print:
   - `Channel is even` if it is even
   - `Channel is odd` if it is odd

Example:

```text
Enter channel ID: 128
Channel is even
```

```text
Enter channel ID: 73
Channel is odd
```

<details>
<summary>Solution (Exercise 2)</summary>

```python
channel = int(input("Enter channel ID: "))

if channel % 2 == 0:
    print("Channel is even")
else:
    print("Channel is odd")
```

</details>

---

## Exercise 3: Access Badge Quick Validation

Create a simple badge checker.

Rules:

- A valid badge must contain only digits.
- A valid badge length is exactly 6 characters.
- If valid, print `Badge accepted`.
- Otherwise, print `Badge rejected`.

1. Ask for badge input as text (do **not** convert to int immediately).
2. Use `isnumeric()` and `len(...)` in your conditions.

Example:

```text
Enter badge ID: 045123
Badge accepted
```

```text
Enter badge ID: 45A123
Badge rejected
```

```text
Enter badge ID: 999
Badge rejected
```

<details>
<summary>Solution (Exercise 3)</summary>

```python
badge = input("Enter badge ID: ").strip()

if badge.isnumeric() and len(badge) == 6:
    print("Badge accepted")
else:
    print("Badge rejected")
```

</details>

---

## Optional Stretch: Cryo Temperature Warning

Ask for temperature in Kelvin (`float`) and print:

- below `1.9`: `Below nominal operating point`
- from `1.9` to `2.1` (inclusive): `Nominal range`
- above `2.1`: `Above nominal operating point`

<details>
<summary>Solution (Optional Stretch)</summary>

```python
temp_k = float(input("Enter temperature (K): "))

if temp_k < 1.9:
    print("Below nominal operating point")
elif temp_k <= 2.1:
    print("Nominal range")
else:
    print("Above nominal operating point")
```

</details>

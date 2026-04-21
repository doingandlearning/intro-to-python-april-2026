# Lab 6: Factorial

The aim of this lab is to practice using both flow of control and iteration structures in Python by writing a short program to calculate the factorial of a number.

You will practice:

- input validation (`isnumeric()`)
- conversion from text to integer
- `if / elif / else`
- `for` loops with an accumulator

---

## Why Factorial Matters Here

Factorials show up in counting and combinatorics (for example, how many ways to order tasks, labels, or channels).

- `5! = 120` means 120 possible orderings of 5 items.
- `0! = 1` by definition.
- Factorial is only defined for non-negative integers in this lab.

---

## Task

Write a program that:

1. asks for a non-negative integer `n`
2. validates the input
3. computes `n!`
4. prints the result clearly

---

## Step 1: Read Input

Ask:

```text
Enter number of items (n):
```

Store the answer as text first.

<details>
<summary>Solution (Step 1)</summary>

```python
n_text = input("Enter number of items (n): ")
print(f"Received: {n_text}")
```

</details>

---

## Step 2: Validate Input

Only continue if the input contains digits.

- If invalid, print: `Invalid input: enter a non-negative integer`
- If valid, continue to conversion

<details>
<summary>Solution (Step 2)</summary>

```python
n_text = input("Enter number of items (n): ")

if n_text.isnumeric():
    print("Input is valid")
else:
    print("Invalid input: enter a non-negative integer")
```

</details>

---

## Step 3: Convert and Branch

Inside the valid-input branch:

- convert to `int`
- treat `0` as a special case (`0! = 1`)
- otherwise prepare for loop calculation

<details>
<summary>Solution (Step 3)</summary>

```python
n_text = input("Enter number of items (n): ")

if n_text.isnumeric():
    n = int(n_text)
    if n == 0:
        print("0! = 1")
    else:
        print(f"Will compute {n}!")
else:
    print("Invalid input: enter a non-negative integer")
```

</details>

---

## Step 4: Compute Factorial with a Loop

Use:

- accumulator starting at `1`
- loop from `1` to `n` (inclusive)

Then print the final result.

<details>
<summary>Solution (Step 4)</summary>

```python
n_text = input("Enter number of items (n): ")

if n_text.isnumeric():
    n = int(n_text)

    if n == 0:
        print("0! = 1")
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(f"{n}! = {factorial}")
else:
    print("Invalid input: enter a non-negative integer")
```

</details>

---

## Example Runs

```text
Enter number of items (n): 5
5! = 120
```

```text
Enter number of items (n): 0
0! = 1
```

```text
Enter number of items (n): abc
Invalid input: enter a non-negative integer
```

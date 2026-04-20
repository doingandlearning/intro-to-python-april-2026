# Lab 4: Python Strings

We are going to try out some string operations.

---

## Hints and Tips

- Use clear variable names like `original_string` and `new_string`.
- Test each string method in isolation before combining everything.
- Print intermediate values often so you can see exactly what changed.
- Remember: `input()` returns a string.
- `find()` returns `-1` when the substring is not found.

---

## Step 1: Explore Replacing a String

1. Create a comma-separated string and replace commas with spaces.
2. Print both the original value and the updated value.

<details>
<summary>Example code</summary>

```python
original_string = 'John,Andrew,Smith,21,London,UK'
new_string = original_string.replace(',', ' ')

print(f"Original string = '{original_string}'")
print(f"New string = '{new_string}'")
```

</details>

---

## Step 2: Handle User Input

1. Ask the user for two strings.
2. Join them with a space and print the result.

<details>
<summary>Example code</summary>

```python
first = input('Please input the first string: ')
second = input('Please input the second string: ')
new_string = f'{first} {second}'
print(new_string)
```

</details>

---

## Step 3: Explore String Operations

1. Print string length.
2. Print uppercase version.
3. Search for `"Albus"`.
4. Compare with `"Hello World"`.
5. Print a formatted message with the current value.

<details>
<summary>Example code</summary>

```python
print(f'Length of new_string = {len(new_string)}')
print(f'Upper case = {new_string.upper()}')
print(f'The position of the string "Albus" is: {new_string.find("Albus")}')
print(f'new_string == "Hello World": {new_string == "Hello World"}')
print(f'The value of new_string is {new_string}')
```

</details>

---

## Step 4: Convert the Following Values into Strings

1. Define `flag`, `count`, and `temperature`.
2. Print each value and type before conversion.
3. Convert each to a string and print the updated types.

<details>
<summary>Example code</summary>

```python
flag = True
count = 10
temperature = 32.6

print(f"flag = '{flag}' with type {type(flag)}")
print(f"count = '{count}' with type {type(count)}")
print(f"temperature = '{temperature}' with type {type(temperature)}")
print('-------------------------')

flag_string = str(flag)
count_string = str(count)
temp_string = str(temperature)

print(f"flag_string = '{flag_string}' with type {type(flag_string)}")
print(f"count_string = '{count_string}' with type {type(count_string)}")
print(f"temp_string = '{temp_string}' with type {type(temp_string)}")
```

</details>

---

## Step 5 (Optional): Convert Kilometres to Miles

1. Ask the user for kilometres.
2. Convert input to a number.
3. Convert to miles and print the result.

<details>
<summary>Example code</summary>

```python
km_text = input('Please input the distance in kilometres: ')
km = int(km_text)
miles = km * 0.6214
print(f'The distance in miles is {miles}')
```

</details>

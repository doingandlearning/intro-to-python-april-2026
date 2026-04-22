# Lab 10: Writing and Reading Plain Text Files

This lab focuses on reading and writing plain text files using functions.

You will practise:

- writing structured lines to a text file
- reading files line-by-line
- splitting text into useful parts
- using functions to organize file operations

---

## Hints and Tips

- Keep one function for writing and one for reading.
- Build each line as a string before writing it.
- Add `\n` when writing line-by-line.
- Use `.strip()` to remove trailing newline characters.
- Use `.split(" | ", 1)` when separating timestamp and message.

---

## Task 1: Write a Structured Log File

Create a function:

`write_log(filename, messages)`

Rules:

1. Use `with open(filename, "w")`.
2. For each message, add a timestamp from `datetime.now().strftime("%Y-%m-%d %H:%M:%S")`.
3. Write each line in this format:
   `2026-04-21 14:35:01 | Sensor initialised`

Use a short list of sample messages (for example 4 messages).

<details>
<summary>Solution (Task 1)</summary>

```python
from datetime import datetime


def write_log(filename, messages):
    with open(filename, "w") as f:
        for message in messages:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line = f"{timestamp} | {message}\n"
            f.write(line)


messages = [
    "Sensor initialised",
    "Reading: 3.41",
    "Reading: 3.39",
    "Sensor stopped",
]

write_log("sensor_log.txt", messages)
```

</details>

---

## Task 2: Read and Display the Log

Create a function:

`read_log(filename)`

Rules:

1. Use `with open(filename, "r")`.
2. Read line-by-line with a loop.
3. Strip newline characters.
4. Split each line into timestamp and message.
5. Print both parts clearly.

<details>
<summary>Solution (Task 2)</summary>

```python
def read_log(filename):
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            timestamp, message = line.split(" | ", 1)
            print(f"Timestamp: {timestamp}")
            print(f"Message: {message}")


read_log("sensor_log.txt")
```

</details>

---

## Task 3: Filter Log Messages

Create a function:

`filter_log_lines(filename, keyword)`

Rules:

1. Read the file line-by-line.
2. If `keyword` appears in the message part, print that line.
3. Return how many matching lines were found.

Call the function with the keyword `"Reading"`.

<details>
<summary>Solution (Task 3)</summary>

```python
def filter_log_lines(filename, keyword):
    matches = 0
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            _, message = line.split(" | ", 1)
            if keyword in message:
                print(line)
                matches += 1
    return matches


count = filter_log_lines("sensor_log.txt", "Reading")
print(f"Matches: {count}")
```

</details>

---

## Task 4 (Optional): Let the User Choose the Filename

Update your main program so the user can:

1. enter a filename
2. write sample messages to that file
3. read the file back

Reuse your existing functions rather than rewriting logic.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
from datetime import datetime


def write_log(filename, messages):
    with open(filename, "w") as f:
        for message in messages:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} | {message}\n")


def read_log(filename):
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            timestamp, message = line.split(" | ", 1)
            print(f"{timestamp} -> {message}")


name = input("Enter output filename: ")
msgs = ["Start", "Reading: 5.10", "Reading: 5.08", "Stop"]
write_log(name, msgs)
read_log(name)
```

</details>

---

## Reflection

- Why is `with open(...)` safer than opening and closing manually?
- Where did functions make your file code cleaner?
- When is plain text logging enough, and when would CSV be better?

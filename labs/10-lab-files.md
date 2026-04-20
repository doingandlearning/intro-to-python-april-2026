# 🧪 Lab 10: Writing and Reading a Plain Text Log

## 🎯 Objective

Practise writing structured text to a file using `with open(...)` and reading it back using a loop.

---

## 📍Step 1: Write a Structured Log File

1. Create a list of messages to log (e.g. `"Sensor initialised"`, `"Reading: 3.41"`).
2. For each message:

   - Get the current timestamp using `datetime.now()`
   - Format the line as:
     `2025-05-21 14:35:01 | Sensor initialised`

3. Write each line to a file using `with open(..., 'w')`.

**Prompts:**

- Use `datetime.now().strftime(...)` to format the timestamp.
- Should you add `\n` manually to each line?
- What filename will you use?

---

## 📍Step 2: View the File

- Open the file in PyCharm or a text editor.
- Confirm that each line is structured and readable.

---

## 📍Step 3: Read the Log Back In

1. Use `with open(..., 'r')` to open the file.
2. Read it line-by-line using a `for` loop.
3. Strip the newline character and print each line.

**Bonus prompt:**
Can you split the line back into timestamp and message using `.split(" | ")`?

---

## 🧠 Optional Extension

- Count how many lines are in the log file.
- Print only lines where the message includes the word `"Reading"`.

---

## ✅ You’ve Used:

- `with open(..., 'w')` and `'r'`
- Writing and reading lines
- String formatting and splitting
- A structured file format that’s readable but **not yet a CSV**

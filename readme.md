# Introduction to Programming for Non-Programmers (using Python)

- Kevin Cunningham
  - https://kevincunningham.co.uk
  - kevin@kevincunningham.co.uk

## Audience

- Individuals who would like to learn the principles of computer programming.
- Uses Python as an introductory language.

## Prerequisites

- None

## Goals

- Learn to think programmatically
- Understand basic data structures
- Understand basic control loops
- Solve numerous practical programming examples

## Duration

- 3 Days

---

## Syllabus

### Welcome and Introductions

- Introduction to the instructor
- Delegate introductions
- Course overview
- Questions

### Introduction to Python and Coding Setup

- What is Python
- Common uses for Python
- How Python programs work
- Running a Python program
- REPL (Read-Eval-Print Loop)
- IDEs: PyCharm, VS Code, Spyder
- Jupyter Notebooks
- Python Hello World

#### Lab 1: Hello World

- Step-by-step guide: `labs/01-lab-hello-world.md`
- PyCharm project setup, running the application, and printing a welcome message

---

### Solving Problems with a Computer

- Problem Decomposition
- Abstraction & Modeling (e.g., London Underground Map)
- Logical and Algorithmic Thinking
  - What is an Algorithm
  - Example: How to book a holiday
  - Evaluation or Testing of Solutions

#### Lab 2: Computational Thinking

- Step-by-step guide: `labs/02-lab-computational-thinking.md`
- Writing detailed directions (e.g. from home to your office) and thinking about reuse and generalisation
- Modeling the smiley face: breaking a picture into instructions someone else could follow

---

### Variables and Values

- Variables, Symbol Names, and Values
- Variable declarations
- Naming conventions
- Variable values
- Numerical Data Types in Python
  - Integers
  - Floating-point numbers
  - Arithmetic operations

#### Lab 3: Types (interactive Hello World)

- Step-by-step guide: `labs/03-lab-interactive-hello.md`
- `input()`, working with numbers and strings, and combining values in output

---

### Strings

- String operations
- Converting numbers to strings
- Basic string formatting

#### Lab 4: Python strings

- Step-by-step guide: `labs/04-lab-strings.md`
- String operations, user input, and simple formatting tasks
- Optional extension: `labs/04-lab--strings-extension.md` (Mad Libs with string methods)

---

### Flow of Control

- Conditional statements
  - `if`, `if-else`, `if-elif`
  - Boolean Logic

#### Lab 5: Flow of control

- Step-by-step guide: `labs/05-lab-flow-control.md`
- Classify integers as positive, negative, or zero; odd or even; optional kilometres-to-miles converter with validation

---

### Loop Constructs

- Counted Loops (`for` loop)
- Conditional Loops (`while` loop)

#### Lab 6: Factorial

- Step-by-step guide: `labs/06-lab-factorial.md`
- Iteration and conditionals to compute factorials, including edge cases
- Optional extension: `labs/06-lab-factorial-extension.md` (validation, sums, and printed number patterns)

---

### Functions

- Abstracting logic
- Defining functions
- Calling functions
- Parameter passing
  - Default parameter values
  - Mandatory and optional parameters
  - Named parameters
- Returning values

#### Lab 7: Mystery Number (guessing game with functions)

- Step-by-step guide: `labs/07-lab-functions.md`
- Structure a small guessing game with functions, loops, and conditionals (random target, limited attempts, higher/lower feedback)

---

### Sequential Data Containers

- Mutable and Immutable types
- Tuples
- Lists

#### Lab 8: Containers (guess history with a list)

- Step-by-step guide: `labs/08-lab-containers.md`
- Keep an ordered list of guesses and print the history after each game

---

### Advanced Data Containers

- Sets
- Dictionaries

#### Lab 9: Sets and dictionaries

- Step-by-step guide: `labs/09-lab-adv-container.md`
- Set operations on simple student cohorts; building and querying a dictionary of flights between cities

---

### File I/O

- Obtaining a file reference
- File access modes
- Reading from a file
- Writing to a file
- Using `with` for file handling
- Simple exception handling
- Renaming and deleting files

#### Lab 10: Plain-text log file

- Step-by-step guide: `labs/10-lab-files.md`
- Write timestamped lines with `with open(...)`, inspect the file, and read it back in a loop

---

### CSV Module

- Introduction to Modules
- CSV module
- Reading CSV data from a file
- Writing data to a CSV file

#### Lab 11: CSV temperature readings

- Step-by-step guide: `labs/11-lab-csv.md`
- Represent readings in nested tuples, write rows with `csv.writer`, and read them back for display

---

### Supplemental materials (`labs/`)

- `labs/z-12-modules.md` — Imports, splitting code across modules, and file or directory helpers with the `os` module
- `labs/z-challenges.md` — Day 3 challenge pack (short independent exercises)
- `labs/z-capstone.md` — Capstone: collect sensor-style readings, summarise them, and export to CSV

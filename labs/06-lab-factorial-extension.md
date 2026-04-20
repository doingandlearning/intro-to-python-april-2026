# 🧠 Extension Lab: Number Patterns and Totals

You’ve built a factorial calculator — now let’s explore **other number-based tasks** using **loops and conditionals**.

This lab includes **four small challenges**. You’ll reuse your input validation, write more loops, and print patterns. You can try them in the same file or separate ones.

---

## ✏️ Step 1: Validate User Input

Ask the user to input a number. Only accept the input if it’s a **non-negative integer**. If the user enters something else, show an error message and **don’t continue**.

*Hint: You’ve already done this in the factorial lab.*

---

## 🔢 Challenge 1: Add All Numbers From 1 to n

Write code that **adds up all the numbers** from `1` to the number the user entered.

* Store the total in a variable.
* Print the result at the end.
* Think about what value your total should start from.

Example:

```
If the user enters 4, the result is 10 (1 + 2 + 3 + 4)
```

What happens when the user enters 0?

---

## 🧮 Challenge 2: Build a Custom Multiplication Table

Ask the user for a number, and print a multiplication table for that number — up to that number.

You decide the layout. A few options:

* One row at a time: `5 x 1 = 5`, `5 x 2 = 10`, ...
* Or just the results: `5 10 15 20 25`
* Or something else?

Try to make it readable.

---

## 🔺 Challenge 3: Draw a Triangle

Print a triangle shape made out of `*` characters.

The number of rows should match the user’s number.

You must use a loop, and the number of stars on each line should change.
Think: what does `print("*" * 3)` do?

Once it works, try changing the character to `#` or the user's name's first letter.

---

## 🔢 Bonus Challenge 4: Number Pattern

Print a triangle using numbers instead of stars.

Example (user enters 3):

```
1
22
333
```

Questions to ask yourself:

* What loop range gives you the right number of lines?
* What line of code builds each row?

---

## ✅ When You're Done

* Check your indentation — is it consistent?
* Did you use variables that are clear and useful?
* Can you make one version use `while` instead of `for`? (optional)
* What happens with input 0? Or 1? Or 100?


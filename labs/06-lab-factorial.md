# Lab 6: Factorial

The aim of this lab is to practice using both flow of control and iteration structures in Python by writing a short program to calculate the factorial of a number.

---

## Hints and Tips

- Keep validation and calculation separated in your code.
- Treat `0` as a special case (`0! = 1`).
- Use a loop accumulator variable (commonly `factorial = 1`).
- Validate input before converting with `int()`.

---

## Calculating the Factorial of a Number

Write a program that can find the factorial of any given number.

- For example, the factorial of the number 5 (written as 5!) is `1 * 2 * 3 * 4 * 5 = 120`.
- The factorial is not defined for negative numbers, and the factorial of zero is 1 (`0! = 1`).

---

## Steps

### Step 1: Create a New File

1. Create a new file for your factorial calculation in PyCharm using `File -> Python File`.
2. Name the file, such as `factorial`. The `.py` extension will be added automatically.

---

### Step 2: Add Initial Code

1. Write code to ask the user to enter the number for which the factorial will be calculated. For example:

   <details>
   <summary>Example starter code</summary>

   ```python
   print('Starting factorial calculation program')
   number = input('Please input the number: ')
   print(f'The number to calculate factorial for is {number}')
   ```

   </details>

2. Save the file and run it to verify that it works correctly.

   Sample output:

   ```
   Starting factorial calculation program
   Please input the number: 5
   The number to calculate factorial for is 5
   ```

---

### Step 3: Validate that the User Entered a Non-Negative Integer

1. Use the `isnumeric()` method to check if the input is a number. If it’s not a number, notify the user.

   <details>
   <summary>Example validation block</summary>

   ```python
   if number.isnumeric():
       print(f'The number to calculate factorial for is {number}')
   else:
       print('Not an integer number')
   ```

   </details>

2. Test this by entering a non-numeric input, such as the letter "H".

   Example output:

   ```
   Starting factorial calculation program
   Please input the number: H
   Not an integer number
   ```

---

### Step 4: Convert the Input String to an Integer

1. Since `input()` always returns a string, convert it to an integer inside the `if` statement if it’s numeric.

   <details>
   <summary>Example conversion block</summary>

   ```python
   if number.isnumeric():
       print(f'The number to calculate factorial for is {number}')
       num = int(number)
   else:
       print('Not an integer number')
   ```

   </details>

---

### Step 5: Add Logic to Perform Calculations

1. Check if the number is zero. If it is, print that the factorial is 1.

2. Otherwise, use a loop to calculate the factorial and print it out.

   <details>
   <summary>Example branch structure</summary>

   ```python
   if num == 0:
       # Termination criteria
       print('0! factorial is 1')
   else:
       # Loop element – write your code here
   ```

   </details>

3. Run this version to ensure it’s error-free, testing various inputs like `-1` and `0` to confirm the correct output.

---

### Step 6: Add Factorial Calculation

1. Inside the final `else` block, replace the `# write your code here` comment with a `for` loop to calculate the factorial.

   <details>
   <summary>Example loop block</summary>

   ```python
   # Loop element
   factorial = 1
   for i in range(1, num + 1):
       factorial *= i
   print(f'{number}! factorial is {factorial}')
   ```

   </details>

2. Your final program should resemble:

   <details>
   <summary>Example full solution</summary>

   ```python
   print('Starting factorial calculation program')
   number = input('Please input the number: ')

   if number.isnumeric():
       print(f'The number to calculate factorial for is {number}')
       num = int(number)

       if num == 0:
           print('0! factorial is 1')
       else:
           factorial = 1
           for i in range(1, num + 1):
               factorial *= i
           print(f'{number}! factorial is {factorial}')
   else:
       print('Not an integer number')
   ```

   </details>

---

### Step 7: Run the Final Code

Sample output from the program:

```
Starting factorial calculation program
Please input the number: 5
The number to calculate factorial for is 5
5! factorial is 120
```

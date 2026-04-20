# 🧠 Lab 7: Mystery Number – Build a Guessing Game

In this lab, you’ll **design and build** a small game using **functions**, **loops**, and **conditional logic**. You’ll focus on **breaking your program into meaningful parts**, not just writing everything in one big block.

---

## Hints and Tips

- Keep each function focused on one job (input, comparison, messaging, etc.).
- Let your `check_guess` function return a value (`"low"`, `"high"`, `"correct"`).
- Use a loop counter for attempts and stop early on success.
- Print friendly feedback each turn so users understand what happened.

---

## 🎯 Game Concept

You are going to build a “Mystery Number” game. The computer picks a random number between 1 and 10, and the player has to guess it in **4 tries or less**.

Each time the player guesses:

* If it’s correct: Congratulate them and end the game.
* If it’s wrong: Tell them whether the guess was too high or too low.
* After 4 tries: Reveal the answer and end the game.

---

## 🧩 Your Task

Use what you’ve learned so far to **design the structure** of the program.

### Start by sketching out:

1. What should the game do?
2. What parts feel like **repeated behaviour**?
3. What small, reusable functions could help?

---

## 🔧 Suggested Steps

Don’t follow this like a recipe — use it for **inspiration** if you’re stuck.

### Step 1: Welcome the Player

* Create a function that prints a welcome message and explains the rules.

### Step 2: Pick a Number

* At the top of your program `import random` (we'll look more at this tomorrow)
* Use `random.randint(1, 10)` inside a function like `generate_number()` to return the mystery number.

### Step 3: Ask for a Guess

* Create a function like `get_guess()` to ask the user for a number.
* Make sure it returns an `int`.
* What happens if the user types something invalid? (optional: handle that)

### Step 4: Compare the Guess

* Create a function like `check_guess(guess, actual)` that returns `"high"`, `"low"`, or `"correct"`.

### Step 5: Track Attempts

* Use a loop (e.g. `for` or `while`) to give the user up to 4 guesses.
* Print helpful messages each time based on the result of `check_guess`.

---

## 🧠 Stretch Ideas

Try one or more of these once your main game works:

* Add a **cheat code** (e.g. guess `0` reveals the answer but doesn’t use up a turn)
* Let the user choose the **range of numbers** at the start
* Keep track of the **number of guesses**, and print it at the end
* Let the user **play again** without restarting the program (you’ll need `while` and more functions)

---

## ✅ What You Should Practise

* Writing **small, reusable functions**
* Using **parameters and return values**
* Combining **loops**, **conditionals**, and **input**
* Keeping your program **well-structured**

---

## 🧪 Example Run

```
Welcome to Mystery Number!
I'm thinking of a number between 1 and 10.
You have 4 tries. Let's begin!

Guess: 7
Too high!

Guess: 3
Too low!

Guess: 5
Correct! You win in 3 guesses.

Game over.
```

---

<details>
<summary>Example solution code</summary>

```python
import random


def welcome():
    print('Welcome to Mystery Number!')
    print("I'm thinking of a number between 1 and 10.")
    print("You have 4 tries. Let's begin!")


def generate_number():
    return random.randint(1, 10)


def get_guess():
    return int(input('Guess: '))


def check_guess(guess, actual):
    if guess == actual:
        return 'correct'
    if guess > actual:
        return 'high'
    return 'low'


def run_game():
    welcome()
    answer = generate_number()

    for attempt in range(1, 5):
        guess = get_guess()
        result = check_guess(guess, answer)

        if result == 'correct':
            print(f'Correct! You win in {attempt} guesses.')
            print('Game over.')
            return
        if result == 'high':
            print('Too high!')
        else:
            print('Too low!')

    print(f'Sorry, you are out of guesses. The number was {answer}.')
    print('Game over.')


run_game()
```

</details>

## 🔍 Reflection

After you finish:

* How many functions did you write?
* Did any of them feel too long or confusing?
* Would someone else understand your code?

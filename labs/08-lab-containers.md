# Lab 8: Containers

In this lab, you will modify your number guess game to maintain a history of the guesses made by the user.

---

## Hints and Tips

- Use a list because order matters and duplicates are allowed.
- Append each guess immediately after reading it.
- At the end, print attempts and then the list itself.
- If you use functions, pass the list around or keep it in one clearly named place.

---

## Objective

Once the game is over, display a printout of the guesses made by the user in the order they were entered. This allows the user to review their gameplay.

---

## Implementation Details

- To maintain the guess history, use a **list**:
  - It should be modifiable.
  - It should allow duplicates (since the user may enter the same guess multiple times).
  - It should preserve the order of the guesses.

- Consider using a global variable to hold the list for simple access across functions.

---

## Sample Output

```
Welcome to the number guess game
Please guess a number between 1 and 10: 5
Sorry, wrong number
Your guess was lower than the number
Please guess again: 7
Sorry, wrong number
Your guess was lower than the number
Please guess again: 9
Sorry, wrong number
Your guess was lower than the number
Please guess again: 10
Well done, you won!
You took 4 attempts to complete the game
Your guesses were:
[5, 7, 9, 10]
Game Over
```

---

Incorporate this list of guesses into your existing game to track and display the guesses after the game concludes.


---

Possible extensions:

- Feedback After Each Guess: After each guess, provide more specific feedback on how close the guess is to the target.
- Hint System: After three incorrect attempts, offer a hint by specifying if the target number is in the upper or lower half of the range.
- Play Again Option: At the end of each game, allow the user to decide if they want to play again.

---

<details>
<summary>Example solution code</summary>

```python
import random

target = random.randint(1, 10)
guesses = []

print('Welcome to the number guess game')

for attempt in range(1, 5):
    guess = int(input('Please guess a number between 1 and 10: '))
    guesses.append(guess)

    if guess == target:
        print('Well done, you won!')
        break

    print('Sorry, wrong number')
    if guess < target:
        print('Your guess was lower than the number')
    else:
        print('Your guess was higher than the number')
else:
    print(f'Out of attempts. The number was {target}')

print(f'You took {len(guesses)} attempts to complete the game')
print('Your guesses were:')
print(guesses)
print('Game Over')
```

</details>

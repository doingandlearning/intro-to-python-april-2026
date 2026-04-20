guesses = []

while True:
    value = input("Enter a number (or 'done' to finish): ")
    if value.lower() == 'done':
        break
    if value.isdigit():
        guesses.append(int(value))
    else:
        print("Invalid input. Please enter a number or 'done'.")

print(f"\nYou entered {len(guesses)} valid numbers.")
if len(guesses) >= 3:
    print("Last three guesses:", guesses[-3:])
else:
    print("Guesses:", guesses)
